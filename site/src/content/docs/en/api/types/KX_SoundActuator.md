---
title: "KX_SoundActuator"
description: "Range.types.KX_SoundActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)

:::tip[See also]
[`KX_Speaker`](../../types/kx_speaker/)
:::



Sound Actuator.

The `startSound`, `pauseSound` and `stopSound` do not require the actuator to be activated - they act instantly provided that the actuator has been activated once at least.

### volume

The volume (gain) of the sound.

**Type:** float

### time

The current position in the audio stream (in seconds).

**Type:** float

### pitch

The pitch of the sound.

**Type:** float

### mode

The operation mode of the actuator. Can be one of `these constants`

**Type:** integer

### sound

The sound the actuator should play.

**Type:** Audaspace factory

### is3D

Whether or not the actuator should be using 3D sound. (read-only)

**Type:** boolean

### volume_maximum

The maximum gain of the sound, no matter how near it is.

**Type:** float

### volume_minimum

The minimum gain of the sound, no matter how far it is away.

**Type:** float

### distance_reference

The distance where the sound has a gain of 1.0.

**Type:** float

### distance_maximum

The maximum distance at which you can hear the sound.

**Type:** float

### attenuation

The influence factor on volume depending on distance.

**Type:** float

### cone_angle_inner

The angle of the inner cone.

**Type:** float

### cone_angle_outer

The angle of the outer cone.

**Type:** float

### cone_volume_outer

The gain outside the outer cone (the gain in the outer cone will be interpolated between this value and the normal gain in the inner cone).

**Type:** float

### startSound()

Starts the sound.

**Returns:** None

### pauseSound()

Pauses the sound.

**Returns:** None

### stopSound()

Stops the sound.

**Returns:** None

