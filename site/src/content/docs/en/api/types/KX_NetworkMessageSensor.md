---
title: "KX_NetworkMessageSensor"
description: "Range.types.KX_NetworkMessageSensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



The Message Sensor logic brick.

Currently only loopback (local) networks are supported.

```python
# Read the messages that arrived on this frame.
import Range

sensor = Range.logic.getCurrentController().sensors["Message"]

if sensor.positive:
    for subject, body in zip(sensor.subjects, sensor.bodies):
        print(subject, body)
```

### subject

The subject the sensor is looking for.

**Type:** string

### frameMessageCount

The number of messages received since the last frame. (read-only).

**Type:** integer

### subjects

The list of message subjects received. (read-only).

**Type:** list of strings

### bodies

The list of message bodies received. (read-only).

**Type:** list of strings

