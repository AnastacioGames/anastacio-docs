---
title: "Range.events"
description: "Range.events module reference"
---

:::tip[See also]
[`KX_PythonKeyboard`](../../types/kx_pythonkeyboard/), [`KX_PythonMouse`](../../types/kx_pythonmouse/), [`SCA_InputEvent`](../../types/sca_inputevent/), [`SCA_KeyboardSensor`](../../types/sca_keyboardsensor/)
:::

## Intro

This module holds key constants for the SCA_KeyboardSensor.

```python

# Set a connected keyboard sensor to accept F1
import Range

co = Range.logic.getCurrentController()
# 'Keyboard' is a keyboard sensor
sensor = co.sensors["Keyboard"]
sensor.key = Range.events.F1KEY
```

```python

# Do the all keys thing
import Range

co = Range.logic.getCurrentController()
# 'Keyboard' is a keyboard sensor
sensor = co.sensors["Keyboard"]

for key, input in sensor.inputs:
	# key[0] == Range.events.keycode = event.type, key[1] = input
	if Range.logic.KX_INPUT_JUST_ACTIVATED in input.queue:
		if key == Range.events.WKEY:
			# Activate Forward!
		if key == Range.events.SKEY:
			# Activate Backward!
		if key == Range.events.AKEY:
			# Activate Left!
		if key == Range.events.DKEY:
			# Activate Right!
```

```python

# The all keys thing without a keyboard sensor (but you will
# need an always sensor with pulse mode on)
import Range

# Just shortening names here
keyboard = Range.logic.keyboard
JUST_ACTIVATED = Range.logic.KX_INPUT_JUST_ACTIVATED

if JUST_ACTIVATED in keyboard.inputs[Range.events.WKEY].queue:
	print("Activate Forward!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.SKEY].queue:
	print("Activate Backward!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.AKEY].queue:
	print("Activate Left!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.DKEY].queue:
	print("Activate Right!")
```

## Functions

### EventToString(event)

Return the string name of a key event. Will raise a ValueError error if its invalid.

- **`event`**: key event constant from `Range.events` or the keyboard sensor.
  - type: int

**Return type:** string

### EventToCharacter(event, shift)

Return the string name of a key event. Returns an empty string if the event cant be represented as a character.

  - type: int
- **`event`**: key event constant from `Range.events` or the keyboard sensor.
  - type: bool
- **`shift`**: set to true if shift is held.

**Return type:** string

## Keys (Constants)

## Mouse Keys

### LEFTMOUSE

Left mouse button.

### MIDDLEMOUSE

Middle mouse button (wheel click).

### RIGHTMOUSE

Right mouse button.

### WHEELUPMOUSE

Mouse wheel scrolled up.

### WHEELDOWNMOUSE

Mouse wheel scrolled down.

### LEFTTHUMBMOUSE

Back side mouse button.

### RIGHTTHUMBMOUSE

Forward side mouse button.

### BUTTON6MOUSE

Extra mouse button 6.

### BUTTON7MOUSE

Extra mouse button 7.

### MOUSEX

Horizontal mouse movement.

### MOUSEY

## Keyboard Keys

## Alphabet keys

### AKEY

A key.

### BKEY

B key.

### CKEY

C key.

### DKEY

D key.

### EKEY

E key.

### FKEY

F key.

### GKEY

G key.

### HKEY

H key.

### IKEY

I key.

### JKEY

J key.

### KKEY

K key.

### LKEY

L key.

### MKEY

M key.

### NKEY

N key.

### OKEY

O key.

### PKEY

P key.

### QKEY

Q key.

### RKEY

R key.

### SKEY

S key.

### TKEY

T key.

### UKEY

U key.

### VKEY

V key.

### WKEY

W key.

### XKEY

X key.

### YKEY

Y key.

### ZKEY

## Number keys

### ZEROKEY

0 key on the number row (not the numpad).

### ONEKEY

1 key on the number row (not the numpad).

### TWOKEY

2 key on the number row (not the numpad).

### THREEKEY

3 key on the number row (not the numpad).

### FOURKEY

4 key on the number row (not the numpad).

### FIVEKEY

5 key on the number row (not the numpad).

### SIXKEY

6 key on the number row (not the numpad).

### SEVENKEY

7 key on the number row (not the numpad).

### EIGHTKEY

8 key on the number row (not the numpad).

### NINEKEY

## Modifiers Keys

### CAPSLOCKKEY

Caps Lock key.

### LEFTCTRLKEY

Left Ctrl key.

### LEFTALTKEY

Left Alt key.

### RIGHTALTKEY

Right Alt key (AltGr).

### RIGHTCTRLKEY

Right Ctrl key.

### RIGHTSHIFTKEY

Right Shift key.

### LEFTSHIFTKEY

## Arrow Keys

### LEFTARROWKEY

Left arrow.

### DOWNARROWKEY

Down arrow.

### RIGHTARROWKEY

Right arrow.

### UPARROWKEY

## Numberpad Keys

### PAD0

Numpad 0 key.

### PAD1

Numpad 1 key.

### PAD2

Numpad 2 key.

### PAD3

Numpad 3 key.

### PAD4

Numpad 4 key.

### PAD5

Numpad 5 key.

### PAD6

Numpad 6 key.

### PAD7

Numpad 7 key.

### PAD8

Numpad 8 key.

### PAD9

Numpad 9 key.

### PADPERIOD

Numpad period key.

### PADSLASHKEY

Numpad / key.

### PADASTERKEY

Numpad * key.

### PADMINUS

Numpad - key.

### PADENTER

Numpad Enter key.

### PADPLUSKEY

## Function Keys

### F1KEY

F1 key.

### F2KEY

F2 key.

### F3KEY

F3 key.

### F4KEY

F4 key.

### F5KEY

F5 key.

### F6KEY

F6 key.

### F7KEY

F7 key.

### F8KEY

F8 key.

### F9KEY

F9 key.

### F10KEY

F10 key.

### F11KEY

F11 key.

### F12KEY

F12 key.

### F13KEY

F13 key.

### F14KEY

F14 key.

### F15KEY

F15 key.

### F16KEY

F16 key.

### F17KEY

F17 key.

### F18KEY

F18 key.

### F19KEY

## Other Keys

### ACCENTGRAVEKEY

Grave accent key (`).

### BACKSLASHKEY

Backslash key (\).

### BACKSPACEKEY

Backspace key.

### COMMAKEY

Comma key (,).

### DELKEY

Delete key.

### ENDKEY

End key.

### EQUALKEY

Equal key (=).

### ESCKEY

Esc key.

### HOMEKEY

Home key.

### INSERTKEY

Insert key.

### LEFTBRACKETKEY

Left bracket key ([).

### LINEFEEDKEY

Line Feed key (rare on modern keyboards).

### MINUSKEY

Minus key (-).

### PAGEDOWNKEY

Page Down key.

### PAGEUPKEY

Page Up key.

### PAUSEKEY

Pause key.

### PERIODKEY

Period key (.).

### QUOTEKEY

Quote key (').

### RIGHTBRACKETKEY

Right bracket key (]).

### RETKEY (Deprecated: use bge.events.ENTERKEY)

### ENTERKEY

Enter key.

### SEMICOLONKEY

Semicolon key (;).

### SLASHKEY

Slash key (/).

### SPACEKEY

Space bar.

### TABKEY

Tab key.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### JOYSTICKA

 <small>constant</small>

Gamepad A button.

### JOYSTICKB

 <small>constant</small>

Gamepad B button.

### JOYSTICKBACK

 <small>constant</small>

Gamepad Back/Select button.

### JOYSTICKGUIDE

 <small>constant</small>

Gamepad Guide (center) button.

### JOYSTICKLEFTSHOUDER

 <small>constant</small>

Gamepad left shoulder button (LB).

### JOYSTICKLEFTSTICK

 <small>constant</small>

Gamepad left stick click.

### JOYSTICKPADDOWN

 <small>constant</small>

Gamepad D-pad down.

### JOYSTICKPADLEFT

 <small>constant</small>

Gamepad D-pad left.

### JOYSTICKPADRIGHT

 <small>constant</small>

Gamepad D-pad right.

### JOYSTICKPADUP

 <small>constant</small>

Gamepad D-pad up.

### JOYSTICKRIGHTSHOUDER

 <small>constant</small>

Gamepad right shoulder button (RB).

### JOYSTICKRIGHTSTICK

 <small>constant</small>

Gamepad right stick click.

### JOYSTICKX

 <small>constant</small>

Gamepad X button.

### JOYSTICKY

 <small>constant</small>

Gamepad Y button.

### OSKEY

 <small>constant</small>

System key (Windows/Command).

