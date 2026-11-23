# Exemplo: criar um jogo na Anastacio Engine com uma IA

Um passo a passo curto para usar o Claude Code ou o Codex como ajudante de criação. A IA conversa com o editor pelo MCP `anastacio-criador`, e você continua no comando: ela só lê até você liberar a edição.

## O que você precisa

- A Anastacio Engine (editor e runtime).
- O Claude Code ou o Codex, com o MCP `anastacio-criador` registrado (README, seção "MCP do criador de jogos") e o MCP `anastacio-api`, que dá a referência da API Python.
- Opcional: a skill `criar-jogo-anastacio` (Claude Code), que ensina a IA o roteiro abaixo.

## 1. Ligue o controle no seu editor

1. Abra o editor.
2. Em **Preferências > Add-ons**, ative **Game Engine: Controle por IA** e clique em **Ligar**.
3. O cabeçalho passa a mostrar **IA: observando**. Nesse modo a IA só olha a cena.

## 2. Peça o jogo em uma frase

Exemplo de pedido:

> Conecte no editor e faça um joguinho: o Cube anda para frente e para trás com as setas, a câmera olha para ele. Rode para testar.

## 3. O que a IA faz (e o que você vê)

1. **Conecta e lê a cena** (`projeto_conectar`, `cena_descrever`). O cabeçalho mostra o nome dela, por exemplo **IA (Claude Code): observando**.
2. **Pede liberação.** Para mexer, a IA chama `pedir_liberacao` com o motivo. Aparece no cabeçalho o aviso "Claude Code pede para editar: …" com **Permitir** e **Negar**. Só o seu clique libera. Se negar, ela não insiste; o pedido some sozinho em 60 s.
3. **Consulta a API antes de escrever código** (`api_guia`, `api_buscar`), porque a engine é nova e a IA não deve inventar funções.
4. **Cria o script e liga ao objeto** (`script_gravar`, `script_ligar`). Antes da primeira alteração o MCP grava um backup em `<projeto>.backups/`.
5. **Roda o jogo** (`jogo_abrir`, sem arquivo, para rodar a cena aberta com o que ainda não foi salvo), aperta teclas (`jogo_tecla`) e confere se o Cube se moveu (`jogo_objetos`), com `jogo_tela` e o log do jogo se algo falhar.
6. **Mostra o resultado e espera.** Ela não salva sozinha: você decide quando usar `projeto_salvar`.

## 4. Quando terminar

- Clique em **Travar** para voltar a só observar, ou em **Desligar** para encerrar a conexão. O botão **Ligar** continua no cabeçalho.
- Desativar o addon remove os controles do cabeçalho.

## Boas práticas

- Peça em passos pequenos e confira a tela a cada um.
- Deixe a IA consultar a API em vez de adivinhar nomes de funções.
- Salve você mesmo antes de uma mudança grande. O backup do MCP é uma rede de segurança, não um substituto.
- Código Python livre pela IA (`editor_py`, `jogo_py`) vem desligado. Só ligue com `ANASTACIO_CRIADOR_PY=1` se souber o que está fazendo.

## Segurança em resumo

A conexão é só local (`127.0.0.1`), protegida por um token que fica na sua conta do Windows. Em modo observar só passam comandos de leitura. A IA não consegue aprovar o próprio pedido de liberação, e dois clientes (por exemplo Claude Code e Codex) podem ficar conectados juntos, cada um identificado no cabeçalho.
