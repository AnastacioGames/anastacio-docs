---
title: "KX_SceneActuator"
description: "Referência da classe Range.types.KX_SceneActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



Scene Actuator logic brick.

:::caution
Scene actuators that use a scene name will be ignored if at game start, the named scene doesn't exist or is empty

This will generate a warning in the console:

```none

Error: GameObject 'Name' has a SceneActuator 'ActuatorName' (SetScene) without scene
```
:::

### scene

the name of the scene to change to/overlay/underlay/remove/suspend/resume.

**Tipo:** string

### camera

the camera to change to.

**Tipo:** `KX_Camera` on read, string or `KX_Camera` on write

:::note
When setting the attribute, you can use either a `KX_Camera` or the name of the camera.
:::

### useRestart

Set flag to True to restart the sene.

**Tipo:** boolean

### mode

The mode of the actuator.

**Tipo:** integer from 0 to 5.

