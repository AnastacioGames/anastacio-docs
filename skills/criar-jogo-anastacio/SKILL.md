---
name: criar-jogo-anastacio
description: Ajuda a criar um jogo na Anastacio Engine usando o editor pelo MCP anastacio-criador (cena, objetos, scripts, teste do jogo) e a referência da API pelo MCP anastacio-api. Use quando o usuário quiser montar, mudar ou testar um jogo ou cena na Anastacio Engine.
---

# Criar jogos na Anastacio Engine

Este skill é para quem **cria jogos** na engine. Ele não serve para mudar o código da engine.
Usa dois MCPs deste repositório: `anastacio-criador` (editor e jogo) e `anastacio-api` (referência da API Python). Instalação: README, seções "MCP do criador de jogos" e do `anastacio_api_mcp.py`.

Se as ferramentas MCP não estiverem disponíveis, diga isso ao usuário e mostre o comando de instalação. Não finja que mexeu no projeto.

## Antes de escrever script

1. Leia `api_guia` uma vez. A engine é nova e nenhum modelo foi treinado nela: não invente funções.
2. Para cada nome de função ou atributo que for usar, confira com `api_buscar` ou `api_item`. Só use o que existir.

## Roteiro de trabalho

1. **Conectar:** `projeto_conectar` com o caminho do projeto. O editor abre com janela visível; o usuário acompanha.
2. **Entender a cena antes de mexer:** `cena_descrever`, `objeto_descrever` e `editor_tela`.
3. **Mudar em passos pequenos:** `op_executar` e `propriedade_definir`. Na primeira alteração o MCP grava um backup em `<projeto>.backups/`; informe o caminho ao usuário. Se o aviso disser que o projeto não foi salvo, peça para ele salvar antes.
   **Scripts do jogo:** crie com `script_gravar` (nome e conteúdo, usando `Range`, nunca `bpy`) e ligue ao objeto com `script_ligar`. Nunca use os operadores `text.*` do editor: eles escrevem no texto ativo, que pode ser um script do usuário. Você pode regravar com o mesmo nome um script que criou nesta sessão (para corrigir); para um script que já existia no projeto, `script_gravar` recusa e só `sobrescrever` com autorização do usuário.
4. **Conferir o resultado:** `editor_tela` depois de cada mudança visual, e `cena_descrever` quando a mudança não é visual.
5. **Testar o jogo:** `jogo_abrir` sem `arquivo` roda uma cópia da cena aberta no editor, inclusive o que ainda não foi salvo (use `arquivo` só para um .range do disco). Para provar que algo anda, `jogo_objetos` antes e depois de `jogo_tecla`. Depois: `jogo_tecla`, `jogo_estado`, `jogo_tela`, e `log_ler` com `qual="jogo"` para ver erros de script. Feche com `jogo_fechar`.
6. **Salvar só quando o usuário aprovar:** `projeto_salvar`. Nunca salve por conta própria. `editor_fechar` não salva.

## Escolher a via: ao vivo ou em segundo plano

Há duas maneiras de editar. Escolha você mesmo e diga ao usuário qual usou e por quê.

| Situação | Via |
|---|---|
| O projeto está aberto no editor, ou o usuário quer acompanhar | **Ao vivo** (`op_executar`, `propriedade_definir`, `script_gravar`...) |
| Mudança visual que precisa ser conferida na tela | **Ao vivo** |
| Muitas mudanças repetitivas (renomear, aplicar material em todos, criar dezenas de objetos) | **Em segundo plano** (`lote_executar`) |
| O arquivo não está aberto em nenhum editor | **Em segundo plano** |
| Mudança grande ou arriscada | **Em segundo plano**, na cópia; mostre o resumo antes de trocar |
| Muitas mudanças e depois conferir como ficou | **As duas**: lote na cópia, depois abra a cópia ao vivo para ver |

Como usar o lote:
1. `arquivo_em_uso` diz se o projeto está aberto num editor com o Controle por IA ligado. Aberto = use a via ao vivo (o lote recusa, para não perder o que não foi salvo). Um editor sem o Controle por IA ligado **não é detectado**: se o usuário pode estar com o arquivo aberto, pergunte antes de usar o lote.
2. `lote_executar` aplica a lista de passos numa cópia (`nome.ia.range`). **O original nunca é alterado**, e se um passo falhar nada é gravado. As proteções são as mesmas do editor ao vivo (código livre continua bloqueado).
3. Mostre o resumo (criados, removidos, alterados) ao usuário.
4. **Só com a aprovação dele**, `lote_aplicar` troca o original pela cópia, guardando um backup em `<projeto>.backups/`. A troca é recusada se o original mudou depois do lote (alguém salvou nele) ou se a cópia foi alterada; nesse caso refaça o lote. Sem aprovação, deixe a cópia onde está.
5. Passos que dependem de ver a tela ou de clicar (`editor_clicar`, `editor_tela`, jogo rodando) não existem no lote: use a via ao vivo.

## Editor que o usuário já abriu

- Se o usuário já tem o editor aberto, peça para ele ativar o addon **Controle por IA** (Preferências > Add-ons) e clicar em Ligar; depois chame `projeto_conectar`. A resposta diz o modo.
- Em **só observar** você só lê (`cena_descrever`, `objeto_descrever`, `editor_tela`, `propriedade_ler`, `op_listar`). Uma alteração recusada com a mensagem de modo observar **não é falha**: explique o que pretende fazer e chame `pedir_liberacao` com o motivo em uma frase (aparece um aviso no editor; só o clique do usuário libera). Se ele negar, não insista; se expirar, peça que clique em **Liberar edição**. Não tente outro caminho para contornar.
- Não use `editor_fechar` para encerrar: num editor do usuário ele só desliga o controle.
- Se a conexão cair, o usuário pode ter desligado o controle; peça para ligar de novo.

## Limites

- `editor_py` e `jogo_py` (código livre) vêm desligados. Não tente contornar; se for realmente necessário, peça ao usuário para ligar `ANASTACIO_CRIADOR_PY=1`.
- `propriedade_ler` e `propriedade_definir` só aceitam caminhos `bpy.a.b[0]["x"]`, sem chamadas. Para criar ou mudar algo mais complexo, procure o operador certo com `op_listar` e `op_descrever`.
- Scripts de jogo usam `Range`, não `bpy` (o jogo exportado roda sem `bpy`). O `bpy` aparece só nas ferramentas do editor.
- Mudou algo grande ou irreversível? Pare e confirme com o usuário primeiro.

## Se algo falhar

- Erro ao abrir o editor: `log_ler` (qual `editor`) e mostre o final do log.
- O programa não foi encontrado: o usuário precisa informar `--editor`/`--runtime` ou as variáveis `ANASTACIO_EDITOR`/`ANASTACIO_RUNTIME`.
- Não repita a mesma chamada que falhou duas vezes: leia o erro, mude de abordagem ou relate ao usuário.
