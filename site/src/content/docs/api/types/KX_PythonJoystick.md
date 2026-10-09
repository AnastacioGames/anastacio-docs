---
title: "KX_PythonJoystick"
description: "Referência da classe Range.types.KX_PythonJoystick"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



A Python interface to a joystick.

### name

The name assigned to the joystick by the operating system. (read-only)

**Tipo:** string

### activeButtons

A list of active button values. (read-only)

**Tipo:** list

### axisValues

The state of the joysticks axis as a list of values `numAxis` long. (read-only).

**Tipo:** list of ints.

Each specifying the value of an axis between -1.0 and 1.0
depending on how far the axis is pushed, 0 for nothing.
The first 2 values are used by most joysticks and gamepads for directional control.
3rd and 4th values are only on some joysticks and can be used for arbitary controls.

* left:[-1.0, 0.0, ...]
* right:[1.0, 0.0, ...]
* up:[0.0, -1.0, ...]
* down:[0.0, 1.0, ...]

### hatValues (Deprecated. Use `activeButtons` instead)

The state of the joysticks hats as a list of values `numHats` long. (read-only).

**Tipo:** list of ints

Each specifying the direction of the hat from 1 to 12, 0 when inactive.

Hat directions are as follows...

* 0:None
* 1:Up
* 2:Right
* 4:Down
* 8:Left
* 3:Up - Right
* 6:Down - Right
* 12:Down - Left
* 9:Up - Left

### numAxis

The number of axes for the joystick at this index. (read-only).

**Tipo:** integer

### numButtons

The number of buttons for the joystick at this index. (read-only).

**Tipo:** integer

### numHats (Deprecated. Use `numButtons` instead)

The number of hats for the joystick at this index. (read-only).

**Tipo:** integer

### startVibration()

Starts the vibration.

**Retorna:** None

### stopVibration()

<span class="ae-badge pendente">sem documentação</span>

Stops the vibration.

**Retorna:** None

### strengthLeft

<span class="ae-badge pendente">sem documentação</span>

Strength of the Low frequency joystick's motor (placed at left position usually).

**Tipo:** float (0.0 to 1.0)

### strengthRight

<span class="ae-badge pendente">sem documentação</span>

Strength of the High frequency joystick's motor (placed at right position usually).

**Tipo:** float (0.0 to 1.0)

### duration

<span class="ae-badge pendente">sem documentação</span>

Duration of the vibration in milliseconds.

**Tipo:** integer (0 to infinite)

### isVibrating

<span class="ae-badge pendente">sem documentação</span>

Check status of joystick vibration

**Tipo:** bool (true vibrating and false stopped)

### hasVibration

<span class="ae-badge pendente">sem documentação</span>

Check if the joystick supports vibration

**Tipo:** bool (true supported and false not supported)

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### stopVibration()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### duration

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### hasVibration

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### inputs

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### isVibrating

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### strengthLeft

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### strengthRight

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

