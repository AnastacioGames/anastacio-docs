---
title: UI Tree (menus e HUD no Node Editor)
description: Monte menus e HUD 2D do jogo com nós, sem escrever código. Funciona no desktop, na Web e no Android.
---

O **UI Tree** é um tipo de árvore do Node Editor para montar a interface 2D do jogo: menu principal, opções, pausa e HUD. Tudo é desenhado por cima do jogo e funciona no desktop, na Web e no Android.

## Começo rápido

1. No Node Editor, troque o tipo para **UI Tree** e clique em **New**.
2. No painel **UI Tree** (tecla N ou aba na prateleira T), clique em **+ Menu** e/ou **+ HUD**.
   - **Menu**: telas `Menu` (Jogar, Opções, Sair) e `Opcoes` (Som, Volume, Voltar).
   - **HUD**: barra e texto de vida no canto de cima e velocímetro no canto de baixo.
3. Clique em **Setup Game Logic**. Ele liga na câmera da cena um sensor Always (pulso) com o controlador Python Module `range_ui_runtime.main` e cria as propriedades `ui_screen`, `ui_hud`, `som`, `volume`, `vida` e `velocidade`. Rodar de novo não duplica nada.
4. Aperte **P**. O Bake é automático ao jogar e ao salvar.

No template, **Jogar** esconde o menu e liga o HUD; **Som** e **Volume** mandam no volume geral do jogo.

## Peças

- **Screen**: Frame marcado como tela (**Add > Widgets > Screen**). Tem Fade, sons padrão de hover e clique, Scale Mode (**Stretch** ou **Keep Aspect**) e imagem de fundo só para o editor (**Capture Camera**).
- **HUD Screen**: fica sempre por baixo do menu. Com o campo **Camera** preenchido, desenha só no viewport daquela câmera (útil em split screen).
- **Widgets**: Button, Toggle, Slider, Panel e Image. No HUD: Progress Bar, Label (com formatação, ex.: `{vida:.0f}`) e Gauge. Cada widget pode ler as propriedades de outro objeto pelo campo **Object**.
- **Eventos do Button**: On Enter, On Exit, On Over, On Press, On Release e On Click. Toggle e Slider têm **On Change**.
- **Ações**: Print, Send Message, Go To Screen, Change Scene, Quit Game, Play Sound, Set/Add/Toggle Property e Run Python (`modulo.funcao(ui)`).
- **Estados**: **Enabled If** e **Selected If** ligam o botão a uma propriedade bool.
- **Âncora**: em Keep Aspect, cada widget segue um dos 9 pontos da tela (escolhido no painel UI Tree).

## Controle pelo jogo

- Propriedade `ui_screen` do dono do script: nome da tela a mostrar; `""` esconde o menu.
- Propriedade `ui_hud` (bool): mostra ou esconde o HUD.
- Logic Bricks: atuador Property em `ui_screen`, ou Send Message + sensor Message.
- Teclado e controle: setas ou analógico mudam o foco; Enter, Espaço ou A apertam; esquerda e direita mexem o Slider.

Pelo Python:

```python
import range_ui_runtime

range_ui_runtime.show("Menu")   # mostra uma tela
range_ui_runtime.hide()         # esconde o menu
range_ui_runtime.set_hud(True)  # liga o HUD
tela = range_ui_runtime.get()   # tela atual
```

Uma ação **Run Python** chama uma função sua recebendo o objeto `ui`:

```python
# meu_menu.py (ação Run Python: meu_menu.ao_jogar)
def ao_jogar(ui):
    print("Jogar clicado")
```

:::tip
O HUD lê as propriedades do jogo a cada frame. Para a barra de vida, basta mudar a propriedade `vida` no seu script ou num atuador Property.
:::
