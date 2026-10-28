# Análise da avaliação do prompt v2

A revisão usa dois arquivos fornecidos pelo usuário: o CSV inicial `promptmateusmba-bug_to_user_story_v2-16d0cf3c.csv` e o [dataset com comentários dos juízes](../datasets/dataset_149f4388-af23-4269-b6a8-203bf9af378f.csv). O segundo exporta 36 linhas de avaliação, cada uma com relato, referência, resposta gerada, cinco notas e justificativas em `results`.

## Separação dos experimentos

O arquivo não representa uma única execução. As médias precisam ser calculadas por `experiment`:

| Experimento, sufixo | Casos | Helpfulness | Correctness | F1-Score | Clarity | Precision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `2989088b` | 15 | 0,8090 | 0,7963 | 0,7665 | 0,7920 | 0,8260 |
| `16d0cf3c` | 15 | 0,7940 | 0,7824 | 0,7555 | 0,7787 | 0,8093 |
| `fbf15da8` | 6 | 0,8183 | 0,8016 | 0,7665 | 0,8000 | 0,8367 |

O experimento de seis casos é parcial; não permite comparar a média geral diretamente com os de 15. No `2989088b`, 11 dos 15 exemplos ficam abaixo de 0,8 em F1. No `16d0cf3c`, são 12 dos 15. A aprovação do script considera as médias das métricas no dataset, não a aprovação individual de todos os exemplos.

As 15 respostas de `16d0cf3c` são idênticas às do CSV inicial. Nenhuma dessas notas comprova o desempenho do YAML após as revisões desta sessão.

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

Para evitar avaliar uma revisão diferente da editada:

- O push calcula SHA256 das mensagens System/User e registra a identificação no prompt e na descrição do commit.
- A avaliação calcula o mesmo SHA256 do YAML local e das mensagens recuperadas do Hub, sem cache.
- Se houver diferença, interrompe antes de criar o modelo ou iniciar o experimento.
- O experimento registra `prompt_local_sha256`, `prompt_remote_sha256` e `prompt_hub_commit_hash`.
- O hash ignora metadados injetados pelo Hub e considera os templates originais, preservando a distinção entre chaves literais e variáveis.
- As tags publicadas refletem as técnicas reais do YAML, sem declarar Skeleton of Thought.

## Validação e próxima medição

```bash
PYTHONDONTWRITEBYTECODE=1 venv/bin/python -m pytest tests/ -q -p no:cacheprovider
```

Resultado: **41 testes passaram**, incluindo os 24 de estrutura/renderização e 17 testes com mocks para identificar a versão e bloquear divergências. Esses testes não geram respostas nem estimam as novas métricas.

Nenhuma publicação ou nova avaliação externa foi executada nesta revisão. A execução pela API permanece dependente da autorização explícita solicitada anteriormente; a revisão automática rejeitou o envio dos relatos à OpenAI sem essa autorização. Portanto, não há notas novas comprovando > 0,8.

Para medir a revisão no fluxo existente:

```bash
venv/bin/python src/push_prompts.py
venv/bin/python src/evaluate.py
```

O push publica o prompt como público no Hub. A avaliação usa essa versão após compará-la com o YAML, aplica os mesmos juízes aos 15 casos e imprime o link do experimento. Preserve os modelos entre rodadas, registre os hashes e compare os 15 casos completos antes de concluir que a meta foi atingida.
