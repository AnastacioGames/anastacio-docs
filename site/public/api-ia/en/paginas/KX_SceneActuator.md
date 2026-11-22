# KX_SceneActuator

Base class: [`SCA_IActuator`](SCA_IActuator.md)

Scene Actuator logic brick.

> **Caution:**
Scene actuators that use a scene name will be ignored if at game start, the named scene doesn't exist or is empty

This will generate a warning in the console:

```text

Error: GameObject 'Name' has a SceneActuator 'ActuatorName' (SetScene) without scene
```

## scene

the name of the scene to change to/overlay/underlay/remove/suspend/resume.

**Type:** string

### camera

the camera to change to.

**Type:** `KX_Camera` on read, string or `KX_Camera` on write

> **Note:**
When setting the attribute, you can use either a `KX_Camera` or the name of the camera.

### useRestart

Set flag to True to restart the sene.

**Type:** boolean

### mode

The mode of the actuator.

**Type:** integer from 0 to 5.
