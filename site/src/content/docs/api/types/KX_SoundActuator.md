---
title: "KX_SoundActuator"
description: "Referência da classe Range.types.KX_SoundActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Sound Actuator.

The `startSound`, `pauseSound` and `stopSound` do not require the actuator to be activated - they act instantly provided that the actuator has been activated once at least.

### volume

The volume (gain) of the sound.

**Tipo:** float

### time

The current position in the audio stream (in seconds).

**Tipo:** float

### pitch

The pitch of the sound.

**Tipo:** float

### mode

The operation mode of the actuator. Can be one of `these constants`

**Tipo:** integer

### sound

The sound the actuator should play.

**Tipo:** Audaspace factory

### is3D

Whether or not the actuator should be using 3D sound. (read-only)

**Tipo:** boolean

### volume_maximum

The maximum gain of the sound, no matter how near it is.

**Tipo:** float

### volume_minimum

The minimum gain of the sound, no matter how far it is away.

**Tipo:** float

### distance_reference

The distance where the sound has a gain of 1.0.

**Tipo:** float

### distance_maximum

The maximum distance at which you can hear the sound.

**Tipo:** float

### attenuation

The influence factor on volume depending on distance.

**Tipo:** float

### cone_angle_inner

The angle of the inner cone.

**Tipo:** float

### cone_angle_outer

The angle of the outer cone.

**Tipo:** float

### cone_volume_outer

The gain outside the outer cone (the gain in the outer cone will be interpolated between this value and the normal gain in the inner cone).

**Tipo:** float

### startSound()

Starts the sound.

**Retorna:** None

### pauseSound()

Pauses the sound.

**Retorna:** None

### stopSound()

Stops the sound.

**Retorna:** None

