---
title: "SCA_DelaySensor"
description: "Range.types.SCA_DelaySensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



The Delay sensor generates positive and negative triggers at precise time,
expressed in number of frames. The delay parameter defines the length of the initial OFF period. A positive trigger is generated at the end of this period.

The duration parameter defines the length of the ON period following the OFF period.
There is a negative trigger at the end of the ON period. If duration is 0, the sensor stays ON and there is no negative trigger.

The sensor runs the OFF-ON cycle once unless the repeat option is set: the OFF-ON cycle repeats indefinately (or the OFF cycle if duration is 0).

Use `SCA_ISensor.reset` at any time to restart sensor.

### delay

length of the initial OFF period as number of frame, 0 for immediate trigger.

**Type:** integer.

### duration

length of the ON period in number of frame after the initial OFF period.

If duration is greater than 0, a negative trigger is sent at the end of the ON pulse.

**Type:** integer

### repeat

1 if the OFF-ON cycle should be repeated indefinately, 0 if it should run once.

**Type:** integer

### repeatTimes

Number of times the actuator will repeat.

**Type:** integer.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### useDelta

 <small>attribute</small>

Counts the delay in seconds (real time) instead of logic frames.

