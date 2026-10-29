# Análise da avaliação do prompt v2

Esta análise descreve a [referência aprovada](iteracoes/referencia/bug_to_user_story_v2_aprovado.yml). O novo ciclo de três rodadas foi concluído, com médias **0,8492**, **0,8659** e **0,8548**, todas aprovadas. O prompt ativo é a versão completa da [iteração 03](iteracoes/iteracao-03.md), commit Git [05bf7a2](https://github.com/ma7euus/mba-ia-pull-evaluation-prompt/commit/05bf7a2e68a5c9a7e8a5aecc3b014ef3cf7c8807) e experimento `1419119b`. As notas abaixo pertencem à referência histórica; os resultados atuais estão nos registros de cada rodada e em [Resultados](resultados/README.md).

A análise histórica usa dois arquivos fornecidos pelo usuário: o CSV inicial `promptmateusmba-bug_to_user_story_v2-16d0cf3c.csv` e `dataset_149f4388-af23-4269-b6a8-203bf9af378f.csv`. O segundo exporta 36 linhas de avaliação, cada uma com relato, referência, resposta gerada, cinco notas e justificativas em `results`. As notas e justificativas das duas avaliações completas foram preservadas em [resultados.json](iteracoes/resultados.json). A [auditoria da etapa 11](iteracoes/etapa11.md) acrescenta a avaliação final aprovada, a identificação do prompt e a análise dos casos fracos.

## Separação dos experimentos

O arquivo não representa uma única execução. As médias precisam ser calculadas por `experiment`:

| Experimento, sufixo | Casos | Helpfulness | Correctness | F1-Score | Clarity | Precision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `2989088b` | 15 | 0,8090 | 0,7963 | 0,7665 | 0,7920 | 0,8260 |
| `16d0cf3c` | 15 | 0,7940 | 0,7824 | 0,7555 | 0,7787 | 0,8093 |
| `fbf15da8` | 6 | 0,8183 | 0,8016 | 0,7665 | 0,8000 | 0,8367 |

O experimento de seis casos é parcial; não permite comparar a média geral diretamente com os de 15. No `2989088b`, 11 dos 15 exemplos ficam abaixo de 0,8 em F1. No `16d0cf3c`, são 12 dos 15. A aprovação do script considera as médias das métricas no dataset, não a aprovação individual de todos os exemplos.

As 15 respostas de `16d0cf3c` são idênticas às do CSV inicial. Esses registros históricos não identificam o commit do prompt avaliado. A correspondência entre o YAML aprovado e a avaliação final `8c034dd1` foi confirmada separadamente na auditoria da etapa 11.

## O que os juízes apontaram

| Padrão nos comentários | Exemplos de lacuna | Mudança na revisão atual |
| --- | --- | --- |
| Excesso de texto, hipóteses e pendências | As respostas dos dois experimentos completos têm em média 700 e 697 palavras. | Encerrar casos simples após os critérios; remover investigações e perguntas de rotina; agrupar efeitos do mesmo evento. |
| Critérios genéricos ou condicionais | “Convergir para um estado consistente”, “regra prevista” e “prazo definido” não dizem como testar. | Identificar estado final, dado, mensagem, ação bloqueada e limite concreto. |
| Resultados imediatos incompletos | Contador do carrinho; mensagem explicando o formato do email; qualidade e tempo comparáveis no Safari; alinhamento no iOS. | Cobrir ação, confirmação e atualização do estado pertinente no mesmo cenário. |
| Diagnóstico sem orientação de correção | Falta de índice, thread principal, N+1, cache desatualizado e z-index aparecem sem ação correspondente. | Indicar ação técnica proporcional ao diagnóstico relatado, sem afirmar uma investigação própria. |
| Integrações e autorização pouco específicas | HTTP 200/403, pedido “aprovado”, confirmação ao cliente, auditoria e middleware omitidos. | Propor contratos explícitos quando ausentes e preservar as regras de acesso já informadas. |
| Soluções técnicas excessivamente cautelosas | Retry com backoff, idempotência, controle atômico, background e streaming ficam em perguntas ou formulações vagas. | Reunir escolhas em “Soluções propostas” e depois descrevê-las concretamente, sem repetir ressalvas em cada linha. |
| Cobertura complexa incompleta | Preservação de versões, resolução de conflito, retomada real, progresso, ordenação e controle da memória. | Um cenário por falha, com volumes e limites recebidos e mecanismos pertinentes identificados como propostas. |
| Falta de parâmetros mensuráveis | Juízes cobram metas de tempo, paginação e limites não fornecidos nos relatos. | Permitir metas iniciais explícitas com cenário de medição e aprovação pelo time, sem apresentá-las como SLAs acordados. |

## Ajustes do prompt

A revisão mantém Role Prompting e análise interna em sete etapas, mas amplia as demonstrações de quatro para seis:

1. Podcast: resultado concreto e resposta curta.
2. Receita favorita: ação, confirmação e atualização do estado.
3. Sessão de estudos: cálculo, datas e exemplo numérico.
4. Documentos privados: contratos HTTP propostos, autorização e auditoria.
5. Exportação de fluxogramas: múltiplos problemas, ações técnicas e meta mensurável proposta.
6. Digitalização ambígua: critérios em aberto e perguntas específicas.

Os relatos das demonstrações são distintos dos casos avaliados; as referências não são copiadas para as respostas do prompt. Não há tabela de respostas por ID ou condicionamento aos nomes dos experimentos.

A distinção central é entre **fato relatado**, **resultado futuro necessário** e **escolha proposta**. Um endpoint sem contrato informado pode receber uma proposta de HTTP 200/403; a resposta não deve afirmar que esse contrato já existe. Uma meta de desempenho ausente pode receber uma proposta inicial mensurável, mas não virar um SLA acordado por suposição.

Algumas referências contêm decisões adicionais: Android em dois segundos e páginas de 20 itens, relatório em 30 segundos, modal com 90% da largura, reserva de estoque por 15 minutos e sincronização em lotes de 50 com limite de 500 MB. O prompt não codifica esses valores por caso. Permite propostas pertinentes e preserva como pendência a decisão financeira ou de negócio que não possa ser inferida com segurança. As rubricas, as fórmulas e o dataset foram preservados.

## Identificação da versão realmente avaliada

As respostas do CSV ainda contêm listas extensas de hipóteses, pendências e cenários provisórios para necessidades claras, padrões já restringidos no YAML local anterior. Isso sugere uso de uma versão diferente no Hub, mas não prova qual: o arquivo não contém hash das mensagens nem commit do prompt. O campo `revision_id=a94ce44-dirty` identifica o código Git, não a versão publicada.

O push mantém os seguintes registros de identificação:

- O push calcula SHA256 das mensagens System/User e registra a identificação no prompt e na descrição do commit.
- O hash ignora metadados injetados pelo Hub e considera os templates originais, preservando a distinção entre chaves literais e variáveis.
- As tags publicadas refletem as técnicas reais do YAML, sem declarar Skeleton of Thought.

Nas execuções arquivadas com rastreabilidade, o avaliador também comparava o SHA256 do YAML local ao das mensagens recuperadas do Hub sem cache, interrompia a execução em caso de divergência e registrava `prompt_local_sha256`, `prompt_remote_sha256` e `prompt_hub_commit_hash` no experimento. Esses registros históricos foram preservados.

Para atender à exigência do enunciado de preservar os arquivos fornecidos, `src/evaluate.py` e `src/utils.py` foram restaurados à versão original. O avaliador atual recupera a versão publicada no Hub sem comparar hashes nem acrescentar esses três metadados. Antes de uma nova avaliação, faça o push e confira no Hub o conteúdo e o commit que será avaliado.

## Validação e avaliação histórica

```bash
PYTHONDONTWRITEBYTECODE=1 venv/bin/python -m pytest tests/ -q -p no:cacheprovider
```

Resultado conferido na etapa 11: **24 testes passaram**, correspondentes à suíte atual de estrutura e renderização. Esses testes não geram respostas nem estimam métricas.

A consulta à API do LangSmith confirmou 15 gerações sem erro e 75 feedbacks na avaliação final `8c034dd1`: Helpfulness **0,8697**, Correctness **0,8660**, F1-Score **0,8626**, Clarity **0,8700**, Precision **0,8693** e média geral **0,8675**. O commit do Hub `42343f3e` e o SHA256 das mensagens coincidem com a cópia da referência aprovada e com os metadados do experimento.

A auditoria recuperou os registros existentes e manteve o prompt aprovado, sem nova publicação ou geração. O histórico, as hipóteses retrospectivas, as execuções excluídas e a revisão dos cinco casos fracos estão em [Etapa 11](iteracoes/etapa11.md).

Para medir uma futura alteração no fluxo existente:

```bash
venv/bin/python src/push_prompts.py
venv/bin/python src/evaluate.py
```

O push publica o prompt como público no Hub. A avaliação recupera o prompt publicado, aplica os mesmos juízes aos 15 casos e imprime o link do experimento. Preserve os modelos entre rodadas, registre a hipótese antes da edição e guarde o hash exibido no push e o commit do Hub. Confira falhas de geração e dos juízes antes de usar as médias.
