---
title: "KX_CameraActuator"
description: "Range.types.KX_CameraActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



Applies changes to a camera.

```python
# Make the camera follow another object, at a set distance.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Camera"]

act.object = Range.logic.getCurrentScene().objects["Car"]
act.min = 4.0
act.max = 8.0
act.height = 2.5
act.damping = 0.1
cont.activate(act)
```

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

