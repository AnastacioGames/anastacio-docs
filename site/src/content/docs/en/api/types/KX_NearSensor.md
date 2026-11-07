---
title: "KX_NearSensor"
description: "Range.types.KX_NearSensor class reference"
---

Base class: [`KX_CollisionSensor`](../kx_collisionsensor/)



A near sensor is a specialised form of touch sensor.

```python
# Open the door when someone gets close, and only close it further away.
import Range

sensor = Range.logic.getCurrentController().sensors["Near"]

sensor.distance = 3.0
sensor.resetDistance = 5.0

if sensor.positive:
    print(sensor.hitObject.name, "is near")
```

### distance

The near sensor activates when an object is within this distance.

**Type:** float

### resetDistance

The near sensor deactivates when the object exceeds this distance.

**Type:** float

