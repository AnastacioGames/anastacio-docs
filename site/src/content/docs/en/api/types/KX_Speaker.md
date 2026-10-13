---
title: "KX_Speaker"
description: "Range.types.KX_Speaker class reference"
---

:::tip[See also]
[`KX_SoundActuator`](../../types/kx_soundactuator/), [`KX_Scene`](../../types/kx_scene/)
:::

Class `Range.types.KX_Speaker`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### GetActiveEffect()

 <small>method</small>

Active sound effect: 0 none, 1 reverb.

**Returns:** `int`

### GetActiveEffectFilter()

 <small>method</small>

Active filter: 0 none, 1 low-pass, 2 high-pass, 3 band-pass.

**Returns:** `int`

### Pause()

 <small>method</small>

Pauses the sound.

### Play()

 <small>method</small>

Plays the sound.

### RemoveEffect()

 <small>method</small>

Removes the sound effect.

### Restart()

 <small>method</small>

Plays the sound from the beginning.

### SetEffect(effectType, filterType=0)

 <small>method</small>

Applies an effect: `effectType` 1 = reverb; `filterType` 0 none, 1 low-pass, 2 high-pass, 3 band-pass. After that, reverb areas leave this Speaker alone.

### SetSound(sound, cache=False)

 <small>method</small>

Changes the sound (an `aud.Sound`). With `cache=True`, keeps the decoded sound in memory.

### Stop()

 <small>method</small>

Stops the sound.

### attenuation

 <small>attribute</small>

How much the volume drops with distance (3D sound).

### catkey

 <small>attribute</small>

Sound category key in the playback manager, or `None`.

### cone_angle_inner

 <small>attribute</small>

Angle, in degrees, of the cone where the sound plays at full volume.

### cone_angle_outer

 <small>attribute</small>

Angle, in degrees, of the cone outside of which the volume is `cone_volume_outer`.

### cone_volume_outer

 <small>attribute</small>

Volume outside the outer cone.

### distance_maximum

 <small>attribute</small>

Distance after which the volume stops dropping.

### distance_reference

 <small>attribute</small>

Distance at which the sound plays at normal volume.

### filter_gain

 <small>attribute</small>

Overall filter gain.

### filter_gainhf

 <small>attribute</small>

High frequency gain in the filter.

### filter_gainlf

 <small>attribute</small>

Low frequency gain in the filter.

### is3D

 <small>attribute · read-only</small>

`True` if the sound is positional (3D).

### mode

 <small>attribute</small>

Playback mode: 1 plays to the end, 2 loops, 3 ping-pong loop.

### pitch

 <small>attribute</small>

Sound pitch (speed). 1.0 is normal.

### playbackManager

 <small>attribute</small>

Playback manager (`aud.PlaybackManager`) used by the Speaker, or `None`.

### reverb_air_absorption_gain_hf

 <small>attribute</small>

Reverb: high frequency absorption by the air.

### reverb_decay_hf_ratio

 <small>attribute</small>

Reverb: how much faster high frequencies fade than low ones.

### reverb_decay_limit_hf

 <small>attribute</small>

Reverb: limits the high frequency decay.

### reverb_decay_time

 <small>attribute</small>

Reverb: time in seconds the echo takes to fade.

### reverb_density

 <small>attribute</small>

Reverb: echo density.

### reverb_diffusion

 <small>attribute</small>

Reverb: echo diffusion.

### reverb_gain

 <small>attribute</small>

Reverb: overall effect volume.

### reverb_gain_hf

 <small>attribute</small>

Reverb: high frequency volume.

### reverb_late_reverb_delay

 <small>attribute</small>

Reverb: delay of the echo tail.

### reverb_late_reverb_gain

 <small>attribute</small>

Reverb: volume of the echo tail.

### reverb_reflections_delay

 <small>attribute</small>

Reverb: delay of the early reflections.

### reverb_reflections_gain

 <small>attribute</small>

Reverb: volume of the early reflections.

### reverb_room_rolloff_factor

 <small>attribute</small>

Reverb: how much the effect drops with distance.

### sound

 <small>attribute</small>

Current sound (`aud.Sound`), or `None`.

### time

 <small>attribute</small>

Current sound position, in seconds. Can be changed to seek.

### volume

 <small>attribute</small>

Sound volume.

### volume_maximum

 <small>attribute</small>

Maximum volume, even up close.

### volume_minimum

 <small>attribute</small>

Minimum volume, even far away.

