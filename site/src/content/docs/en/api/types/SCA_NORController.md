---
title: "SCA_NORController"
description: "Range.types.SCA_NORController class reference"
---

Base class: [`SCA_IController`](../sca_icontroller/)



An NOR controller activates only when all linked sensors are de-activated.

There are no special python methods for this controller.

```python
# NOR turns the actuators on only when no sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(not any(sensor.positive for sensor in cont.sensors))
```



