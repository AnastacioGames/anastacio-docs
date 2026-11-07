---
title: "SCA_AlwaysSensor"
description: "Range.types.SCA_AlwaysSensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



This sensor is always activated.

```python
# Run a script only once, when the object starts.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Always"]

sensor.usePosPulseMode = False

if sensor.positive:
    cont.owner["life"] = 100
```

```python
# Repeat every 30 logic frames.
import Range

sensor = Range.logic.getCurrentController().sensors["Always"]

sensor.usePosPulseMode = True
sensor.skippedTicks = 30
```



