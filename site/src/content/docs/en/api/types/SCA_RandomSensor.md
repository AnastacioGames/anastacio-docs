---
title: "SCA_RandomSensor"
description: "Range.types.SCA_RandomSensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



This sensor activates randomly.

```python
# Use a fixed seed to repeat the same sequence.
import Range

sensor = Range.logic.getCurrentController().sensors["Random"]

sensor.seed = 1234
print(sensor.lastDraw)
```

### lastDraw

The seed of the random number generator.

**Type:** integer

### seed

The seed of the random number generator.

**Type:** integer

