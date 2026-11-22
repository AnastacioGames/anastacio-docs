# KX_MicrophoneSensor

Class `Range.types.KX_MicrophoneSensor`.

```python
# Open the mouth of the character while the player talks.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Microphone"]
cont.owner["mouth"] = sensor.level
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### hold

*(new in Anastacio)* `attribute`

Seconds, 0 to 60: how long talking stays positive, or how much silence is needed.

### level

*(new in Anastacio)* `attribute · read-only`

Voice level now (read-only).

### mode

*(new in Anastacio)* `attribute`

Mode: `0` talking (level above `threshold`), `1` peak (one pulse, like a clap or blow), `2` silence (after `hold` seconds below `threshold`).

### peak

*(new in Anastacio)* `attribute · read-only`

Voice peak (read-only).

### propName

*(new in Anastacio)* `attribute`

Name of the object property tied to the sensor.

### threshold

*(new in Anastacio)* `attribute`

Voice level that triggers the sensor, 0 to 1.
