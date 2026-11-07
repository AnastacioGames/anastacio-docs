---
title: "SCA_VibrationActuator"
description: "Range.types.SCA_VibrationActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Vibration Actuator.

```python
# Vibrate the first controller when hit.
import Range

act = Range.logic.getCurrentController().actuators["Vibration"]

if act.hasVibration and not act.isVibrating:
    act.joyindex = 0
    act.strengthLeft = 1.0
    act.strengthRight = 0.5
    act.duration = 300
    act.startVibration()
```

### joyindex

Joystick index.

**Type:** integer (0 to 7)

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

### startVibration()

Starts the vibration.

**Returns:** None

### stopVibration()

Stops the vibration.

**Returns:** None

