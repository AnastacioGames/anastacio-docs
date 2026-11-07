---
title: "KX_RadarSensor"
description: "Range.types.KX_RadarSensor class reference"
---

Base class: [`KX_NearSensor`](../kx_nearsensor/)



Radar sensor is a near sensor with a conical sensor object.

```python
# Detect enemies in a cone in front of the object.
import Range

sensor = Range.logic.getCurrentController().sensors["Radar"]

sensor.axis = Range.logic.KX_RADAR_AXIS_POS_Y
sensor.distance = 15.0
sensor.angle = 45.0

if sensor.positive:
    print(sensor.hitObject.name)
```

### coneOrigin

The origin of the cone with which to test. The origin is in the middle of the cone. (read-only).

**Type:** `mathutils.Vector`

### coneTarget

The center of the bottom face of the cone with which to test. (read-only).

**Type:** `mathutils.Vector`

### distance

The height of the cone with which to test.

**Type:** float

### angle

The angle of the cone (in degrees) with which to test.

**Type:** float

### axis

The axis on which the radar cone is cast.

**Type:** integer from 0 to 5

KX_RADAR_AXIS_POS_X, KX_RADAR_AXIS_POS_Y, KX_RADAR_AXIS_POS_Z,
KX_RADAR_AXIS_NEG_X, KX_RADAR_AXIS_NEG_Y, KX_RADAR_AXIS_NEG_Z

