---
title: "SCA_AnimationEventSensor"
description: "Range.types.SCA_AnimationEventSensor class reference"
---

Class `Range.types.SCA_AnimationEventSensor`.

```python
# Fires on the frames marked in the animation.
import Range

cont = Range.logic.getCurrentController()

if cont.sensors["AnimationEvent"].positive:
    print("Step")
```



