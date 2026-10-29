# Iteração 01 — Prompt reduzido

Estado: **concluída e aprovada por médias**, com média geral **0,8492**. Esta é a primeira rodada de um novo ciclo controlado, posterior às avaliações históricas. O usuário criou o commit do prompt, publicou e executou a avaliação; os resultados foram conferidos em [CSV da iteração 01](../resultados/iteracao-01_prompt-reduzido_bd3aa4bf.csv).

## Hipótese registrada antes da avaliação

Reduzir as demonstrações de seis para duas e retirar o bloco explícito de regras de cobertura por domínio pode reduzir a completude das User Stories, especialmente em integrações, autorização e cálculos. A hipótese principal é que restaurar esses componentes nas rodadas seguintes melhore o F1. Uma resposta menor também pode melhorar clareza ou foco; nenhuma queda ou melhoria é presumida como resultado.

Esta rodada estabelece o ponto de partida reduzido. Ela modifica dois componentes em relação à referência aprovada e, sozinha, não permite atribuir diferenças a um deles isoladamente. Nas próximas transições será restaurado um grupo de regras por vez, após registrar e concluir esta rodada.

## Alterações realizadas

| Componente | Referência aprovada | Iteração 01 |
| --- | --- | --- |
| Demonstrações | Seis pares completos. | Dois pares originais: `exemplo_1`, podcast simples, e `exemplo_5`, exportação complexa. |
| Bloco `REGRAS DE COBERTURA` | Checklist explícito por domínio. | Retirado. |
| Persona e análise interna | Analista de requisitos e sete etapas. | Preservadas. |
| Formato, fatos/requisitos/propostas e exceções | Regras gerais da referência. | Preservadas. |
| Técnicas declaradas | Role Prompting, Chain of Thought e Few-shot Learning. | Preservadas e efetivamente presentes. |
| Nome e entrada | `bug_to_user_story_v2`; somente `bug_report`. | Preservados. |

Os IDs 1 e 5 foram mantidos para rastrear os exemplos de origem. As etapas de análise, o User e o exemplo complexo ainda orientam cobertura; a alteração remove o **bloco explícito**, não toda instrução sobre completude. A descrição do YAML foi atualizada para refletir os dois exemplos.

A variante desta rodada está preservada no commit Git [2c5e310c46ac210d00784b445e7366186e41c276](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/2c5e310c46ac210d00784b445e7366186e41c276). O [prompt ativo](../../prompts/bug_to_user_story_v2.yml) contém agora a versão completa da [iteração 03](iteracao-03.md); a segunda variante permanece registrada em [iteracao-02.md](iteracao-02.md). A [referência aprovada](referencia/bug_to_user_story_v2_aprovado.yml) foi preservada byte a byte antes da edição. Dataset, código dos avaliadores e testes não foram alterados.

## Identificação e configuração

| Registro | Valor |
| --- | --- |
| Commit Git da iteração | [2c5e310c46ac210d00784b445e7366186e41c276](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/2c5e310c46ac210d00784b445e7366186e41c276) — “Versão reduzida: dois exemplos e sem o bloco detalhado de cobertura.” |
| Commit Hub da iteração | `05922c6053c1fb3691ab54a6de6fb1e48e24d488ee42d4e72e86ab3da39d4b9c` |
| Experimento | `promptmateusmba-bug_to_user_story_v2-bd3aa4bf` |
| ID do experimento | `52a1815e-4859-4b49-aa01-d0a64f13d9b7` |
| Revisão Git registrada nos runs | `2c5e310-dirty` |
| Referência histórica | Hub `42343f3e00c6f179ab050fc92b67e10b81970d7b85bd24923a38c58bef58153c`; experimento `8c034dd1`. |
| Provider | `openai` |
| Gerador / avaliador | `gpt-5.4` / `gpt-5.5` |
| Temperatura configurada | `0` |
| Dataset | `mba-ia-pull-evaluation-prompt-eval`; os mesmos 15 casos de `datasets/bug_to_user_story.jsonl`. |

SHA256 das mensagens efetivamente enviadas ao modelo, calculado por `prompt_fingerprint`:

```text
Referência aprovada: 727f2c278765824fe9cb44d329a540a2a3979c98973204a94d9edf8d9e2433d9
Iteração 01:        721e2c18d9685b21f4726dadd74b4e78a09a72bbbecf5b5aa8815ee25192f2df
```

SHA256 dos arquivos YAML completos, incluindo descrição e metadados:

```text
Referência aprovada: e1f8c3fb7403ad21e1c1778ea4d48e591b8b6d119bdbee724960f1624304ac8e
Iteração 01:        735b6e3ee7f57af52e151877c2c71093f94f4ea266912f1b3f95161518f4a8fe
```

O commit [2c5e310](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/2c5e310c46ac210d00784b445e7366186e41c276) altera somente `prompts/bug_to_user_story_v2.yml`. Na conferência desta rodada, o arquivo ativo era byte a byte idêntico ao YAML desse commit; o fingerprint calculado coincide com os hashes local e remoto nos 15 runs. O sufixo `-dirty` registra alterações locais na árvore de trabalho durante a avaliação e não deve ser omitido. A correspondência do prompt com o commit foi conferida separadamente.

SHA256 do CSV usado nesta conferência:

```text
8746ff0aa6c4ee4d628551706b9cc628cdb3a2660076b1a714c08035dc507861
```

## Validação e execução desta rodada

Os **24 testes passaram** com o prompt reduzido, incluindo os seis requisitos obrigatórios, a variável `bug_report` e a renderização dos 15 relatos. Isso valida a estrutura; não mede a qualidade semântica.

```bash
PYTHONDONTWRITEBYTECODE=1 venv/bin/python -m pytest tests/test_prompts.py -v -p no:cacheprovider
```

Após a preparação, o usuário criou o commit [2c5e310](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/2c5e310c46ac210d00784b445e7366186e41c276) e executou a publicação e a avaliação. O CSV preserva a identificação do prompt publicado e a revisão Git. A atualização da documentação registra os resultados após a execução, para um commit posterior.

```bash
git rev-parse HEAD
venv/bin/python src/push_prompts.py
venv/bin/python src/evaluate.py
```

## Resultados conferidos

O CSV contém 15 linhas com status `success`, nenhum erro de geração registrado e cinco notas preenchidas em cada linha. Os pares de entrada e referência correspondem exatamente aos 15 casos do JSONL local. Os scores estão entre 0 e 1, as respostas não estão vazias e as duas métricas derivadas correspondem às fórmulas do avaliador.

| Métrica | Referência completa histórica | Iteração 01 | Diferença |
| --- | ---: | ---: | ---: |
| Helpfulness | 0,8697 | 0,8547 | −0,0150 |
| Correctness | 0,8660 | 0,8417 | −0,0243 |
| F1-Score | 0,8626 | 0,8401 | −0,0225 |
| Clarity | 0,8700 | 0,8660 | −0,0040 |
| Precision | 0,8693 | 0,8433 | −0,0260 |
| **Média geral** | **0,8675** | **0,8492** | **−0,0183** |

As médias foram calculadas a partir das 15 notas por métrica. A média geral exata é **0,849168**; a diferença para a referência é **−0,018348**. As diferenças da tabela usam as médias antes do arredondamento.

Cinco casos têm alguma nota abaixo de 0,8:

| Caso do JSONL | Helpfulness | Correctness | F1-Score | Clarity | Precision |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 — adicionar ao carrinho | 0,8000 | 0,8140 | 0,8581 | 0,8300 | 0,7700 |
| 4 — dashboard de usuários ativos | 0,8500 | 0,8038 | 0,7677 | 0,8600 | 0,8400 |
| 5 — imagens no Safari | 0,7950 | 0,7817 | 0,7834 | 0,8100 | 0,7800 |
| 7 — relatório de vendas | 0,8000 | 0,7848 | 0,7995 | 0,8300 | 0,7700 |
| 14 — relatórios gerenciais | 0,8600 | 0,7854 | 0,7408 | 0,8900 | 0,8300 |

São quatro casos com F1 abaixo da meta. O CSV exporta respostas e notas, mas não as justificativas dos juízes. Portanto, esta conferência não atribui uma omissão ou um erro específico como causa de cada nota, nem substitui a inspeção de feedbacks operacionais dos juízes.

## Decisão e interpretação da hipótese

**Aprovada:** todas as cinco médias e a média geral atingem pelo menos 0,8. A variante reduzida não foi reprovada.

O F1 caiu de 0,8626 para 0,8401 e a Precision de 0,8693 para 0,8433 em relação à referência histórica. A direção é compatível com a hipótese de menor cobertura e foco, mas não prova o efeito isolado de cada componente: foram retirados dois componentes e as avaliações ocorreram em momentos diferentes. A previsão de que restaurar as regras ou os exemplos melhore as notas ainda depende das próximas medições.

A possibilidade de respostas menores não se confirmou nesta comparação: a média aumentou de **403,9 para 425,4 palavras**. Os modelos registrados permaneceram `gpt-5.4` e `gpt-5.5`, com provider `openai`.

Esta página preserva os resultados da primeira iteração. A preparação da segunda variante está registrada separadamente em [iteracao-02.md](iteracao-02.md).
