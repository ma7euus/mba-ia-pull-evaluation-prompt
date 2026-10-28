# Pull, Otimização e Avaliação de Prompts com LangChain e LangSmith

Projeto do desafio de Prompt Engineering do MBA em Engenharia de Software com IA. O fluxo recupera um prompt inicial do LangSmith Prompt Hub, otimiza a conversão de relatos de bugs em User Stories, publica a versão otimizada e avalia suas respostas.

O objetivo é atingir **pelo menos 0,8 em cada uma das cinco métricas**: Helpfulness, Correctness, F1-Score, Clarity e Precision. O processo está organizado nas cinco fases do desafio.

## Como Executar

### Pré-requisitos

- Python 3.10 ou superior, Git e pip.
- Conta no LangSmith, API Key e handle público do Prompt Hub.
- API Key do provedor escolhido: OpenAI ou Google Gemini.

As dependências de LangChain, LangSmith, dos provedores e de testes estão em [requirements.txt](requirements.txt).

### Instalação

Execute no terminal:

```bash
# 1. Clonar o repositório
git clone https://github.com/ma7euus/mba-ia-pull-evaluation-prompt.git
cd mba-ia-pull-evaluation-prompt

# 2. Criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Instalar as dependências
pip install -r requirements.txt
```

### Configuração do `.env`

Copie o template e preencha as variáveis:

```bash
cp .env.example .env            # Windows: copy .env.example .env
```

| Variável | Descrição |
| --- | --- |
| `LANGSMITH_TRACING` | `true` para gravar os traces no LangSmith. |
| `LANGSMITH_ENDPOINT` | `https://api.smith.langchain.com`. |
| `LANGSMITH_API_KEY` | Sua API Key do LangSmith. |
| `LANGSMITH_PROJECT` | Nome do projeto; também é usado para montar o nome do dataset (`<projeto>-eval`). |
| `USERNAME_LANGSMITH_HUB` | Seu handle público do LangSmith Hub. |
| `LLM_PROVIDER` | `openai` ou `google`. |
| `OPENAI_API_KEY` | Obrigatória se o provider for `openai`. |
| `GOOGLE_API_KEY` | Obrigatória se o provider for `google`. |
| `LLM_MODEL` | Modelo que gera as User Stories. |
| `EVAL_MODEL` | Modelo que avalia as respostas; pode ser o mesmo ou um mais capaz. |

**Configuração que usei (valores atuais do `.env`):** provider `openai`, `LLM_MODEL=gpt-5.4` e `EVAL_MODEL=gpt-5.5`.

Para criar o handle, abra um prompt no LangSmith, acesse o menu de três pontos ao lado de **Playground**, selecione **Make Public** e defina o nome em **Choose your public handle**. Use esse valor em `USERNAME_LANGSMITH_HUB`.

### Sequência das fases

Execute os comandos na raiz do projeto, com o ambiente virtual ativo e o `.env` preenchido.

| Fase | Ação | Comando ou arquivo |
| --- | --- | --- |
| 1 | Recuperar o prompt original. | `python src/pull_prompts.py` |
| 2 | Revisar o prompt otimizado e as técnicas aplicadas. | `prompts/bug_to_user_story_v2.yml` |
| 3 | Publicar e avaliar a versão otimizada. | `python src/push_prompts.py` e `python src/evaluate.py` |
| 4 | Ajustar o prompt e repetir a publicação e a avaliação. | Ciclo descrito na Fase 4. |
| 5 | Validar a estrutura e os requisitos do prompt. | `pytest tests/test_prompts.py -v` |

Embora apareçam na Fase 5 do enunciado, execute os testes também antes de cada push.

## Fase 1 — Pull do Prompt Inicial

O script [pull_prompts.py](src/pull_prompts.py) recupera o prompt público `leonanluppi/bug_to_user_story_v1` e salva suas mensagens em [bug_to_user_story_v1.yml](prompts/bug_to_user_story_v1.yml).

```bash
python src/pull_prompts.py
```

A versão original contém orientações genéricas, repete `{bug_report}` nas mensagens System e User e não apresenta exemplos de entrada e saída nem um contrato explícito de resposta. Esse é o ponto de partida para a otimização.

## Técnicas Aplicadas (Fase 2)

O [prompt v2](prompts/bug_to_user_story_v2.yml) foi revisado a partir dos relatos, referências e comentários dos juízes. A revisão atual combina três técnicas e seis demonstrações independentes dos exemplos avaliados. A análise dos arquivos está em [Avaliação do v2](docs/avaliacao_prompt_v2.md).

| Técnica | Aplicação | Objetivo |
| --- | --- | --- |
| Role Prompting | Analista de requisitos com experiência em produto, engenharia e testes de aceitação. | Escrever a necessidade, seu benefício e uma correção que o time consiga verificar. |
| Chain of Thought | Análise interna em sete etapas, sem publicar o raciocínio. | Relacionar sintomas, resultados, contratos e ações técnicas antes de redigir. |
| Few-shot Learning | Seis pares de relato e resposta em `system_prompt`. | Demonstrar concisão, cobertura funcional, cálculos, autorização, propostas mensuráveis e tratamento de ambiguidade. |

### Análise interna

O roteiro identifica o papel e o benefício, extrai os fatos, mapeia cada falha para resultados, escolhe a profundidade, escreve cenários concretos, completa contratos e soluções pertinentes e revisa cobertura e foco. Seu cumprimento interno não pode ser comprovado pelo tracing; o que pode ser avaliado são as respostas e seus feedbacks.

### Demonstrações

| Exemplo | Situação | Comportamento demonstrado |
| --- | --- | --- |
| 1 | Avançar um podcast de 1:00 para 1:15 retrocede a reprodução. | Story curta com condição, ação e resultado exatos. |
| 2 | Salvar uma receita nos favoritos não inclui o item. | Inclusão, confirmação visual e atualização do estado associado no mesmo cenário. |
| 3 | Uma sessão de estudos que atravessa a meia-noite mostra duração negativa. | Cálculo com datas completas, exemplo numérico e preservação do caso correto informado. |
| 4 | Documentos privados são expostos a colaboradores de outras equipes. | Cenários de acesso negado e permitido, contrato HTTP proposto, middleware e auditoria. |
| 5 | Exportar fluxogramas desloca conectores, sobrepõe rótulos e bloqueia o editor. | Um cenário por problema, ações técnicas, preservação do documento e meta inicial de desempenho explicitamente proposta. |
| 6 | A digitalização de um documento “saiu errada”, sem indicar a diferença. | Story preliminar, critérios em aberto e duas perguntas específicas. |

Os seis relatos são distintos dos 15 casos do dataset. As respostas de referência da avaliação não foram incluídas nas demonstrações.

### Fatos, requisitos e propostas

O contrato distingue:

| Tipo de informação | Tratamento |
| --- | --- |
| Fato ou diagnóstico relatado | Preservar dados, condições e significado, sem afirmar investigação própria. |
| Requisito futuro | Especificar diretamente o resultado que comprova a correção e seus efeitos funcionais imediatos. |
| Contrato ou solução propostos | Identificar uma vez como proposta e descrever a escolha de forma concreta. |
| Meta ou parâmetro ausente, mas necessário | Propor valor mensurável com cenário de medição e aprovação pelo time; não apresentar como SLA existente. |
| Regra de negócio realmente indefinida | Manter a pendência específica sem enfraquecer os requisitos já conhecidos. |

Por exemplo, um endpoint sem contrato informado pode receber uma proposta explícita de HTTP 200/403; isso não afirma que o contrato já existe. Da mesma forma, uma meta proposta de tempo não é uma medição atual nem um requisito aprovado. O prompt proíbe inventar stack, causas confirmadas, baselines, regras financeiras, cronogramas ou metas de receita.

### Formato e cobertura

| Profundidade | Organização |
| --- | --- |
| Simples | Frase “Como um... eu quero... para que...” e critérios Dado/Quando/Então; até cerca de 150 palavras. |
| Médio | Story, critérios e complementos necessários para cálculos, integrações, permissões ou ações técnicas; até cerca de 350 palavras. |
| Complexo | Story principal, um cenário por problema, critérios técnicos e complementos úteis; até cerca de 1000 palavras. |

Não há mínimo de palavras, e a cobertura útil tem prioridade sobre os limites aproximados. Efeitos do mesmo evento usam linhas `E`, sem multiplicar cenários. Hipóteses, regressões e perguntas não são adicionadas por rotina. Relato breve com objetivo claro recebe critérios normais; somente ambiguidade real justifica critérios em aberto.

As regras de cobertura incluem confirmação e estado da interface, compatibilidade, cálculos, integração, segurança, desempenho, cache, concorrência e sincronização. Elas orientam resultados e mecanismos pertinentes, sem exigir todos os tópicos em toda resposta.

### Separação entre System e User

As instruções e demonstrações ficam na mensagem System. A mensagem User recebe o relato em `{bug_report}`, única variável do template. O texto do relato é tratado como dado, incluindo quando contém comandos ou tags.

O formato complexo é produzido em uma geração, sem expansão de um esqueleto intermediário; por isso **Skeleton of Thought não é uma técnica declarada**. O push usa as técnicas efetivamente listadas no YAML para gerar suas tags.

## Fase 3 — Push e Avaliação

Publique o prompt otimizado no LangSmith Prompt Hub:

```bash
python src/push_prompts.py
```

O script lê [bug_to_user_story_v2.yml](prompts/bug_to_user_story_v2.yml), valida sua estrutura, monta as mensagens System e User e publica o prompt como público em `{USERNAME_LANGSMITH_HUB}/bug_to_user_story_v2`. Confira o conteúdo, a descrição e as tags no Hub usando a URL exibida no terminal.

O push imprime o SHA256 das mensagens e registra essa identificação nos metadados e na descrição do commit do prompt. As tags refletem as técnicas declaradas no YAML.

Depois, execute a avaliação:

```bash
python src/evaluate.py
```

O avaliador recupera **a v2 publicada no Hub** e cria ou reutiliza o dataset `{LANGSMITH_PROJECT}-eval`, a partir de [bug_to_user_story.jsonl](datasets/bug_to_user_story.jsonl). São 15 relatos: 5 simples, 7 médios e 3 complexos. A cada execução, um experimento recebe as respostas e as cinco notas como feedback, e o terminal exibe seu link.

Antes de chamar os modelos, compara o SHA256 das mensagens do YAML com o prompt obtido do Hub sem cache. Se forem diferentes, interrompe a avaliação e pede um novo push. O experimento registra `prompt_local_sha256`, `prompt_remote_sha256` e `prompt_hub_commit_hash`, permitindo conferir qual versão foi avaliada. O campo `revision_id` de um CSV não substitui esses registros: ele identifica a revisão Git do código.

### Métricas e critério de aprovação

| Métrica | Como é obtida | Meta |
| --- | --- | --- |
| F1-Score | Média harmônica das estimativas de Precision e Recall de um juiz LLM: `2 × P × R / (P + R)`. | ≥ 0,8 |
| Clarity | Juiz LLM avalia organização, linguagem e clareza da resposta. | ≥ 0,8 |
| Precision | Juiz LLM avalia fidelidade ao relato, foco e ausência de informações inventadas. | ≥ 0,8 |
| Helpfulness | `(Clarity + Precision) / 2`. | ≥ 0,8 |
| Correctness | `(F1-Score + Precision) / 2`. | ≥ 0,8 |

A aprovação exige que **a média de cada métrica no dataset** e a média geral sejam pelo menos 0,8. Isso não significa que todos os exemplos individuais atingiram a meta; revise também os casos com notas baixas.

Se houver falha na geração ou nos juízes, a avaliação é marcada como **incompleta**. O link do experimento é preservado, e notas parciais não são usadas para aprovar ou reprovar o prompt. Resolva a falha e execute novamente.

## Fase 4 — Iteração

O desafio prevê **3–5 iterações**. Em cada rodada, examine os feedbacks e os traces dos casos com notas baixas, registre uma hipótese de melhoria e ajuste [bug_to_user_story_v2.yml](prompts/bug_to_user_story_v2.yml).

Repita o ciclo:

```bash
# Após editar o prompt local
pytest tests/test_prompts.py -v
python src/push_prompts.py
python src/evaluate.py
```

Mantenha o nome `bug_to_user_story_v2` e faça um novo push após cada alteração: a avaliação lê o prompt do Hub. Preserve o dataset e os modelos entre rodadas para comparar os efeitos das mudanças. Se mudar a configuração, registre-a junto ao experimento.

O registro abaixo apresenta a avaliação final com os 15 exemplos. As médias foram calculadas a partir das notas visíveis nas capturas em Resultados Finais.

| Iteração | Alteração e motivo | Commit do prompt / experimento | Helpfulness | Correctness | F1-Score | Clarity | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Avaliação final | Execução completa dos 15 exemplos com o prompt v2. | [8c034dd1](https://smith.langchain.com/o/2c51ef9f-d3a5-4178-8c6f-d5729a609c19/datasets/5d70698d-a1a2-4bec-8551-270fbf6165b3/compare?selectedSessions=03725a14-86f3-4d00-9481-5b1821c82b70) | 0,8697 | 0,8660 | 0,8626 | 0,8700 | 0,8693 |

Encerre a otimização quando todas as cinco médias e a média geral atingirem pelo menos 0,8, registrando também a análise dos exemplos mais fracos.

## Fase 5 — Testes de Validação

Os testes de [test_prompts.py](tests/test_prompts.py) verificam os requisitos do prompt otimizado:

```bash
pytest tests/test_prompts.py -v
```

| Teste obrigatório | O que verifica |
| --- | --- |
| `test_prompt_has_system_prompt` | Presença de um System Prompt não vazio. |
| `test_prompt_has_role_definition` | Definição de persona e atuação na tarefa. |
| `test_prompt_mentions_format` | Contrato de saída da User Story e dos critérios de aceitação. |
| `test_prompt_has_few_shot_examples` | Pares de entrada e saída nas mensagens enviadas ao modelo. |
| `test_prompt_no_todos` | Ausência de marcadores `TODO` no texto. |
| `test_minimum_techniques` | Pelo menos duas técnicas distintas, incluindo Few-shot. |

Há também verificações da estrutura do YAML, da variável de entrada `bug_report` e da renderização do template. Esses testes validam o artefato; a qualidade das respostas é medida nos experimentos do LangSmith.

Para executar toda a suíte local:

```bash
pytest tests/ -v
```

## Resultados Finais

O experimento `promptmateusmba-bug_to_user_story_v2-8c034dd1`, concluído em 28/10/2026, avaliou os 15 exemplos do dataset. Todas as cinco médias superaram 0,8, e o terminal confirmou a aprovação.

### Métricas do experimento final

| Métrica | Média dos 15 exemplos | Meta |
| --- | ---: | --- |
| Helpfulness | 0,8697 | ≥ 0,8 |
| Correctness | 0,8660 | ≥ 0,8 |
| F1-Score | 0,8626 | ≥ 0,8 |
| Clarity | 0,8700 | ≥ 0,8 |
| Precision | 0,8693 | ≥ 0,8 |
| **Média geral** | **0,8675** | **≥ 0,8** |

As médias foram calculadas a partir das 15 notas de cada métrica visíveis na captura detalhada e arredondadas para quatro casas decimais. A média geral considera as cinco médias antes do arredondamento. O LangSmith exibe os valores agregados com duas casas decimais. A aprovação considera as médias; alguns exemplos têm notas individuais abaixo de 0,8.

**Experimento final:** [Abrir a avaliação no LangSmith](https://smith.langchain.com/o/2c51ef9f-d3a5-4178-8c6f-d5729a609c19/datasets/5d70698d-a1a2-4bec-8551-270fbf6165b3/compare?selectedSessions=03725a14-86f3-4d00-9481-5b1821c82b70).

**Prompt avaliado:** `promptmateusmba/bug_to_user_story_v2`.

### Comparação entre o prompt original (v1) e o otimizado (v2)

| Aspecto | v1 | v2 | Motivo da mudança |
| --- | --- | --- | --- |
| Persona | Assistente genérico que transforma bugs em tarefas. | Analista de requisitos com atuação em produto e testes de aceitação. | Direcionar a resposta para necessidades e comportamentos verificáveis. |
| Instruções | Pedido genérico para criar uma User Story. | Objetivo, prioridades, regras e roteiro de análise em sete etapas. | Orientar a cobertura do relato e a revisão de consistência. |
| Exemplos | Sem demonstrações. | Seis pares completos de relato e resposta. | Demonstrar formato, profundidade, contratos, propostas e tratamento de lacunas. |
| Formato | Sem estrutura de saída definida. | Story e critérios em Dado/Quando/Então, com complementos proporcionais ao caso. | Facilitar leitura, implementação e validação. |
| System e User | Relato repetido nas duas mensagens. | Orientações no System; `{bug_report}` somente no User. | Separar instruções permanentes dos dados de cada execução. |
| Exceções e fidelidade | Sem política explícita. | Regras para relatos vazios, incompletos, contraditórios ou com assuntos independentes; separação entre fatos, hipóteses e propostas. | Reduzir omissões e informações sem sustentação. |

A comparação descreve mudanças no prompt. Os resultados medidos acima correspondem ao v2; não há notas medidas da v1 nesta tabela.

### Evidências no LangSmith

**Dataset público com os experimentos:** [Acessar o dataset e suas avaliações no LangSmith](https://smith.langchain.com/public/f4f47f9e-2f88-4cac-9c1e-568c8f4970a9/d).

O link público informado acima é o registro das avaliações do dataset. O link impresso pelo avaliador exige acesso ao workspace. Caso seja necessário compartilhar outro dataset, execute na raiz do projeto:

```bash
python - <<'PYTHON'
import os
from dotenv import load_dotenv
from langsmith import Client

load_dotenv(".env")
dataset_name = f"{os.environ['LANGSMITH_PROJECT']}-eval"
print(Client().share_dataset(dataset_name=dataset_name)["url"])
PYTHON
```

Guarde a URL retornada e confira o acesso sem autenticação. Evite compartilhar novamente depois de registrar o endereço, pois o link pode mudar.

As capturas em `docs/evidencias/` mostram o experimento com **15 exemplos**, as **cinco médias acima de 0,8**, as notas por exemplo e a confirmação de aprovação no terminal.

| Evidência | Registro |
| --- | --- |
| Dataset com os 15 exemplos e experimentos. | [Dataset e avaliações no LangSmith](https://smith.langchain.com/public/f4f47f9e-2f88-4cac-9c1e-568c8f4970a9/d). |
| Dashboard do experimento final com as cinco métricas. | [Visão geral das métricas](docs/evidencias/dashboard-metricas-finais.png). |
| Avaliação detalhada dos 15 exemplos. | [Notas por exemplo](docs/evidencias/avaliacao-15-exemplos.png). |
| Confirmação da aprovação pelo avaliador. | [Resultado no terminal](docs/evidencias/resultado-terminal-aprovado.png). |
| Comparação das iterações. | [Experimentos do dataset](https://smith.langchain.com/public/f4f47f9e-2f88-4cac-9c1e-568c8f4970a9/d). |
| Trace de um exemplo simples. | A preencher com link ou captura. |
| Trace de um exemplo médio. | A preencher com link ou captura. |
| Trace de um exemplo complexo. | A preencher com link ou captura. |

#### Dashboard do experimento final

![Dashboard do LangSmith com 15 execuções e as médias das cinco métricas acima de 0,8](docs/evidencias/dashboard-metricas-finais.png)

#### Notas dos 15 exemplos

![Tabela do LangSmith com as notas de Clarity, Correctness, F1-Score, Helpfulness e Precision por exemplo](docs/evidencias/avaliacao-15-exemplos.png)

#### Aprovação no terminal

![Saída do avaliador confirmando que todas as métricas atingiram pelo menos 0,8](docs/evidencias/resultado-terminal-aprovado.png)

Os traces permitem inspecionar entradas, mensagens, respostas, chamadas e feedbacks. Use essas informações para explicar os resultados dos exemplos selecionados.
