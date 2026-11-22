# Range.logic

> **See also:**
[`KX_GameObject`](KX_GameObject.md), [`KX_Scene`](KX_Scene.md), [`Range.events`](Range.events.md), [`SCA_PythonController`](SCA_PythonController.md)

```python
# Save a value between scenes and between game sessions.
import Range

Range.logic.globalDict["level"] = 3
Range.logic.saveGlobalDict()
```

```python
# Read it back when the game opens.
import Range

Range.logic.loadGlobalDict()
level = Range.logic.globalDict.get("level", 1)
print("Level:", level)
```

```python
# Move the object with the keyboard, at the same speed on any frame rate.
import Range

own = Range.logic.getCurrentController().owner
keys = Range.logic.keyboard.inputs

if keys[Range.events.WKEY].active:
    own.applyMovement((0.0, 0.1, 0.0), True)
```

```python
# Slow the whole game down for a dramatic moment.
import Range

Range.logic.setTimeScale(0.3)
Range.logic.setAnimationsUseTimeScale(True)
```

```python
# Load another file while the game keeps running.
import Range

path = Range.logic.expandPath("//levels/forest.range")
status = Range.logic.LibLoad(path, "Scene", asynchronous=True)
print(status.libraryName)
```

```python
# Send a message that a Message sensor can receive.
import Range

Range.logic.sendMessage("door_open", "north")
```

## Introduction

Module to access logic functions, imported automatically into the python controllers namespace.

```python

# To get the controller thats running this python script:
cont = Range.logic.getCurrentController() # Range.logic is automatically imported

# To get the game object this controller is on:
obj = cont.owner
```

`KX_GameObject` and `KX_Camera` or `KX_LightObject` methods are available depending on the type of object

```python

# To get a sensor linked to this controller.
# "sensorname" is the name of the sensor as defined in the Blender interface.
# +---------------------+  +--------+
# | Sensor "sensorname" +--+ Python +
# +---------------------+  +--------+
sens = cont.sensors["sensorname"]

# To get a sequence of all sensors:
sensors = co.sensors
```

See the sensor's reference for available methods:

* `KX_MouseFocusSensor`
* `KX_NearSensor`
* `KX_NetworkMessageSensor`
* `KX_RadarSensor`
* `KX_RaySensor`
* `KX_CollisionSensor`
* `SCA_DelaySensor`
* `SCA_JoystickSensor`
* `SCA_KeyboardSensor`
* `SCA_MouseSensor`
* `SCA_PropertySensor`
* `SCA_RandomSensor`
You can also access actuators linked to the controller

```python

# To get an actuator attached to the controller:
#                          +--------+  +-------------------------+
#                          + Python +--+ Actuator "actuatorname" |
#                          +--------+  +-------------------------+
actuator = co.actuators["actuatorname"]

# Activate an actuator
controller.activate(actuator)
```

See the actuator's reference for available methods

* `BL_ActionActuator`
* `KX_CameraActuator`
* `KX_ConstraintActuator`
* `KX_GameActuator`
* `KX_MouseActuator`
* `KX_NetworkMessageActuator`
* `KX_ObjectActuator`
* `KX_ParentActuator`
* `KX_SCA_AddObjectActuator`
* `KX_SCA_DynamicActuator`
* `KX_SCA_EndObjectActuator`
* `KX_SCA_ReplaceMeshActuator`
* `KX_SceneActuator`
* `KX_SoundActuator`
* `KX_StateActuator`
* `KX_TrackToActuator`
* `KX_VisibilityActuator`
* `SCA_2DFilterActuator`
* `SCA_PropertyActuator`
* `SCA_RandomActuator`
Most logic brick's methods are accessors for the properties available in the logic buttons.
Consult the logic bricks documentation for more information on how each logic brick works.

There are also methods to access the current `Range.types.KX_Scene`

```python

# Get the current scene
scene = Range.logic.getCurrentScene()

# Get the current camera
cam = scene.active_camera
```

Matricies as used by the game engine are **row major**
`matrix[row][col] = float`

`Range.types.KX_Camera` has some examples using matrices.

## Variables

## Armature Sensor

See `Range.types.KX_ArmatureSensor.type`

## Radar Sensor

See `Range.types.KX_RadarSensor`

## Ray Sensor

See `Range.types.KX_RaySensor`

## Action Actuator

See `Range.types.BL_ActionActuator`

## Armature Actuator

See `Range.types.BL_ArmatureActuator.type`

## Constraint Actuator

See `Range.types.KX_ConstraintActuator.option`

* Applicable to Distance constraint:

## Dynamic Actuator

See `Range.types.KX_SCA_DynamicActuator`

## Game Actuator

See `Range.types.KX_GameActuator`

## Random Distributions

See `Range.types.SCA_RandomActuator`

## Scene Actuator

See `Range.types.KX_SceneActuator`

## Sound Actuator

See `Range.types.KX_SoundActuator`

## Steering Actuator

See `Range.types.KX_SteeringActuator.behavior`

## TrackTo Actuator

See `Range.types.KX_TrackToActuator`

## Armature Channel

See `Range.types.BL_ArmatureChannel.rotation_mode`

.. note:
euler mode are named as in Blender UI but the actual axis order is reversed

## Armature Constraint

See `Range.types.BL_ArmatureConstraint.type`

## Input Status

See `Range.types.SCA_PythonKeyboard`, `Range.types.SCA_PythonMouse`, `Range.types.SCA_MouseSensor`, `Range.types.SCA_KeyboardSensor`

## KX_GameObject

See `Range.types.KX_GameObject.playAction`

## Mouse Buttons

See `Range.types.SCA_MouseSensor`

## States

See `Range.types.KX_StateActuator`

Overview. The items are in the parts below:

- [attributes](Range.logic--props.md) (6 items)
- [methods and functions](Range.logic--funcs.md) (66 items)
- [constants](Range.logic--consts.md) (283 items)
