# KX_PythonKeyboard

Base class: [`EXP_PyObjectPlus`](EXP_PyObjectPlus.md)

> **See also:**
[`Range.events`](Range.events.md), [`SCA_InputEvent`](SCA_InputEvent.md), [`KX_PythonMouse`](KX_PythonMouse.md)

The current keyboard.

```python
# Check keys by state.
import Range

keyboard = Range.logic.keyboard

if keyboard.inputs[Range.events.ESCKEY].activated:
    print("Pause")
```

```python
# Read typed text and use the clipboard.
import Range

keyboard = Range.logic.keyboard

print(keyboard.text)
keyboard.setClipboard("Saved code: 1234")
print(keyboard.getClipboard())
```

## inputs

A dictionary containing the input of each keyboard key. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~events~~

A dictionary containing the status of each keyboard event or key. (read-only).

> **Deprecated use :data:`inputs`:**

**Type:** dictionary {`keycode`:`status`, ...}

### activeInputs

A dictionary containing the input of only the active keyboard keys. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### ~~active_events~~

A dictionary containing the status of only the active keyboard events or keys. (read-only).

> **Deprecated use :data:`activeInputs`:**

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
