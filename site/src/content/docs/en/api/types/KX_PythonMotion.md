---
title: "KX_PythonMotion"
description: "Range.types.KX_PythonMotion class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Motion sensors of the device (phone or tablet), available as `Range.logic.motion`.

Values come from the browser in the Web runtime (`DeviceMotionEvent` and `DeviceOrientationEvent`),
including the Android app, which runs the Web runtime inside a WebView. On other platforms there is no
sensor source yet: `available` is `False`, vectors are zero and `tilt` is `(0.0, 0.0)`, so the
same script runs everywhere.

Vectors use the axes of the screen as it is currently shown, in portrait or landscape: x to the right, y to
the top of the screen and z out of the screen, toward the player.

A tilt-controlled object:

```python

from Range import logic, events

def main(cont):
    own = cont.owner
    if logic.mouse.inputs[events.LEFTMOUSE].activated:  # a tap on the screen
        logic.motion.calibrate()
    x, y = logic.motion.tilt
    own.applyForce((x * 20.0, y * 20.0, 0.0))
```

### available

`True` while the sensors are sending data. It becomes `False` when no reading arrived in the last
second (no sensor, desktop browser, page in background). (read-only).

**Type:** boolean

### gyroscope

Rotation speed around each screen axis, in radians per second. (read-only).

**Type:** `mathutils.Vector`

### accelerometer

Acceleration including gravity, in m/s². With the device lying still, face up, it is close to
`(0, 0, 9.8)`. (read-only).

**Type:** `mathutils.Vector`

### gravity

Gravity alone, in m/s², pointing up as in `accelerometer`. When the device does not report
acceleration without gravity, it is estimated from `accelerometer` with a low-pass filter. (read-only).

**Type:** `mathutils.Vector`

### orientation

Device orientation angles `(alpha, beta, gamma)` in degrees, exactly as given by the browser. They follow
the device axes, not the screen axes. (read-only).

**Type:** `mathutils.Vector`

### tilt

How far the device is tilted from its neutral position, from -1.0 to 1.0 on each axis: the screen direction
a ball would roll to. `x` is positive when the right edge of the screen goes down, `y` when the top edge
goes down. The neutral position is the device lying flat until `calibrate` is called. (read-only).

**Type:** tuple (float, float)

### calibrate()

Take the current position as neutral for `tilt`, so the player can hold the device the way they like.

**Returns:** `True` if there was a sensor reading to calibrate with, `False` otherwise.

**Return type:** boolean

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### recenter()

<span class="ae-badge novo">new in Anastacio</span> <small>method</small>

Uses the current head direction (VR) as "forward". `False` if the sensor is not ready.

**Returns:** `bool`

### headOrientation

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Head orientation (3×3 matrix), already recentered.

### recenterTime

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Time in seconds to recenter by itself when the head stays still (0 turns it off).

### smoothing

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Head movement smoothing (0 to 5).

