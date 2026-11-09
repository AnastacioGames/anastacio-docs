---
title: "Range.audio"
description: "Range.audio module reference"
---

Anastacio Engine module `Range.audio`. Also available as `bge.audio`.

```python
# Turn the microphone on and read the voice level.
import Range

if Range.audio.microphoneState() == "closed":
    Range.audio.microphoneStart()

print("Voice:", Range.audio.microphoneLevel())
```

```python
# Record the voice and play it back with a robot effect.
import Range

Range.audio.microphoneRecordStart()

# Later, when the player stops talking.
Range.audio.microphoneRecordStop("taunt")
Range.audio.playVoice("taunt", effect="ROBOT", reverb=True)
```

```python
# Control a World Sound module by name.
import Range

Range.audio.play("Music", fade=2.0)
Range.audio.setVolume("Music", 0.5)
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### edit(sound, start=0, end=-1, fade_in=0, fade_out=0, normalize=False)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Trims, fades and normalizes a sound; same as `aud.edit`.

**Returns:** `aud.Sound`

### getVolume(module)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Module volume; `None` when it does not exist.

**Returns:** `float`

### isLive()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

`True` while the microphone is being heard.

**Returns:** `bool`

### isPlaying(module)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

`True` while a sound of the module plays.

**Returns:** `bool`

### microphone()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

The `aud.Microphone` in use, for advanced use; `None` before it starts.

**Returns:** `aud.Microphone`

### microphoneDropped()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Times audio was lost because the game hitched.

**Returns:** `int`

### microphoneError()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Why the microphone did not open.

**Returns:** `str`

### microphoneIsRecording()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

`True` while recording.

**Returns:** `bool`

### microphoneLevel()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Voice level now, 0 to 1.

**Returns:** `float`

### microphonePeak()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Peak with a slow fall, 0 to 1.

**Returns:** `float`

### microphoneRecordingSeconds()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Length of the recording in progress, in seconds.

**Returns:** `float`

### microphoneRecordStart()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Starts recording.

### microphoneRecordStop(slot="last")

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Stops and keeps the recording as `slot`. Returns the `aud.Sound` or `None`.

**Returns:** `aud.Sound`

### microphoneSave(slot, path)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Saves a recording as WAV. Relative paths go to the game folder (Web: `/saves`).

### microphoneStart(device="")

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Turns the microphone on. On the Web, call it after a click or touch. `False` when it cannot open.

**Returns:** `bool`

### microphoneState()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Microphone state: `'closed'`, `'pending'`, `'granted'`, `'denied'` or `'error'`.

**Returns:** `str`

### microphoneStop()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Turns the microphone off.

### modules()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Names of the World Sound modules loaded so far.

**Returns:** `list`

### next(module)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Music: crosses to the next track.

### pause(module)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Pauses every sound of the module where it is.

### play(module, sound="", fade=-1.0)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Plays a sound of a World Sound module, or resumes a paused module. Without `sound`, Music plays the current track and Ambient plays every layer. `fade` is in seconds; negative uses the module Fade. `False` when the module or sound does not exist.

**Returns:** `bool`

### playing(module)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Names of the sounds playing now (Music: the current track).

**Returns:** `list`

### playLive(effect="NONE", amount=1.0, volume=1.0, reverb=False)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Plays the microphone now with a voice effect. One at a time; calling again swaps the effect. Use headphones: speakers feed back into the microphone.

### playVoice(sound, effect="NONE", amount=1.0, volume=1.0, reverb=False)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Plays a recording (name or `aud.Sound`) with a voice effect; see `voicePresets()`. `reverb=True` uses the area or World reverb. `False` when the recording or effect does not exist.

**Returns:** `bool`

### previous(module)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Music: crosses to the previous track.

### recording(slot)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

The `aud.Sound` of a recording, or `None`.

**Returns:** `aud.Sound`

### recordings()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Names of the recordings kept so far.

**Returns:** `list`

### resume(module)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Goes on from where `pause(module)` stopped.

### setRecording(slot, sound)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Keeps an `aud.Sound` under a name. `None` removes it.

### setVolume(module, volume)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Sets the module volume, 0.0 to 1.0.

### sounds(module)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Names of the sounds of the module.

**Returns:** `list`

### stop(module, sound="", fade=-1.0)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Stops a World Sound module, or only one of its sounds. `fade` is in seconds; negative uses the module Fade.

### stopLive()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Stops hearing the microphone.

### voiceFx(sound, preset, amount=1.0)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Applies a voice effect; same as `aud.voice_fx`.

**Returns:** `aud.Sound`

### voicePresets(live=False)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Names of the voice effects.

**Returns:** `list`

