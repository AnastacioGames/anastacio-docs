# KX_EndObjectActuator

Base class: [`SCA_IActuator`](SCA_IActuator.md)

Edit Object Actuator (in End Object mode)

This actuator has no python methods.

```python
# Remove the object when its life runs out.
import Range

cont = Range.logic.getCurrentController()

if cont.owner["life"] <= 0:
    cont.activate(cont.actuators["EndObject"])
```
