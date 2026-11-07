---
title: "SCA_XORController"
description: "Range.types.SCA_XORController class reference"
---

Base class: [`SCA_IController`](../sca_icontroller/)



An XOR controller activates when there is the input is mixed, but not when all are on or off.

There are no special python methods for this controller.

```python
# XOR turns the actuators on when exactly one sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(sum(sensor.positive for sensor in cont.sensors) == 1)
```



