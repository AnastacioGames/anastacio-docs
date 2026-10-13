---
title: Weather (rain, lightning, clouds and fog)
description: Turn on and change the World weather during the game with setWeather and strikeLightning.
---

Anastacio's weather lives in the **World**: rain, splashes, puddles, lightning, clouds, Sky Layers, volumetric clouds and volumetric fog. You set everything up in the editor and change the values during the game from Python, with [`setWeather`](../../api/types/kx_worldinfo/).

:::note
The code is the same one tested on the Portuguese page, so names such as `mundo` (world) and `tempestade` (storm) are in Portuguese.
:::

## 1. Set it up in the editor

1. Open the **World** tab in the properties.
2. In the **Weather** panel, turn on **Rain** and adjust the intensity until it looks right in the viewport.
3. If you will use clouds, turn on **Clouds** (or Sky Layers / Volumetric Clouds) in the editor already.

:::caution
Clouds need a pass created at load time. If none of them is on in the World when the game starts, `setWeather("clouds", True)` has nowhere to draw. Turn them on in the editor and, if you want to start without clouds, set the coverage to zero from the script.
:::

## 2. Change the weather from a script

Create `clima.py` in the Text Editor, attach it as a component to any object in the scene (the Cube, for example) and register it as in the [First script](../primeiro-script/) guide.

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

What happens:

- at the start, a light rain falls;
- after 5 seconds the rain gets heavy, puddles appear and lightning strikes right away; automatic lightning keeps coming at intervals.

## Names you can change

Names accept the `weather.` prefix (optional). Some of the most used:

| Name | Type | What it does |
|---|---|---|
| `rain` | bool | Turns rain on |
| `rain_intensity` | float | How hard it rains |
| `rain_wind` | float | Rain slant from wind |
| `puddles` | bool | Puddles on the ground |
| `lightning` | bool | Automatic lightning |
| `clouds` | bool | Clouds (needs the pass, see the warning above) |
| `cloud_coverage` | float | How much of the sky is covered |
| `vfog` | bool | Volumetric fog |
| `vfog_density` | float | Fog density |

The full list is in [`KX_WorldInfo.setWeather`](../../api/types/kx_worldinfo/). A wrong name raises an error, which helps catch typos.

## Without a script: Logic Bricks

The **Weather Effects** actuator makes the same changes without Python. Connect a sensor (Keyboard, Delay, Property) to it and choose what to change.
