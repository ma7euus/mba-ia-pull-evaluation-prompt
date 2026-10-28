"""Validação local da estrutura e da formatação do prompt otimizado."""

import json
import re
import sys
from pathlib import Path

import pytest
import yaml
from langchain_core.prompts import ChatPromptTemplate

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATH = PROJECT_ROOT / "prompts" / "bug_to_user_story_v2.yml"
DATASET_PATH = PROJECT_ROOT / "datasets" / "bug_to_user_story.jsonl"

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from utils import validate_prompt_structure


def load_prompts(file_path: str | Path):
    """Carrega o dicionário com os campos do prompt na raiz do YAML."""
    with open(file_path, encoding="utf-8") as file:
        return yaml.safe_load(file)


def instructions_before_examples(prompt_data):
    """Evita que exemplos escondam a ausência de instruções de persona/formato."""
    system_prompt = prompt_data.get("system_prompt")
    assert isinstance(system_prompt, str), "system_prompt deve ser um texto"
    return re.split(
        r"^\s*#\s*EXEMPLOS\b|<exemplo_\d+\b",
        system_prompt,
        maxsplit=1,
        flags=re.IGNORECASE | re.MULTILINE,
    )[0]


def prompt_texts(value, path="prompt"):
    """Percorre mensagens e metadados, incluindo listas e campos aninhados."""
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from prompt_texts(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from prompt_texts(item, f"{path}[{index}]")


def dataset_cases():
    with DATASET_PATH.open(encoding="utf-8") as file:
        examples = [json.loads(line) for line in file if line.strip()]
    assert examples, "O dataset deve conter relatos para validar a formatação"
    return [
        pytest.param(example["inputs"]["bug_report"], id=f"bug-{index:02d}")
        for index, example in enumerate(examples, 1)
    ]


@pytest.fixture(scope="module")
def prompt_data():
    data = load_prompts(PROMPT_PATH)
    assert isinstance(data, dict), "O YAML deve conter um dicionário de campos"
    return data


@pytest.fixture(scope="module")
def prompt_template(prompt_data):
    return ChatPromptTemplate.from_messages(
        [
            ("system", prompt_data["system_prompt"]),
            ("user", prompt_data["user_prompt"]),
        ]
    )


class TestPrompts:
    def test_prompt_has_system_prompt(self, prompt_data):
        system_prompt = prompt_data.get("system_prompt")
        assert isinstance(system_prompt, str), "system_prompt deve existir e ser texto"
        assert system_prompt.strip(), "system_prompt não pode estar vazio"

    def test_prompt_has_role_definition(self, prompt_data):
        instructions = instructions_before_examples(prompt_data)
        role = re.search(
            r"^\s*(?:Você\s+é|Atue\s+como|Assuma\s+o\s+papel\s+de)\s+([^\n.!?]+)",
            instructions,
            re.IGNORECASE | re.MULTILINE,
        )
        assert role, "As instruções devem definir explicitamente uma persona"
        role_text = re.sub(r"\[[^\]]*\]|<[^>]*>", "", role.group(1))
        assert any(word.casefold() not in {"um", "uma", "o", "a"} for word in role_text.split()), (
            "A persona deve descrever um papel concreto"
        )

    def test_prompt_mentions_format(self, prompt_data):
        instructions = instructions_before_examples(prompt_data)
        markdown = re.search(r"\bMarkdown\b", instructions, re.IGNORECASE)
        user_story = re.search(
            r"\bComo\b.*?\beu\s+quero\b.*?\bpara\s+que\b",
            instructions,
            re.IGNORECASE | re.DOTALL,
        )
        assert markdown or user_story, (
            "As instruções devem exigir Markdown ou o formato Como/eu quero/para que"
        )

    def test_prompt_has_few_shot_examples(self, prompt_data):
        messages = []
        for key in ("system_prompt", "user_prompt"):
            message = prompt_data.get(key)
            assert isinstance(message, str), f"{key} deve ser texto"
            messages.append(message)
        content = "\n".join(messages)
        openings = re.findall(r"<(exemplo_\d+)\b[^>]*>", content)
        closings = re.findall(r"</(exemplo_\d+)\s*>", content)
        assert len(openings) >= 2, "São necessários pelo menos dois exemplos"
        assert sorted(openings) == sorted(closings), "Há exemplos sem fechamento correto"
        examples = re.findall(
            r"<(exemplo_\d+)\b[^>]*>(.*?)</\1\s*>", content, re.DOTALL
        )
        assert len(examples) == len(openings), "Há exemplos incompletos ou aninhados"

        reports = []
        for name, body in examples:
            for tag in ("bug_report", "resposta"):
                parts = re.findall(rf"<{tag}>(.*?)</{tag}>", body, re.DOTALL)
                assert len(parts) == 1, f"{name} deve conter uma única {tag}"
                text = re.sub(r"<[^>]*>", "", parts[0]).strip()
                written_text = re.sub(r"\[[^\]]*\]", "", text)
                assert re.search(r"\w", written_text), (
                    f"{name}: {tag} deve ter conteúdo além de marcadores de preenchimento"
                )
                if tag == "bug_report":
                    reports.append(" ".join(text.split()).casefold())
        assert len(set(reports)) >= 2, "Os exemplos devem demonstrar relatos distintos"

    def test_prompt_no_todos(self, prompt_data):
        marker = re.compile(r"\bTODO\b|\[\s*(?i:todo)\s*\]")
        unfinished = [path for path, text in prompt_texts(prompt_data) if marker.search(text)]
        assert not unfinished, f"Marcadores pendentes encontrados em: {unfinished}"

    def test_minimum_techniques(self, prompt_data):
        techniques = prompt_data.get("techniques_applied")
        assert isinstance(techniques, list), "techniques_applied deve ser uma lista"
        assert all(isinstance(item, str) and item.strip() for item in techniques), (
            "Cada técnica deve ter um nome não vazio"
        )
        normalized = {re.sub(r"[\s_-]+", "", item).casefold() for item in techniques}
        assert normalized & {"fewshot", "fewshotlearning"}, "Few-shot é obrigatório"
        additional = {
            "chainofthought", "cot", "treeofthought", "treeofthoughts", "tot",
            "skeletonofthought", "sot", "react", "roleprompting",
        }
        assert normalized & additional, (
            "Declare pelo menos uma técnica adicional permitida além de Few-shot"
        )

    def test_prompt_structure_is_valid(self, prompt_data):
        valid, errors = validate_prompt_structure(prompt_data)
        assert valid, "\n".join(errors)

    def test_prompt_uses_expected_input(self, prompt_data, prompt_template):
        assert prompt_template.input_variables == ["bug_report"], (
            "O template deve depender somente da entrada bug_report do dataset"
        )
        user_prompt = prompt_data.get("user_prompt")
        assert isinstance(user_prompt, str) and user_prompt.strip()
        assert "{bug_report}" in user_prompt, "O relato deve ser inserido na mensagem User"
        assert "{bug_report}" not in prompt_data["system_prompt"], (
            "O relato variável deve ficar separado das instruções permanentes"
        )

    @pytest.mark.parametrize(
        "bug_report",
        dataset_cases()
        + [
            pytest.param(
                'Falha ao enviar JSON: {"campo": "ação"}.\nTexto literal: {{valor}}.',
                id="texto-com-chaves-e-quebra-de-linha",
            )
        ],
    )
    def test_prompt_renders_inputs(self, prompt_template, bug_report):
        messages = prompt_template.format_messages(bug_report=bug_report)
        assert [message.type for message in messages] == ["system", "human"]
        assert messages[0].content.strip(), "As instruções devem ser preservadas"
        assert bug_report in messages[1].content, "O relato deve ser preservado integralmente"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "--tb=short"]))
