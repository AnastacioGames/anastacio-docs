# KX_AnimationEvent

Class `Range.types.KX_AnimationEvent`.

```python
# See how many times each event of the animation fired.
import Range

own = Range.logic.getCurrentController().owner

for event in own.animationEventManager.events:
    print(event.triggers, event.getFireCount())
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### getFireCount(index=-1)

 `method`

How many times trigger number `index` fired. With -1, adds up all triggers.

**Returns:** `int`

### triggers

 `attribute · read-only`

List of the animation frames where the event fires.
