---
title: "Range.logic"
description: "Referência do módulo Range.logic"
---

## Introduction

Module to access logic functions, imported automatically into the python controllers namespace.

```python

# To get the controller thats running this python script:
cont = Range.logic.getCurrentController() # Range.logic is automatically imported

# To get the game object this controller is on:
obj = cont.owner
```

**class:** `~Range.types.KX_GameObject` and `KX_Camera` or `KX_LightObject` methods are available depending on the type of object

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

**columns:** 3

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

**columns:** 3

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

**class:** `Range.types.KX_Camera` has some examples using matrices.

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

**Tipo do retorno:** `Range.types.SCA_PythonController`

### getCurrentScene()

Gets the current Scene.

**Tipo do retorno:** `Range.types.KX_Scene`

### getSceneList()

Gets a list of the current scenes loaded in the game engine.

**Tipo do retorno:** list of `Range.types.KX_Scene`

:::note
Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes.
:::

### getInactiveSceneNames()

Gets a list of the scene's names not loaded in the game engine.

**Tipo do retorno:** list of string

### loadGlobalDict()

Loads Range.logic.globalDict from a file.

### saveGlobalDict()

Saves Range.logic.globalDict to a file.

### startGame(blend)

Loads the blend file.

- **`blend`**: The name of the blend file
  - tipo: string

### endGame()

Ends the current game.

### restartGame()

Restarts the current game by reloading the .blend file (the last saved version, not what is currently running).

### LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None)

Converts the all of the datablocks of the given type from the given blend.

- **`blend`**: The path to the blend file (or the name to use for the library if data is supplied)
  - tipo: string
- **`type`**: The datablock type (currently only "Action", "Mesh" and "Scene" are supported)
  - tipo: string
- **`data`**: Binary data from a blend file (optional)
  - tipo: bytes
- **`load_actions`**: Search for and load all actions in a given Scene and not just the "active" actions (Scene type only)
  - tipo: bool
- **`verbose`**: Whether or not to print debugging information (e.g., "SceneName: Scene")
  - tipo: bool
- **`load_scripts`**: Whether or not to load text datablocks as well (can be disabled for some extra security)
  - tipo: bool   
- **`asynchronous`**: Whether or not to do the loading asynchronously (in another thread). Only the "Scene" type is currently supported for this feature.
  - tipo: bool
- **`scene`**: Scene to merge loaded data to, if `None` use the current scene.
  - tipo: `Range.types.KX_Scene` or string

**Tipo do retorno:** `Range.types.KX_LibLoadStatus`

:::note
Asynchronously loaded libraries will not be available immediately after LibLoad() returns. Use the returned KX_LibLoadStatus to figure out when the libraries are ready.
:::

### LibNew(name, type, data)

Uses existing datablock data and loads in as a new library.

- **`name`**: A unique library name used for removal later
  - tipo: string
- **`type`**: The datablock type (currently only "Mesh" is supported)
  - tipo: string
- **`data`**: A list of names of the datablocks to load
  - tipo: list of strings

### LibFree(name)

Frees a library, removing all objects and meshes from the currently active scenes.

- **`name`**: The name of the library to free (the name used in LibNew)
  - tipo: string

### LibList()

Returns a list of currently loaded libraries.

**Tipo do retorno:** list [str]

### setLibLoadFrameBudget([ms])

Time per frame, in milliseconds, that asynchronous LibLoad may spend merging loaded libraries into the
scene (textures, shaders, objects). The default of 8 keeps the game frame rate; a loading screen can raise
it (e.g. 30) to finish sooner at a lower frame rate, then set it back.

- **`ms`**: New budget; omitted, only returns the current one.
  - tipo: float

**Retorna:** The current budget in milliseconds.

**Tipo do retorno:** float

### addScene(name, overlay=1, asynchronous=False)

Loads a scene into the game engine.

:::note
This function is not effective immediately, the scene is queued
and added on the next logic cycle where it will be available
from `getSceneList`
:::

- **`name`**: The name of the scene
  - tipo: string
- **`overlay`**: Overlay or underlay (optional)
  - tipo: integer
- **`asynchronous`**: Compile the scene shaders a few per frame (budget of `setLibLoadFrameBudget`) before the scene joins `getSceneList`, so a loading screen keeps drawing; its logic starts only then.
  - tipo: boolean

### sendMessage(subject, body="", to="", message_from="")

Sends a message to sensors in any active scene.

- **`subject`**: The subject of the message
  - tipo: string
- **`body`**: The body of the message (optional)
  - tipo: string
- **`to`**: The name of the object to send the message to (optional)
  - tipo: string
- **`message_from`**: The name of the object that the message is coming from (optional)
  - tipo: string

### setGravity(gravity)

Sets the world gravity.

- **`gravity`**: gravity vector
  - tipo: Vector((fx, fy, fz))

### getSpectrum() (Deprecated)

Returns a 512 point list from the sound card.
This only works if the fmod sound driver is being used.

**Tipo do retorno:** list [float], len(getSpectrum()) == 512

### getMaxLogicFrame()

Gets the maximum number of logic frames per render frame.

**Retorna:** The maximum number of logic frames per render frame

**Tipo do retorno:** integer

### setMaxLogicFrame(maxlogic)

Sets the maximum number of logic frames that are executed per render frame.
This does not affect the physic system that still runs at full frame rate.

- **`maxlogic`**: The new maximum number of logic frames per render frame. Valid values: 1..5
  - tipo: integer

### getMaxPhysicsFrame()

:::danger[Obsoleto ]
No scheduler in the engine consumes this limit; the value set here has no effect.
Kept only for compatibility with existing scripts. It also no longer controls shadow
culling, which used to alias this same underlying setting.
:::

Gets the value last passed to `setMaxPhysicsFrame`.

**Retorna:** The value last set (default: 5)

**Tipo do retorno:** integer

### setMaxPhysicsFrame(maxphysics)

:::danger[Obsoleto ]
No scheduler in the engine consumes this limit; calling this has no effect on physics
or on shadows. Kept only for compatibility with existing scripts.
:::

Stores the value for later retrieval via `getMaxPhysicsFrame`. Historically documented
as the maximum number of physics timesteps executed per render frame, but no code path in
the engine reads it for that purpose.

- **`maxphysics`**: The new maximum number of physics timestep per render frame. Valid values: 1..5.
  - tipo: integer

### getLogicTicRate()

Gets the logic update frequency.

**Retorna:** The logic frequency in Hz

**Tipo do retorno:** float

### setLogicTicRate(ticrate)

Sets the logic update frequency.

The logic update frequency is the number of times logic bricks are executed every second.
The default is 60 Hz.

- **`ticrate`**: The new logic update frequency (in Hz).
  - tipo: float

### getPhysicsTicRate()

Gets the physics update frequency

**Retorna:** The physics update frequency in Hz

**Tipo do retorno:** float

.. warning: Not implimented yet

### setPhysicsTicRate(ticrate)

Sets the physics update frequency

The physics update frequency is the number of times the physics system is executed every second.
The default is 60 Hz.

- **`ticrate`**: The new update frequency (in Hz).
  - tipo: float
.. warning: Not implimented yet

### getExitKey()

Gets the key used to exit the game engine

**Retorna:** The key (defaults to `Range.events.ESCKEY`)

**Tipo do retorno:** int

### setExitKey(key)

Sets the key used to exit the game engine

- **`key`**: A key constant from `Range.events`
  - tipo: int

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
  - tipo: bool

### getRender()

Get the current value of the global render flag

**Retorna:** The flag value

**Tipo do retorno:** bool

## Time related functions

### getClockTime()

Get the current BGE render time, in seconds. The BGE render time is the
simulation time corresponding to the next scene that will be rendered.

**Tipo do retorno:** double

### getFrameTime()

Get the current BGE frame time, in seconds. The BGE frame time is the
simulation time corresponding to the current call of the logic system.
Generally speaking, it is what the user is interested in.

**Tipo do retorno:** double

### getRealTime()

Get the number of real (system-clock) seconds elapsed since the beginning
of the simulation.

**Tipo do retorno:** double

### getTimeScale()

Get the time multiplier between real-time and simulation time. The default
value is 1.0. A value greater than 1.0 means that the simulation is going
faster than real-time, a value lower than 1.0 means that the simulation is
going slower than real-time.

**Tipo do retorno:** double

### setTimeScale(time_scale)

Set the time multiplier between real-time and simulation time. A value
greater than 1.0 means that the simulation is going faster than real-time,
a value lower than 1.0 means that the simulation is going slower than
real-time. Note that a too large value may lead to some physics
instabilities.

- **`time_scale`**: The new time multiplier.

### getUseExternalClock()

Get if the BGE use the inner BGE clock, or rely or on an external
clock. The default is to use the inner BGE clock.

**Tipo do retorno:** bool

### setUseExternalClock(use_external_clock)

Set if the BGE use the inner BGE clock, or rely or on an external
clock. If the user selects the use of an external clock, he should call
regularly the setClockTime method.

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
  - tipo: string

**Retorna:** The converted string

**Tipo do retorno:** string

### getAverageFrameRate()

Gets the estimated/average framerate for all the active scenes, not only the current scene.

**Retorna:** The estimated average framerate in frames per second

**Tipo do retorno:** float

### getBlendFileList(path = "//")

Returns a list of blend files in the same directory as the open blend file, or from using the option argument.

- **`path`**: Optional directory argument, will be expanded (like expandPath) into the full path.
  - tipo: string

**Retorna:** A list of filenames, with no directory prefix

**Tipo do retorno:** list

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

.. _sensor-status:

## Sensor Status

### KX_SENSOR_INACTIVE

<span class="ae-badge pendente">sem descrição</span>

### KX_SENSOR_JUST_ACTIVATED

<span class="ae-badge pendente">sem descrição</span>

### KX_SENSOR_ACTIVE

<span class="ae-badge pendente">sem descrição</span>

### KX_SENSOR_JUST_DEACTIVATED

## Armature Sensor

.. _armaturesensor-type:

See `Range.types.KX_ArmatureSensor.type`

### KX_ARMSENSOR_STATE_CHANGED

Detect that the constraint is changing state (active/inactive)

**value:** 0

### KX_ARMSENSOR_LIN_ERROR_BELOW

Detect that the constraint linear error is above a threshold

**value:** 1

### KX_ARMSENSOR_LIN_ERROR_ABOVE

Detect that the constraint linear error is below a threshold

**value:** 2

### KX_ARMSENSOR_ROT_ERROR_BELOW

Detect that the constraint rotation error is above a threshold

**value:** 3

### KX_ARMSENSOR_ROT_ERROR_ABOVE

Detect that the constraint rotation error is below a threshold

**value:** 4

.. _logic-property-sensor:

## Property Sensor

### KX_PROPSENSOR_EQUAL

Activate when the property is equal to the sensor value.

**value:** 1

### KX_PROPSENSOR_NOTEQUAL

Activate when the property is not equal to the sensor value.

**value:** 2

### KX_PROPSENSOR_INTERVAL

Activate when the property is between the specified limits.

**value:** 3

### KX_PROPSENSOR_CHANGED

Activate when the property changes

**value:** 4

### KX_PROPSENSOR_EXPRESSION

Activate when the expression matches

**value:** 5

### KX_PROPSENSOR_LESSTHAN

Activate when the property is less than the sensor value

**value:** 6

### KX_PROPSENSOR_GREATERTHAN

Activate when the property is greater than the sensor value

**value:** 7

## Radar Sensor

See `Range.types.KX_RadarSensor`

### KX_RADAR_AXIS_POS_X

<span class="ae-badge pendente">sem descrição</span>

### KX_RADAR_AXIS_POS_Y

<span class="ae-badge pendente">sem descrição</span>

### KX_RADAR_AXIS_POS_Z

<span class="ae-badge pendente">sem descrição</span>

### KX_RADAR_AXIS_NEG_X

<span class="ae-badge pendente">sem descrição</span>

### KX_RADAR_AXIS_NEG_Y

<span class="ae-badge pendente">sem descrição</span>

### KX_RADAR_AXIS_NEG_Z

## Ray Sensor

See `Range.types.KX_RaySensor`

### KX_RAY_AXIS_POS_X

<span class="ae-badge pendente">sem descrição</span>

### KX_RAY_AXIS_POS_Y

<span class="ae-badge pendente">sem descrição</span>

### KX_RAY_AXIS_POS_Z

<span class="ae-badge pendente">sem descrição</span>

### KX_RAY_AXIS_NEG_X

<span class="ae-badge pendente">sem descrição</span>

### KX_RAY_AXIS_NEG_Y

<span class="ae-badge pendente">sem descrição</span>

### KX_RAY_AXIS_NEG_Z

## Actuators

.. _action-actuator:

## Action Actuator

See `Range.types.BL_ActionActuator`

### KX_ACTIONACT_PLAY

<span class="ae-badge pendente">sem descrição</span>

### KX_ACTIONACT_PINGPONG

<span class="ae-badge pendente">sem descrição</span>

### KX_ACTIONACT_FLIPPER

<span class="ae-badge pendente">sem descrição</span>

### KX_ACTIONACT_LOOPSTOP

<span class="ae-badge pendente">sem descrição</span>

### KX_ACTIONACT_LOOPEND

<span class="ae-badge pendente">sem descrição</span>

### KX_ACTIONACT_PROPERTY

## Armature Actuator

.. _armatureactuator-constants-type:

See `Range.types.BL_ArmatureActuator.type`

### KX_ACT_ARMATURE_RUN

Just make sure the armature will be updated on the next graphic frame.
This is the only persistent mode of the actuator:
it executes automatically once per frame until stopped by a controller

**value:** 0

### KX_ACT_ARMATURE_ENABLE

Enable the constraint.

**value:** 1

### KX_ACT_ARMATURE_DISABLE

Disable the constraint (runtime constraint values are not updated).

**value:** 2

### KX_ACT_ARMATURE_SETTARGET

Change target and subtarget of constraint.

**value:** 3

### KX_ACT_ARMATURE_SETWEIGHT

Change weight of constraint (IK only).

**value:** 4

### KX_ACT_ARMATURE_SETINFLUENCE

Change influence of constraint.

**value:** 5

## Constraint Actuator

.. _constraint-actuator-option:

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

.. _constraint-actuator-limit:

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

<span class="ae-badge pendente">sem descrição</span>

### KX_DYN_DISABLE_DYNAMICS

<span class="ae-badge pendente">sem descrição</span>

### KX_DYN_ENABLE_RIGID_BODY

<span class="ae-badge pendente">sem descrição</span>

### KX_DYN_DISABLE_RIGID_BODY

<span class="ae-badge pendente">sem descrição</span>

### KX_DYN_SET_MASS

.. _game-actuator:

## Game Actuator

See `Range.types.KX_GameActuator`

### KX_GAME_LOAD

<span class="ae-badge pendente">sem descrição</span>

### KX_GAME_START

<span class="ae-badge pendente">sem descrição</span>

### KX_GAME_RESTART

<span class="ae-badge pendente">sem descrição</span>

### KX_GAME_QUIT

<span class="ae-badge pendente">sem descrição</span>

### KX_GAME_SAVECFG

<span class="ae-badge pendente">sem descrição</span>

### KX_GAME_LOADCFG

.. _mouse-actuator:

## Mouse Actuator

### KX_ACT_MOUSE_OBJECT_AXIS_X

<span class="ae-badge pendente">sem descrição</span>

### KX_ACT_MOUSE_OBJECT_AXIS_Y

<span class="ae-badge pendente">sem descrição</span>

### KX_ACT_MOUSE_OBJECT_AXIS_Z

## Parent Actuator

### KX_PARENT_REMOVE

<span class="ae-badge pendente">sem descrição</span>

### KX_PARENT_SET

.. _logic-random-distributions:

## Random Distributions

See `Range.types.SCA_RandomActuator`

### KX_RANDOMACT_BOOL_CONST

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_BOOL_UNIFORM

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_BOOL_BERNOUILLI

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_INT_CONST

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_INT_UNIFORM

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_INT_POISSON

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_FLOAT_CONST

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_FLOAT_UNIFORM

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_FLOAT_NORMAL

<span class="ae-badge pendente">sem descrição</span>

### KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL

## Scene Actuator

See `Range.types.KX_SceneActuator`

### KX_SCENE_RESTART

<span class="ae-badge pendente">sem descrição</span>

### KX_SCENE_SET_SCENE

<span class="ae-badge pendente">sem descrição</span>

### KX_SCENE_SET_CAMERA

<span class="ae-badge pendente">sem descrição</span>

### KX_SCENE_ADD_FRONT_SCENE

<span class="ae-badge pendente">sem descrição</span>

### KX_SCENE_ADD_BACK_SCENE

<span class="ae-badge pendente">sem descrição</span>

### KX_SCENE_REMOVE_SCENE

<span class="ae-badge pendente">sem descrição</span>

### KX_SCENE_SUSPEND

<span class="ae-badge pendente">sem descrição</span>

### KX_SCENE_RESUME

.. _logic-sound-actuator:

## Sound Actuator

See `Range.types.KX_SoundActuator`

### KX_SOUNDACT_PLAYSTOP

<span class="ae-badge pendente">sem descrição</span>

**value:** 1

### KX_SOUNDACT_PLAYEND

<span class="ae-badge pendente">sem descrição</span>

**value:** 2

### KX_SOUNDACT_LOOPSTOP

<span class="ae-badge pendente">sem descrição</span>

**value:** 3

### KX_SOUNDACT_LOOPEND

<span class="ae-badge pendente">sem descrição</span>

**value:** 4

### KX_SOUNDACT_LOOPBIDIRECTIONAL

<span class="ae-badge pendente">sem descrição</span>

**value:** 5

### KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP

**value:** 6

## Steering Actuator

.. _logic-steering-actuator:

See `Range.types.KX_SteeringActuator.behavior`

### KX_STEERING_SEEK

<span class="ae-badge pendente">sem descrição</span>

**value:** 1

### KX_STEERING_FLEE

<span class="ae-badge pendente">sem descrição</span>

**value:** 2

### KX_STEERING_PATHFOLLOWING

**value:** 3

.. _logic-trackto-actuator:

## TrackTo Actuator

See `Range.types.KX_TrackToActuator`

### KX_TRACK_UPAXIS_POS_X

<span class="ae-badge pendente">sem descrição</span>

### KX_TRACK_UPAXIS_POS_Y

<span class="ae-badge pendente">sem descrição</span>

### KX_TRACK_UPAXIS_POS_Z

<span class="ae-badge pendente">sem descrição</span>

### KX_TRACK_TRAXIS_POS_X

<span class="ae-badge pendente">sem descrição</span>

### KX_TRACK_TRAXIS_POS_Y

<span class="ae-badge pendente">sem descrição</span>

### KX_TRACK_TRAXIS_POS_Z

<span class="ae-badge pendente">sem descrição</span>

### KX_TRACK_TRAXIS_NEG_X

<span class="ae-badge pendente">sem descrição</span>

### KX_TRACK_TRAXIS_NEG_Y

<span class="ae-badge pendente">sem descrição</span>

### KX_TRACK_TRAXIS_NEG_Z

## Various

## 2D Filter

.. _Two-D-FilterActuator-mode:

### RAS_2DFILTER_BLUR

<span class="ae-badge pendente">sem descrição</span>

**value:** 2

### RAS_2DFILTER_CUSTOMFILTER

Customer filter, the code code is set via shaderText property.

**value:** 12

### RAS_2DFILTER_DILATION

<span class="ae-badge pendente">sem descrição</span>

**value:** 4

### RAS_2DFILTER_DISABLED

Disable the filter that is currently active

**value:** -1

### RAS_2DFILTER_ENABLED

Enable the filter that was previously disabled

**value:** -2

### RAS_2DFILTER_EROSION

<span class="ae-badge pendente">sem descrição</span>

**value:** 5

### RAS_2DFILTER_GRAYSCALE

<span class="ae-badge pendente">sem descrição</span>

**value:** 9

### RAS_2DFILTER_INVERT

<span class="ae-badge pendente">sem descrição</span>

**value:** 11

### RAS_2DFILTER_LAPLACIAN

<span class="ae-badge pendente">sem descrição</span>

**value:** 6

### RAS_2DFILTER_MOTIONBLUR

Create and enable preset filters

**value:** 1

### RAS_2DFILTER_NOFILTER

Disable and destroy the filter that is currently active

**value:** 0

### RAS_2DFILTER_PREWITT

<span class="ae-badge pendente">sem descrição</span>

**value:** 8

### RAS_2DFILTER_SEPIA

<span class="ae-badge pendente">sem descrição</span>

**value:** 10

### RAS_2DFILTER_SHARPEN

<span class="ae-badge pendente">sem descrição</span>

**value:** 3

### RAS_2DFILTER_SOBEL

**value:** 7

### RAS_2DFILTER_SOBEL

**value:** 14

## Armature Channel

.. _armaturechannel-constants-rotation-mode:

See `Range.types.BL_ArmatureChannel.rotation_mode`

.. note:
euler mode are named as in Blender UI but the actual axis order is reversed

### ROT_MODE_QUAT

Use quaternion in rotation attribute to update bone rotation.

**value:** 0

### ROT_MODE_XYZ

Use euler_rotation and apply angles on bone's Z, Y, X axis successively.

**value:** 1

### ROT_MODE_XZY

Use euler_rotation and apply angles on bone's Y, Z, X axis successively.

**value:** 2

### ROT_MODE_YXZ

Use euler_rotation and apply angles on bone's Z, X, Y axis successively.

**value:** 3

### ROT_MODE_YZX

Use euler_rotation and apply angles on bone's X, Z, Y axis successively.

**value:** 4

### ROT_MODE_ZXY

Use euler_rotation and apply angles on bone's Y, X, Z axis successively.

**value:** 5

### ROT_MODE_ZYX

Use euler_rotation and apply angles on bone's X, Y, Z axis successively.

**value:** 6

## Armature Constraint

.. _armatureconstraint-constants-type:

See `Range.types.BL_ArmatureConstraint.type`

### CONSTRAINT_TYPE_TRACKTO

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_KINEMATIC

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_ROTLIKE

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_LOCLIKE

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_MINMAX

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_SIZELIKE

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_LOCKTRACK

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_STRETCHTO

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_CLAMPTO

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_TRANSFORM

<span class="ae-badge pendente">sem descrição</span>

### CONSTRAINT_TYPE_DISTLIMIT

.. _armatureconstraint-constants-ik-type:

See `Range.types.BL_ArmatureConstraint.ik_type`

### CONSTRAINT_IK_COPYPOSE

constraint is trying to match the position and eventually the rotation of the target.

**value:** 0

### CONSTRAINT_IK_DISTANCE

Constraint is maintaining a certain distance to target subject to ik_mode

**value:** 1

.. _armatureconstraint-constants-ik-flag:

See `Range.types.BL_ArmatureConstraint.ik_flag`

### CONSTRAINT_IK_FLAG_TIP

Set when the constraint operates on the head of the bone and not the tail

**value:** 1

### CONSTRAINT_IK_FLAG_ROT

Set when the constraint tries to match the orientation of the target

**value:** 2

### CONSTRAINT_IK_FLAG_STRETCH

Set when the armature is allowed to stretch (only the bones with stretch factor > 0.0)

**value:** 16

### CONSTRAINT_IK_FLAG_POS

Set when the constraint tries to match the position of the target.

**value:** 32

.. _armatureconstraint-constants-ik-mode:

See `Range.types.BL_ArmatureConstraint.ik_mode`

### CONSTRAINT_IK_MODE_INSIDE

The constraint tries to keep the bone within ik_dist of target

**value:** 0

### CONSTRAINT_IK_MODE_OUTSIDE

The constraint tries to keep the bone outside ik_dist of the target

**value:** 1

### CONSTRAINT_IK_MODE_ONSURFACE

The constraint tries to keep the bone exactly at ik_dist of the target.

**value:** 2

.. _input-status:

## Blender Material

### BL_DST_ALPHA

<span class="ae-badge pendente">sem descrição</span>

### BL_DST_COLOR

<span class="ae-badge pendente">sem descrição</span>

### BL_ONE

<span class="ae-badge pendente">sem descrição</span>

### BL_ONE_MINUS_DST_ALPHA

<span class="ae-badge pendente">sem descrição</span>

### BL_ONE_MINUS_DST_COLOR

<span class="ae-badge pendente">sem descrição</span>

### BL_ONE_MINUS_SRC_ALPHA

<span class="ae-badge pendente">sem descrição</span>

### BL_ONE_MINUS_SRC_COLOR

<span class="ae-badge pendente">sem descrição</span>

### BL_SRC_ALPHA

<span class="ae-badge pendente">sem descrição</span>

### BL_SRC_ALPHA_SATURATE

<span class="ae-badge pendente">sem descrição</span>

### BL_SRC_COLOR

<span class="ae-badge pendente">sem descrição</span>

### BL_ZERO

## Input Status

See `Range.types.SCA_PythonKeyboard`, `Range.types.SCA_PythonMouse`, `Range.types.SCA_MouseSensor`, `Range.types.SCA_KeyboardSensor`

### KX_INPUT_NONE

<span class="ae-badge pendente">sem descrição</span>

### KX_INPUT_JUST_ACTIVATED

<span class="ae-badge pendente">sem descrição</span>

### KX_INPUT_ACTIVE

<span class="ae-badge pendente">sem descrição</span>

### KX_INPUT_JUST_RELEASED

## KX_GameObject

.. _gameobject-playaction-mode:

See `Range.types.KX_GameObject.playAction`

### KX_ACTION_MODE_PLAY

Play the action once.

**value:** 0

### KX_ACTION_MODE_LOOP

Loop the action (repeat it).

**value:** 1

### KX_ACTION_MODE_PING_PONG

Play the action one direct then back the other way when it has completed.

**value:** 2

.. _gameobject-playaction-blend:

### KX_ACTION_BLEND_BLEND

Blend layers using linear interpolation

**value:** 0

### KX_ACTION_BLEND_ADD

Adds the layers together

**value:** 1

## Mouse Buttons

See `Range.types.SCA_MouseSensor`

### KX_MOUSE_BUT_LEFT

<span class="ae-badge pendente">sem descrição</span>

### KX_MOUSE_BUT_MIDDLE

<span class="ae-badge pendente">sem descrição</span>

### KX_MOUSE_BUT_RIGHT

## Navigation Mesh Draw Modes

.. _navmesh-draw-mode:

### RM_WALLS

Draw only the walls.

### RM_POLYS

Draw only polygons.

### RM_TRIS

Draw triangle mesh.

## Shader

.. _shader-defined-uniform:

### VIEWMATRIX

<span class="ae-badge pendente">sem descrição</span>

### VIEWMATRIX_INVERSE

<span class="ae-badge pendente">sem descrição</span>

### VIEWMATRIX_INVERSETRANSPOSE

<span class="ae-badge pendente">sem descrição</span>

### VIEWMATRIX_TRANSPOSE

<span class="ae-badge pendente">sem descrição</span>

### MODELMATRIX

<span class="ae-badge pendente">sem descrição</span>

### MODELMATRIX_INVERSE

<span class="ae-badge pendente">sem descrição</span>

### MODELMATRIX_INVERSETRANSPOSE

<span class="ae-badge pendente">sem descrição</span>

### MODELMATRIX_TRANSPOSE

<span class="ae-badge pendente">sem descrição</span>

### MODELVIEWMATRIX

<span class="ae-badge pendente">sem descrição</span>

### MODELVIEWMATRIX_INVERSE

<span class="ae-badge pendente">sem descrição</span>

### MODELVIEWMATRIX_INVERSETRANSPOSE

<span class="ae-badge pendente">sem descrição</span>

### MODELVIEWMATRIX_TRANSPOSE

<span class="ae-badge pendente">sem descrição</span>

### CAM_POS

Current camera position

### CONSTANT_TIMER

<span class="ae-badge pendente">sem descrição</span>

### EYE

User a timer for the uniform value.

### SHD_TANGENT

## States

See `Range.types.KX_StateActuator`

### KX_STATE1

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE2

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE3

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE4

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE5

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE6

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE7

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE8

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE9

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE10

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE11

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE12

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE13

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE14

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE15

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE16

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE17

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE18

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE19

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE20

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE21

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE22

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE23

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE24

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE25

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE26

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE27

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE28

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE29

<span class="ae-badge pendente">sem descrição</span>

### KX_STATE30

.. _state-actuator-operation:

See `Range.types.KX_StateActuator.operation`

### KX_STATE_OP_CLR

Substract bits to state mask

**value:** 0

### KX_STATE_OP_CPY

Copy state mask

**value:** 1

### KX_STATE_OP_NEG

Invert bits to state mask

**value:** 2

### KX_STATE_OP_SET

Add bits to state mask

**value:** 3

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### deltaTime()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### freeUnconvertedData()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### getAnimationRate()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### getGraphicsCardRenderer()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### getGraphicsCardVendor()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### getLoadLog()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### getMessages()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### getObjectConvert()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### getProcessorName()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### getRangeFileList()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### getRasecFileList()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### getRenderRate()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setAnimationRate()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setNeedsParents()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setObjectConvert()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

### setRenderRate()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### KX_GAME_SCREENSHOT

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_A

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_B

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_BACK

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_GUIDE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_LEFTSHOUDER

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_LEFTSTICK

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_PADDOWN

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_PADLEFT

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_PADRIGHT

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_PADUP

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_RIGHTSHOUDER

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_RIGHTSTICK

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_X

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_JOYSTICK_BUT_Y

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOUSE_BUT_BUTTON6

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOUSE_BUT_BUTTON7

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOUSE_BUT_LEFTTHUMBMOUSE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOUSE_BUT_RIGHTTHUMBMOUSE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOVEMENT_ALL_AXIS

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOVEMENT_AXIS_NEG_X

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOVEMENT_AXIS_NEG_Y

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOVEMENT_AXIS_NEG_Z

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOVEMENT_AXIS_POS_X

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOVEMENT_AXIS_POS_Y

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### KX_MOVEMENT_AXIS_POS_Z

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_2DFILTER_BLOOM

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_2DFILTER_FXAA

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_2DFILTER_LIGHTSCATTER

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_2DFILTER_OUTLINE

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_2DFILTER_SSAO

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_2DFILTER_SSR

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

### RAS_2DFILTER_TONEMAP

<span class="ae-badge pendente">sem documentação</span> <small>constante</small>

