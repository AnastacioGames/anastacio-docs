---
title: "BL_ActionActuator"
description: "Referência da classe Range.types.BL_ActionActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Action Actuators apply an action to an actor.

### action

The name of the action to set as the current action.

**Tipo:** string

### frameStart

Specifies the starting frame of the animation.

**Tipo:** float

### frameEnd

Specifies the ending frame of the animation.

**Tipo:** float

### blendIn

Specifies the number of frames of animation to generate when making transitions between actions.

**Tipo:** float

### priority

Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers.

**Tipo:** integer

### frame

Sets the current frame for the animation.

**Tipo:** float

### propName

Sets the property to be used in FromProp playback mode.

**Tipo:** string

### mode

The operation mode of the actuator. Can be one of `these constants`.

**Tipo:** integer

### useContinue

The actions continue option, True or False. When True, the action will always play from where last left off, otherwise negative events to this actuator will reset it to its start frame.

**Tipo:** boolean

### framePropName

The name of the property that is set to the current frame number.

**Tipo:** string

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### layer

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### layerWeight

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

