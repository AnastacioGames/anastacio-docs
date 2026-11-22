# Testes pendentes (IA para criadores de jogos)

Estas ferramentas foram escritas e testadas só contra um editor falso, sem a engine instalada. Falta validar com a engine de verdade. Marque cada item quando passar; se falhar, anote a mensagem de erro e o conteúdo de `log_ler`.

## Pré-requisito

Engine instalada, com `AnastacioEngine` e `AnastacioRuntime`. Um projeto `.range` de teste **salvo**.

```
claude mcp add anastacio-criador -- python tools/anastacio_criador_mcp.py --editor "<caminho>/AnastacioEngine" --runtime "<caminho>/AnastacioRuntime"
claude mcp add anastacio-api -- python tools/anastacio_api_mcp.py --lang pt
```

## MCP do criador (`tools/anastacio_criador_mcp.py`, `tools/criador/servidor_editor.py`)

- [x] **Abrir:** `projeto_conectar` abre o editor com o projeto e a janela fica visível. Se não abrir, ver o log: o editor aceita `--python <arquivo> -- <sessão>` como a ferramenta interna `controle.py`?
- [x] **Sessão:** o arquivo de sessão aparece e `cena_descrever` lista os objetos (nome, tipo, posição, pai) e a câmera.
- [x] **`objeto_descrever`:** devolve propriedades de jogo, materiais e filhos. Suposição a confirmar: `o.game.properties` existe nesta versão do `bpy`; se vier `null`, ajustar.
- [x] **Backup:** o primeiro `op_executar` cria `<projeto>.backups/<data>.range` sem trocar o arquivo aberto. Suposição a confirmar: `save_as_mainfile(copy=True)` funciona e o backup abre.
- [x] **Backup só uma vez:** o segundo `op_executar` não cria outro backup.
- [x] **Operadores:** `op_listar` com filtro `primitive`, `op_descrever mesh.primitive_cube_add` e `op_executar` criam um cubo na cena.
- [x] **Propriedades:** `propriedade_ler` de `bpy.data.objects["Cube"].location` e `propriedade_definir` de `...location[0]` mudam o objeto. Recusa de caminho com chamada (`...remove(...)`) já foi testada com o editor falso.
- [x] **Tela:** `editor_tela` devolve uma imagem legível (a tela de abertura não cobre a janela; se cobrir, ver `show_splash` em `servidor_editor.py`, que hoje não é mexido).
- [x] **Entrada:** `editor_clicar` e `editor_tecla` agem no editor (precisa de `ANASTACIO_EVENT_SIMULATE=1`, que o MCP define).
- [x] **Recarregar arquivo:** abrir outro `.range` pelo editor e conferir que o servidor se religa (`load_post`) e o MCP volta a responder.
- [x] **Fechar:** `editor_fechar` fecha sem salvar e sem criar `quit.blend`.
- [x] **Código livre:** `editor_py` recusa por padrão; com `ANASTACIO_CRIADOR_PY=1` roda e devolve `resultado`.

## Jogo (`tools/criador/servidor_jogo.py`)

- [x] `jogo_abrir` roda o projeto no Runtime, janela visível.
- [x] `jogo_estado` mostra frame, FPS e cenas; `jogo_tecla` e `jogo_mouse` mexem no jogo; `jogo_tela` devolve imagem.
- [x] Erro de script no jogo aparece em `log_ler` com `qual="jogo"`.
- [x] O jogo fecha sozinho depois de 60 s sem conexão e quando o MCP sai.

## MCP da documentação (`tools/anastacio_api_mcp.py`)

- [x] No Claude Code real, as ferramentas `api_guia`, `api_indice`, `api_buscar`, `api_pagina` e `api_item` aparecem e respondem (testar com `worldPosition` e `KX_GameObject`).
- [x] Com `--fonte https://anastaciogames.github.io/anastacio-docs/api-ia/pt/` lê a doc publicada.
- [x] Abrir no navegador (200 por curl) `.../api-ia/pt/INDEX.md` e `.../api-ia/pt/paginas/Range.texture--consts.md` (o ambiente de desenvolvimento não alcança o site).

## Skills

- [x] O skill `criar-jogo-anastacio` (`skills/`) é instalado em `.claude/skills/` de um projeto de jogo e dispara ao pedir "monta uma cena com um cubo que anda".
- [x] O skill `api-anastacio` (repo da engine) cai para a doc publicada quando o MCP não está instalado.

## Depois de passar tudo

Tirar a ressalva "não verificado" do skill `api-anastacio` e do changelog da engine, e fazer o merge no `main`.
