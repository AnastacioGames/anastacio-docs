# Plano: IA para criadores de jogos (partes A e B)

Para seguir no chat do PC (Claude Code aberto no VS Code, com a engine instalada). Estado em 2026-11-22.

- **Parte A:** o MCP abre o editor com o projeto (janela visível). **Escrita e testada só contra um editor falso.**
- **Parte B:** a IA conecta no editor que o usuário já abriu. **Só o desenho abaixo; nada implementado.** Exige mudar a engine, então é seu (decisão de 2026-11-22: mexer na engine fica para depois).

A e B usam as mesmas ferramentas e o mesmo protocolo. A diferença é só quem sobe o servidor dentro do editor.

## Parte A: validar com a engine

1. Branch `ccr-7536d00d-qdc44d` no `anastacio-docs` (`git fetch` e `git checkout`).
2. Seguir [testes-pendentes.md](testes-pendentes.md) de cima para baixo, marcando cada item.
3. Se um item falhar: copiar o erro e o resultado de `log_ler`, corrigir o arquivo apontado na lista e repetir só aquele item. Não repetir o mesmo comando mais de duas vezes sem mudar a causa.
4. Quando tudo passar: tirar a ressalva "não verificado" do skill `api-anastacio` (repo da engine) e do changelog, e fazer o merge nos dois repos.

Prompt para colar no chat do PC:

> Estou no repo anastacio-docs, branch ccr-7536d00d-qdc44d. Leia docs/plano-ia-criador.md e docs/testes-pendentes.md. A engine está instalada em <CAMINHO>. Instale o MCP anastacio-criador apontando para ela e execute os testes da Parte A um por vez, marcando cada caixinha no arquivo. Pare no primeiro erro e me mostre o erro e o log. Não altere o código da engine.

## Parte B: o desenho (a fazer depois, na engine)

**Objetivo:** o usuário abre o editor como sempre, liga "Controle por IA" uma vez, e o MCP conecta nele sem abrir outro editor.

**O que já existe e serve:** `tools/criador/servidor_editor.py` já abre o servidor TCP, escreve o arquivo de sessão (porta, token, pid) e se religa ao recarregar arquivo. O MCP já procura esse arquivo e conecta se existir (`conectar()` em `anastacio_criador_mcp.py`). Falta só quem inicia o servidor dentro do editor sem a flag `--python`.

**Mudança na engine (a confirmar olhando o código):**
- Um complemento que faz o que o `servidor_editor.py` faz, ligado por um botão. Verificado: a engine tem `source/release/scripts/startup/bl_operators/anastacio_*.py` (um por recurso), `startup/anastacio_default_addons.py` e a pasta `addons/`. Não verificado: onde registrar o botão. Um candidato é o menu `INFO_MT_file` em `startup/bl_ui/space_info.py`; outro é um painel de Preferências.
- **Desligado por padrão**, e o usuário liga a cada sessão (ou numa preferência). Mostrar no editor que o controle está ativo, com a porta e um botão para desligar.
- O token e a porta vão para um arquivo de sessão numa pasta do usuário (a mesma que o MCP procura). Revisar permissões do arquivo.
- Copiar o `caminhos.py` junto, ou empacotar os dois no complemento, e manter uma só fonte para não divergir do `tools/criador/`.

**Perguntas que precisam de decisão sua antes de implementar:**
1. O complemento mora na engine (`startup/bl_operators`) ou como addon opcional em `addons/`? Recomendação: addon opcional, para não aumentar a superfície da engine.
2. Se o usuário estiver editando enquanto a IA age, o que acontece? Recomendação: modo "só observar" por padrão (a IA lê cena e tela, e alterar exige o usuário liberar), para não haver duas pessoas mexendo ao mesmo tempo.
3. O arquivo de sessão fica em qual pasta no Windows e no Linux? Hoje o MCP usa a pasta temporária do sistema.
4. O código livre (`py`) continua só por `ANASTACIO_CRIADOR_PY=1`? Recomendação: sim, e nunca por botão no editor.

**Testes de aceite (para quando existir):**
- Abrir o editor normalmente, ligar o controle, e `projeto_conectar` conecta sem abrir outro editor.
- Desligar o controle: o MCP perde a conexão com mensagem clara e não derruba o editor.
- Recarregar outro arquivo: o servidor se religa e o token novo é aceito.
- Duas janelas do editor abertas: o MCP conecta na certa e avisa se houver ambiguidade.
- Fechar o editor: o arquivo de sessão antigo não engana o MCP (checar pid).

Prompt para colar no chat do PC quando chegar a hora (repo da engine):

> Leia docs/plano-ia-criador.md, Parte B, no repo anastacio-docs. Vou decidir as quatro perguntas abaixo e quero que você implemente o complemento "Controle por IA" na engine seguindo o AGENTS.md (build pelo vcvars64, cascata de propriedade, check_cascata.py, changelog). Primeiro me mostre onde pretende registrar o botão e espere minha confirmação.

## O que NÃO entra

- Assistente de IA dentro do editor com chave de API própria: descartado por ora.
- Editar o código da engine pela IA: é outro uso, com a ferramenta interna `tools/testes_engine/controle.py` (que não é o MCP do criador).
