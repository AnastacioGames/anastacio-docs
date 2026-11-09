---
title: Microphone and voice recording
description: Record sounds in the editor and use the player's microphone in the game, with voice effects, on desktop, Web and Android.
---

The engine records voice in the editor and listens to the microphone during the game. It works on desktop, Web and Android.

## Record in the editor

The **Record** button is in the top bar. One click records straight to the Sequencer. While recording it turns red and shows the time and volume.

The options next to the button are:

- **Record New Sound**: records a new sound without placing it in the Sequencer.
- **Select Microphone**: picks the microphone.
- **Adjust Sound**: trim, fades, normalize and voice effects, saved to a new WAV.
- **Open Video Sequencer Window**: opens the Sequencer in a separate window.

There is also a record button where the sound is used: on the cutscene line, on the Logic Tree Sound node and on Sequencer sound strips.

## Use it in the game without code

**Microphone sensor**

| Mode | When it fires |
|---|---|
| **Talking** | While the voice is above the threshold. Stays on for **Hold** seconds. |
| **Shout / Clap** | One pulse when a loud sound passes the threshold (clap, shout, blow). |
| **Silence** | After **Hold** seconds below the threshold. |

**Voice actuator**

| Mode | What it does |
|---|---|
| **Record** | Records while the sensor is on, or until **Max Seconds**. |
| **Play Recording** | Plays the recording with the effect. |
| **Live** | Plays the microphone with the effect while the sensor is on. |
| **Stop** | Stops the live voice. |
| **Save WAV** | Saves the recording as `<name>.wav` in the game folder. |

In Logic Tree, use the **When Talking** and **Voice** nodes. UI Tree has **Microphone Meter** and **Enable Microphone**.

## Voice effects

`NONE`, `CHIPMUNK` (high), `GIANT` (deep), `ROBOT`, `RADIO`, `ECHO`, `CAVE` and `REVERSE` (recordings only).

:::caution
In live mode, use headphones: speakers feed back into the microphone.
:::

## Use it from Python

```python
import Range

# Turn the microphone on (on the Web, after a click or tap).
if Range.audio.microphoneState() == "closed":
    Range.audio.microphoneStart()

# Open the character's mouth with the voice level.
own["mouth"] = Range.audio.microphoneLevel()

# Record, stop and play with an effect.
Range.audio.microphoneRecordStart()
Range.audio.microphoneRecordStop("taunt")
Range.audio.playVoice("taunt", effect="ROBOT", reverb=True)
```

In the example, `own` is your script's object. The full list is in [`Range.audio`](../../api/modulos/audio/), [`KX_MicrophoneSensor`](../../api/types/kx_microphonesensor/) and [`KX_VoiceActuator`](../../api/types/kx_voiceactuator/).

## Web and Android

In the Web export panel, the **Microphone** option has **Auto**, **On** and **Off**. **Auto** turns it on when the game uses the microphone.

- **Web:** the browser asks the player for permission. The microphone starts after the first tap or click and needs `https` (or `localhost`).
- **Android:** the APK only asks for `RECORD_AUDIO` when the package was exported with microphone.
