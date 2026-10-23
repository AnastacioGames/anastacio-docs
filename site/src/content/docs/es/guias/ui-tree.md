---
title: UI Tree (menús y HUD en el Node Editor)
description: Arma menús y HUD 2D del juego con nodos, sin escribir código. Funciona en escritorio, Web y Android.
---

**UI Tree** es un tipo de árbol del Node Editor para armar la interfaz 2D del juego: menú principal, opciones, pausa y HUD. Todo se dibuja encima del juego y funciona en escritorio, Web y Android.

## Inicio rápido

1. En el Node Editor, cambia el tipo a **UI Tree** y haz clic en **New**.
2. En el panel **UI Tree** (tecla N o pestaña en la barra T), haz clic en **+ Menu** y/o **+ HUD**.
   - **Menu**: pantallas `Menu` (Jugar, Opciones, Salir) y `Opcoes` (Sonido, Volumen, Volver).
   - **HUD**: barra y texto de vida arriba y velocímetro abajo.
3. Haz clic en **Setup Game Logic**. Agrega a la cámara de la escena un sensor Always (pulso) con el controlador Python Module `range_ui_runtime.main` y crea las propiedades `ui_screen`, `ui_hud`, `som`, `volume`, `vida` y `velocidade`. Ejecutarlo de nuevo no duplica nada.
4. Pulsa **P**. El Bake es automático al jugar y al guardar.

En la plantilla, **Jugar** oculta el menú y enciende el HUD; **Sonido** y **Volumen** controlan el volumen general del juego.

## Piezas

- **Screen**: Frame marcado como pantalla (**Add > Widgets > Screen**). Tiene Fade, sonidos de hover y clic, Scale Mode (**Stretch** o **Keep Aspect**) e imagen de fondo solo para el editor (**Capture Camera**).
- **HUD Screen**: siempre queda debajo del menú. Con **Camera** definida, dibuja solo en el viewport de esa cámara (pantalla dividida).
- **Widgets**: Button, Toggle, Slider, Panel e Image. En el HUD: Progress Bar, Label (con formato, ej.: `{vida:.0f}`) y Gauge. Cada widget puede leer propiedades de otro objeto con el campo **Object**.
- **Eventos del Button**: On Enter, On Exit, On Over, On Press, On Release y On Click. Toggle y Slider tienen **On Change**.
- **Acciones**: Print, Send Message, Go To Screen, Change Scene, Quit Game, Play Sound, Set/Add/Toggle Property y Run Python (`modulo.funcion(ui)`).
- **Estados**: **Enabled If** y **Selected If** vinculan el botón a una propiedad bool.
- **Ancla**: en Keep Aspect, cada widget sigue uno de los 9 puntos de la pantalla.

## Control desde el juego

- Propiedad `ui_screen` del dueño del script: nombre de la pantalla; `""` oculta el menú.
- Propiedad `ui_hud` (bool): muestra u oculta el HUD.
- Logic Bricks: actuador Property en `ui_screen`, o Send Message + sensor Message.
- Teclado y mando: flechas o stick cambian el foco; Enter, Espacio o A pulsan; izquierda y derecha mueven el Slider.

Desde Python:

```python
import range_ui_runtime

range_ui_runtime.show("Menu")      # muestra una pantalla
range_ui_runtime.hide()            # oculta el menú
range_ui_runtime.set_hud(True)     # enciende el HUD
pantalla = range_ui_runtime.get()  # pantalla actual
```
