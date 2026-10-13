---
title: "KX_InputSystem"
description: "Range.types.KX_InputSystem class reference"
---

:::tip[See also]
[`KX_InputTable`](../../types/kx_inputtable/), [`KX_PythonKeyboard`](../../types/kx_pythonkeyboard/), [`KX_PythonJoystick`](../../types/kx_pythonjoystick/)
:::

Class `Range.types.KX_InputSystem`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### changeJoystickIndex(inputMap, inputTable, name, value)

 <small>method</small>

Changes which gamepad (joystick index) an action uses.

### changeKeyMap(inputMap, inputTable, name, keyType, value)

 <small>method</small>

Changes the key or button bound to an action. Use it for "rebind controls" menus.

### changeSensitivity(inputMap, inputTable, name, value)

 <small>method</small>

Changes an action sensitivity (e.g. mouse or analog stick).

### reloadInputMaps()

 <small>method</small>

Reloads the input maps from the file. It is slow; avoid calling it repeatedly.

### inputMaps

 <small>attribute · read-only</small>

Dictionary `{map: {table: KX_InputTable}}` with all loaded input maps.

