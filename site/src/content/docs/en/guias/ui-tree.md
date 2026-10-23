---
title: UI Tree (menus and HUD in the Node Editor)
description: Build 2D game menus and HUD with nodes, no code required. Works on desktop, Web and Android.
---

**UI Tree** is a Node Editor tree type for building the game's 2D interface: main menu, options, pause and HUD. Everything is drawn on top of the game and works on desktop, Web and Android.

## Quick start

1. In the Node Editor, switch the type to **UI Tree** and click **New**.
2. In the **UI Tree** panel (N key or the tab in the T shelf), click **+ Menu** and/or **+ HUD**.
   - **Menu**: screens `Menu` (Play, Options, Quit) and `Opcoes` (Sound, Volume, Back).
   - **HUD**: health bar and text at the top and a speedometer at the bottom.
3. Click **Setup Game Logic**. It adds to the scene camera an Always sensor (pulse) with the Python Module controller `range_ui_runtime.main` and creates the properties `ui_screen`, `ui_hud`, `som`, `volume`, `vida` and `velocidade`. Running it again duplicates nothing.
4. Press **P**. Bake runs automatically on play and on save.

In the template, **Play** hides the menu and turns on the HUD; **Sound** and **Volume** drive the game master volume.

## Pieces

- **Screen**: a Frame marked as a screen (**Add > Widgets > Screen**). It has Fade, default hover and click sounds, Scale Mode (**Stretch** or **Keep Aspect**) and an editor-only backdrop (**Capture Camera**).
- **HUD Screen**: always drawn under the menu. With **Camera** set, it draws only in that camera's viewport (useful for split screen).
- **Widgets**: Button, Toggle, Slider, Panel and Image. HUD: Progress Bar, Label (with formatting, e.g. `{vida:.0f}`) and Gauge. Each widget can read another object's properties through the **Object** field.
- **Button events**: On Enter, On Exit, On Over, On Press, On Release and On Click. Toggle and Slider have **On Change**.
- **Actions**: Print, Send Message, Go To Screen, Change Scene, Quit Game, Play Sound, Set/Add/Toggle Property and Run Python (`module.function(ui)`).
- **States**: **Enabled If** and **Selected If** bind a button to a bool property.
- **Anchor**: in Keep Aspect, each widget follows one of 9 screen points (chosen in the UI Tree panel).

## Controlling it from the game

- `ui_screen` property on the script owner: name of the screen to show; `""` hides the menu.
- `ui_hud` property (bool): shows or hides the HUD.
- Logic Bricks: Property actuator on `ui_screen`, or Send Message + Message sensor.
- Keyboard and gamepad: arrows or stick move the focus; Enter, Space or A press; left and right move the Slider.

From Python:

```python
import range_ui_runtime

range_ui_runtime.show("Menu")    # show a screen
range_ui_runtime.hide()          # hide the menu
range_ui_runtime.set_hud(True)   # turn the HUD on
screen = range_ui_runtime.get()  # current screen
```

A **Run Python** action calls your function with the `ui` object:

```python
# my_menu.py (Run Python action: my_menu.on_play)
def on_play(ui):
    print("Play clicked")
```

:::tip
The HUD reads game properties every frame. For the health bar, just change the `vida` property in your script or with a Property actuator.
:::
