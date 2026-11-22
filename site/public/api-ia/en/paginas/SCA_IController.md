# SCA_IController

Base class: [`SCA_ILogicBrick`](SCA_ILogicBrick.md)

Base class for all controller logic bricks.

```python
# List what is connected to this controller.
import Range

cont = Range.logic.getCurrentController()

print([sensor.name for sensor in cont.sensors])
print([act.name for act in cont.actuators])
```

```python
# Run this controller before the others.
import Range

Range.logic.getCurrentController().useHighPriority = True
```

## state

The controllers state bitmask. This can be used with the GameObject's state to test if the controller is active.

**Type:** int bitmask

### sensors

A list of sensors linked to this controller.

**Type:** sequence supporting index/string lookups and iteration.

> **Note:**
The sensors are not necessarily owned by the same object.

> **Note:**
When objects are instanced in dupligroups links may be lost from objects outside the dupligroup.

### actuators

A list of actuators linked to this controller.

**Type:** sequence supporting index/string lookups and iteration.

> **Note:**
The sensors are not necessarily owned by the same object.

> **Note:**
When objects are instanced in dupligroups links may be lost from objects outside the dupligroup.

### useHighPriority

When set the controller executes always before all other controllers that dont have this set.

**Type:** boolen

> **Note:**
Order of execution between high priority controllers is not guaranteed.
