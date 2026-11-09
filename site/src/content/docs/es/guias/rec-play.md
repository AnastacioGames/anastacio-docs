---
title: Rec Play (graba escenas jugando)
description: Graba actores en Takes mientras juegas, por capas, y úsalos en cutscenes, vídeo o Python.
---

**Rec Play** graba lo que ocurre mientras juegas. Cada grabación se convierte en un **Take**, con la pose de cada actor. Después, el Take puede convertirse en vídeo, entrar en una cutscene o reproducirse por script.

## Grabar en Rec Studio

1. Abre **Window > Rec Studio**. Si no tienes biblioteca propia, abre un kit con 3 personajes, 6 acciones y 4 escenarios.
2. En **Scenery**, arrastra un escenario a la escena.
3. En **Characters**, arrastra un personaje. Se convierte en actor de inmediato.
4. En **Actions**, arrastra una acción sobre el actor.
5. Haz clic en **Record**, mueve al actor y detén con **F10**. El Take aparece en la lista.

## Botones

| Botón | Qué hace |
|---|---|
| **Watch** | Reproduce todos los Takes en el juego, sin grabar. |
| **Rerecord** | Vuelve a grabar los actores del Take seleccionado y lo sustituye. |
| **Undo** | Deshace la última grabación. |
| **Movie** | Reproduce los Takes y guarda un vídeo con sonido en la carpeta del archivo. |

## Grabar por capas

Al grabar, los actores sin marcar repiten su Take más reciente, así que puedes grabar un actor cada vez. **Play Other Takes** activa esta repetición, y **Collide on Replay** define si los actores repetidos colisionan.

## Llevarlo a una cutscene

1. En la pestaña **Render**, abre **Motion Recording (Experimental)**.
2. Selecciona el Take y haz clic en **Add to Cutscene**. La grabación no crea el evento por sí sola.
3. En **Cutscene Sequences** aparece un evento Play Take. Renombrar el Take actualiza el evento.

## Reproducir desde Python

```python
import Range

scene = Range.logic.getCurrentScene()
door = scene.objects["Door"]
if not door.is_playing_take():
    door.play_take("Take 1")
```

`scene.takes` lista los nombres, `scene.play_take(nombre)` reproduce todos los actores y `obj.stop_take()` detiene en el punto actual. Durante la reproducción, el actor no tiene lógica ni física; ambas vuelven al final. Consulta [`KX_Scene`](../../api/types/kx_scene/) / [`KX_GameObject`](../../api/types/kx_gameobject/).

:::note
La pose por hueso aún no se graba, así que el IK y los scripts que mueven huesos no entran en el Take. El movimiento del cuerpo y las Actions sí.
:::
