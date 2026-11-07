---
title: "KX_AnimationEventManager"
description: "Range.types.KX_AnimationEventManager class reference"
---

:::tip[See also]
[`KX_AnimationEvent`](../../types/kx_animationevent/), [`SCA_AnimationEventSensor`](../../types/sca_animationeventsensor/)
:::

Class `Range.types.KX_AnimationEventManager`.

```python
# Play a step sound on the frames marked in the animation.
import Range

cont = Range.logic.getCurrentController()
own = cont.owner

fired = sum(event.getFireCount() for event in own.animationEventManager.events)

if fired != own.get("steps", 0):
    own["steps"] = fired
    cont.activate("StepSound")
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### events

 <small>attribute · read-only</small>

List of the object animation events (`KX_AnimationEvent`).

