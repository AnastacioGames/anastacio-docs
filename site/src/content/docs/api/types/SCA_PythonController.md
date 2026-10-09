---
title: "SCA_PythonController"
description: "Referência da classe Range.types.SCA_PythonController"
---

Classe base: [`SCA_IController`](../sca_icontroller/)



A Python controller uses a Python script to activate it's actuators, based on it's sensors.

### owner

The object the controller is attached to.

**Tipo:** `KX_GameObject`

### script

The value of this variable depends on the execution methid.

* When 'Script' execution mode is set this value contains the entire python script as a single string (not the script name as you might expect) which can be modified to run different scripts.
* When 'Module' execution mode is set this value will contain a single line string - module name and function "module.func" or "package.modile.func" where the module names are python textblocks or external scripts.

**Tipo:** string

:::note
Once this is set the script name given for warnings will remain unchanged.
:::

### mode

the execution mode for this controller (read-only).

* Script: 0, Execite the `script` as a python code.
* Module: 1, Execite the `script` as a module and function.

**Tipo:** integer

### activate(actuator)

Activates an actuator attached to this controller.

- **`actuator`**: The actuator to operate on.
  - tipo: actuator or the actuator name as a string

### deactivate(actuator)

Deactivates an actuator attached to this controller.

- **`actuator`**: The actuator to operate on.
  - tipo: actuator or the actuator name as a string

