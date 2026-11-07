---
title: "SCA_PropertySensor"
description: "Range.types.SCA_PropertySensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



Activates when the game object property matches.

```python
# Fire when the life property reaches zero.
import Range

sensor = Range.logic.getCurrentController().sensors["Property"]

sensor.mode = Range.logic.KX_PROPSENSOR_EQUAL
sensor.propName = "life"
sensor.value = "0"
```

```python
# Fire when the value is inside an interval.
import Range

sensor = Range.logic.getCurrentController().sensors["Property"]

sensor.mode = Range.logic.KX_PROPSENSOR_INTERVAL
sensor.propName = "life"
sensor.min = "1"
sensor.max = "20"
```

### mode

Type of check on the property. Can be one of `these constants`

**Type:** integer.

### propName

the property the sensor operates.

**Type:** string

### value

the value with which the sensor compares to the value of the property.

**Type:** string

### min

the minimum value of the range used to evaluate the property when in interval mode.

**Type:** string

### max

the maximum value of the range used to evaluate the property when in interval mode.

**Type:** string

