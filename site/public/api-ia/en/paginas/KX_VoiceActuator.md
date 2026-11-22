# KX_VoiceActuator

Class `Range.types.KX_VoiceActuator`.

```python
# Change the voice effect before playing.
import Range

cont = Range.logic.getCurrentController()
voice = cont.actuators["Voice"]
voice.effect = "RADIO"
cont.activate(voice)
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### amount

*(new in Anastacio)* `attribute`

Effect strength, 0 to 1.

### effect

*(new in Anastacio)* `attribute`

Voice effect, such as `NONE`, `CHIPMUNK`, `GIANT`, `ROBOT`, `RADIO`, `ECHO` or `CAVE`.

### maxSeconds

*(new in Anastacio)* `attribute`

Maximum recording time in seconds, 0 to 600.

### mode

*(new in Anastacio)* `attribute`

Action: `0` record, `1` play, `2` live, `3` stop, `4` save.

### slot

*(new in Anastacio)* `attribute`

Name of the recording used by the actuator.

### useReverb

*(new in Anastacio)* `attribute`

Uses the area or World reverb.

### volume

*(new in Anastacio)* `attribute`

Volume, 0 to 4.
