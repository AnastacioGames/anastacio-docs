# KX_AnimationEventManager

> **See also:**
[`KX_AnimationEvent`](KX_AnimationEvent.md), [`SCA_AnimationEventSensor`](SCA_AnimationEventSensor.md)

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

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### events

 `attribute · read-only`

List of the object animation events (`KX_AnimationEvent`).
