# SCA_MouseSensor

Base class: [`SCA_ISensor`](SCA_ISensor.md)

Mouse Sensor logic brick.

```python
# Read the position of the mouse and the left button.
import Range

sensor = Range.logic.getCurrentController().sensors["Mouse"]

print(sensor.position)

if sensor.getButtonStatus(Range.logic.KX_MOUSE_BUT_LEFT) == Range.logic.KX_INPUT_ACTIVE:
    print("Left button held")
```

## position

current [x, y] coordinates of the mouse, in frame coordinates (pixels).

**Type:** [integer, interger]

### mode

sensor mode.

Unlike UPBGE, Range has the thumb buttons and buttons 6 and 7 before the wheel, so wheel up, wheel down and movement are 8, 9 and 10 (4, 5 and 6 in UPBGE). Compare with the Range.logic.KX_MOUSESENSORMODE_* constants instead of numbers. Mouse sensors in .blend files from UPBGE and the original BGE are converted when the file is opened.

**Type:** integer * KX_MOUSESENSORMODE_LEFTBUTTON(1) * KX_MOUSESENSORMODE_MIDDLEBUTTON(2) * KX_MOUSESENSORMODE_RIGHTBUTTON(3) * KX_MOUSESENSORMODE_LEFTTHUMBMOUSE(4) * KX_MOUSESENSORMODE_RIGHTTHUMBMOUSE(5) * KX_MOUSESENSORMODE_BUTTON6(6) * KX_MOUSESENSORMODE_BUTTON7(7) * KX_MOUSESENSORMODE_WHEELUP(8) * KX_MOUSESENSORMODE_WHEELDOWN(9) * KX_MOUSESENSORMODE_MOVEMENT(10)

### getButtonStatus(button)

Get the mouse button status.

- **`button`**: The code that represents the key you want to get the state of, use one of `these constants`
  - type: int

**Returns:** The state of the given key, can be one of `these constants`

**Return type:** int

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### holdTime

*(new in Anastacio)* `attribute`

Time in seconds holding the button for the sensor to fire (0 to 30).
