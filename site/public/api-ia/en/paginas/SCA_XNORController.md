# SCA_XNORController

Base class: [`SCA_IController`](SCA_IController.md)

An XNOR controller activates when all linked sensors are the same (activated or inative).

There are no special python methods for this controller.

```python
# XNOR turns the actuators on unless exactly one sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(sum(sensor.positive for sensor in cont.sensors) != 1)
```
