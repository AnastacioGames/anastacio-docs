---
title: "SCA_KeyboardSensor"
description: "Range.types.SCA_KeyboardSensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



A keyboard sensor detects player key presses.

See module `Range.events` for keycode values.

### key

The key code this sensor is looking for.

**Type:** keycode from `Range.events` module

### hold1

The key code for the first modifier this sensor is looking for.

**Type:** keycode from `Range.events` module

### hold2

The key code for the second modifier this sensor is looking for.

**Type:** keycode from `Range.events` module

### toggleProperty

The name of the property that indicates whether or not to log keystrokes as a string.

**Type:** string

### targetProperty

The name of the property that receives keystrokes in case in case a string is logged.

**Type:** string

### useAllKeys

Flag to determine whether or not to accept all keys.

**Type:** boolean

### inputs

A list of pressed input keys that have either been pressed, or just released, or are active this frame. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~events~~

a list of pressed keys that have either been pressed, or just released, or are active this frame. (read-only).

:::danger[Deprecated use :data:`inputs`]

:::

**Type:** list [[`keycode`, `status`], ...]

### getKeyStatus(keycode)

Get the status of a key.

- **`keycode`**: The code that represents the key you want to get the state of, use one of `these constants`
  - type: integer

**Returns:** The state of the given key, can be one of `these constants`

**Return type:** int

