---
title: "BL_ActionActuator"
description: "Range.types.BL_ActionActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)

:::tip[See also]
[`KX_GameObject`](../../types/kx_gameobject/), [`BL_ArmatureObject`](../../types/bl_armatureobject/), [`KX_AnimationEventManager`](../../types/kx_animationeventmanager/)
:::



Action Actuators apply an action to an actor.

### action

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

 <small>attribute</small>

Animation layer (0 to 7) the actuator plays the action on. Different layers play at the same time.

### layerWeight

 <small>attribute</small>

Layer weight, from 0.0 to 1.0: how much this action blends with the layers below.

