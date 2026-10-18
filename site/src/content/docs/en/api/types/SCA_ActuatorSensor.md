---
title: "SCA_ActuatorSensor"
description: "Range.types.SCA_ActuatorSensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



Actuator sensor detect change in actuator state of the parent object.
It generates a positive pulse if the corresponding actuator is activated
and a negative pulse if the actuator is deactivated.

### actuator

the name of the actuator that the sensor is monitoring.

**Type:** string

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### mode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

`0` Active: true while the watched actuator is active. `1` Finished: pulses when the actuator finishes (e.g. Wait, Action, Video).

