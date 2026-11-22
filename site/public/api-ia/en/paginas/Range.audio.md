# Range.audio

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

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### edit(sound, start=0, end=-1, fade_in=0, fade_out=0, normalize=False)

*(new in Anastacio)* `function`

Trims, fades and normalizes a sound; same as `aud.edit`.

**Returns:** `aud.Sound`

### getVolume(module)

*(new in Anastacio)* `function`

Module volume; `None` when it does not exist.

**Returns:** `float`

### isLive()

*(new in Anastacio)* `function`

`True` while the microphone is being heard.

**Returns:** `bool`

### isPlaying(module)

*(new in Anastacio)* `function`

`True` while a sound of the module plays.

**Returns:** `bool`

### microphone()

*(new in Anastacio)* `function`

The `aud.Microphone` in use, for advanced use; `None` before it starts.

**Returns:** `aud.Microphone`

### microphoneDropped()

*(new in Anastacio)* `function`

Times audio was lost because the game hitched.

**Returns:** `int`

### microphoneError()

*(new in Anastacio)* `function`

Why the microphone did not open.

**Returns:** `str`

### microphoneIsRecording()

*(new in Anastacio)* `function`

`True` while recording.

**Returns:** `bool`

### microphoneLevel()

*(new in Anastacio)* `function`

Voice level now, 0 to 1.

**Returns:** `float`

### microphoneNote(a4=440.0)

*(new in Anastacio)* `function`

(name, cents, midi) of the current note, e.g. ('A4', -12.5, 69); ('', 0.0, 0) with no clear note.

### microphonePeak()

*(new in Anastacio)* `function`

Peak with a slow fall, 0 to 1.

**Returns:** `float`

### microphonePitch()

*(new in Anastacio)* `function`

### microphoneRecordingSeconds()

*(new in Anastacio)* `function`

Length of the recording in progress, in seconds.

**Returns:** `float`

### microphoneRecordStart()

*(new in Anastacio)* `function`

Starts recording.

### microphoneRecordStop(slot="last")

*(new in Anastacio)* `function`

Stops and keeps the recording as `slot`. Returns the `aud.Sound` or `None`.

**Returns:** `aud.Sound`

### microphoneSave(slot, path)

*(new in Anastacio)* `function`

Saves a recording as WAV. Relative paths go to the game folder (Web: `/saves`).

### microphoneStart(device="")

*(new in Anastacio)* `function`

Turns the microphone on. On the Web, call it after a click or touch. `False` when it cannot open.

**Returns:** `bool`

### microphoneState()

*(new in Anastacio)* `function`

Microphone state: `'closed'`, `'pending'`, `'granted'`, `'denied'` or `'error'`.

**Returns:** `str`

### microphoneStop()

*(new in Anastacio)* `function`

Turns the microphone off.

### modules()

*(new in Anastacio)* `function`

Names of the World Sound modules loaded so far.

**Returns:** `list`

### next(module)

*(new in Anastacio)* `function`

Music: crosses to the next track.

### pause(module)

*(new in Anastacio)* `function`

Pauses every sound of the module where it is.

### play(module, sound="", fade=-1.0)

*(new in Anastacio)* `function`

Plays a sound of a World Sound module, or resumes a paused module. Without `sound`, Music plays the current track and Ambient plays every layer. `fade` is in seconds; negative uses the module Fade. `False` when the module or sound does not exist.

**Returns:** `bool`

### playing(module)

*(new in Anastacio)* `function`

Names of the sounds playing now (Music: the current track).

**Returns:** `list`

### playLive(effect="NONE", amount=1.0, volume=1.0, reverb=False)

*(new in Anastacio)* `function`

Plays the microphone now with a voice effect. One at a time; calling again swaps the effect. Use headphones: speakers feed back into the microphone.

### playVoice(sound, effect="NONE", amount=1.0, volume=1.0, reverb=False)

*(new in Anastacio)* `function`

Plays a recording (name or `aud.Sound`) with a voice effect; see `voicePresets()`. `reverb=True` uses the area or World reverb. `False` when the recording or effect does not exist.

**Returns:** `bool`

### previous(module)

*(new in Anastacio)* `function`

Music: crosses to the previous track.

### recording(slot)

*(new in Anastacio)* `function`

The `aud.Sound` of a recording, or `None`.

**Returns:** `aud.Sound`

### recordings()

*(new in Anastacio)* `function`

Names of the recordings kept so far.

**Returns:** `list`

### resume(module)

*(new in Anastacio)* `function`

Goes on from where `pause(module)` stopped.

### setRecording(slot, sound)

*(new in Anastacio)* `function`

Keeps an `aud.Sound` under a name. `None` removes it.

### setVolume(module, volume)

*(new in Anastacio)* `function`

Sets the module volume, 0.0 to 1.0.

### sounds(module)

*(new in Anastacio)* `function`

Names of the sounds of the module.

**Returns:** `list`

### stop(module, sound="", fade=-1.0)

*(new in Anastacio)* `function`

Stops a World Sound module, or only one of its sounds. `fade` is in seconds; negative uses the module Fade.

### stopLive()

*(new in Anastacio)* `function`

Stops hearing the microphone.

### voiceFx(sound, preset, amount=1.0)

*(new in Anastacio)* `function`

Applies a voice effect; same as `aud.voice_fx`.

**Returns:** `aud.Sound`

### voicePresets(live=False)

*(new in Anastacio)* `function`

Names of the voice effects.

**Returns:** `list`
