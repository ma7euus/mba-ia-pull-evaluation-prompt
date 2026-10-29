# Resultados das três iterações

Esta pasta reúne as exportações originais do LangSmith para o ciclo controlado de `bug_to_user_story_v2`. Os arquivos foram movidos e renomeados sem alterar o conteúdo. Cada CSV contém 15 casos, as respostas geradas, cinco notas por caso e metadados com a identidade do prompt.

| Iteração | Configuração | Commit Git | Experimento | Média geral | CSV |
| --- | --- | --- | --- | ---: | --- |
| 01 | Dois exemplos, sem o bloco explícito de cobertura. | [2c5e310](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/2c5e310c46ac210d00784b445e7366186e41c276) | `bd3aa4bf` | 0,8492 | [Prompt reduzido](iteracao-01_prompt-reduzido_bd3aa4bf.csv) |
| 02 | Dois exemplos, com o bloco de cobertura restaurado. | [b6bcdd7](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e) | `d29b125d` | **0,8659** | [Cobertura restaurada](iteracao-02_cobertura-restaurada_d29b125d.csv) |
| 03 | Versão completa, com seis exemplos e todas as regras. | [05bf7a2](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/05bf7a2e68a5c9a7e8a5aecc3b014ef3cf7c8807) | `1419119b` | 0,8548 | [Versão completa](iteracao-03_versao-completa_1419119b.csv) |

As três variantes foram aprovadas por médias. A segunda teve a maior média nesta comparação; restaurar os seis exemplos não aumentou o F1 na terceira execução. A versão completa foi mantida como a versão final solicitada. Uma execução por variante não demonstra superioridade robusta nem permite atribuir cada diferença somente ao prompt.

| Métrica | Iteração 01 | Iteração 02 | Iteração 03 |
| --- | ---: | ---: | ---: |
| Helpfulness | 0,8547 | 0,8673 | 0,8590 |
| Correctness | 0,8417 | 0,8638 | 0,8471 |
| F1-Score | 0,8401 | 0,8636 | 0,8501 |
| Clarity | 0,8660 | 0,8707 | 0,8740 |
| Precision | 0,8433 | 0,8640 | 0,8440 |
| **Média geral** | **0,8492** | **0,8659** | **0,8548** |

Os hashes local e remoto das mensagens em cada CSV foram comparados ao respectivo commit Git. Os 45 pares de entrada e referência correspondem ao JSONL local, as 225 notas estão preenchidas e as fórmulas derivadas foram conferidas. Os CSVs registram revisões Git com sufixo `-dirty`, preservado nos documentos; o conteúdo dos prompts foi verificado diretamente. As exportações não incluem justificativas dos juízes.

SHA256 dos arquivos, preservados após a movimentação:

```text
iteracao-01_prompt-reduzido_bd3aa4bf.csv
8746ff0aa6c4ee4d628551706b9cc628cdb3a2660076b1a714c08035dc507861

iteracao-02_cobertura-restaurada_d29b125d.csv
2c4a31b9eaba17ad272d651c002bc55dfa58f6abfcedb483d20bdd389fa2770f

iteracao-03_versao-completa_1419119b.csv
8e810053a25ee2fc09c79b267278d26f36618ca6336161a1ac2e0b5a7f72a57b
```

Para recalcular as médias sem rede, execute na raiz do projeto:

```bash
python3 - <<'PY'
import csv
from pathlib import Path
from statistics import mean

metrics = ('helpfulness', 'correctness', 'f1_score', 'clarity', 'precision')
for path in sorted(Path('docs/resultados').glob('iteracao-*.csv')):
    with path.open(encoding='utf-8-sig', newline='') as file:
        rows = list(csv.DictReader(file))
    assert len(rows) == 15
    assert all(row['status'] == 'success' and not row['error'] for row in rows)
    scores = {key: mean(float(row[key]) for row in rows) for key in metrics}
    print(path.name, scores, 'media_geral=', mean(scores.values()))
PY
```

Hipóteses, identidades completas e análise dos casos fracos estão nos registros das iterações [01](../iteracoes/iteracao-01.md), [02](../iteracoes/iteracao-02.md) e [03](../iteracoes/iteracao-03.md). As medições históricas anteriores a esse ciclo permanecem separadas em [Etapa 11](../iteracoes/etapa11.md).
