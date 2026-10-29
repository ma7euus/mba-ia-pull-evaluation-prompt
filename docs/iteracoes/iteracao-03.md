# Iteração 03 — Versão completa

Estado: **concluída e aprovada por médias**, com média geral **0,8548**. O usuário criou o commit da versão completa, publicou e avaliou o prompt. A exportação está em [CSV da iteração 03](../resultados/iteracao-03_versao-completa_1419119b.csv), e os três arquivos estão organizados em [Resultados](../resultados/README.md).

## Hipótese registrada antes da avaliação

Restaurar os seis exemplos completos, mantendo as regras de cobertura e as demais instruções da segunda rodada, pode melhorar a cobertura e a consistência das respostas. A hipótese principal é obter F1 médio maior que **0,8636**, resultado da iteração 02. Precision e Clarity também serão comparadas, sem presumir ganho de nota ou redução de texto.

A intervenção nas mensagens é um único grupo: as quatro demonstrações adicionais. Foram reintegrados os exemplos 2 (favoritos), 3 (cálculo entre datas), 4 (autorização) e 6 (resultado ambíguo), preservando integralmente os exemplos 1 e 5. Persona, sete etapas, formato, regras de cobertura, concisão, exceções, User e variável `bug_report` permanecem iguais aos da segunda rodada.

## Restauração da versão completa

O [prompt ativo](../../prompts/bug_to_user_story_v2.yml) foi restaurado **byte a byte** a partir da [referência completa preservada](referencia/bug_to_user_story_v2_aprovado.yml), incluindo a descrição original. O conjunto continua usando Role Prompting, Chain of Thought e Few-shot Learning. Dataset, avaliadores, métricas e testes não foram alterados.

| Componente | Iteração 02 | Iteração 03 |
| --- | --- | --- |
| Demonstrações | Dois pares: exemplos 1 e 5. | Seis pares: exemplos 1 a 6. |
| Regras de cobertura | Bloco completo. | Preservado integralmente. |
| Demais instruções e User | Conteúdo da segunda rodada. | Preservado integralmente. |
| Descrição do YAML | Identificação da variante intermediária. | Descrição original da versão completa. |

Os exemplos restaurados são os mesmos da referência, distintos dos 15 casos de avaliação. Nenhuma resposta de referência do dataset foi inserida no prompt. A descrição é metadado; a mudança nas mensagens efetivas se limita às quatro demonstrações.

## Identificação e configuração

| Registro | Valor |
| --- | --- |
| Commit Git da iteração 03 | [05bf7a2e68a5c9a7e8a5aecc3b014ef3cf7c8807](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/05bf7a2e68a5c9a7e8a5aecc3b014ef3cf7c8807) — “Versão completa: restaurar os seis exemplos, chegando ao prompt aprovado.” |
| Commit Hub da iteração 03 | `d2a6b0313a4351c1a7e51c0912a33ee74b81b0d8007da925e879423e5ebf2496` |
| Experimento | `promptmateusmba-bug_to_user_story_v2-1419119b` |
| ID do experimento | `8641a25b-eae7-48af-8535-ad3ea10df020` |
| Revisão Git registrada nos runs | `05bf7a2-dirty` |
| Base de comparação | Iteração 02, Git [b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e), experimento `d29b125d`, resultado em [CSV da iteração 02](../resultados/iteracao-02_cobertura-restaurada_d29b125d.csv). |
| Provider / gerador / avaliador registrados | `openai` / `gpt-5.4` / `gpt-5.5`, mantendo a configuração das duas rodadas anteriores. |
| Temperatura configurada | `0` |
| Dataset | `mba-ia-pull-evaluation-prompt-eval`; inputs e referências dos 15 casos conferidos contra o JSONL local. |
| Nome do prompt e entrada | `bug_to_user_story_v2`; somente `bug_report`. |

SHA256 das mensagens efetivas:

```text
Iteração 02: 864509da07789fae7c5487e12a3b672424bc737fc35b9a66d39728754c7a7864
Iteração 03: 727f2c278765824fe9cb44d329a540a2a3979c98973204a94d9edf8d9e2433d9
```

SHA256 do arquivo YAML completo da iteração 03:

```text
e1f8c3fb7403ad21e1c1778ea4d48e591b8b6d119bdbee724960f1624304ac8e
```

O fingerprint e o arquivo coincidem com a referência histórica e com o YAML do commit [05bf7a2](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/05bf7a2e68a5c9a7e8a5aecc3b014ef3cf7c8807). Os hashes local e remoto registrados nos 15 runs coincidem com o fingerprint acima. A execução desta rodada é identificada pelo novo experimento `1419119b`, pelo commit do Hub e pela revisão Git; sua média foi calculada do novo CSV. A média histórica **0,8675** de `8c034dd1` não foi reutilizada. O sufixo `-dirty` foi preservado: indica alterações locais na árvore de trabalho durante a execução, e a correspondência do prompt com o commit foi verificada diretamente.

SHA256 do CSV, preservado após a movimentação e a mudança de nome:

```text
8e810053a25ee2fc09c79b267278d26f36618ca6336161a1ac2e0b5a7f72a57b
```

## Resultados das três rodadas

A terceira exportação contém 15 gerações com status `success`, nenhum erro de geração registrado e 75 notas preenchidas. Os scores estão entre 0 e 1, as respostas não estão vazias e as fórmulas derivadas foram conferidas. Os pares de input e referência correspondem ao JSONL local e às duas rodadas anteriores. As 15 respostas diferem das respostas das duas primeiras execuções.

| Métrica | Iteração 01 | Iteração 02 | Iteração 03 |
| --- | ---: | ---: | ---: |
| Helpfulness | 0,8547 | 0,8673 | 0,8590 |
| Correctness | 0,8417 | 0,8638 | 0,8471 |
| F1-Score | 0,8401 | 0,8636 | 0,8501 |
| Clarity | 0,8660 | 0,8707 | 0,8740 |
| Precision | 0,8433 | 0,8640 | 0,8440 |
| **Média geral** | **0,8492** | **0,8659** | **0,8548** |

As médias exatas da terceira rodada são Helpfulness **0,859**, Correctness **0,84706**, F1 **0,8500866666666667**, Clarity **0,874** e Precision **0,844**. A média geral é **0,8548293333333333**. Todas as cinco médias e a média geral são ≥0,8: **a versão completa foi aprovada**.

| Métrica | Diferença, terceira − segunda |
| --- | ---: |
| Helpfulness | −0,0083 |
| Correctness | −0,0167 |
| F1-Score | −0,0135 |
| Clarity | +0,0033 |
| Precision | −0,0200 |
| Média geral | −0,0110 |

As diferenças usam as médias antes do arredondamento. O F1 aumentou em sete casos e caiu em oito em relação à segunda rodada. A média de palavras diminuiu de **412,3 para 409,1**. Em relação à primeira rodada, a média geral aumentou **0,0056613333333333**, e o F1 aumentou **0,0099666666666667**.

## Casos abaixo da meta individual

Cinco casos têm alguma nota abaixo de 0,8; quatro têm F1 abaixo do limite. A aprovação por médias não representa aprovação individual de todos os exemplos.

| Caso | Helpfulness | Correctness | F1-Score | Clarity | Precision |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 — adicionar ao carrinho | 0,8200 | 0,8386 | 0,8972 | 0,8600 | 0,7800 |
| 5 — imagens no Safari | 0,8150 | 0,7627 | 0,7553 | 0,8600 | 0,7700 |
| 12 — modal atrás do menu | 0,8500 | 0,7852 | 0,7503 | 0,8800 | 0,8200 |
| 14 — relatórios gerenciais | 0,8700 | 0,8124 | 0,7747 | 0,8900 | 0,8500 |
| 15 — sincronização offline | 0,8900 | 0,8444 | 0,7988 | 0,8900 | 0,8900 |

Entre os casos priorizados antes da execução, o caso 1 manteve Precision em 0,78; o caso 14 caiu de F1 0,7988 para 0,7747; o caso 15 aumentou de F1 0,7926 para 0,7988, ainda abaixo de 0,8. Safari e modal voltaram ao grupo de casos fracos. Os CSVs não incluem justificativas dos juízes, portanto não foram atribuídas causas específicas às notas ou auditados feedbacks operacionais ausentes das exportações.

## Interpretação e decisão final

A hipótese de F1 maior que **0,8636** **não se confirmou nesta execução**: a terceira rodada obteve **0,8501**. Clarity aumentou, mas Precision e as demais médias diminuíram em relação à segunda. Os resultados não apresentam melhora monotônica com o aumento do número de exemplos.

A segunda variante teve a maior média entre as três medições atuais (**0,8659**). A versão completa permanece como a versão final solicitada e foi aprovada com **0,8548**. Uma medição por variante não demonstra superioridade robusta nem permite atribuir a queda exclusivamente aos exemplos; o prompt completo também apresentou média histórica diferente com o mesmo fingerprint.

O ciclo é encerrado com três variantes avaliadas, hipóteses registradas, commits Git/Hub e hashes conferidos. A versão completa e as notas das exportações foram preservadas.

## Validação e execução realizada

Os **24 testes passaram** com a versão completa, incluindo os seis exemplos, a estrutura obrigatória, a variável `bug_report` e a renderização dos 15 relatos. A restauração exata da referência e a preservação das demais mensagens em relação à segunda rodada também foram conferidas.

```bash
PYTHONDONTWRITEBYTECODE=1 venv/bin/python -m pytest tests/test_prompts.py -v -p no:cacheprovider
```

Após a validação, o usuário criou o commit [05bf7a2](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/05bf7a2e68a5c9a7e8a5aecc3b014ef3cf7c8807) e executou a publicação e a avaliação. O CSV exportado preserva os registros desses passos:

```bash
git rev-parse HEAD
venv/bin/python src/push_prompts.py
venv/bin/python src/evaluate.py
```

Os três CSVs originais foram organizados em [docs/resultados](../resultados/README.md), com nomes que identificam a iteração, a variante e o experimento. O conteúdo e os SHA256 dos arquivos foram preservados.
