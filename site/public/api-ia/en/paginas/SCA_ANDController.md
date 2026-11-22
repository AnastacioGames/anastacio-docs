# SCA_ANDController

Base class: [`SCA_IController`](SCA_IController.md)

An AND controller activates only when all linked sensors are activated.

There are no special python methods for this controller.

```python
# With an AND controller, the actuators run when all sensors are positive. This script shows the same rule.
import Range

cont = Range.logic.getCurrentController()

if all(sensor.positive for sensor in cont.sensors):
    print("All sensors are on")
```
