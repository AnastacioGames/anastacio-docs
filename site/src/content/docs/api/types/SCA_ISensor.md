---
title: "SCA_ISensor"
description: "Referência da classe Range.types.SCA_ISensor"
---

Classe base: [`SCA_ILogicBrick`](../sca_ilogicbrick/)



Base class for all sensor logic bricks.

### usePosPulseMode

Flag to turn positive pulse mode on and off.

**Tipo:** boolean

### useNegPulseMode

Flag to turn negative pulse mode on and off.

**Tipo:** boolean

### frequency

The frequency for pulse mode sensors. (Deprecated: use SCA_ISensor.skippedTicks)

**Tipo:** integer

### skippedTicks

Number of logic ticks skipped between 2 active pulses

**Tipo:** integer

### level

level Option whether to detect level or edge transition when entering a state.
It makes a difference only in case of logic state transition (state actuator).
A level detector will immediately generate a pulse, negative or positive
depending on the sensor condition, as soon as the state is activated.
A edge detector will wait for a state change before generating a pulse.
note: mutually exclusive with `tap`, enabling will disable `tap`.

**Tipo:** boolean

### tap

When enabled only sensors that are just activated will send a positive event,
after this they will be detected as negative by the controllers.
This will make a key thats held act as if its only tapped for an instant.
note: mutually exclusive with `level`, enabling will disable `level`.

**Tipo:** boolean

### invert

Flag to set if this sensor activates on positive or negative events.

**Tipo:** boolean

### triggered

True if this sensor brick is in a positive state. (read-only).

**Tipo:** boolean

### positive

True if this sensor brick is in a positive state. (read-only).

**Tipo:** boolean

### pos_ticks

The number of ticks since the last positive pulse (read-only).

**Tipo:** int

### neg_ticks

The number of ticks since the last negative pulse (read-only).

**Tipo:** int

### status

The status of the sensor (read-only): can be one of `these constants`.

**Tipo:** int

:::note
This convenient attribute combines the values of triggered and positive attributes.
:::

### reset()

Reset sensor internal state, effect depends on the type of sensor and settings.

The sensor is put in its initial state as if it was just activated.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### useDeltaTime

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

