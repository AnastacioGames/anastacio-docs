---
title: "SCA_JoystickSensor"
description: "Range.types.SCA_JoystickSensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



This sensor detects player joystick events.

### axisValues

The state of the joysticks axis as a list of values `numAxis` long. (read-only).

**Type:** list of ints.

Each specifying the value of an axis between -32767 and 32767 depending on how far the axis is pushed, 0 for nothing.
The first 2 values are used by most joysticks and gamepads for directional control. 3rd and 4th values are only on some joysticks and can be used for arbitary controls.

* left:[-32767, 0, ...]
* right:[32767, 0, ...]
* up:[0, -32767, ...]
* down:[0, 32767, ...]

### axisSingle

like `axisValues` but returns a single axis value that is set by the sensor. (read-only).

**Type:** integer

:::note
Only use this for "Single Axis" type sensors otherwise it will raise an error.
:::

### hatValues (Deprecated. Use :data:button instead)

The state of the joysticks hats as a list of values `numHats` long. (read-only).

**Type:** list of ints

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

### hatSingle (Deprecated. Use :data:button instead)

Like `hatValues` but returns a single hat direction value that is set by the sensor. (read-only).

**Type:** integer

### numAxis

The number of axes for the joystick at this index. (read-only).

**Type:** integer

### numButtons

The number of buttons for the joystick at this index. (read-only).

**Type:** integer

### numHats (Deprecated. Use :data:numButtons instead)

The number of hats for the joystick at this index. (read-only).

**Type:** integer

### connected

True if a joystick is connected at this joysticks index. (read-only).

**Type:** boolean

### index

The joystick index to use (from 0 to 7). The first joystick is always 0.

**Type:** integer

### threshold

Axis threshold. Joystick axis motion below this threshold wont trigger an event. Use values between (0 and 32767), lower values are more sensitive.

**Type:** integer

### button

The button index the sensor reacts to (first button = 0). When the "All Events" toggle is set, this option has no effect.

**Type:** integer

### axis

The axis this sensor reacts to, as a list of two values [axisIndex, axisDirection]

* axisIndex: the axis index to use when detecting axis movement, 1=primary directional control, 2=secondary directional control.
* axisDirection: 0=right, 1=up, 2=left, 3=down.

**Type:** [integer, integer]

### hat (Deprecated. Use :data:button instead)

The hat the sensor reacts to, as a list of two values: [hatIndex, hatDirection]

* hatIndex: the hat index to use when detecting hat movement, 1=primary hat, 2=secondary hat (4 max).
* hatDirection: 1-12.

**Type:** [integer, integer]

### getButtonActiveList()

**Returns:** A list containing the indicies of the currently pressed buttons.

**Return type:** list

### getButtonStatus(buttonIndex)

- **`buttonIndex`**: the button index, 0=first button
  - type: integer

**Returns:** The current pressed state of the specified button.

**Return type:** boolean

