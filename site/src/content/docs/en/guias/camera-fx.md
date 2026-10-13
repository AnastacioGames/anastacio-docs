---
title: Game camera (focus, effects and shake)
description: Automatic focus, a camera that follows the target, speed blur, DOF and shake, without Python filters.
---

Anastacio's camera has native effects: focus that follows an object, tracking (the camera turns to follow the target), DOF, speed blur, chromatic aberration, vignette and shake. Everything is set in the camera properties and can be changed from Python in [`KX_Camera`](../../api/types/kx_camera/).

Everything starts off. Only the scene's active camera is updated.

:::note
The code is the same one tested on the Portuguese page, so some names are in Portuguese (`TremerNoEspaco` = shake on space, `cena` = scene).
:::

## 1. Focus and tracking in the editor

Select the camera and open **Properties > Camera** (with the Range Game engine).

In the **Focus & Tracking** panel:

1. In **Focus**, choose **Object** and set the object the camera should follow (the car, the player).
2. In **Tracking**, choose **Look At**. The camera stays in place but turns smoothly to keep the target on screen.
3. **Track Smooth** sets the smoothness (in seconds). **Framing Offset** with a negative Y keeps the target a little below the center.

## 2. Effects

In the **Camera Effects** panel:

- **DOF**: blurs what is outside the focus distance. Works together with the focus from the previous step.
- **Speed Blur**: radial blur that grows with the camera speed. **Full Speed** is the speed (m/s) at which the effect reaches its maximum.
- **Protect Focus**: keeps the target in focus out of the blur (the car stays sharp).
- **Vignette / Fisheye**: dark corners and lens distortion.

Each effect only costs performance while it is on.

## 3. Shake from a script

`shake(trauma, duration)` shakes the camera. `trauma` goes from 0 to 1 and several shakes add up. Example: shake when Space is pressed, as in an explosion.

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

Attach it to any object in the scene. Shake strength and frequency are in the camera's **Camera Shake** panel (or in `shakeAmplitude` and `shakeFrequency`).

## 4. Turning effects on from the game menu

An options menu can turn effects on or off during the game:

```python
camera = Range.logic.getCurrentScene().active_camera
camera.useSpeedBlur = True
camera.speedBlurStrength = 0.5
camera.useDof = False
```

## Film grain

Grain belongs to the scene, not the camera: **Render > Post Processing**, Film Grain option. In the game:

```python
cena = Range.logic.getCurrentScene()
cena.filterManager.changeGrainValues(True, 0.3)
```
