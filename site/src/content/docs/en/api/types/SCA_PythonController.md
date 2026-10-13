---
title: "SCA_PythonController"
description: "Range.types.SCA_PythonController class reference"
---

Base class: [`SCA_IController`](../sca_icontroller/)

:::tip[See also]
[`KX_PythonComponent`](../../types/kx_pythoncomponent/), [`SCA_ISensor`](../../types/sca_isensor/), [`SCA_IActuator`](../../types/sca_iactuator/), [`Range.logic`](../../modulos/logic/)
:::



A Python controller uses a Python script to activate it's actuators,
based on it's sensors.

### owner

The object the controller is attached to.

**Type:** `KX_GameObject`

### script

The value of this variable depends on the execution methid.

* When 'Script' execution mode is set this value contains the entire python script as a single string (not the script name as you might expect) which can be modified to run different scripts.
* When 'Module' execution mode is set this value will contain a single line string - module name and function "module.func" or "package.modile.func" where the module names are python textblocks or external scripts.

**Type:** string

:::note
Once this is set the script name given for warnings will remain unchanged.
:::

### mode

the execution mode for this controller (read-only).

* Script: 0, Execite the `script` as a python code.
* Module: 1, Execite the `script` as a module and function.

**Type:** integer

### activate(actuator)

Activates an actuator attached to this controller.

- **`actuator`**: The actuator to operate on.
  - type: actuator or the actuator name as a string

### deactivate(actuator)

Deactivates an actuator attached to this controller.

- **`actuator`**: The actuator to operate on.
  - type: actuator or the actuator name as a string

