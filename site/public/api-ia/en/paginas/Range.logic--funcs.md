# Range.logic - methods and functions

Part of [Range.logic](Range.logic.md).

## getCurrentController()

Gets the Python controller associated with this Python script.

**Return type:** `Range.types.SCA_PythonController`

## getCurrentScene()

Gets the current Scene.

**Return type:** `Range.types.KX_Scene`

## getSceneList()

Gets a list of the current scenes loaded in the game engine.

**Return type:** list of `Range.types.KX_Scene`

> **Note:**
Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes.

## getInactiveSceneNames()

Gets a list of the scene's names not loaded in the game engine.

**Return type:** list of string

## loadGlobalDict()

Loads Range.logic.globalDict from a file.

## saveGlobalDict()

Saves Range.logic.globalDict to a file.

## startGame(blend)

Loads the blend file.

- **`blend`**: The name of the blend file
  - type: string

## endGame()

Ends the current game.

## restartGame()

Restarts the current game by reloading the .blend file (the last saved version, not what is currently running).

## LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None)

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

> **Note:**
Asynchronously loaded libraries will not be available immediately after LibLoad() returns. Use the returned KX_LibLoadStatus to figure out when the libraries are ready.

## LibNew(name, type, data)

Uses existing datablock data and loads in as a new library.

- **`name`**: A unique library name used for removal later
  - type: string
- **`type`**: The datablock type (currently only "Mesh" is supported)
  - type: string
- **`data`**: A list of names of the datablocks to load
  - type: list of strings

## LibFree(name)

Frees a library, removing all objects and meshes from the currently active scenes.

- **`name`**: The name of the library to free (the name used in LibNew)
  - type: string

## LibList()

Returns a list of currently loaded libraries.

**Return type:** list [str]

## setLibLoadFrameBudget([ms])

Time per frame, in milliseconds, that asynchronous LibLoad may spend merging loaded libraries into the
scene (textures, shaders, objects). The default of 8 keeps the game frame rate; a loading screen can raise
it (e.g. 30) to finish sooner at a lower frame rate, then set it back.

- **`ms`**: New budget; omitted, only returns the current one.
  - type: float

**Returns:** The current budget in milliseconds.

**Return type:** float

## addScene(name, overlay=1, asynchronous=False)

Loads a scene into the game engine.

> **Note:**
This function is not effective immediately, the scene is queued
and added on the next logic cycle where it will be available
from `getSceneList`

- **`name`**: The name of the scene
  - type: string
- **`overlay`**: Overlay or underlay (optional)
  - type: integer
- **`asynchronous`**: Compile the scene shaders a few per frame (budget of `setLibLoadFrameBudget`) before the scene joins `getSceneList`, so a loading screen keeps drawing; its logic starts only then.
  - type: boolean

## sendMessage(subject, body="", to="", message_from="")

Sends a message to sensors in any active scene.

- **`subject`**: The subject of the message
  - type: string
- **`body`**: The body of the message (optional)
  - type: string
- **`to`**: The name of the object to send the message to (optional)
  - type: string
- **`message_from`**: The name of the object that the message is coming from (optional)
  - type: string

## setGravity(gravity)

Sets the world gravity.

- **`gravity`**: gravity vector
  - type: Vector((fx, fy, fz))

## getSpectrum() (Deprecated)

Returns a 512 point list from the sound card.
This only works if the fmod sound driver is being used.

**Return type:** list [float], len(getSpectrum()) == 512

## getMaxLogicFrame()

Gets the maximum number of logic frames per render frame.

**Returns:** The maximum number of logic frames per render frame

**Return type:** integer

## setMaxLogicFrame(maxlogic)

Sets the maximum number of logic frames that are executed per render frame.
This does not affect the physic system that still runs at full frame rate.

- **`maxlogic`**: The new maximum number of logic frames per render frame. Valid values: 1..5
  - type: integer

## ~~getMaxPhysicsFrame()~~

> **Deprecated :**
No scheduler in the engine consumes this limit; the value set here has no effect.
Kept only for compatibility with existing scripts. It also no longer controls shadow
culling, which used to alias this same underlying setting.

Gets the value last passed to `setMaxPhysicsFrame`.

**Returns:** The value last set (default: 5)

**Return type:** integer

## ~~setMaxPhysicsFrame(maxphysics)~~

> **Deprecated :**
No scheduler in the engine consumes this limit; calling this has no effect on physics
or on shadows. Kept only for compatibility with existing scripts.

Stores the value for later retrieval via `getMaxPhysicsFrame`. Historically documented
as the maximum number of physics timesteps executed per render frame, but no code path in
the engine reads it for that purpose.

- **`maxphysics`**: The new maximum number of physics timestep per render frame. Valid values: 1..5.
  - type: integer

## getLogicTicRate()

Gets the logic update frequency.

**Returns:** The logic frequency in Hz

**Return type:** float

## setLogicTicRate(ticrate)

Sets the logic update frequency.

The logic update frequency is the number of times logic bricks are executed every second.
The default is 60 Hz.

- **`ticrate`**: The new logic update frequency (in Hz).
  - type: float

## getPhysicsTicRate()

Gets the physics update frequency

**Returns:** The physics update frequency in Hz

**Return type:** float

## setPhysicsTicRate(ticrate)

Sets the physics update frequency

The physics update frequency is the number of times the physics system is executed every second.
The default is 60 Hz.

- **`ticrate`**: The new update frequency (in Hz).
  - type: float

## getExitKey()

Gets the key used to exit the game engine

**Returns:** The key (defaults to `Range.events.ESCKEY`)

**Return type:** int

## setExitKey(key)

Sets the key used to exit the game engine

- **`key`**: A key constant from `Range.events`
  - type: int

## NextFrame()

Render next frame (if Python has control)

## setRender(render)

Sets the global flag that controls the render of the scene.
If True, the render is done after the logic frame.
If False, the render is skipped and another logic frame starts immediately.

> **Note:**
GPU VSync no longer limits the number of frame per second when render is off,
but the *Use Frame Rate* option still regulates the fps. To run as many frames
as possible, untick this option (Render Properties, System panel).

- **`render`**: the render flag
  - type: bool

## getRender()

Get the current value of the global render flag

**Returns:** The flag value

**Return type:** bool

## getClockTime()

Get the current BGE render time, in seconds. The BGE render time is the
simulation time corresponding to the next scene that will be rendered.

**Return type:** double

## getFrameTime()

Get the current BGE frame time, in seconds. The BGE frame time is the
simulation time corresponding to the current call of the logic system.
Generally speaking, it is what the user is interested in.

**Return type:** double

## getRealTime()

Get the number of real (system-clock) seconds elapsed since the beginning
of the simulation.

**Return type:** double

## getTimeScale()

Get the time multiplier between real-time and simulation time. The default
value is 1.0. A value greater than 1.0 means that the simulation is going
faster than real-time, a value lower than 1.0 means that the simulation is
going slower than real-time.

**Return type:** double

## setTimeScale(time_scale)

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

## setAnimationsUseTimeScale(use)

Choose whether actions follow `setTimeScale`. With `False` the
animation clock advances by the unscaled logic step, so actions play at
full speed while physics, timers and logic stay scaled. Default `True`.

- **`use`**: `True` to scale animations, `False` to keep them at full speed.
  - type: bool

## getAnimationsUseTimeScale()

**Returns:** `True` if actions follow the time scale.

**Return type:** bool

## ~~getUseExternalClock()~~

> **Deprecated 0.5.5:**
The flag has no effect; the simulation always uses its own clock.

**Return type:** bool

## ~~setUseExternalClock(use_external_clock)~~

> **Deprecated 0.5.5:**
Has no effect on the simulation and emits a `DeprecationWarning`.

- **`use_external_clock`**: the new setting

## setClockTime(new_time)

Set the next value of the simulation clock. It is preferable to use this
method from a custom main function in python, as calling it in the logic
block can easily lead to a blocked system (if the time does not advance
enough to run at least the next logic step).

- **`new_time`**: the next value of the BGE clock (in second).

## expandPath(path)

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

## getAverageFrameRate()

Gets the estimated/average framerate for all the active scenes, not only the current scene.

**Returns:** The estimated average framerate in frames per second

**Return type:** float

## getBlendFileList(path = "//")

Returns a list of blend files in the same directory as the open blend file, or from using the option argument.

- **`path`**: Optional directory argument, will be expanded (like expandPath) into the full path.
  - type: string

**Returns:** A list of filenames, with no directory prefix

**Return type:** list

## getRandomFloat()

Returns a random floating point value in the range [0 - 1)

## PrintGLInfo()

Prints GL Extension Info into the console

## PrintMemInfo()

Prints engine statistics into the console

## getProfileInfo()

Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time.

## getRenderStats()

Returns a Python dictionary of integer counters from the last completed frame, the same numbers the Debug Mode render queries show. Unlike the frame times from `getProfileInfo`, these do not depend on the hardware or the clock, so they are what A/B tests should compare.

Rasterizer counters, covering every pass of the frame (main camera, shadows, 2D filters):

* `drawCalls` -- draw calls issued.
* `materialBinds` -- material (shader program) binds.
* `lightBinds` -- uploads of the scene light and shadow lamp uniforms. The light set is constant per light layer, so this counts how often the same values were re-uploaded.

Counters of the active scene:

* `cullingTotal`, `cullingTested`, `cullingVisible` -- objects in the render list, tested against the frustum/DBVT, and found visible, from the last main-camera culling pass.
* `lightsTotal`, `lightsShadowUpdated`, `shadowPasses` -- lights in the scene, lights whose shadow buffer was refreshed, and shadow passes rendered (each cascade split counts as one).
* `sensors`, `controllersTriggered`, `actuatorsUpdated` -- registered sensors, and controllers/actuators run on the logic frame. Beware that these two are counted as the frame runs, and a Python controller calling this function is itself part of that frame: it sees only what ran before it, so from a controller the value is usually 0. The Debug Mode overlay reads them after the frame and shows the complete count. The rasterizer and culling counters above have no such caveat -- they are always from the last completed frame.

## deltaTime()

 `function`

Time in seconds since the previous frame. Multiply movement by it so it doesn't depend on FPS.

**Returns:** `float`

## freeUnconvertedData(scene)

*(new in Anastacio)* `function`

Exported game only: frees geometry used only by scene objects left out by the **Convert** option. They can no longer be converted. Returns the bytes freed.

**Returns:** `int`

## getAnimationRate()

 `function`

Animation update rate (times per second).

**Returns:** `float`

## getGraphicsCardRenderer()

 `function`

Graphics card name.

**Returns:** `str`

## getGraphicsCardVendor()

 `function`

Graphics card vendor.

**Returns:** `str`

## getLoadLog(clear=False)

*(new in Anastacio)* `function`

Report of the latest scene loads: dicts with `scene`, `stage`, `ms`, `detail` and `total`. With `clear=True`, clears it after reading.

**Returns:** `list`

## getMessages(to, subject='')

*(new in Anastacio)* `function`

Messages `(subject, body)` that a Message sensor of object `to` receives this frame.

**Returns:** `list`

## getObjectConvert(scene, object)

*(new in Anastacio)* `function`

Value of the object **Convert** option in the scene.

**Returns:** `bool`

## getProcessorName()

 `function`

Processor name.

**Returns:** `str`

## getRangeFileList(path='')

 `function`

`.range` files in the current game folder (or in `path`).

**Returns:** `list`

## getRasecFileList(path='')

 `function`

`.rasec` files in the current game folder (or in `path`).

**Returns:** `list`

## getRenderRate()

 `function`

Render rate (times per second).

**Returns:** `float`

## preloadScene(name)

*(new in Anastacio)* `function`

Converts a scene ahead of time, at the end of this frame (shaders and textures included), without adding it. A later `addScene` or `replaceScene` of it only inserts the ready scene, without stalling. Call it while a loading screen is showing. Returns `False` if the scene doesn't exist.

**Returns:** `bool`

## setAnimationRate(rate)

 `function`

Changes the animation update rate.

## setNeedsParents(count)

 `function`

How many times per frame the parent hierarchy is updated (going from 3 to 1 saves CPU).

## setObjectConvert(scene, object, convert, children=True)

*(new in Anastacio)* `function`

Changes the **Convert** option of an object in a scene not loaded yet. Returns how many objects changed.

**Returns:** `int`

## setRenderRate(rate)

 `function`

Changes the render rate.
