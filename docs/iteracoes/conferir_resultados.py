"""Confere as notas arquivadas e recalcula as médias sem chamar serviços externos."""

import hashlib
import json
import math
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[2]
METRICS = ("helpfulness", "correctness", "f1_score", "clarity", "precision")


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def main():
    archive = json.loads(Path(__file__).with_name("resultados.json").read_text(encoding="utf-8"))
    dataset_path = ROOT / archive["dataset"]["path"]
    assert hashlib.sha256(dataset_path.read_bytes()).hexdigest() == archive["dataset"]["file_sha256"]
    examples = [json.loads(line) for line in dataset_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    fingerprints = {
        index: hashlib.sha256(canonical({"inputs": row["inputs"], "outputs": row["outputs"]}).encode()).hexdigest()
        for index, row in enumerate(examples, 1)
    }
    assert len(examples) == archive["dataset"]["cases"] == 15
    assert hashlib.sha256(canonical(sorted(fingerprints.values())).encode()).hexdigest() == archive["dataset"]["canonical_examples_sha256"]

    threshold = archive["threshold"]
    for experiment in archive["experiments"]:
        cases = experiment["cases"]
        assert len(cases) == len(examples)
        assert {case["case"] for case in cases} == set(fingerprints)
        assert experiment["configuration"] == archive["configuration"]
        for case in cases:
            assert case["example_sha256"] == fingerprints[case["case"]]
            scores = case["scores"]
            assert set(scores) == set(METRICS)
            assert all(math.isfinite(value) and 0 <= value <= 1 for value in scores.values())
            assert math.isclose(scores["helpfulness"], round((scores["clarity"] + scores["precision"]) / 2, 4), abs_tol=1e-12)
            assert math.isclose(scores["correctness"], round((scores["f1_score"] + scores["precision"]) / 2, 4), abs_tol=1e-12)
        averages = {key: mean(case["scores"][key] for case in cases) for key in METRICS}
        summary = experiment["summary"]
        for key in METRICS:
            assert math.isclose(averages[key], summary["means"][key], abs_tol=1e-12)
        overall = mean(averages.values())
        passed = all(value >= threshold for value in averages.values()) and overall >= threshold
        assert math.isclose(overall, summary["overall_mean"], abs_tol=1e-12)
        assert passed == summary["passed"]
        assert sum(min(case["scores"].values()) < threshold for case in cases) == summary["cases_below_threshold"]
        assert sum(case["scores"]["f1_score"] < threshold for case in cases) == summary["f1_cases_below_threshold"]
        values = " | ".join(f"{key}={averages[key]:.4f}" for key in METRICS)
        print(f"{experiment['name']}: {values} | média={overall:.4f} | {'APROVADO' if passed else 'REPROVADO'}")

    final = archive["experiments"][-1]
    revision = next(item for item in archive["prompt_revisions"] if item["commit"] == final["prompt_hub_commit"])
    assert revision["sha256"] == final["prompt_sha256"]
    assert set(final["prompt_identity"].values()) == {final["prompt_sha256"]}
    case_count = sum(len(experiment["cases"]) for experiment in archive["experiments"])
    print(f"Conferência concluída: {case_count} casos, {case_count * len(METRICS)} notas e dataset consistentes com o registro arquivado.")


if __name__ == "__main__":
    main()
