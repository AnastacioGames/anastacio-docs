---
title: "Range.events"
description: "Referência do módulo Range.events"
---

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
  - tipo: int

**Tipo do retorno:** string

### EventToCharacter(event, shift)

Return the string name of a key event. Returns an empty string if the event cant be represented as a character.

  - tipo: int
- **`event`**: key event constant from `Range.events` or the keyboard sensor.
  - tipo: bool
- **`shift`**: set to true if shift is held.

**Tipo do retorno:** string

## Keys (Constants)

## Mouse Keys

### LEFTMOUSE

<span class="ae-badge pendente">sem descrição</span>

### MIDDLEMOUSE

<span class="ae-badge pendente">sem descrição</span>

### RIGHTMOUSE

<span class="ae-badge pendente">sem descrição</span>

### WHEELUPMOUSE

<span class="ae-badge pendente">sem descrição</span>

### WHEELDOWNMOUSE

<span class="ae-badge pendente">sem descrição</span>

### LEFTTHUMBMOUSE

<span class="ae-badge pendente">sem descrição</span>

### RIGHTTHUMBMOUSE

<span class="ae-badge pendente">sem descrição</span>

### BUTTON6MOUSE

<span class="ae-badge pendente">sem descrição</span>

### BUTTON7MOUSE

<span class="ae-badge pendente">sem descrição</span>

### MOUSEX

<span class="ae-badge pendente">sem descrição</span>

### MOUSEY

## Keyboard Keys

## Alphabet keys

### AKEY

<span class="ae-badge pendente">sem descrição</span>

### BKEY

<span class="ae-badge pendente">sem descrição</span>

### CKEY

<span class="ae-badge pendente">sem descrição</span>

### DKEY

<span class="ae-badge pendente">sem descrição</span>

### EKEY

<span class="ae-badge pendente">sem descrição</span>

### FKEY

<span class="ae-badge pendente">sem descrição</span>

### GKEY

<span class="ae-badge pendente">sem descrição</span>

### HKEY

<span class="ae-badge pendente">sem descrição</span>

### IKEY

<span class="ae-badge pendente">sem descrição</span>

### JKEY

<span class="ae-badge pendente">sem descrição</span>

### KKEY

<span class="ae-badge pendente">sem descrição</span>

### LKEY

<span class="ae-badge pendente">sem descrição</span>

### MKEY

<span class="ae-badge pendente">sem descrição</span>

### NKEY

<span class="ae-badge pendente">sem descrição</span>

### OKEY

<span class="ae-badge pendente">sem descrição</span>

### PKEY

<span class="ae-badge pendente">sem descrição</span>

### QKEY

<span class="ae-badge pendente">sem descrição</span>

### RKEY

<span class="ae-badge pendente">sem descrição</span>

### SKEY

<span class="ae-badge pendente">sem descrição</span>

### TKEY

<span class="ae-badge pendente">sem descrição</span>

### UKEY

<span class="ae-badge pendente">sem descrição</span>

### VKEY

<span class="ae-badge pendente">sem descrição</span>

### WKEY

<span class="ae-badge pendente">sem descrição</span>

### XKEY

<span class="ae-badge pendente">sem descrição</span>

### YKEY

<span class="ae-badge pendente">sem descrição</span>

### ZKEY

## Number keys

### ZEROKEY

<span class="ae-badge pendente">sem descrição</span>

### ONEKEY

<span class="ae-badge pendente">sem descrição</span>

### TWOKEY

<span class="ae-badge pendente">sem descrição</span>

### THREEKEY

<span class="ae-badge pendente">sem descrição</span>

### FOURKEY

<span class="ae-badge pendente">sem descrição</span>

### FIVEKEY

<span class="ae-badge pendente">sem descrição</span>

### SIXKEY

<span class="ae-badge pendente">sem descrição</span>

### SEVENKEY

<span class="ae-badge pendente">sem descrição</span>

### EIGHTKEY

<span class="ae-badge pendente">sem descrição</span>

### NINEKEY

## Modifiers Keys

### CAPSLOCKKEY

<span class="ae-badge pendente">sem descrição</span>

### LEFTCTRLKEY

<span class="ae-badge pendente">sem descrição</span>

### LEFTALTKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTALTKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTCTRLKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTSHIFTKEY

<span class="ae-badge pendente">sem descrição</span>

### LEFTSHIFTKEY

## Arrow Keys

### LEFTARROWKEY

<span class="ae-badge pendente">sem descrição</span>

### DOWNARROWKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTARROWKEY

<span class="ae-badge pendente">sem descrição</span>

### UPARROWKEY

## Numberpad Keys

### PAD0

<span class="ae-badge pendente">sem descrição</span>

### PAD1

<span class="ae-badge pendente">sem descrição</span>

### PAD2

<span class="ae-badge pendente">sem descrição</span>

### PAD3

<span class="ae-badge pendente">sem descrição</span>

### PAD4

<span class="ae-badge pendente">sem descrição</span>

### PAD5

<span class="ae-badge pendente">sem descrição</span>

### PAD6

<span class="ae-badge pendente">sem descrição</span>

### PAD7

<span class="ae-badge pendente">sem descrição</span>

### PAD8

<span class="ae-badge pendente">sem descrição</span>

### PAD9

<span class="ae-badge pendente">sem descrição</span>

### PADPERIOD

<span class="ae-badge pendente">sem descrição</span>

### PADSLASHKEY

<span class="ae-badge pendente">sem descrição</span>

### PADASTERKEY

<span class="ae-badge pendente">sem descrição</span>

### PADMINUS

<span class="ae-badge pendente">sem descrição</span>

### PADENTER

<span class="ae-badge pendente">sem descrição</span>

### PADPLUSKEY

## Function Keys

### F1KEY

<span class="ae-badge pendente">sem descrição</span>

### F2KEY

<span class="ae-badge pendente">sem descrição</span>

### F3KEY

<span class="ae-badge pendente">sem descrição</span>

### F4KEY

<span class="ae-badge pendente">sem descrição</span>

### F5KEY

<span class="ae-badge pendente">sem descrição</span>

### F6KEY

<span class="ae-badge pendente">sem descrição</span>

### F7KEY

<span class="ae-badge pendente">sem descrição</span>

### F8KEY

<span class="ae-badge pendente">sem descrição</span>

### F9KEY

<span class="ae-badge pendente">sem descrição</span>

### F10KEY

<span class="ae-badge pendente">sem descrição</span>

### F11KEY

<span class="ae-badge pendente">sem descrição</span>

### F12KEY

<span class="ae-badge pendente">sem descrição</span>

### F13KEY

<span class="ae-badge pendente">sem descrição</span>

### F14KEY

<span class="ae-badge pendente">sem descrição</span>

### F15KEY

<span class="ae-badge pendente">sem descrição</span>

### F16KEY

<span class="ae-badge pendente">sem descrição</span>

### F17KEY

<span class="ae-badge pendente">sem descrição</span>

### F18KEY

<span class="ae-badge pendente">sem descrição</span>

### F19KEY

## Other Keys

### ACCENTGRAVEKEY

<span class="ae-badge pendente">sem descrição</span>

### BACKSLASHKEY

<span class="ae-badge pendente">sem descrição</span>

### BACKSPACEKEY

<span class="ae-badge pendente">sem descrição</span>

### COMMAKEY

<span class="ae-badge pendente">sem descrição</span>

### DELKEY

<span class="ae-badge pendente">sem descrição</span>

### ENDKEY

<span class="ae-badge pendente">sem descrição</span>

### EQUALKEY

<span class="ae-badge pendente">sem descrição</span>

### ESCKEY

<span class="ae-badge pendente">sem descrição</span>

### HOMEKEY

<span class="ae-badge pendente">sem descrição</span>

### INSERTKEY

<span class="ae-badge pendente">sem descrição</span>

### LEFTBRACKETKEY

<span class="ae-badge pendente">sem descrição</span>

### LINEFEEDKEY

<span class="ae-badge pendente">sem descrição</span>

### MINUSKEY

<span class="ae-badge pendente">sem descrição</span>

### PAGEDOWNKEY

<span class="ae-badge pendente">sem descrição</span>

### PAGEUPKEY

<span class="ae-badge pendente">sem descrição</span>

### PAUSEKEY

<span class="ae-badge pendente">sem descrição</span>

### PERIODKEY

<span class="ae-badge pendente">sem descrição</span>

### QUOTEKEY

<span class="ae-badge pendente">sem descrição</span>

### RIGHTBRACKETKEY

<span class="ae-badge pendente">sem descrição</span>

### RETKEY (Deprecated: use bge.events.ENTERKEY)

### ENTERKEY

<span class="ae-badge pendente">sem descrição</span>

### SEMICOLONKEY

<span class="ae-badge pendente">sem descrição</span>

### SLASHKEY

<span class="ae-badge pendente">sem descrição</span>

### SPACEKEY

<span class="ae-badge pendente">sem descrição</span>

### TABKEY

<span class="ae-badge pendente">sem descrição</span>

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### JOYSTICKA

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKB

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKBACK

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKGUIDE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKLEFTSHOUDER

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKLEFTSTICK

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKPADDOWN

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKPADLEFT

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKPADRIGHT

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKPADUP

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKRIGHTSHOUDER

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKRIGHTSTICK

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKX

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### JOYSTICKY

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### OSKEY

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

