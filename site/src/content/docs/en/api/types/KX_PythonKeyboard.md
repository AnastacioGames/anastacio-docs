---
title: "KX_PythonKeyboard"
description: "Range.types.KX_PythonKeyboard class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`Range.events`](../../modulos/events/), [`SCA_InputEvent`](../../types/sca_inputevent/), [`KX_PythonMouse`](../../types/kx_pythonmouse/)
:::



The current keyboard.

### inputs

A dictionary containing the input of each keyboard key. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~events~~

A dictionary containing the status of each keyboard event or key. (read-only).

:::danger[Deprecated use :data:`inputs`]

:::

**Type:** dictionary {`keycode`:`status`, ...}

### activeInputs

A dictionary containing the input of only the active keyboard keys. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~active_events~~

A dictionary containing the status of only the active keyboard events or keys. (read-only).

:::danger[Deprecated use :data:`activeInputs`]

:::

**Type:** dictionary {`keycode`:`status`, ...}

### text

The typed unicode text from the last frame.

**Type:** string

### getClipboard()

Gets the clipboard text.

**Return type:** string

### setClipboard(text)

Sets the clipboard text.

- **`text`**: New clipboard text
  - type: string

