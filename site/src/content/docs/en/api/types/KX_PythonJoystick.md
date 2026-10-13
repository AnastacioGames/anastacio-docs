---
title: "KX_PythonJoystick"
description: "Range.types.KX_PythonJoystick class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`SCA_JoystickSensor`](../../types/sca_joysticksensor/), [`Range.events`](../../modulos/events/), [`KX_InputSystem`](../../types/kx_inputsystem/)
:::



A Python interface to a joystick.

### name

The name assigned to the joystick by the operating system. (read-only)

**Type:** string

### activeButtons

A list of active button values. (read-only)

**Type:** list

### axisValues

The state of the joysticks axis as a list of values `numAxis` long. (read-only).

**Type:** list of ints.

Each specifying the value of an axis between -1.0 and 1.0
depending on how far the axis is pushed, 0 for nothing.
The first 2 values are used by most joysticks and gamepads for directional control.
3rd and 4th values are only on some joysticks and can be used for arbitary controls.

* left:[-1.0, 0.0, ...]
* right:[1.0, 0.0, ...]
* up:[0.0, -1.0, ...]
* down:[0.0, 1.0, ...]

### hatValues (Deprecated. Use :data:`activeButtons` instead)

The state of the joysticks hats as a list of values `numHats` long. (read-only).

**Type:** list of ints

Each specifying the direction of the hat from 1 to 12, 0 when inactive.

Hat directions are as follows...

* 0:None
* 1:Up
* 2:Right
* 4:Down
* 8:Left
* 3:Up - Right
* 6:Down - Right
* 12:Down - Left
* 9:Up - Left

### numAxis

The number of axes for the joystick at this index. (read-only).

**Type:** integer

### numButtons

The number of buttons for the joystick at this index. (read-only).

**Type:** integer

### numHats (Deprecated. Use :data:`numButtons` instead)

The number of hats for the joystick at this index. (read-only).

**Type:** integer

### startVibration()

Starts the vibration.

**Returns:** None

### stopVibration()

Stops the vibration.

**Returns:** None

### strengthLeft

Strength of the Low frequency joystick's motor (placed at left position usually).

**Type:** float (0.0 to 1.0)

### strengthRight

Strength of the High frequency joystick's motor (placed at right position usually).

**Type:** float (0.0 to 1.0)

### duration

Duration of the vibration in milliseconds.

**Type:** integer (0 to infinite)

### isVibrating

Check status of joystick vibration

**Type:** bool (true vibrating and false stopped)

### hasVibration

Check if the joystick supports vibration

**Type:** bool (true supported and false not supported)

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### stopVibration()

 <small>method</small>

Stops the gamepad vibration.

### duration

 <small>attribute</small>

Vibration duration, in milliseconds.

### hasVibration

 <small>attribute · read-only</small>

`True` if the gamepad supports vibration.

### inputs

 <small>attribute · read-only</small>

Dictionary `{button: SCA_InputEvent}` with the state of each gamepad button.

### isVibrating

 <small>attribute · read-only</small>

`True` while the gamepad is vibrating.

### strengthLeft

 <small>attribute</small>

Left vibration motor strength (0 to 1).

### strengthRight

 <small>attribute</small>

Right vibration motor strength (0 to 1).

