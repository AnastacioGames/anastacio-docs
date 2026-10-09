---
title: "KX_CameraActuator"
description: "Referência da classe Range.types.KX_CameraActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Applies changes to a camera.

### damping

strength of of the camera following movement.

**Tipo:** float

### axis

The camera axis (0, 1, 2) for positive `XYZ`, (3, 4, 5) for negative `XYZ`.

**Tipo:** int

### min

minimum distance to the target object maintained by the actuator.

**Tipo:** float

### max

maximum distance to stay from the target object.

**Tipo:** float

### height

height to stay above the target object.

**Tipo:** float

### object

the object this actuator tracks.

**Tipo:** `KX_GameObject` or None

