# SCA_NANDController

Base class: [`SCA_IController`](SCA_IController.md)

An NAND controller activates when all linked sensors are not active.

There are no special python methods for this controller.

```python
# NAND turns the actuators on unless all sensors are positive.
import Range

cont = Range.logic.getCurrentController()

print(not all(sensor.positive for sensor in cont.sensors))
```
