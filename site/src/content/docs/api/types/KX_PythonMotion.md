---
title: "KX_PythonMotion"
description: "Referência da classe Range.types.KX_PythonMotion"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Motion sensors of the device (phone or tablet), available as `Range.logic.motion`.

Values come from the browser in the Web runtime (`DeviceMotionEvent` and `DeviceOrientationEvent`),
including the Android app, which runs the Web runtime inside a WebView. On other platforms there is no
sensor source yet: `available` is `False`, vectors are zero and `tilt` is `(0.0, 0.0)`, so the
same script runs everywhere.

Vectors use the axes of the screen as it is currently shown, in portrait or landscape: x to the right, y to
the top of the screen and z out of the screen, toward the player.

A tilt-controlled object:

``python

from Range import logic, events

def main(cont):
    own = cont.owner
    if logic.mouse.inputs[events.LEFTMOUSE].activated:  # a tap on the screen
        logic.motion.calibrate()
    x, y = logic.motion.tilt
    own.applyForce((x * 20.0, y * 20.0, 0.0))
``

### available

`True` while the sensors are sending data. It becomes `False` when no reading arrived in the last
second (no sensor, desktop browser, page in background). (read-only).

**Tipo:** boolean

### gyroscope

Rotation speed around each screen axis, in radians per second. (read-only).

**Tipo:** `mathutils.Vector`

### accelerometer

Acceleration including gravity, in m/s². With the device lying still, face up, it is close to
`(0, 0, 9.8)`. (read-only).

**Tipo:** `mathutils.Vector`

### gravity

Gravity alone, in m/s², pointing up as in `accelerometer`. When the device does not report
acceleration without gravity, it is estimated from `accelerometer` with a low-pass filter. (read-only).

**Tipo:** `mathutils.Vector`

### orientation

Device orientation angles `(alpha, beta, gamma)` in degrees, exactly as given by the browser. They follow
the device axes, not the screen axes. (read-only).

**Tipo:** `mathutils.Vector`

### tilt

How far the device is tilted from its neutral position, from -1.0 to 1.0 on each axis: the screen direction
a ball would roll to. `x` is positive when the right edge of the screen goes down, `y` when the top edge
goes down. The neutral position is the device lying flat until `calibrate` is called. (read-only).

**Tipo:** tuple (float, float)

### calibrate()

Take the current position as neutral for `tilt`, so the player can hold the device the way they like.

**Retorna:** `True` if there was a sensor reading to calibrate with, `False` otherwise.

**Tipo do retorno:** boolean

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### recenter()

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

### headOrientation

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### recenterTime

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### smoothing

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

