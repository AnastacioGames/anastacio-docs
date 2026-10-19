---
title: Cámara del juego (enfoque, efectos y vibración)
description: Enfoque automático, cámara que sigue al objetivo, desenfoque por velocidad, DOF y vibración, sin filtros de Python.
---

La cámara de Anastacio tiene efectos nativos: enfoque que sigue a un objeto, seguimiento (la cámara gira para seguir al objetivo), DOF, desenfoque por velocidad, aberración cromática, viñeta y vibración. Todo se configura en las propiedades de la cámara y se puede cambiar desde Python en [`KX_Camera`](../../api/types/kx_camera/).

Todo empieza apagado. Solo se actualiza la cámara activa de la escena.

:::note
El código es el mismo probado en la página en portugués, por eso algunos nombres están en portugués (`TremerNoEspaco` = vibrar con espacio, `cena` = escena).
:::

## 1. Enfoque y seguimiento en el editor

Selecciona la cámara y abre **Properties > Camera** (con el motor Range Game).

En el panel **Focus & Tracking**:

1. En **Focus**, elige **Object** e indica el objeto que la cámara debe seguir (el auto, el jugador).
2. En **Tracking**, elige **Look At**. La cámara se queda en su lugar pero gira suavemente para mantener el objetivo en pantalla.
3. **Track Smooth** ajusta la suavidad (en segundos). **Framing Offset** con Y negativo mantiene el objetivo un poco por debajo del centro.

## 2. Efectos

En el panel **Camera Effects**:

- **DOF**: desenfoca lo que está fuera de la distancia de enfoque. Funciona junto con el enfoque del paso anterior.
- **Speed Blur**: desenfoque radial que crece con la velocidad de la cámara. **Full Speed** es la velocidad (m/s) a la que el efecto llega al máximo.
- **Protect Focus**: mantiene el objetivo enfocado, fuera del desenfoque (el auto queda nítido).
- **Vignette / Fisheye**: esquinas oscuras y distorsión de lente.

Cada efecto solo cuesta rendimiento mientras está encendido.

## 3. Vibración desde un script

`shake(trauma, duration)` hace vibrar la cámara. `trauma` va de 0 a 1 y varias vibraciones se suman. Ejemplo: vibrar al presionar Espacio, como en una explosión.

```python
import Range
from Range import events, logic


class TremerNoEspaco(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        pass

    def update(self):
        teclado = logic.keyboard.inputs[events.SPACEKEY]
        if teclado.activated:
            camera = self.object.scene.active_camera
            camera.shake(0.8, 0.6)
```

Asígnalo a cualquier objeto de la escena. La fuerza y la frecuencia de la vibración están en el panel **Camera Shake** de la cámara (o en `shakeAmplitude` y `shakeFrequency`).

## 4. Activar efectos desde el menú del juego

Un menú de opciones puede activar o desactivar efectos durante el juego:

```python
camera = Range.logic.getCurrentScene().active_camera
camera.useSpeedBlur = True
camera.speedBlurStrength = 0.5
camera.useDof = False
```

## Grano de película

El grano pertenece a la escena, no a la cámara: **Render > Post Processing**, opción Film Grain. En el juego:

```python
cena = Range.logic.getCurrentScene()
cena.filterManager.changeGrainValues(True, 0.3)
```
