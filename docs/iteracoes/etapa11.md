# Etapa 11 — Histórico das avaliações e decisão de encerramento

Este documento preserva a auditoria histórica da referência aprovada. O novo ciclo foi concluído com três variantes identificadas por commits Git/Hub e hashes: [iteração 01](iteracao-01.md), Git [2c5e310](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/2c5e310c46ac210d00784b445e7366186e41c276), experimento `bd3aa4bf`, média **0,8492**; [iteração 02](iteracao-02.md), Git [b6bcdd7](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/b6bcdd76ba6784d9e9fdcda4bd5449ce20f4977e), experimento `d29b125d`, média **0,8659**; e [iteração 03](iteracao-03.md), Git [05bf7a2](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/05bf7a2e68a5c9a7e8a5aecc3b014ef3cf7c8807), experimento `1419119b`, média **0,8548**. As três foram aprovadas. O YAML ativo contém a versão completa da terceira rodada; os CSVs estão organizados em [Resultados](../resultados/README.md).

A limitação de identificação dos experimentos antigos, descrita abaixo, permanece restrita ao histórico. O novo ciclo possui três variantes efetivamente avaliadas e rastreadas. A segunda teve a maior média nesta comparação; a versão completa final também foi aprovada. As hipóteses e os casos fracos de cada rodada estão nos registros próprios.

A auditoria de 28/10/2026 recuperou **três avaliações completas com 15 casos cada**, confirmou as cinco médias finais acima de 0,8 e revisou os cinco exemplos finais com alguma nota individual abaixo desse limite. O prompt aprovado foi mantido. Nesta etapa foram consultados os registros existentes, sem novas gerações, publicação ou avaliação por modelos.

O histórico contém três avaliações completas e três revisões publicadas, mas **não comprova três revisões distintas avaliadas**. Os CSVs antigos não registram o commit do Hub nem o SHA256 das mensagens. As hipóteses deste documento foram reconstruídas a partir dos comentários preservados e das diferenças observáveis entre os prompts publicados; não são anotações anteriores às execuções. A identidade da revisão está comprovada para a avaliação final.

## Configuração e fontes

| Item | Valor conferido |
| --- | --- |
| Provider | `openai` |
| Gerador | `gpt-5.4` |
| Avaliador | `gpt-5.5` |
| Temperatura configurada no código | `0` |
| Dataset | `datasets/bug_to_user_story.jsonl`: 15 casos, sendo 5 simples, 7 médios e 3 complexos |
| Dataset remoto atual | `mba-ia-pull-evaluation-prompt-eval`, ID `5d70698d-a1a2-4bec-8551-270fbf6165b3` |
| Prompt | `promptmateusmba/bug_to_user_story_v2` |
| Critério de aprovação | Média de cada uma das cinco métricas e média geral ≥ 0,8 |

Os metadados dos runs confirmam os mesmos nomes de modelos e provider nas três avaliações completas. Os 15 pares de entrada e referência de cada CSV histórico e do dataset remoto foram comparados ao JSONL local e correspondem ao seu conteúdo. Isso permite comparar os registros disponíveis, preservando a limitação sobre a identidade dos prompts antigos. Nomes iguais de modelos e temperatura zero não garantem respostas idênticas nem isolam o efeito causal de uma mudança.

Fontes recuperadas:

- `promptmateusmba-bug_to_user_story_v2-2989088b.csv` e `promptmateusmba-bug_to_user_story_v2-16d0cf3c.csv`: respostas, cinco notas por caso e metadados de execução.
- `dataset_149f4388-af23-4269-b6a8-203bf9af378f.csv`: comentários dos juízes das duas avaliações acima e seis registros de uma execução parcial.
- `promptmateusmba-bug_to_user_story_v2-bdd2693f.csv`: tentativa com falhas operacionais, excluída da comparação de qualidade.
- API autenticada do LangSmith: 15 runs sem erro e 75 feedbacks da avaliação final, estatísticas do experimento, exemplos do dataset atual e três revisões do Hub.

Os CSVs originais foram encontrados na pasta local de downloads. Suas notas, comentários e metadados relevantes estão preservados em [resultados.json](resultados.json), junto dos SHA256 das fontes. O artefato permite recalcular as métricas sem depender desses arquivos locais. Os registros históricos não foram encontrados na listagem atual de experimentos; sua fonte é a exportação preservada.

## Avaliações completas

As duas linhas históricas não estabelecem sua ordem cronológica nem identificam uma alteração de prompt entre elas.

| Avaliação | Casos | Helpfulness | Correctness | F1-Score | Clarity | Precision | Média geral | Decisão |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Histórico `2989088b` | 15 | 0,8090 | 0,7963 | 0,7665 | 0,7920 | 0,8260 | 0,7980 | Meta não atingida; revisar cobertura e concisão. |
| Histórico `16d0cf3c` | 15 | 0,7940 | 0,7824 | 0,7555 | 0,7787 | 0,8093 | 0,7840 | Meta não atingida; revisar cobertura e concisão. |
| Final `8c034dd1` | 15 | 0,8697 | 0,8660 | 0,8626 | 0,8700 | 0,8693 | **0,8675** | **Aprovado; manter o prompt após revisar os casos fracos.** |

As médias usam as notas individuais antes do arredondamento. A média geral considera as cinco médias com sua precisão original. Nenhuma nota das execuções parcial ou com falhas participa dessa tabela.

| Indicador de revisão | `2989088b` | `16d0cf3c` | Final `8c034dd1` |
| --- | ---: | ---: | ---: |
| Casos com F1 abaixo de 0,8 | 11/15 | 12/15 | 4/15 |
| Casos com alguma métrica abaixo de 0,8 | 13/15 | 12/15 | 5/15 |
| Média de palavras por resposta | 700,1 | 697,1 | 403,9 |

A avaliação final apresenta menos texto e maior cobertura medida pelo F1 em relação aos dois registros históricos. A comparação descreve os resultados observados; não demonstra qual ajuste, isoladamente, produziu a diferença.

## Hipóteses reconstruídas e alterações observáveis

| Evidência nos feedbacks históricos | Hipótese retrospectiva | Comportamento presente no prompt final | Resultado observado / decisão |
| --- | --- | --- | --- |
| Respostas extensas, repetição entre seções e perguntas que não bloqueiam requisitos claros. | Profundidade proporcional e remoção de investigações de rotina devem melhorar clareza e foco. | Limites aproximados de 150/350/1000 palavras; efeitos do mesmo evento em linhas `E`; exclusão de hipóteses e perguntas rotineiras. | Clarity final 0,8700 e média de 403,9 palavras; manter, reconhecendo a redundância residual no caso 7. |
| Omissões de confirmação visual, atualização de estado e resultados das integrações. | Cobrir a ação e seus efeitos imediatos deve melhorar a completude funcional. | Regras explícitas para confirmação, estado associado, transições de integração e tratamento do resultado. | F1 final 0,8626; revisar os casos 4 e 5, que ainda omitem resultados esperados. |
| Critérios como “estado consistente” e soluções conhecidas transformadas em perguntas. | Separar fatos, requisitos futuros e propostas deve permitir critérios concretos sem inventar fatos. | Bloco “Fatos, requisitos e propostas”, contratos propostos identificados e rejeição de critérios vagos. | Precision final 0,8693; manter a distinção e registrar propostas excessivas do caso 4. |
| Casos complexos cobrem sintomas, mas deixam ações técnicas e efeitos sem especificação. | Um cenário por falha e ações ligadas ao diagnóstico devem aumentar cobertura. | Regras por domínio e seis demonstrações, incluindo exportação complexa, autorização e cálculo. | Checkout final com F1 0,8845; relatórios gerenciais ainda com F1 0,7747, analisado abaixo. |

As diferenças entre revisões foram confirmadas recuperando o conteúdo dos três commits do Hub:

| Commit do Hub | Publicação, horário de São Paulo | Conteúdo observado | Vínculo com avaliação |
| --- | --- | --- | --- |
| `b6ac3f78` | 26/10/2026, 01:50 | Product Owner, classificação mecânica de complexidade, checklist obrigatório e quatro demonstrações; declara Skeleton of Thought no formato. | Sem vínculo comprovado com os CSVs antigos. |
| `ec5e2ae7` | 28/10/2026, 00:13 | Analista de requisitos, classificação contextual, maior cautela com propostas e quatro demonstrações. | Sem avaliação completa identificada por hash. |
| `42343f3e` | 28/10/2026, 02:05 | Cobertura explícita, fatos/requisitos/propostas, concisão por complexidade e seis demonstrações; sem declaração de Skeleton of Thought. | Confirmado nos metadados de `8c034dd1`. |

O Git registrado nos três experimentos é `a94ce44-dirty`: indica código com alterações locais, não uma revisão do prompt. Os commits posteriores do repositório não alteram retroativamente essa identificação.

Identificação da avaliação final:

```text
Experimento: promptmateusmba-bug_to_user_story_v2-8c034dd1
ID: 03725a14-86f3-4d00-9481-5b1821c82b70
Commit Hub: 42343f3e00c6f179ab050fc92b67e10b81970d7b85bd24923a38c58bef58153c
SHA256 das mensagens: 727f2c278765824fe9cb44d329a540a2a3979c98973204a94d9edf8d9e2433d9
```

Na auditoria, o SHA256 coincidiu no YAML local, no prompt recuperado sem cache e nos dois campos de identificação do experimento. A cópia da referência aprovada preserva esse conteúdo, restaurado e novamente avaliado na iteração 03 com o mesmo fingerprint e novo experimento. A avaliação histórica está disponível no [LangSmith](https://smith.langchain.com/o/2c51ef9f-d3a5-4178-8c6f-d5729a609c19/datasets/5d70698d-a1a2-4bec-8551-270fbf6165b3/compare?selectedSessions=03725a14-86f3-4d00-9481-5b1821c82b70); o [dataset público](https://smith.langchain.com/public/f4f47f9e-2f88-4cac-9c1e-568c8f4970a9/d) e as [capturas](../evidencias/) complementam o registro.

## Execuções excluídas

| Execução | Evidência | Tratamento |
| --- | --- | --- |
| `fbf15da8` | Exportação com seis casos. | Parcial; sem comparação de médias com os experimentos completos. |
| `bdd2693f` | 15 tentativas, nove gerações bem-sucedidas e seis erros HTTP 429: cinco por tokens/minuto e um por requisições/dia. | Falha operacional; zeros e notas afetados por erros não aprovam nem reprovam o prompt. |

Uma execução com 15 linhas não basta: é preciso verificar o sucesso das gerações e dos juízes. O registro deste documento faz essa separação. O avaliador fornecido ainda pode converter falhas dos juízes em zero; não foi alterado nesta etapa.

## Revisão dos cinco casos finais abaixo de 0,8

Os números dos casos seguem a ordem do JSONL. As justificativas integrais dos três juízes foram preservadas no JSON; abaixo estão a análise e a decisão de revisão.

| Caso | Notas abaixo de 0,8 | Leitura do feedback e da resposta | Decisão |
| --- | --- | --- | --- |
| 4 — dashboard de usuários ativos | F1 0,7838; Precision 0,77; Correctness 0,7769 | Cobre 42 versus 50, mas repete o exemplo em cenário separado, propõe regras de consulta e condiciona a atualização sem recarga. O juiz cobra papel administrativo, status ativo e atualização em tempo real. | Registrar a necessidade de critérios mais diretos e menos propostas de arquitetura. O papel e o tempo de atualização da referência não devem ser tratados como fatos fornecidos no relato. |
| 5 — imagens no Safari | F1 0,7969 | Garante exibição no Safari e preservação no Chrome, mas omite equivalência explícita de qualidade e tempo; acrescenta detalhes técnicos e repete o contexto. | A regra de compatibilidade do prompt já pede qualidade e carregamento comparáveis; a resposta não a cumpre integralmente. Registrar a omissão sem introduzir tecnologias ou tempos fixos. |
| 7 — relatório de vendas | Clarity 0,78 | Cobre índice em `data_venda`, mais de 1000 registros e timeout de 120s, mas repete fatos e acrescenta fluxo assíncrono. O juiz cobra 30s como obrigação, embora esse valor não esteja no relato. | Priorizar concisão em eventual rodada futura; preservar 30s como proposta, sem convertê-lo em SLA existente. |
| 12 — modal atrás do menu | F1 0,7503 | Cobre tela <768px, botões clicáveis e empilhamento, mas não explicita `z-index > 1050`, foco e fechamento por teclado; o juiz também cobra largura de 90% ausente do relato. | Registrar omissões de acessibilidade e de concretude da proposta. Não fixar 90% como regra geral para aumentar a nota. |
| 14 — relatórios gerenciais | F1 0,7747 | Cobre N+1, SLA de 3s, MRR, cache e exportação; falta notificação de conclusão e a atualização do cache permanece pouco mensurável. O juiz também cobra 10 mil usuários, CPU <70%, lotes de 1000, sprints e uma regra financeira ausentes ou indefinidos no relato. | Registrar as lacunas úteis e manter a decisão de MRR pendente: o relato diz que nenhuma fonte está correta. Não adotar valores da referência nem inventar cronograma. |

Os três casos complexos foram conferidos: checkout com F1 **0,8845**, relatórios gerenciais com **0,7747** e sincronização offline com **0,8154**. A nota fraca do caso 14 não foi escondida pela média geral.

As rubricas comparam a saída a referências que contêm decisões adicionais. Parte da perda de recall decorre dessas decisões; outra parte revela omissões úteis ou descumprimento das próprias instruções. A análise distingue essas situações em vez de adaptar o prompt a cada resposta esperada.

## Encerramento e conferência reproduzível

O critério de qualidade foi atendido: cinco médias ≥0,8, média geral **0,8675**, 15 casos completos e exemplos problemáticos revisados. A decisão é manter o commit `42343f3e`. A auditoria encerra a etapa com o histórico recuperável e sua limitação de rastreabilidade explícita; não afirma que houve três ciclos distintos de edição e avaliação comprovados por hash.

Para recalcular os registros arquivados, sem rede nem chamadas a modelos:

```bash
venv/bin/python docs/iteracoes/conferir_resultados.py
```

O comando confere 45 casos, 225 notas, fórmulas derivadas, modelos registrados, hashes dos exemplos e identidade do JSONL. A execução desta etapa também aprovou os **24 testes atuais** de estrutura e renderização:

```bash
PYTHONDONTWRITEBYTECODE=1 venv/bin/python -m pytest tests/test_prompts.py -v -p no:cacheprovider
```

Se houver uma nova hipótese a testar, registre-a **antes** da edição, altere um grupo coerente de regras e execute testes → push → avaliação, mantendo dataset e modelos. Registre o hash exibido no push, commit do Hub, experimento e decisão. O avaliador foi restaurado à versão original e não registra automaticamente os hashes local e remoto. Essa medição futura avalia uma nova revisão; não recupera a identificação ausente dos CSVs históricos.
