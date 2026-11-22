# SCA_WaitActuator

Class `Range.types.SCA_WaitActuator`.

```python
# Wait three seconds.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Wait"]

act.duration = 3.0
act.useRestart = False
cont.activate(act)
```

```python
# Show the remaining time.
import Range

act = Range.logic.getCurrentController().actuators["Wait"]

if act.waiting:
    print(act.duration - act.elapsed)
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### duration

*(new in Anastacio)* `attribute`

Wait time in seconds (0 to 100000). A positive pulse starts the count; when it elapses the actuator finishes and an **Actuator** sensor in Finished mode fires.

### elapsed

*(new in Anastacio)* `attribute · read-only`

Seconds elapsed since the current wait started.

### useRestart

*(new in Anastacio)* `attribute`

If `True`, a new positive pulse while waiting restarts the count from zero.

### waiting

*(new in Anastacio)* `attribute · read-only`

`True` while the actuator is counting.
