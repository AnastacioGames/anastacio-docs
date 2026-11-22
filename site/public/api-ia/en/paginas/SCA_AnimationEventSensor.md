# SCA_AnimationEventSensor

Class `Range.types.SCA_AnimationEventSensor`.

```python
# Fires on the frames marked in the animation.
import Range

cont = Range.logic.getCurrentController()

if cont.sensors["AnimationEvent"].positive:
    print("Step")
```
