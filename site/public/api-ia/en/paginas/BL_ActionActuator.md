# BL_ActionActuator

Base class: [`SCA_IActuator`](SCA_IActuator.md)

> **See also:**
[`KX_GameObject`](KX_GameObject.md), [`BL_ArmatureObject`](BL_ArmatureObject.md), [`KX_AnimationEventManager`](KX_AnimationEventManager.md)

Action Actuators apply an action to an actor.

```python
# Play part of an action on a separate layer.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Action"]

act.action = "Wave"
act.frameStart = 1
act.frameEnd = 30
act.layer = 1
act.mode = Range.logic.KX_ACTIONACT_PLAY
cont.activate(act)
```

## action

The name of the action to set as the current action.

**Type:** string

### frameStart

Specifies the starting frame of the animation.

**Type:** float

### frameEnd

Specifies the ending frame of the animation.

**Type:** float

### blendIn

Specifies the number of frames of animation to generate when making transitions between actions.

**Type:** float

### priority

Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers.

**Type:** integer

### frame

Sets the current frame for the animation.

**Type:** float

### propName

Sets the property to be used in FromProp playback mode.

**Type:** string

### mode

The operation mode of the actuator. Can be one of `these constants`.

**Type:** integer

### useContinue

The actions continue option, True or False. When True, the action will always play from where last left off,
otherwise negative events to this actuator will reset it to its start frame.

**Type:** boolean

### framePropName

The name of the property that is set to the current frame number.

**Type:** string

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### layer

 `attribute`

Animation layer (0 to 7) the actuator plays the action on. Different layers play at the same time.

### layerWeight

 `attribute`

Layer weight, from 0.0 to 1.0: how much this action blends with the layers below.
