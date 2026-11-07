---
title: "KX_MovementSensor"
description: "Range.types.KX_MovementSensor class reference"
---

Class `Range.types.KX_MovementSensor`.

```python
# Fire when the object moves on any axis.
import Range

sensor = Range.logic.getCurrentController().sensors["Movement"]

sensor.axis = 6
sensor.threshold = 0.05

if sensor.positive:
    print("Moving")
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### axis

 <small>attribute</small>

Watched axis: 0 to 2 = +X, +Y, +Z; 3 to 5 = -X, -Y, -Z; 6 = all.

### threshold

 <small>attribute</small>

How much the object must move for the sensor to fire.

