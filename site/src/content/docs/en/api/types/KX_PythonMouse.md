---
title: "KX_PythonMouse"
description: "Range.types.KX_PythonMouse class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`Range.events`](../../modulos/events/), [`SCA_InputEvent`](../../types/sca_inputevent/), [`KX_PythonKeyboard`](../../types/kx_pythonkeyboard/)
:::



The current mouse.

:::caution
Mouse normalization is using the maximum coordinate in width and height, whether `Range.render.getWindowWidth() - 1` or `Range.render.getWindowHeight() - 1`.

A script setting the mouse at center is similar to the following example:

```python

import Range

w, h = Range.render.getWindowWidth() - 1, Range.render.getWindowHeight() - 1
center_x, center_y = (w // 2) / w, (h // 2) / h

Range.logic.mouse.position = center_x, center_y
```

Note the usage of floor division to round an existing coordinate.
:::

### inputs

A dictionary containing the input of each mouse event. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~events~~

a dictionary containing the status of each mouse event. (read-only).

:::danger[Deprecated use :data:`inputs`]

:::

**Type:** dictionary {`keycode`:`status`, ...}

### activeInputs

A dictionary containing the input of only the active mouse events. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~active_events~~

a dictionary containing the status of only the active mouse events. (read-only).

:::danger[Deprecated use :data:`activeInputs`]

:::

**Type:** dictionary {`keycode`:`status`, ...}

### position

The normalized x and y position of the mouse cursor.

**Type:** tuple (x, y)

### visible

The visibility of the mouse cursor.

**Type:** boolean

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### reCenter()

 <small>method</small>

Puts the cursor back in the window center (useful for first-person cameras).

### deltaPosition

 <small>attribute · read-only</small>

How much the mouse moved since the last frame, `(x, y)`.

