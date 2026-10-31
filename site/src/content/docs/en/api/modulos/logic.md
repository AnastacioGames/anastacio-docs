---
title: "Range.logic"
description: "Range.logic module reference"
---

:::tip[See also]
[`KX_GameObject`](../../types/kx_gameobject/), [`KX_Scene`](../../types/kx_scene/), [`Range.events`](../../modulos/events/), [`SCA_PythonController`](../../types/sca_pythoncontroller/)
:::

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

### globalDict

A dictionary that is saved between loading blend files so you can use it to store inventory and other variables you want to store between scenes and blend files.
It can also be written to a file and loaded later on with the game load/save actuators.

:::note
only python built in types such as int/string/bool/float/tuples/lists can be saved, GameObjects, Actuators etc will not work as expected.
:::

### keyboard

The current keyboard wrapped in an `SCA_PythonKeyboard` object.

### mouse

The current mouse wrapped in an `SCA_PythonMouse` object.

### motion

Device motion sensors (gyroscope, accelerometer, tilt) wrapped in a `KX_PythonMotion` object.

### joysticks

A list of attached `SCA_PythonJoystick`.
The list size is the maximum number of supported joysticks.
If no joystick is available for a given slot, the slot is set to None.

## General functions

### getCurrentController()

Gets the Python controller associated with this Python script.

**Return type:** `Range.types.SCA_PythonController`

### getCurrentScene()

Gets the current Scene.

**Return type:** `Range.types.KX_Scene`

### getSceneList()

Gets a list of the current scenes loaded in the game engine.

**Return type:** list of `Range.types.KX_Scene`

:::note
Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes.
:::

### getInactiveSceneNames()

Gets a list of the scene's names not loaded in the game engine.

**Return type:** list of string

### loadGlobalDict()

Loads Range.logic.globalDict from a file.

### saveGlobalDict()

Saves Range.logic.globalDict to a file.

### startGame(blend)

Loads the blend file.

- **`blend`**: The name of the blend file
  - type: string

### endGame()

Ends the current game.

### restartGame()

Restarts the current game by reloading the .blend file (the last saved version, not what is currently running).

### LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None)

Converts the all of the datablocks of the given type from the given blend.

- **`blend`**: The path to the blend file (or the name to use for the library if data is supplied)
  - type: string
- **`type`**: The datablock type (currently only "Action", "Mesh" and "Scene" are supported)
  - type: string
- **`data`**: Binary data from a blend file (optional)
  - type: bytes
- **`load_actions`**: Search for and load all actions in a given Scene and not just the "active" actions (Scene type only)
  - type: bool
- **`verbose`**: Whether or not to print debugging information (e.g., "SceneName: Scene")
  - type: bool
- **`load_scripts`**: Whether or not to load text datablocks as well (can be disabled for some extra security)
  - type: bool   
- **`asynchronous`**: Whether or not to do the loading asynchronously (in another thread). Only the "Scene" type is currently supported for this feature.
  - type: bool
- **`scene`**: Scene to merge loaded data to, if `None` use the current scene.
  - type: `Range.types.KX_Scene` or string

**Return type:** `Range.types.KX_LibLoadStatus`

:::note
Asynchronously loaded libraries will not be available immediately after LibLoad() returns. Use the returned KX_LibLoadStatus to figure out when the libraries are ready.
:::

### LibNew(name, type, data)

Uses existing datablock data and loads in as a new library.

- **`name`**: A unique library name used for removal later
  - type: string
- **`type`**: The datablock type (currently only "Mesh" is supported)
  - type: string
- **`data`**: A list of names of the datablocks to load
  - type: list of strings

### LibFree(name)

Frees a library, removing all objects and meshes from the currently active scenes.

- **`name`**: The name of the library to free (the name used in LibNew)
  - type: string

### LibList()

Returns a list of currently loaded libraries.

**Return type:** list [str]

### setLibLoadFrameBudget([ms])

Time per frame, in milliseconds, that asynchronous LibLoad may spend merging loaded libraries into the
scene (textures, shaders, objects). The default of 8 keeps the game frame rate; a loading screen can raise
it (e.g. 30) to finish sooner at a lower frame rate, then set it back.

- **`ms`**: New budget; omitted, only returns the current one.
  - type: float

**Returns:** The current budget in milliseconds.

**Return type:** float

### addScene(name, overlay=1, asynchronous=False)

Loads a scene into the game engine.

:::note
This function is not effective immediately, the scene is queued
and added on the next logic cycle where it will be available
from `getSceneList`
:::

- **`name`**: The name of the scene
  - type: string
- **`overlay`**: Overlay or underlay (optional)
  - type: integer
- **`asynchronous`**: Compile the scene shaders a few per frame (budget of `setLibLoadFrameBudget`) before the scene joins `getSceneList`, so a loading screen keeps drawing; its logic starts only then.
  - type: boolean

### sendMessage(subject, body="", to="", message_from="")

Sends a message to sensors in any active scene.

- **`subject`**: The subject of the message
  - type: string
- **`body`**: The body of the message (optional)
  - type: string
- **`to`**: The name of the object to send the message to (optional)
  - type: string
- **`message_from`**: The name of the object that the message is coming from (optional)
  - type: string

### setGravity(gravity)

Sets the world gravity.

- **`gravity`**: gravity vector
  - type: Vector((fx, fy, fz))

### getSpectrum() (Deprecated)

Returns a 512 point list from the sound card.
This only works if the fmod sound driver is being used.

**Return type:** list [float], len(getSpectrum()) == 512

### getMaxLogicFrame()

Gets the maximum number of logic frames per render frame.

**Returns:** The maximum number of logic frames per render frame

**Return type:** integer

### setMaxLogicFrame(maxlogic)

Sets the maximum number of logic frames that are executed per render frame.
This does not affect the physic system that still runs at full frame rate.

- **`maxlogic`**: The new maximum number of logic frames per render frame. Valid values: 1..5
  - type: integer

### ~~getMaxPhysicsFrame()~~

:::danger[Deprecated ]
No scheduler in the engine consumes this limit; the value set here has no effect.
Kept only for compatibility with existing scripts. It also no longer controls shadow
culling, which used to alias this same underlying setting.
:::

Gets the value last passed to `setMaxPhysicsFrame`.

**Returns:** The value last set (default: 5)

**Return type:** integer

### ~~setMaxPhysicsFrame(maxphysics)~~

:::danger[Deprecated ]
No scheduler in the engine consumes this limit; calling this has no effect on physics
or on shadows. Kept only for compatibility with existing scripts.
:::

Stores the value for later retrieval via `getMaxPhysicsFrame`. Historically documented
as the maximum number of physics timesteps executed per render frame, but no code path in
the engine reads it for that purpose.

- **`maxphysics`**: The new maximum number of physics timestep per render frame. Valid values: 1..5.
  - type: integer

### getLogicTicRate()

Gets the logic update frequency.

**Returns:** The logic frequency in Hz

**Return type:** float

### setLogicTicRate(ticrate)

Sets the logic update frequency.

The logic update frequency is the number of times logic bricks are executed every second.
The default is 60 Hz.

- **`ticrate`**: The new logic update frequency (in Hz).
  - type: float

### getPhysicsTicRate()

Gets the physics update frequency

**Returns:** The physics update frequency in Hz

**Return type:** float

### setPhysicsTicRate(ticrate)

Sets the physics update frequency

The physics update frequency is the number of times the physics system is executed every second.
The default is 60 Hz.

- **`ticrate`**: The new update frequency (in Hz).
  - type: float

### getExitKey()

Gets the key used to exit the game engine

**Returns:** The key (defaults to `Range.events.ESCKEY`)

**Return type:** int

### setExitKey(key)

Sets the key used to exit the game engine

- **`key`**: A key constant from `Range.events`
  - type: int

### NextFrame()

Render next frame (if Python has control)

### setRender(render)

Sets the global flag that controls the render of the scene.
If True, the render is done after the logic frame.
If False, the render is skipped and another logic frame starts immediately.

:::note
GPU VSync no longer limits the number of frame per second when render is off,
but the *Use Frame Rate* option still regulates the fps. To run as many frames
as possible, untick this option (Render Properties, System panel).
:::

- **`render`**: the render flag
  - type: bool

### getRender()

Get the current value of the global render flag

**Returns:** The flag value

**Return type:** bool

## Time related functions

### getClockTime()

Get the current BGE render time, in seconds. The BGE render time is the
simulation time corresponding to the next scene that will be rendered.

**Return type:** double

### getFrameTime()

Get the current BGE frame time, in seconds. The BGE frame time is the
simulation time corresponding to the current call of the logic system.
Generally speaking, it is what the user is interested in.

**Return type:** double

### getRealTime()

Get the number of real (system-clock) seconds elapsed since the beginning
of the simulation.

**Return type:** double

### getTimeScale()

Get the time multiplier between real-time and simulation time. The default
value is 1.0. A value greater than 1.0 means that the simulation is going
faster than real-time, a value lower than 1.0 means that the simulation is
going slower than real-time.

**Return type:** double

### setTimeScale(time_scale)

Set the time multiplier between real-time and simulation time. A value
greater than 1.0 means that the simulation is going faster than real-time,
a value lower than 1.0 means that the simulation is going slower than
real-time. Note that a too large value may lead to some physics
instabilities.

The scale applies to every game clock: physics, timers, `getFrameTime`,
actions and cutscenes. A value of 0.0 pauses the logic, so no logic brick or
script runs until the scale changes again; resume it from outside the game
logic, or pause with `KX_Scene.suspend` instead.

- **`time_scale`**: The new time multiplier.

### setAnimationsUseTimeScale(use)

Choose whether actions follow `setTimeScale`. With `False` the
animation clock advances by the unscaled logic step, so actions play at
full speed while physics, timers and logic stay scaled. Default `True`.

- **`use`**: `True` to scale animations, `False` to keep them at full speed.
  - type: bool

### getAnimationsUseTimeScale()

**Returns:** `True` if actions follow the time scale.

**Return type:** bool

### ~~getUseExternalClock()~~

:::danger[Deprecated 0.5.5]
The flag has no effect; the simulation always uses its own clock.
:::

**Return type:** bool

### ~~setUseExternalClock(use_external_clock)~~

:::danger[Deprecated 0.5.5]
Has no effect on the simulation and emits a `DeprecationWarning`.
:::

- **`use_external_clock`**: the new setting

### setClockTime(new_time)

Set the next value of the simulation clock. It is preferable to use this
method from a custom main function in python, as calling it in the logic
block can easily lead to a blocked system (if the time does not advance
enough to run at least the next logic step).

- **`new_time`**: the next value of the BGE clock (in second).

## Utility functions

### expandPath(path)

Converts a blender internal path into a proper file system path.

Use / as directory separator in path
You can use '//' at the start of the string to define a relative path;
Blender replaces that string by the directory of the current .blend or runtime file
to make a full path name. The function also converts the directory separator to
the local file system format.

- **`path`**: The path string to be converted/expanded.
  - type: string

**Returns:** The converted string

**Return type:** string

### getAverageFrameRate()

Gets the estimated/average framerate for all the active scenes, not only the current scene.

**Returns:** The estimated average framerate in frames per second

**Return type:** float

### getBlendFileList(path = "//")

Returns a list of blend files in the same directory as the open blend file, or from using the option argument.

- **`path`**: Optional directory argument, will be expanded (like expandPath) into the full path.
  - type: string

**Returns:** A list of filenames, with no directory prefix

**Return type:** list

### getRandomFloat()

Returns a random floating point value in the range [0 - 1)

### PrintGLInfo()

Prints GL Extension Info into the console

### PrintMemInfo()

Prints engine statistics into the console

### getProfileInfo()

Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time.

### getRenderStats()

Returns a Python dictionary of integer counters from the last completed frame, the same numbers the Debug Mode render queries show. Unlike the frame times from `getProfileInfo`, these do not depend on the hardware or the clock, so they are what A/B tests should compare.

Rasterizer counters, covering every pass of the frame (main camera, shadows, 2D filters):

* `drawCalls` -- draw calls issued.
* `materialBinds` -- material (shader program) binds.
* `lightBinds` -- uploads of the scene light and shadow lamp uniforms. The light set is constant per light layer, so this counts how often the same values were re-uploaded.

Counters of the active scene:

* `cullingTotal`, `cullingTested`, `cullingVisible` -- objects in the render list, tested against the frustum/DBVT, and found visible, from the last main-camera culling pass.
* `lightsTotal`, `lightsShadowUpdated`, `shadowPasses` -- lights in the scene, lights whose shadow buffer was refreshed, and shadow passes rendered (each cascade split counts as one).
* `sensors`, `controllersTriggered`, `actuatorsUpdated` -- registered sensors, and controllers/actuators run on the logic frame. Beware that these two are counted as the frame runs, and a Python controller calling this function is itself part of that frame: it sees only what ran before it, so from a controller the value is usually 0. The Debug Mode overlay reads them after the frame and shows the complete count. The rasterizer and culling counters above have no such caveat -- they are always from the last completed frame.

## Constants

### KX_TRUE

True value used by some modules.

### KX_FALSE

False value used by some modules.

## Sensors

## Sensor Status

### KX_SENSOR_INACTIVE

Sensor state: off.

### KX_SENSOR_JUST_ACTIVATED

Sensor state: just turned on this frame.

### KX_SENSOR_ACTIVE

Sensor state: still on.

### KX_SENSOR_JUST_DEACTIVATED

## Armature Sensor

See `Range.types.KX_ArmatureSensor.type`

### KX_ARMSENSOR_STATE_CHANGED

Detect that the constraint is changing state (active/inactive)

**Value:** `0`

### KX_ARMSENSOR_LIN_ERROR_BELOW

Detect that the constraint linear error is above a threshold

**Value:** `1`

### KX_ARMSENSOR_LIN_ERROR_ABOVE

Detect that the constraint linear error is below a threshold

**Value:** `2`

### KX_ARMSENSOR_ROT_ERROR_BELOW

Detect that the constraint rotation error is above a threshold

**Value:** `3`

### KX_ARMSENSOR_ROT_ERROR_ABOVE

Detect that the constraint rotation error is below a threshold

**Value:** `4`

## Property Sensor

### KX_PROPSENSOR_EQUAL

Activate when the property is equal to the sensor value.

**Value:** `1`

### KX_PROPSENSOR_NOTEQUAL

Activate when the property is not equal to the sensor value.

**Value:** `2`

### KX_PROPSENSOR_INTERVAL

Activate when the property is between the specified limits.

**Value:** `3`

### KX_PROPSENSOR_CHANGED

Activate when the property changes

**Value:** `4`

### KX_PROPSENSOR_EXPRESSION

Activate when the expression matches

**Value:** `5`

### KX_PROPSENSOR_LESSTHAN

Activate when the property is less than the sensor value

**Value:** `6`

### KX_PROPSENSOR_GREATERTHAN

Activate when the property is greater than the sensor value

**Value:** `7`

## Radar Sensor

See `Range.types.KX_RadarSensor`

### KX_RADAR_AXIS_POS_X

Radar sensor: cone pointing along the object +X axis.

### KX_RADAR_AXIS_POS_Y

Radar sensor: cone pointing along the object +Y axis.

### KX_RADAR_AXIS_POS_Z

Radar sensor: cone pointing along the object +Z axis.

### KX_RADAR_AXIS_NEG_X

Radar sensor: cone pointing along the object -X axis.

### KX_RADAR_AXIS_NEG_Y

Radar sensor: cone pointing along the object -Y axis.

### KX_RADAR_AXIS_NEG_Z

## Ray Sensor

See `Range.types.KX_RaySensor`

### KX_RAY_AXIS_POS_X

Ray sensor: ray cast along the object +X axis.

### KX_RAY_AXIS_POS_Y

Ray sensor: ray cast along the object +Y axis.

### KX_RAY_AXIS_POS_Z

Ray sensor: ray cast along the object +Z axis.

### KX_RAY_AXIS_NEG_X

Ray sensor: ray cast along the object -X axis.

### KX_RAY_AXIS_NEG_Y

Ray sensor: ray cast along the object -Y axis.

### KX_RAY_AXIS_NEG_Z

## Actuators

## Action Actuator

See `Range.types.BL_ActionActuator`

### KX_ACTIONACT_PLAY

Action actuator: plays the animation once.

### KX_ACTIONACT_PINGPONG

Action actuator: plays forward and, on the next activation, backward.

### KX_ACTIONACT_FLIPPER

Action actuator: plays while active and goes back to the start when turned off.

### KX_ACTIONACT_LOOPSTOP

Action actuator: loops while the sensor is active.

### KX_ACTIONACT_LOOPEND

Action actuator: loops and, when turned off, finishes the current loop.

### KX_ACTIONACT_PROPERTY

## Armature Actuator

See `Range.types.BL_ArmatureActuator.type`

### KX_ACT_ARMATURE_RUN

Just make sure the armature will be updated on the next graphic frame.
This is the only persistent mode of the actuator:
it executes automatically once per frame until stopped by a controller

**Value:** `0`

### KX_ACT_ARMATURE_ENABLE

Enable the constraint.

**Value:** `1`

### KX_ACT_ARMATURE_DISABLE

Disable the constraint (runtime constraint values are not updated).

**Value:** `2`

### KX_ACT_ARMATURE_SETTARGET

Change target and subtarget of constraint.

**Value:** `3`

### KX_ACT_ARMATURE_SETWEIGHT

Change weight of constraint (IK only).

**Value:** `4`

### KX_ACT_ARMATURE_SETINFLUENCE

Change influence of constraint.

**Value:** `5`

## Constraint Actuator

See `Range.types.KX_ConstraintActuator.option`

* Applicable to Distance constraint:

### KX_CONSTRAINTACT_NORMAL

Activate alignment to surface

### KX_CONSTRAINTACT_DISTANCE

Activate distance control

### KX_CONSTRAINTACT_LOCAL

Direction of the ray is along the local axis

* Applicable to Force field constraint:

### KX_CONSTRAINTACT_DOROTFH

Force field act on rotation as well

* Applicable to both:

### KX_CONSTRAINTACT_MATERIAL

Detect material rather than property

### KX_CONSTRAINTACT_PERMANENT

No deactivation if ray does not hit target

See `Range.types.KX_ConstraintActuator.limit`

### KX_CONSTRAINTACT_LOCX

Limit X coord.

### KX_CONSTRAINTACT_LOCY

Limit Y coord

### KX_CONSTRAINTACT_LOCZ

Limit Z coord

### KX_CONSTRAINTACT_ROTX

Limit X rotation

### KX_CONSTRAINTACT_ROTY

Limit Y rotation

### KX_CONSTRAINTACT_ROTZ

Limit Z rotation

### KX_CONSTRAINTACT_DIRNX

Set distance along negative X axis

### KX_CONSTRAINTACT_DIRNY

Set distance along negative Y axis

### KX_CONSTRAINTACT_DIRNZ

Set distance along negative Z axis

### KX_CONSTRAINTACT_DIRPX

Set distance along positive X axis

### KX_CONSTRAINTACT_DIRPY

Set distance along positive Y axis

### KX_CONSTRAINTACT_DIRPZ

Set distance along positive Z axis

### KX_CONSTRAINTACT_ORIX

Set orientation of X axis

### KX_CONSTRAINTACT_ORIY

Set orientation of Y axis

### KX_CONSTRAINTACT_ORIZ

Set orientation of Z axis

### KX_CONSTRAINTACT_FHNX

Set force field along negative X axis

### KX_CONSTRAINTACT_FHNY

Set force field along negative Y axis

### KX_CONSTRAINTACT_FHNZ

Set force field along negative Z axis

### KX_CONSTRAINTACT_FHPX

Set force field along positive X axis

### KX_CONSTRAINTACT_FHPY

Set force field along positive Y axis

### KX_CONSTRAINTACT_FHPZ

Set force field along positive Z axis

## Dynamic Actuator

See `Range.types.KX_SCA_DynamicActuator`

### KX_DYN_RESTORE_DYNAMICS

Dynamic actuator: turns physics back on.

### KX_DYN_DISABLE_DYNAMICS

Dynamic actuator: turns off the object physics.

### KX_DYN_ENABLE_RIGID_BODY

Dynamic actuator: turns on rigid body mode (physics rotation).

### KX_DYN_DISABLE_RIGID_BODY

Dynamic actuator: turns off rigid body mode.

### KX_DYN_SET_MASS

## Game Actuator

See `Range.types.KX_GameActuator`

### KX_GAME_LOAD

Game actuator: loads another game file.

### KX_GAME_START

Game actuator: starts another game file.

### KX_GAME_RESTART

Game actuator: restarts the game.

### KX_GAME_QUIT

Game actuator: quits the game.

### KX_GAME_SAVECFG

Game actuator: saves the global properties to a file.

### KX_GAME_LOADCFG

## Mouse Actuator

### KX_ACT_MOUSE_OBJECT_AXIS_X

Mouse (look) actuator: rotates around the object X axis.

### KX_ACT_MOUSE_OBJECT_AXIS_Y

Mouse (look) actuator: rotates around the object Y axis.

### KX_ACT_MOUSE_OBJECT_AXIS_Z

## Parent Actuator

### KX_PARENT_REMOVE

Parent actuator: removes the object from its parent.

### KX_PARENT_SET

## Random Distributions

See `Range.types.SCA_RandomActuator`

### KX_RANDOMACT_BOOL_CONST

Random actuator: fixed true/false.

### KX_RANDOMACT_BOOL_UNIFORM

Random actuator: true or false, 50% chance each.

### KX_RANDOMACT_BOOL_BERNOUILLI

Random actuator: true with the chance you set.

### KX_RANDOMACT_INT_CONST

Random actuator: fixed integer.

### KX_RANDOMACT_INT_UNIFORM

Random actuator: integer picked between a minimum and a maximum.

### KX_RANDOMACT_INT_POISSON

Random actuator: integer with a Poisson distribution (given mean).

### KX_RANDOMACT_FLOAT_CONST

Random actuator: fixed float.

### KX_RANDOMACT_FLOAT_UNIFORM

Random actuator: float picked between a minimum and a maximum.

### KX_RANDOMACT_FLOAT_NORMAL

Random actuator: float with a normal distribution (mean and deviation).

### KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL

## Scene Actuator

See `Range.types.KX_SceneActuator`

### KX_SCENE_RESTART

Scene actuator: restarts the scene.

### KX_SCENE_SET_SCENE

Scene actuator: switches to another scene.

### KX_SCENE_SET_CAMERA

Scene actuator: changes the active camera.

### KX_SCENE_ADD_FRONT_SCENE

Scene actuator: adds a scene on top (overlay, like a HUD).

### KX_SCENE_ADD_BACK_SCENE

Scene actuator: adds a scene behind (background).

### KX_SCENE_REMOVE_SCENE

Scene actuator: removes a scene.

### KX_SCENE_SUSPEND

Scene actuator: pauses a scene.

### KX_SCENE_RESUME

## Sound Actuator

See `Range.types.KX_SoundActuator`

### KX_SOUNDACT_PLAYSTOP

Sound actuator: plays while the sensor is active and stops when it turns off.

**Value:** `1`

### KX_SOUNDACT_PLAYEND

Sound actuator: plays the whole sound once.

**Value:** `2`

### KX_SOUNDACT_LOOPSTOP

Sound actuator: loops while the sensor is active.

**Value:** `3`

### KX_SOUNDACT_LOOPEND

Sound actuator: loops and, when turned off, finishes the current loop.

**Value:** `4`

### KX_SOUNDACT_LOOPBIDIRECTIONAL

Sound actuator: plays forward and backward in a loop.

**Value:** `5`

### KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP

**Value:** `6`

## Steering Actuator

See `Range.types.KX_SteeringActuator.behavior`

### KX_STEERING_SEEK

Steering actuator: goes to the target.

**Value:** `1`

### KX_STEERING_FLEE

Steering actuator: runs away from the target.

**Value:** `2`

### KX_STEERING_PATHFOLLOWING

**Value:** `3`

## TrackTo Actuator

See `Range.types.KX_TrackToActuator`

### KX_TRACK_UPAXIS_POS_X

Track To actuator: the object +X axis points up.

### KX_TRACK_UPAXIS_POS_Y

Track To actuator: the object +Y axis points up.

### KX_TRACK_UPAXIS_POS_Z

Track To actuator: the object +Z axis points up.

### KX_TRACK_TRAXIS_POS_X

Track To actuator: the object +X axis points at the target.

### KX_TRACK_TRAXIS_POS_Y

Track To actuator: the object +Y axis points at the target.

### KX_TRACK_TRAXIS_POS_Z

Track To actuator: the object +Z axis points at the target.

### KX_TRACK_TRAXIS_NEG_X

Track To actuator: the object -X axis points at the target.

### KX_TRACK_TRAXIS_NEG_Y

Track To actuator: the object -Y axis points at the target.

### KX_TRACK_TRAXIS_NEG_Z

## Various

## 2D Filter

### RAS_2DFILTER_BLUR

2D Filter actuator: blur.

**Value:** `2`

### RAS_2DFILTER_CUSTOMFILTER

Customer filter, the code code is set via shaderText property.

**Value:** `12`

### RAS_2DFILTER_DILATION

2D Filter actuator: dilation (brightens edges).

**Value:** `4`

### RAS_2DFILTER_DISABLED

Disable the filter that is currently active

**Value:** `-1`

### RAS_2DFILTER_ENABLED

Enable the filter that was previously disabled

**Value:** `-2`

### RAS_2DFILTER_EROSION

2D Filter actuator: erosion (darkens edges).

**Value:** `5`

### RAS_2DFILTER_GRAYSCALE

2D Filter actuator: grayscale.

**Value:** `9`

### RAS_2DFILTER_INVERT

2D Filter actuator: inverted colors.

**Value:** `11`

### RAS_2DFILTER_LAPLACIAN

2D Filter actuator: edge detection (Laplace).

**Value:** `6`

### RAS_2DFILTER_MOTIONBLUR

Create and enable preset filters

**Value:** `1`

### RAS_2DFILTER_NOFILTER

Disable and destroy the filter that is currently active

**Value:** `0`

### RAS_2DFILTER_PREWITT

2D Filter actuator: edge detection (Prewitt).

**Value:** `8`

### RAS_2DFILTER_SEPIA

2D Filter actuator: sepia.

**Value:** `10`

### RAS_2DFILTER_SHARPEN

2D Filter actuator: sharpen.

**Value:** `3`

### RAS_2DFILTER_SOBEL

**Value:** `7`

### RAS_2DFILTER_SOBEL

**Value:** `14`

## Armature Channel

See `Range.types.BL_ArmatureChannel.rotation_mode`

.. note:
euler mode are named as in Blender UI but the actual axis order is reversed

### ROT_MODE_QUAT

Use quaternion in rotation attribute to update bone rotation.

**Value:** `0`

### ROT_MODE_XYZ

Use euler_rotation and apply angles on bone's Z, Y, X axis successively.

**Value:** `1`

### ROT_MODE_XZY

Use euler_rotation and apply angles on bone's Y, Z, X axis successively.

**Value:** `2`

### ROT_MODE_YXZ

Use euler_rotation and apply angles on bone's Z, X, Y axis successively.

**Value:** `3`

### ROT_MODE_YZX

Use euler_rotation and apply angles on bone's X, Z, Y axis successively.

**Value:** `4`

### ROT_MODE_ZXY

Use euler_rotation and apply angles on bone's Y, X, Z axis successively.

**Value:** `5`

### ROT_MODE_ZYX

Use euler_rotation and apply angles on bone's X, Y, Z axis successively.

**Value:** `6`

## Armature Constraint

See `Range.types.BL_ArmatureConstraint.type`

### CONSTRAINT_TYPE_TRACKTO

Bone constraint type: Track To (points at a target).

### CONSTRAINT_TYPE_KINEMATIC

Bone constraint type: IK (inverse kinematics).

### CONSTRAINT_TYPE_ROTLIKE

Bone constraint type: Copy Rotation.

### CONSTRAINT_TYPE_LOCLIKE

Bone constraint type: Copy Location.

### CONSTRAINT_TYPE_MINMAX

Bone constraint type: Floor (min/max limit).

### CONSTRAINT_TYPE_SIZELIKE

Bone constraint type: Copy Scale.

### CONSTRAINT_TYPE_LOCKTRACK

Bone constraint type: Locked Track.

### CONSTRAINT_TYPE_STRETCHTO

Bone constraint type: Stretch To.

### CONSTRAINT_TYPE_CLAMPTO

Bone constraint type: Clamp To (sticks to a curve).

### CONSTRAINT_TYPE_TRANSFORM

Bone constraint type: Transformation.

### CONSTRAINT_TYPE_DISTLIMIT

See `Range.types.BL_ArmatureConstraint.ik_type`

### CONSTRAINT_IK_COPYPOSE

constraint is trying to match the position and eventually the rotation of the target.

**Value:** `0`

### CONSTRAINT_IK_DISTANCE

Constraint is maintaining a certain distance to target subject to ik_mode

**Value:** `1`

See `Range.types.BL_ArmatureConstraint.ik_flag`

### CONSTRAINT_IK_FLAG_TIP

Set when the constraint operates on the head of the bone and not the tail

**Value:** `1`

### CONSTRAINT_IK_FLAG_ROT

Set when the constraint tries to match the orientation of the target

**Value:** `2`

### CONSTRAINT_IK_FLAG_STRETCH

Set when the armature is allowed to stretch (only the bones with stretch factor > 0.0)

**Value:** `16`

### CONSTRAINT_IK_FLAG_POS

Set when the constraint tries to match the position of the target.

**Value:** `32`

See `Range.types.BL_ArmatureConstraint.ik_mode`

### CONSTRAINT_IK_MODE_INSIDE

The constraint tries to keep the bone within ik_dist of target

**Value:** `0`

### CONSTRAINT_IK_MODE_OUTSIDE

The constraint tries to keep the bone outside ik_dist of the target

**Value:** `1`

### CONSTRAINT_IK_MODE_ONSURFACE

The constraint tries to keep the bone exactly at ik_dist of the target.

**Value:** `2`

## Blender Material

### BL_DST_ALPHA

Material blend factor: destination alpha. Used in setBlending().

### BL_DST_COLOR

Material blend factor: destination color. Used in setBlending().

### BL_ONE

Material blend factor: one (full color). Used in setBlending().

### BL_ONE_MINUS_DST_ALPHA

Material blend factor: one minus destination alpha. Used in setBlending().

### BL_ONE_MINUS_DST_COLOR

Material blend factor: one minus destination color. Used in setBlending().

### BL_ONE_MINUS_SRC_ALPHA

Material blend factor: one minus source alpha. Used in setBlending().

### BL_ONE_MINUS_SRC_COLOR

Material blend factor: one minus source color. Used in setBlending().

### BL_SRC_ALPHA

Material blend factor: source alpha. Used in setBlending().

### BL_SRC_ALPHA_SATURATE

Material blend factor: saturated source alpha. Used in setBlending().

### BL_SRC_COLOR

Material blend factor: source color. Used in setBlending().

### BL_ZERO

## Input Status

See `Range.types.SCA_PythonKeyboard`, `Range.types.SCA_PythonMouse`, `Range.types.SCA_MouseSensor`, `Range.types.SCA_KeyboardSensor`

### KX_INPUT_NONE

Key/button state: released.

### KX_INPUT_JUST_ACTIVATED

Key/button state: just pressed.

### KX_INPUT_ACTIVE

Key/button state: held down.

### KX_INPUT_JUST_RELEASED

## KX_GameObject

See `Range.types.KX_GameObject.playAction`

### KX_ACTION_MODE_PLAY

Play the action once.

**Value:** `0`

### KX_ACTION_MODE_LOOP

Loop the action (repeat it).

**Value:** `1`

### KX_ACTION_MODE_PING_PONG

Play the action one direct then back the other way when it has completed.

**Value:** `2`

### KX_ACTION_BLEND_BLEND

Blend layers using linear interpolation

**Value:** `0`

### KX_ACTION_BLEND_ADD

Adds the layers together

**Value:** `1`

## Mouse Buttons

See `Range.types.SCA_MouseSensor`

### KX_MOUSE_BUT_LEFT

Left mouse button (for the mouse sensor).

### KX_MOUSE_BUT_MIDDLE

Middle mouse button (for the mouse sensor).

### KX_MOUSE_BUT_RIGHT

## Navigation Mesh Draw Modes

### RM_WALLS

Draw only the walls.

### RM_POLYS

Draw only polygons.

### RM_TRIS

Draw triangle mesh.

## Shader

### VIEWMATRIX

Shader uniform with the view (world → camera) matrix. Used in setUniformDef().

### VIEWMATRIX_INVERSE

Shader uniform with the view (world → camera) matrix, inverse. Used in setUniformDef().

### VIEWMATRIX_INVERSETRANSPOSE

Shader uniform with the view (world → camera) matrix, inverse transposed. Used in setUniformDef().

### VIEWMATRIX_TRANSPOSE

Shader uniform with the view (world → camera) matrix, transposed. Used in setUniformDef().

### MODELMATRIX

Shader uniform with the model (object → world) matrix. Used in setUniformDef().

### MODELMATRIX_INVERSE

Shader uniform with the model (object → world) matrix, inverse. Used in setUniformDef().

### MODELMATRIX_INVERSETRANSPOSE

Shader uniform with the model (object → world) matrix, inverse transposed. Used in setUniformDef().

### MODELMATRIX_TRANSPOSE

Shader uniform with the model (object → world) matrix, transposed. Used in setUniformDef().

### MODELVIEWMATRIX

Shader uniform with the model × view matrix. Used in setUniformDef().

### MODELVIEWMATRIX_INVERSE

Shader uniform with the model × view matrix, inverse. Used in setUniformDef().

### MODELVIEWMATRIX_INVERSETRANSPOSE

Shader uniform with the model × view matrix, inverse transposed. Used in setUniformDef().

### MODELVIEWMATRIX_TRANSPOSE

Shader uniform with the model × view matrix, transposed. Used in setUniformDef().

### CAM_POS

Current camera position

### CONSTANT_TIMER

Shader uniform with the game time, for animated effects.

### EYE

User a timer for the uniform value.

### SHD_TANGENT

## States

See `Range.types.KX_StateActuator`

### KX_STATE1

Mask for logic brick state 1.

### KX_STATE2

Mask for logic brick state 2.

### KX_STATE3

Mask for logic brick state 3.

### KX_STATE4

Mask for logic brick state 4.

### KX_STATE5

Mask for logic brick state 5.

### KX_STATE6

Mask for logic brick state 6.

### KX_STATE7

Mask for logic brick state 7.

### KX_STATE8

Mask for logic brick state 8.

### KX_STATE9

Mask for logic brick state 9.

### KX_STATE10

Mask for logic brick state 10.

### KX_STATE11

Mask for logic brick state 11.

### KX_STATE12

Mask for logic brick state 12.

### KX_STATE13

Mask for logic brick state 13.

### KX_STATE14

Mask for logic brick state 14.

### KX_STATE15

Mask for logic brick state 15.

### KX_STATE16

Mask for logic brick state 16.

### KX_STATE17

Mask for logic brick state 17.

### KX_STATE18

Mask for logic brick state 18.

### KX_STATE19

Mask for logic brick state 19.

### KX_STATE20

Mask for logic brick state 20.

### KX_STATE21

Mask for logic brick state 21.

### KX_STATE22

Mask for logic brick state 22.

### KX_STATE23

Mask for logic brick state 23.

### KX_STATE24

Mask for logic brick state 24.

### KX_STATE25

Mask for logic brick state 25.

### KX_STATE26

Mask for logic brick state 26.

### KX_STATE27

Mask for logic brick state 27.

### KX_STATE28

Mask for logic brick state 28.

### KX_STATE29

Mask for logic brick state 29.

### KX_STATE30

See `Range.types.KX_StateActuator.operation`

### KX_STATE_OP_CLR

Substract bits to state mask

**Value:** `0`

### KX_STATE_OP_CPY

Copy state mask

**Value:** `1`

### KX_STATE_OP_NEG

Invert bits to state mask

**Value:** `2`

### KX_STATE_OP_SET

Add bits to state mask

**Value:** `3`

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### deltaTime()

 <small>function</small>

Time in seconds since the previous frame. Multiply movement by it so it doesn't depend on FPS.

**Returns:** `float`

### freeUnconvertedData(scene)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Exported game only: frees geometry used only by scene objects left out by the **Convert** option. They can no longer be converted. Returns the bytes freed.

**Returns:** `int`

### getAnimationRate()

 <small>function</small>

Animation update rate (times per second).

**Returns:** `float`

### getGraphicsCardRenderer()

 <small>function</small>

Graphics card name.

**Returns:** `str`

### getGraphicsCardVendor()

 <small>function</small>

Graphics card vendor.

**Returns:** `str`

### getLoadLog(clear=False)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Report of the latest scene loads: dicts with `scene`, `stage`, `ms`, `detail` and `total`. With `clear=True`, clears it after reading.

**Returns:** `list`

### getMessages(to, subject='')

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Messages `(subject, body)` that a Message sensor of object `to` receives this frame.

**Returns:** `list`

### getObjectConvert(scene, object)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Value of the object **Convert** option in the scene.

**Returns:** `bool`

### getProcessorName()

 <small>function</small>

Processor name.

**Returns:** `str`

### getRangeFileList(path='')

 <small>function</small>

`.range` files in the current game folder (or in `path`).

**Returns:** `list`

### getRasecFileList(path='')

 <small>function</small>

`.rasec` files in the current game folder (or in `path`).

**Returns:** `list`

### getRenderRate()

 <small>function</small>

Render rate (times per second).

**Returns:** `float`

### preloadScene(name)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Converts a scene ahead of time, at the end of this frame (shaders and textures included), without adding it. A later `addScene` or `replaceScene` of it only inserts the ready scene, without stalling. Call it while a loading screen is showing. Returns `False` if the scene doesn't exist.

**Returns:** `bool`

### setAnimationRate(rate)

 <small>function</small>

Changes the animation update rate.

### setNeedsParents(count)

 <small>function</small>

How many times per frame the parent hierarchy is updated (going from 3 to 1 saves CPU).

### setObjectConvert(scene, object, convert, children=True)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Changes the **Convert** option of an object in a scene not loaded yet. Returns how many objects changed.

**Returns:** `int`

### setRenderRate(rate)

 <small>function</small>

Changes the render rate.

### KX_GAME_SCREENSHOT

 <small>constant</small>

Game actuator mode: takes a screenshot.

### KX_JOYSTICK_BUT_A

 <small>constant</small>

Gamepad A button.

### KX_JOYSTICK_BUT_B

 <small>constant</small>

Gamepad B button.

### KX_JOYSTICK_BUT_BACK

 <small>constant</small>

Gamepad Back/Select button.

### KX_JOYSTICK_BUT_GUIDE

 <small>constant</small>

Gamepad Guide (center) button.

### KX_JOYSTICK_BUT_LEFTSHOUDER

 <small>constant</small>

Gamepad left shoulder button (LB).

### KX_JOYSTICK_BUT_LEFTSTICK

 <small>constant</small>

Gamepad left stick click.

### KX_JOYSTICK_BUT_PADDOWN

 <small>constant</small>

Gamepad D-pad down.

### KX_JOYSTICK_BUT_PADLEFT

 <small>constant</small>

Gamepad D-pad left.

### KX_JOYSTICK_BUT_PADRIGHT

 <small>constant</small>

Gamepad D-pad right.

### KX_JOYSTICK_BUT_PADUP

 <small>constant</small>

Gamepad D-pad up.

### KX_JOYSTICK_BUT_RIGHTSHOUDER

 <small>constant</small>

Gamepad right shoulder button (RB).

### KX_JOYSTICK_BUT_RIGHTSTICK

 <small>constant</small>

Gamepad right stick click.

### KX_JOYSTICK_BUT_X

 <small>constant</small>

Gamepad X button.

### KX_JOYSTICK_BUT_Y

 <small>constant</small>

Gamepad Y button.

### KX_MOUSE_BUT_BUTTON6

 <small>constant</small>

Mouse button 6.

### KX_MOUSE_BUT_BUTTON7

 <small>constant</small>

Mouse button 7.

### KX_MOUSE_BUT_LEFTTHUMBMOUSE

 <small>constant</small>

Left side mouse button (thumb).

### KX_MOUSE_BUT_RIGHTTHUMBMOUSE

 <small>constant</small>

Right side mouse button (thumb).

### KX_MOVEMENT_ALL_AXIS

 <small>constant</small>

Movement sensor: watches all axes.

### KX_MOVEMENT_AXIS_NEG_X

 <small>constant</small>

Movement sensor: -X axis.

### KX_MOVEMENT_AXIS_NEG_Y

 <small>constant</small>

Movement sensor: -Y axis.

### KX_MOVEMENT_AXIS_NEG_Z

 <small>constant</small>

Movement sensor: -Z axis.

### KX_MOVEMENT_AXIS_POS_X

 <small>constant</small>

Movement sensor: +X axis.

### KX_MOVEMENT_AXIS_POS_Y

 <small>constant</small>

Movement sensor: +Y axis.

### KX_MOVEMENT_AXIS_POS_Z

 <small>constant</small>

Movement sensor: +Z axis.

### RAS_2DFILTER_BLOOM

 <small>constant</small>

2D filter: Bloom.

### RAS_2DFILTER_FXAA

 <small>constant</small>

2D filter: FXAA.

### RAS_2DFILTER_LIGHTSCATTER

 <small>constant</small>

2D filter: light scattering (light rays).

### RAS_2DFILTER_OUTLINE

 <small>constant</small>

2D filter: outline.

### RAS_2DFILTER_SSAO

 <small>constant</small>

2D filter: ambient occlusion (SSAO).

### RAS_2DFILTER_SSR

 <small>constant</small>

2D filter: screen-space reflections (SSR).

### RAS_2DFILTER_TONEMAP

 <small>constant</small>

2D filter: tonemap.

