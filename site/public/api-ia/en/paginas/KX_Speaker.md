# KX_Speaker

> **See also:**
[`KX_SoundActuator`](KX_SoundActuator.md), [`KX_Scene`](KX_Scene.md)

Class `Range.types.KX_Speaker`.

```python
# Control a speaker of the scene.
import Range

scene = Range.logic.getCurrentScene()

for speaker in scene.speakers:
    speaker.volume = 0.5
    speaker.pitch = 1.0
    speaker.Play()
```

```python
# Pause, continue from the start or stop.
import Range

speaker = Range.logic.getCurrentScene().speakers[0]

speaker.Pause()
speaker.Restart()
speaker.Stop()
```

```python
# Sound that gets lower with distance.
import Range

speaker = Range.logic.getCurrentScene().speakers[0]

speaker.distance_reference = 2.0
speaker.distance_maximum = 40.0
speaker.attenuation = 1.0
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### GetActiveEffect()

 `method`

Active sound effect: 0 none, 1 reverb.

**Returns:** `int`

### GetActiveEffectFilter()

 `method`

Active filter: 0 none, 1 low-pass, 2 high-pass, 3 band-pass.

**Returns:** `int`

### Pause()

 `method`

Pauses the sound.

### Play()

 `method`

Plays the sound.

### RemoveEffect()

 `method`

Removes the sound effect.

### Restart()

 `method`

Plays the sound from the beginning.

### SetEffect(effectType, filterType=0)

 `method`

Applies an effect: `effectType` 1 = reverb; `filterType` 0 none, 1 low-pass, 2 high-pass, 3 band-pass. After that, reverb areas leave this Speaker alone.

### SetSound(sound, cache=False)

 `method`

Changes the sound (an `aud.Sound`). With `cache=True`, keeps the decoded sound in memory.

### Stop()

 `method`

Stops the sound.

### attenuation

 `attribute`

How much the volume drops with distance (3D sound).

### catkey

 `attribute`

Sound category key in the playback manager, or `None`.

### cone_angle_inner

 `attribute`

Angle, in degrees, of the cone where the sound plays at full volume.

### cone_angle_outer

 `attribute`

Angle, in degrees, of the cone outside of which the volume is `cone_volume_outer`.

### cone_volume_outer

 `attribute`

Volume outside the outer cone.

### distance_maximum

 `attribute`

Distance after which the volume stops dropping.

### distance_reference

 `attribute`

Distance at which the sound plays at normal volume.

### filter_gain

 `attribute`

Overall filter gain.

### filter_gainhf

 `attribute`

High frequency gain in the filter.

### filter_gainlf

 `attribute`

Low frequency gain in the filter.

### is3D

 `attribute · read-only`

`True` if the sound is positional (3D).

### mode

 `attribute`

Playback mode: 1 plays to the end, 2 loops, 3 ping-pong loop.

### pitch

 `attribute`

Sound pitch (speed). 1.0 is normal.

### playbackManager

 `attribute`

Playback manager (`aud.PlaybackManager`) used by the Speaker, or `None`.

### reverb_air_absorption_gain_hf

 `attribute`

Reverb: high frequency absorption by the air.

### reverb_decay_hf_ratio

 `attribute`

Reverb: how much faster high frequencies fade than low ones.

### reverb_decay_limit_hf

 `attribute`

Reverb: limits the high frequency decay.

### reverb_decay_time

 `attribute`

Reverb: time in seconds the echo takes to fade.

### reverb_density

 `attribute`

Reverb: echo density.

### reverb_diffusion

 `attribute`

Reverb: echo diffusion.

### reverb_gain

 `attribute`

Reverb: overall effect volume.

### reverb_gain_hf

 `attribute`

Reverb: high frequency volume.

### reverb_late_reverb_delay

 `attribute`

Reverb: delay of the echo tail.

### reverb_late_reverb_gain

 `attribute`

Reverb: volume of the echo tail.

### reverb_reflections_delay

 `attribute`

Reverb: delay of the early reflections.

### reverb_reflections_gain

 `attribute`

Reverb: volume of the early reflections.

### reverb_room_rolloff_factor

 `attribute`

Reverb: how much the effect drops with distance.

### sound

 `attribute`

Current sound (`aud.Sound`), or `None`.

### time

 `attribute`

Current sound position, in seconds. Can be changed to seek.

### volume

 `attribute`

Sound volume.

### volume_maximum

 `attribute`

Maximum volume, even up close.

### volume_minimum

 `attribute`

Minimum volume, even far away.
