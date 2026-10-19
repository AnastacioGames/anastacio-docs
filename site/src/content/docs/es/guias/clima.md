---
title: Clima (lluvia, rayos, nubes y niebla)
description: Activa y cambia el clima del World durante el juego con setWeather y strikeLightning.
---

El clima de Anastacio vive en el **World**: lluvia, salpicaduras, charcos, rayos, nubes, Sky Layers, nubes volumétricas y niebla volumétrica. Configuras todo en el editor y cambias los valores durante el juego desde Python, con [`setWeather`](../../api/types/kx_worldinfo/).

:::note
El código es el mismo probado en la página en portugués, por eso nombres como `mundo` (mundo) y `tempestade` (tormenta) están en portugués.
:::

## 1. Configurarlo en el editor

1. Abre la pestaña **World** en las propiedades.
2. En el panel **Weather**, activa **Rain** y ajusta la intensidad hasta que se vea bien en la viewport.
3. Si vas a usar nubes, activa **Clouds** (o Sky Layers / Volumetric Clouds) ya en el editor.

:::caution
Las nubes necesitan una pasada creada al cargar. Si ninguna está activa en el World cuando el juego empieza, `setWeather("clouds", True)` no tiene dónde dibujar. Actívalas en el editor y, si quieres empezar sin nubes, pon la cobertura en cero desde el script.
:::

## 2. Cambiar el clima desde un script

Crea `clima.py` en el Text Editor, asígnalo como componente a cualquier objeto de la escena (el Cube, por ejemplo) y regístralo como en la guía [Primer script](../primeiro-script/).

```python
import Range
from collections import OrderedDict


class Clima(Range.types.KX_PythonComponent):
    args = OrderedDict([
        ("Segundos ate a tempestade", 5.0),
    ])

    def start(self, args):
        self.espera = args["Segundos ate a tempestade"]
        self.tempo = 0.0
        self.tempestade = False
        mundo = self.object.scene.world
        mundo.setWeather("rain", True)
        mundo.setWeather("rain_intensity", 0.2)

    def update(self):
        self.tempo += 1.0 / Range.logic.getAverageFrameRate()
        if not self.tempestade and self.tempo >= self.espera:
            self.tempestade = True
            mundo = self.object.scene.world
            mundo.setWeather("rain_intensity", 1.0)
            mundo.setWeather("puddles", True)
            mundo.setWeather("lightning", True)
            mundo.strikeLightning()
```

Qué sucede:

- al inicio cae una lluvia ligera;
- después de 5 segundos la lluvia se vuelve intensa, aparecen charcos y cae un rayo de inmediato; los rayos automáticos siguen llegando a intervalos.

## Nombres que puedes cambiar

Los nombres aceptan el prefijo `weather.` (opcional). Algunos de los más usados:

| Nombre | Tipo | Qué hace |
|---|---|---|
| `rain` | bool | Activa la lluvia |
| `rain_intensity` | float | Qué tan fuerte llueve |
| `rain_wind` | float | Inclinación de la lluvia por el viento |
| `puddles` | bool | Charcos en el suelo |
| `lightning` | bool | Rayos automáticos |
| `clouds` | bool | Nubes (necesita la pasada, ver el aviso arriba) |
| `cloud_coverage` | float | Cuánto del cielo está cubierto |
| `vfog` | bool | Niebla volumétrica |
| `vfog_density` | float | Densidad de la niebla |

La lista completa está en [`KX_WorldInfo.setWeather`](../../api/types/kx_worldinfo/). Un nombre incorrecto genera un error, lo que ayuda a detectar errores de escritura.

## Sin script: Logic Bricks

El actuador **Weather Effects** hace los mismos cambios sin Python. Conéctale un sensor (Keyboard, Delay, Property) y elige qué cambiar.
