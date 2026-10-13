---
title: "SCA_MouseSensor"
description: "Range.types.SCA_MouseSensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



Mouse Sensor logic brick.

### position

current [x, y] coordinates of the mouse, in frame coordinates (pixels).

**Type:** [integer, interger]

### mode

sensor mode.

**Type:** integer * KX_MOUSESENSORMODE_LEFTBUTTON(1) * KX_MOUSESENSORMODE_MIDDLEBUTTON(2) * KX_MOUSESENSORMODE_RIGHTBUTTON(3) * KX_MOUSESENSORMODE_WHEELUP(4) * KX_MOUSESENSORMODE_WHEELDOWN(5) * KX_MOUSESENSORMODE_MOVEMENT(6)

### getButtonStatus(button)

Get the mouse button status.

- **`button`**: The code that represents the key you want to get the state of, use one of `these constants`
  - type: int

**Returns:** The state of the given key, can be one of `these constants`

**Return type:** int

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### holdTime

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Time in seconds holding the button for the sensor to fire (0 to 30).

