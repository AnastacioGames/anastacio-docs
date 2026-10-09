---
title: "SCA_VibrationActuator"
description: "Referência da classe Range.types.SCA_VibrationActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Vibration Actuator.

### joyindex

Joystick index.

**Tipo:** integer (0 to 7)

### strengthLeft

Strength of the Low frequency joystick's motor (placed at left position usually).

**Tipo:** float (0.0 to 1.0)

### strengthRight

Strength of the High frequency joystick's motor (placed at right position usually).

**Tipo:** float (0.0 to 1.0)

### duration

Duration of the vibration in milliseconds.

**Tipo:** integer (0 to infinite)

### isVibrating

Check status of joystick vibration

**Tipo:** bool (true vibrating and false stopped)

### hasVibration

Check if the joystick supports vibration

**Tipo:** bool (true supported and false not supported)

### startVibration()

Starts the vibration.

**Retorna:** None

### stopVibration()

Stops the vibration.

**Retorna:** None

