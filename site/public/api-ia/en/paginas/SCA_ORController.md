# SCA_ORController

Base class: [`SCA_IController`](SCA_IController.md)

An OR controller activates when any connected sensor activates.

There are no special python methods for this controller.

```python
# OR turns the actuators on when at least one sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(any(sensor.positive for sensor in cont.sensors))
```
