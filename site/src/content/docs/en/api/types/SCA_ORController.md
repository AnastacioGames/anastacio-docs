---
title: "SCA_ORController"
description: "Range.types.SCA_ORController class reference"
---

Base class: [`SCA_IController`](../sca_icontroller/)



An OR controller activates when any connected sensor activates.

There are no special python methods for this controller.

```python
# OR turns the actuators on when at least one sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(any(sensor.positive for sensor in cont.sensors))
```



