---
title: "KX_VoiceActuator"
description: "Range.types.KX_VoiceActuator class reference"
---

Class `Range.types.KX_VoiceActuator`.

```python
# Change the voice effect before playing.
import Range

cont = Range.logic.getCurrentController()
voice = cont.actuators["Voice"]
voice.effect = "RADIO"
cont.activate(voice)
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### amount

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Effect strength, 0 to 1.

### effect

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Voice effect, such as `NONE`, `CHIPMUNK`, `GIANT`, `ROBOT`, `RADIO`, `ECHO` or `CAVE`.

### maxSeconds

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Maximum recording time in seconds, 0 to 600.

### mode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Action: `0` record, `1` play, `2` live, `3` stop, `4` save.

### slot

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Name of the recording used by the actuator.

### useReverb

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Uses the area or World reverb.

### volume

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Volume, 0 to 4.

