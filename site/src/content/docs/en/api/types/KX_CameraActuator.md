---
title: "KX_CameraActuator"
description: "Range.types.KX_CameraActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Applies changes to a camera.

### damping

strength of of the camera following movement.

**Type:** float

### axis

The camera axis (0, 1, 2) for positive `XYZ`, (3, 4, 5) for negative `XYZ`.

**Type:** int

### min

minimum distance to the target object maintained by the actuator.

**Type:** float

### max

maximum distance to stay from the target object.

**Type:** float

### height

height to stay above the target object.

**Type:** float

### object

the object this actuator tracks.

**Type:** `KX_GameObject` or None

