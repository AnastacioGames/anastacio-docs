---
title: "SCA_ISensor"
description: "Range.types.SCA_ISensor class reference"
---

Base class: [`SCA_ILogicBrick`](../sca_ilogicbrick/)



Base class for all sensor logic bricks.

### usePosPulseMode

Flag to turn positive pulse mode on and off.

**Type:** boolean

### useNegPulseMode

Flag to turn negative pulse mode on and off.

**Type:** boolean

### frequency

The frequency for pulse mode sensors. (Deprecated: use SCA_ISensor.skippedTicks)

**Type:** integer

### skippedTicks

Number of logic ticks skipped between 2 active pulses

**Type:** integer

### level

level Option whether to detect level or edge transition when entering a state.
It makes a difference only in case of logic state transition (state actuator).
A level detector will immediately generate a pulse, negative or positive
depending on the sensor condition, as soon as the state is activated.
A edge detector will wait for a state change before generating a pulse.
note: mutually exclusive with `tap`, enabling will disable `tap`.

**Type:** boolean

### tap

When enabled only sensors that are just activated will send a positive event,
after this they will be detected as negative by the controllers.
This will make a key thats held act as if its only tapped for an instant.
note: mutually exclusive with `level`, enabling will disable `level`.

**Type:** boolean

### invert

Flag to set if this sensor activates on positive or negative events.

**Type:** boolean

### triggered

True if this sensor brick is in a positive state. (read-only).

**Type:** boolean

### positive

True if this sensor brick is in a positive state. (read-only).

**Type:** boolean

### pos_ticks

The number of ticks since the last positive pulse (read-only).

**Type:** int

### neg_ticks

The number of ticks since the last negative pulse (read-only).

**Type:** int

### status

The status of the sensor (read-only): can be one of `these constants`.

**Type:** int

:::note
This convenient attribute combines the values of triggered and positive attributes.
:::

### reset()

Reset sensor internal state, effect depends on the type of sensor and settings.

The sensor is put in its initial state as if it was just activated.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### useDeltaTime

 <small>attribute</small>

Uses real time (delta time) for the sensor intervals instead of counting frames.

