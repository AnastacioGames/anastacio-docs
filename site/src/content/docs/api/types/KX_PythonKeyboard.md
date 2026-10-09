---
title: "KX_PythonKeyboard"
description: "Referência da classe Range.types.KX_PythonKeyboard"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



The current keyboard.

### inputs

A dictionary containing the input of each keyboard key. (read-only).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### events

A dictionary containing the status of each keyboard event or key. (read-only).

:::danger[Obsoleto use `inputs`]

:::

**Tipo:** dictionary {`keycode`:`status`, ...}

### activeInputs

A dictionary containing the input of only the active keyboard keys. (read-only).

**Tipo:** dictionary {`keycode`:`SCA_InputEvent`, ...}

### active_events

A dictionary containing the status of only the active keyboard events or keys. (read-only).

:::danger[Obsoleto use `activeInputs`]

:::

**Tipo:** dictionary {`keycode`:`status`, ...}

### text

The typed unicode text from the last frame.

**Tipo:** string

### getClipboard()

Gets the clipboard text.

**Tipo do retorno:** string

### setClipboard(text)

Sets the clipboard text.

- **`text`**: New clipboard text
  - tipo: string

