---
title: "KX_MicrophoneSensor"
description: "Range.types.KX_MicrophoneSensor class reference"
---

Class `Range.types.KX_MicrophoneSensor`.

```python
# Open the mouth of the character while the player talks.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Microphone"]
cont.owner["mouth"] = sensor.level
```



## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### hold

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Seconds, 0 to 60: how long talking stays positive, or how much silence is needed.

### level

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Voice level now (read-only).

### mode

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Mode: `0` talking (level above `threshold`), `1` peak (one pulse, like a clap or blow), `2` silence (after `hold` seconds below `threshold`).

### peak

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Voice peak (read-only).

### propName

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Name of the object property tied to the sensor.

### threshold

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Voice level that triggers the sensor, 0 to 1.

