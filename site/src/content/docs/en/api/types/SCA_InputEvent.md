---
title: "SCA_InputEvent"
description: "Range.types.SCA_InputEvent class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Events for a keyboard or mouse input.

### status

A list of existing status of the input from the last frame.
Can contain `Range.logic.KX_INPUT_NONE` and `Range.logic.KX_INPUT_ACTIVE`.
The list always contains one value.
The first value of the list is the last value of the list in the last frame. (read-only)

**Type:** list of integer.

### queue

A list of existing events of the input from the last frame.
Can contain `Range.logic.KX_INPUT_JUST_ACTIVATED` and `Range.logic.KX_INPUT_JUST_RELEASED`.
The list can be empty. (read-only)

**Type:** list of integer.

### values

A list of existing value of the input from the last frame.
For keyboard it contains 1 or 0 and for mouse the coordinate of the mouse or the movement of the wheel mouse.
The list contains always one value, the size of the list is the same than `queue` + 1 only for keyboard inputs.
The first value of the list is the last value of the list in the last frame. (read-only)

Example to get the non-normalized mouse coordinates:

```python

import Range

x = Range.logic.mouse.inputs[Range.events.MOUSEX].values[-1]
y = Range.logic.mouse.inputs[Range.events.MOUSEY].values[-1]

print("Mouse non-normalized position: x: {0}, y: {1}".format(x, y))
```

**Type:** list of integer.

### inactive

True if the input was inactive from the last frame.

**Type:** boolean

### active

True if the input was active from the last frame.

**Type:** boolean

### activated

True if the input was activated from the last frame.

**Type:** boolean

### released

True if the input was released from the last frame.

**Type:** boolean

### type

The type of the input.
One of `these constants`

**Type:** integer

