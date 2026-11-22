# SCA_ActuatorSensor

Base class: [`SCA_ISensor`](SCA_ISensor.md)

Actuator sensor detect change in actuator state of the parent object.
It generates a positive pulse if the corresponding actuator is activated
and a negative pulse if the actuator is deactivated.

```python
# Wait for an action to end before going on.
import Range

sensor = Range.logic.getCurrentController().sensors["ActuatorDone"]

sensor.actuator = "Wait"
sensor.mode = 1

if sensor.positive:
    print("Finished")
```

## actuator

the name of the actuator that the sensor is monitoring.

**Type:** string

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### mode

*(new in Anastacio)* `attribute`

`0` Active: true while the watched actuator is active. `1` Finished: pulses when the actuator finishes (e.g. Wait, Action, Video).
