# Iteração 02 — Restaurar as regras de cobertura

Estado: **concluída e aprovada por médias**, com média geral **0,8659**. O usuário criou o commit, publicou e avaliou a variante; os resultados foram conferidos em [CSV da iteração 02](../resultados/iteracao-02_cobertura-restaurada_d29b125d.csv) e comparados a [CSV da iteração 01](../resultados/iteracao-01_prompt-reduzido_bd3aa4bf.csv).

## Hipótese registrada antes da avaliação

Restaurar o bloco explícito de regras de cobertura por domínio, mantendo os mesmos dois exemplos da primeira rodada, pode melhorar a completude das User Stories. A hipótese principal é obter F1 médio maior que **0,84012**, resultado da iteração 01. A avaliação também acompanhará Precision e Clarity para identificar eventual aumento de escopo ou de texto sem ganho útil.

A intervenção desta transição é um único grupo de instruções: o bloco `REGRAS DE COBERTURA`, copiado integralmente da referência aprovada. Os exemplos, a persona, as sete etapas de análise, o contrato de saída, as regras gerais, as exceções e o User foram preservados. A descrição do YAML foi atualizada para identificar a segunda rodada.

## Alteração e comparação planejada

| Componente | Iteração 01 | Iteração 02 |
| --- | --- | --- |
| Demonstrações | `exemplo_1`, podcast simples, e `exemplo_5`, exportação complexa. | Os mesmos dois pares, sem alteração. |
| Bloco explícito de cobertura | Ausente. | Restaurado da referência completa. |
| Demais instruções e entrada | Persona, análise, formato, fatos/requisitos/propostas, concisão, exceções e `bug_report`. | Preservados. |

O bloco restaurado trata de interface, compatibilidade e layout, cálculos e contagens, integrações, segurança, desempenho, cache e exportação, concorrência e sincronização offline. Seus pontos continuam condicionados à pertinência ao relato; não devem ser aplicados como requisitos de todos os bugs.

A variante desta rodada está preservada no commit Git [b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e). O [prompt ativo](../../prompts/bug_to_user_story_v2.yml) contém agora a versão completa da [iteração 03](iteracao-03.md). A primeira variante permanece em [2c5e310c46ac210d00784b445e7366186e41c276](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/2c5e310c46ac210d00784b445e7366186e41c276), e a [referência completa](referencia/bug_to_user_story_v2_aprovado.yml) segue disponível para conferência. Dataset, métricas, avaliador e testes não foram alterados.

## Identificação

| Registro | Valor |
| --- | --- |
| Commit Git da iteração 02 | [b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e) — “Primeira melhoria: restaurar as regras de cobertura.” |
| Commit Hub da iteração 02 | `ac0fdcce89e8a89c966142fb128ef637557b5598def6e4357250bb0d85c1180e` |
| Experimento | `promptmateusmba-bug_to_user_story_v2-d29b125d` |
| ID do experimento | `b1f85632-0def-4361-8edb-8955db719dfa` |
| Revisão Git registrada nos runs | `b6bcdd7-dirty` |
| Base de comparação | Iteração 01, experimento `bd3aa4bf`, resultado em [CSV da iteração 01](../resultados/iteracao-01_prompt-reduzido_bd3aa4bf.csv). |
| Provider / gerador / avaliador registrados | `openai` / `gpt-5.4` / `gpt-5.5`, mantendo a configuração da rodada anterior. |
| Temperatura configurada | `0` |
| Dataset | `mba-ia-pull-evaluation-prompt-eval`; os mesmos 15 casos do JSONL local, com inputs e referências conferidos no CSV. |
| Nome do prompt e entrada | `bug_to_user_story_v2`; somente `bug_report`. |

SHA256 das mensagens efetivas:

```text
Iteração 01: 721e2c18d9685b21f4726dadd74b4e78a09a72bbbecf5b5aa8815ee25192f2df
Iteração 02: 864509da07789fae7c5487e12a3b672424bc737fc35b9a66d39728754c7a7864
```

SHA256 do arquivo YAML completo da iteração 02:

```text
a172f2415eb85c8b0cc809f9e6f628180558e7412b8805c6c3fc165f77488b12
```

O commit [b6bcdd7](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e) altera somente o YAML do prompt: restaura o bloco de cobertura e atualiza a descrição. Na conferência desta rodada, seu conteúdo coincidia byte a byte com o arquivo ativo; o fingerprint coincide com os hashes local e remoto dos 15 runs. Os dois exemplos foram preservados. O sufixo `-dirty` registra alterações locais na árvore de trabalho durante a execução; a correspondência do conteúdo com o commit foi conferida separadamente.

SHA256 do CSV da segunda rodada:

```text
2c4a31b9eaba17ad272d651c002bc55dfa58f6abfcedb483d20bdd389fa2770f
```

## Resultados e comparação entre rodadas

O CSV contém 15 gerações com status `success`, nenhum erro de geração registrado e 75 notas preenchidas. As respostas não estão vazias, os scores estão entre 0 e 1 e as fórmulas de Helpfulness e Correctness foram conferidas por caso. Os 15 pares de input e referência são os mesmos da primeira rodada e do JSONL local.

| Métrica | Iteração 01 | Iteração 02 | Diferença |
| --- | ---: | ---: | ---: |
| Helpfulness | 0,8547 | 0,8673 | +0,0127 |
| Correctness | 0,8417 | 0,8638 | +0,0221 |
| F1-Score | 0,8401 | 0,8636 | +0,0235 |
| Clarity | 0,8660 | 0,8707 | +0,0047 |
| Precision | 0,8433 | 0,8640 | +0,0207 |
| **Média geral** | **0,8492** | **0,8659** | **+0,0167** |

As médias da segunda rodada, antes do arredondamento, são: Helpfulness **0,8673333333333333**, Correctness **0,8637933333333333**, F1 **0,8636**, Clarity **0,8706666666666667** e Precision **0,864**. A média geral é **0,8658786666666667**, diferença de **+0,0167106666666667** para a primeira. As diferenças da tabela usam as médias antes do arredondamento.

**Aprovada:** todas as cinco médias e a média geral atingem pelo menos 0,8. O F1 aumentou em 11 casos e caiu em quatro. O número de casos com F1 abaixo da meta diminuiu de quatro para dois; o de casos com alguma nota abaixo da meta diminuiu de cinco para três.

| Caso ainda abaixo da meta | Helpfulness | Correctness | F1-Score | Clarity | Precision |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 — adicionar ao carrinho | 0,8150 | 0,8406 | 0,9011 | 0,8500 | 0,7800 |
| 14 — relatórios gerenciais | 0,8600 | 0,8294 | 0,7988 | 0,8600 | 0,8600 |
| 15 — sincronização offline | 0,9200 | 0,8513 | 0,7926 | 0,9300 | 0,9100 |

Nos casos priorizados antes da execução, o F1 variou assim:

| Caso | F1 da iteração 01 | F1 da iteração 02 |
| --- | ---: | ---: |
| 4 — dashboard | 0,7677 | 0,8180 |
| 5 — Safari | 0,7834 | 0,8899 |
| 7 — relatório de vendas | 0,7995 | 0,8395 |
| 14 — relatórios gerenciais | 0,7408 | 0,7988 |

Em Precision, os casos 1, 5 e 7 passaram de 0,77/0,78/0,77 para 0,78/0,85/0,83. O caso 1 continua abaixo da meta. O caso 15, que tinha F1 0,8229, caiu para 0,7926 e entrou no grupo de casos fracos; a melhora não foi uniforme.

## Por que as notas parecem semelhantes

Os arquivos foram alinhados pelo relato de bug, sem depender da ordem das linhas. As 15 respostas geradas são diferentes e nenhum dos 15 conjuntos completos de cinco notas se repete. Há cinco notas individuais exatamente iguais: três de Clarity, uma de Precision e uma de Helpfulness. F1 e Correctness diferem em todos os casos.

| Média exibida com duas casas | Iteração 01 | Iteração 02 |
| --- | ---: | ---: |
| Helpfulness | 0,85 | 0,87 |
| Correctness | 0,84 | 0,86 |
| F1-Score | 0,84 | 0,86 |
| Clarity | 0,87 | 0,87 |
| Precision | 0,84 | 0,86 |

A repetição de Clarity em 0,87 é efeito do arredondamento das médias 0,8660 e 0,8707. Os experimentos, commits do Hub e fingerprints das mensagens são distintos e correspondem às respectivas revisões Git. O registro comprova o uso da segunda variante, sem evidência de repetição do CSV anterior.

Comparada à referência completa histórica, a média geral da segunda rodada está próxima: **0,8659 contra 0,8675**, diferença de aproximadamente **−0,0016**. Com duas casas, ambas aparecem como **0,87**. Essa comparação histórica é distinta da comparação direta entre as iterações 01 e 02.

## Interpretação da hipótese

A previsão principal recebeu evidência favorável nesta execução: F1 aumentou de **0,84012 para 0,8636**. Precision e Clarity também aumentaram. A média de palavras por resposta caiu de **425,4 para 412,3**.

A mudança entre prompts foi somente a restauração do bloco de cobertura, além da descrição que não é enviada como mensagem. Ainda assim, uma execução por variante não separa de forma robusta o efeito da instrução da variabilidade das gerações e dos julgamentos. Os CSVs não contêm justificativas dos juízes; não foi atribuída uma causa específica às notas ou auditado feedback operacional ausente da exportação.

## Validação e execução realizada

Os **24 testes passaram** com a segunda variante, incluindo a estrutura obrigatória, os dois pares Few-shot, a única variável `bug_report` e a renderização dos 15 relatos.

```bash
PYTHONDONTWRITEBYTECODE=1 venv/bin/python -m pytest tests/test_prompts.py -v -p no:cacheprovider
```

Após a validação local, o usuário criou o commit [b6bcdd7](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e) e executou a publicação e a avaliação. O CSV fornecido preserva a identificação dos resultados desses passos:

```bash
git rev-parse HEAD
venv/bin/python src/push_prompts.py
venv/bin/python src/evaluate.py
```

Esta página preserva o resultado da segunda rodada. A preparação da versão completa para a terceira rodada está registrada em [iteracao-03.md](iteracao-03.md).
