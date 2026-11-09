# Anastacio Engine - Python API reference

Single-file version of the API reference, for search and local AI (RAG). Each function and property has its own heading.

123 pages, 2182 entries (functions, properties and constants).

## Contents

**Modules**

- [Range.audio](#rangeaudio)
- [Range.constraints](#rangeconstraints)
- [Range.events](#rangeevents)
- [Range.imgui](#rangeimgui)
- [Range.logic](#rangelogic)
- [Range.network](#rangenetwork)
- [Range.network.steam](#rangenetworksteam)
- [Range.render](#rangerender)
- [Range.texture](#rangetexture)
- [Range.track](#rangetrack)

**Types**

- [BL_ActionActuator](#bl_actionactuator)
- [BL_ArmatureActuator](#bl_armatureactuator)
- [BL_ArmatureBone](#bl_armaturebone)
- [BL_ArmatureChannel](#bl_armaturechannel)
- [BL_ArmatureConstraint](#bl_armatureconstraint)
- [BL_ArmatureObject](#bl_armatureobject)
- [BL_Shader](#bl_shader)
- [BL_Texture](#bl_texture)
- [EXP_BaseListValue](#exp_baselistvalue)
- [EXP_BaseListWrapper](#exp_baselistwrapper)
- [EXP_ListValue](#exp_listvalue)
- [EXP_PropValue](#exp_propvalue)
- [EXP_PyObjectPlus](#exp_pyobjectplus)
- [EXP_Value](#exp_value)
- [KX_2DFilter](#kx_2dfilter)
- [KX_2DFilterManager](#kx_2dfiltermanager)
- [KX_2DFilterOffScreen](#kx_2dfilteroffscreen)
- [KX_AddObjectActuator](#kx_addobjectactuator)
- [KX_AnimationEvent](#kx_animationevent)
- [KX_AnimationEventManager](#kx_animationeventmanager)
- [KX_ArmatureSensor](#kx_armaturesensor)
- [KX_BatchGroup](#kx_batchgroup)
- [KX_BlenderMaterial](#kx_blendermaterial)
- [KX_BoundingBox](#kx_boundingbox)
- [KX_Camera](#kx_camera)
- [KX_CameraActuator](#kx_cameraactuator)
- [KX_ChangeColorActuator](#kx_changecoloractuator)
- [KX_CharacterWrapper](#kx_characterwrapper)
- [KX_CollisionContactPoint](#kx_collisioncontactpoint)
- [KX_CollisionSensor](#kx_collisionsensor)
- [KX_ConstraintActuator](#kx_constraintactuator)
- [KX_ConstraintWrapper](#kx_constraintwrapper)
- [KX_CubeMap](#kx_cubemap)
- [KX_DynamicActuator](#kx_dynamicactuator)
- [KX_EndObjectActuator](#kx_endobjectactuator)
- [KX_FontObject](#kx_fontobject)
- [KX_GameActuator](#kx_gameactuator)
- [KX_GameObject](#kx_gameobject)
- [KX_InputSystem](#kx_inputsystem)
- [KX_InputTable](#kx_inputtable)
- [KX_LibLoadStatus](#kx_libloadstatus)
- [KX_LightningActuator](#kx_lightningactuator)
- [KX_LightObject](#kx_lightobject)
- [KX_LodLevel](#kx_lodlevel)
- [KX_LodManager](#kx_lodmanager)
- [KX_Mesh](#kx_mesh)
- [KX_MeshBuilder](#kx_meshbuilder)
- [KX_MeshBuilderSlot](#kx_meshbuilderslot)
- [KX_MicrophoneSensor](#kx_microphonesensor)
- [KX_MouseActuator](#kx_mouseactuator)
- [KX_MouseFocusSensor](#kx_mousefocussensor)
- [KX_MovementSensor](#kx_movementsensor)
- [KX_NavMeshObject](#kx_navmeshobject)
- [KX_NearSensor](#kx_nearsensor)
- [KX_NetworkMessageActuator](#kx_networkmessageactuator)
- [KX_NetworkMessageSensor](#kx_networkmessagesensor)
- [KX_ObjectActuator](#kx_objectactuator)
- [KX_ParentActuator](#kx_parentactuator)
- [KX_ParticleSystem](#kx_particlesystem)
- [KX_PlanarMap](#kx_planarmap)
- [KX_PolyProxy](#kx_polyproxy)
- [KX_PythonComponent](#kx_pythoncomponent)
- [KX_PythonJoystick](#kx_pythonjoystick)
- [KX_PythonKeyboard](#kx_pythonkeyboard)
- [KX_PythonMotion](#kx_pythonmotion)
- [KX_PythonMouse](#kx_pythonmouse)
- [KX_RadarSensor](#kx_radarsensor)
- [KX_RaySensor](#kx_raysensor)
- [KX_ReplaceMeshActuator](#kx_replacemeshactuator)
- [KX_Scene](#kx_scene)
- [KX_SceneActuator](#kx_sceneactuator)
- [KX_SoundActuator](#kx_soundactuator)
- [KX_Speaker](#kx_speaker)
- [KX_StateActuator](#kx_stateactuator)
- [KX_SteeringActuator](#kx_steeringactuator)
- [KX_TextureRenderer](#kx_texturerenderer)
- [KX_TrackToActuator](#kx_tracktoactuator)
- [KX_VehicleWrapper](#kx_vehiclewrapper)
- [KX_VertexProxy](#kx_vertexproxy)
- [KX_VideoActuator](#kx_videoactuator)
- [KX_VisibilityActuator](#kx_visibilityactuator)
- [KX_VoiceActuator](#kx_voiceactuator)
- [KX_VRHeadSensor](#kx_vrheadsensor)
- [KX_WorldInfo](#kx_worldinfo)
- [SCA_2DFilterActuator](#sca_2dfilteractuator)
- [SCA_ActuatorSensor](#sca_actuatorsensor)
- [SCA_AlwaysSensor](#sca_alwayssensor)
- [SCA_ANDController](#sca_andcontroller)
- [SCA_AnimationEventSensor](#sca_animationeventsensor)
- [SCA_DelaySensor](#sca_delaysensor)
- [SCA_IActuator](#sca_iactuator)
- [SCA_IController](#sca_icontroller)
- [SCA_ILogicBrick](#sca_ilogicbrick)
- [SCA_InputEvent](#sca_inputevent)
- [SCA_IObject](#sca_iobject)
- [SCA_ISensor](#sca_isensor)
- [SCA_JoystickSensor](#sca_joysticksensor)
- [SCA_KeyboardSensor](#sca_keyboardsensor)
- [SCA_MouseSensor](#sca_mousesensor)
- [SCA_NANDController](#sca_nandcontroller)
- [SCA_NORController](#sca_norcontroller)
- [SCA_ORController](#sca_orcontroller)
- [SCA_PropertyActuator](#sca_propertyactuator)
- [SCA_PropertySensor](#sca_propertysensor)
- [SCA_PythonController](#sca_pythoncontroller)
- [SCA_RandomActuator](#sca_randomactuator)
- [SCA_RandomSensor](#sca_randomsensor)
- [SCA_VibrationActuator](#sca_vibrationactuator)
- [SCA_WaitActuator](#sca_waitactuator)
- [SCA_XNORController](#sca_xnorcontroller)
- [SCA_XORController](#sca_xorcontroller)
- [Texture](#texture)
- [TrackLine](#trackline)

---

# Modules

---

## Range.audio

Anastacio Engine module `Range.audio`. Also available as `bge.audio`.

```python
# Turn the microphone on and read the voice level.
import Range

if Range.audio.microphoneState() == "closed":
    Range.audio.microphoneStart()

print("Voice:", Range.audio.microphoneLevel())
```

```python
# Record the voice and play it back with a robot effect.
import Range

Range.audio.microphoneRecordStart()

# Later, when the player stops talking.
Range.audio.microphoneRecordStop("taunt")
Range.audio.playVoice("taunt", effect="ROBOT", reverb=True)
```

```python
# Control a World Sound module by name.
import Range

Range.audio.play("Music", fade=2.0)
Range.audio.setVolume("Music", 0.5)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### edit(sound, start=0, end=-1, fade_in=0, fade_out=0, normalize=False)

*(new in Anastacio)* `function`

Trims, fades and normalizes a sound; same as `aud.edit`.

**Returns:** `aud.Sound`

#### getVolume(module)

*(new in Anastacio)* `function`

Module volume; `None` when it does not exist.

**Returns:** `float`

#### isLive()

*(new in Anastacio)* `function`

`True` while the microphone is being heard.

**Returns:** `bool`

#### isPlaying(module)

*(new in Anastacio)* `function`

`True` while a sound of the module plays.

**Returns:** `bool`

#### microphone()

*(new in Anastacio)* `function`

The `aud.Microphone` in use, for advanced use; `None` before it starts.

**Returns:** `aud.Microphone`

#### microphoneDropped()

*(new in Anastacio)* `function`

Times audio was lost because the game hitched.

**Returns:** `int`

#### microphoneError()

*(new in Anastacio)* `function`

Why the microphone did not open.

**Returns:** `str`

#### microphoneIsRecording()

*(new in Anastacio)* `function`

`True` while recording.

**Returns:** `bool`

#### microphoneLevel()

*(new in Anastacio)* `function`

Voice level now, 0 to 1.

**Returns:** `float`

#### microphonePeak()

*(new in Anastacio)* `function`

Peak with a slow fall, 0 to 1.

**Returns:** `float`

#### microphoneRecordingSeconds()

*(new in Anastacio)* `function`

Length of the recording in progress, in seconds.

**Returns:** `float`

#### microphoneRecordStart()

*(new in Anastacio)* `function`

Starts recording.

#### microphoneRecordStop(slot="last")

*(new in Anastacio)* `function`

Stops and keeps the recording as `slot`. Returns the `aud.Sound` or `None`.

**Returns:** `aud.Sound`

#### microphoneSave(slot, path)

*(new in Anastacio)* `function`

Saves a recording as WAV. Relative paths go to the game folder (Web: `/saves`).

#### microphoneStart(device="")

*(new in Anastacio)* `function`

Turns the microphone on. On the Web, call it after a click or touch. `False` when it cannot open.

**Returns:** `bool`

#### microphoneState()

*(new in Anastacio)* `function`

Microphone state: `'closed'`, `'pending'`, `'granted'`, `'denied'` or `'error'`.

**Returns:** `str`

#### microphoneStop()

*(new in Anastacio)* `function`

Turns the microphone off.

#### modules()

*(new in Anastacio)* `function`

Names of the World Sound modules loaded so far.

**Returns:** `list`

#### next(module)

*(new in Anastacio)* `function`

Music: crosses to the next track.

#### pause(module)

*(new in Anastacio)* `function`

Pauses every sound of the module where it is.

#### play(module, sound="", fade=-1.0)

*(new in Anastacio)* `function`

Plays a sound of a World Sound module, or resumes a paused module. Without `sound`, Music plays the current track and Ambient plays every layer. `fade` is in seconds; negative uses the module Fade. `False` when the module or sound does not exist.

**Returns:** `bool`

#### playing(module)

*(new in Anastacio)* `function`

Names of the sounds playing now (Music: the current track).

**Returns:** `list`

#### playLive(effect="NONE", amount=1.0, volume=1.0, reverb=False)

*(new in Anastacio)* `function`

Plays the microphone now with a voice effect. One at a time; calling again swaps the effect. Use headphones: speakers feed back into the microphone.

#### playVoice(sound, effect="NONE", amount=1.0, volume=1.0, reverb=False)

*(new in Anastacio)* `function`

Plays a recording (name or `aud.Sound`) with a voice effect; see `voicePresets()`. `reverb=True` uses the area or World reverb. `False` when the recording or effect does not exist.

**Returns:** `bool`

#### previous(module)

*(new in Anastacio)* `function`

Music: crosses to the previous track.

#### recording(slot)

*(new in Anastacio)* `function`

The `aud.Sound` of a recording, or `None`.

**Returns:** `aud.Sound`

#### recordings()

*(new in Anastacio)* `function`

Names of the recordings kept so far.

**Returns:** `list`

#### resume(module)

*(new in Anastacio)* `function`

Goes on from where `pause(module)` stopped.

#### setRecording(slot, sound)

*(new in Anastacio)* `function`

Keeps an `aud.Sound` under a name. `None` removes it.

#### setVolume(module, volume)

*(new in Anastacio)* `function`

Sets the module volume, 0.0 to 1.0.

#### sounds(module)

*(new in Anastacio)* `function`

Names of the sounds of the module.

**Returns:** `list`

#### stop(module, sound="", fade=-1.0)

*(new in Anastacio)* `function`

Stops a World Sound module, or only one of its sounds. `fade` is in seconds; negative uses the module Fade.

#### stopLive()

*(new in Anastacio)* `function`

Stops hearing the microphone.

#### voiceFx(sound, preset, amount=1.0)

*(new in Anastacio)* `function`

Applies a voice effect; same as `aud.voice_fx`.

**Returns:** `aud.Sound`

#### voicePresets(live=False)

*(new in Anastacio)* `function`

Names of the voice effects.

**Returns:** `list`

---

## Range.constraints

> **See also:**
[`KX_VehicleWrapper`](#kx_vehiclewrapper), [`KX_CharacterWrapper`](#kx_characterwrapper), [`KX_ConstraintWrapper`](#kx_constraintwrapper)

Bullet Physics provides collision detection
and rigid body dynamics for the Blender Game Engine.

Features:

- Vehicle simulation.
- Rigid body constraints: hinge and point to point (ball socket).
- Access to internal physics settings,
like deactivation time, and debugging features

> **Note:**
Since this API is not well documented, it can be unclear what kind of values to use for setting parameters.
In general, damping settings should be in the range of 0 to 1 and
stiffness settings should not be much higher than about 10.

```python
# Connect two objects with a hinge.
import Range
from Range import constraints

scene = Range.logic.getCurrentScene()
door = scene.objects["Door"]
frame = scene.objects["Frame"]

hinge = constraints.createConstraint(
    door.getPhysicsId(), frame.getPhysicsId(),
    constraints.LINEHINGE_CONSTRAINT,
    0.0, 0.0, 1.0)
```

```python
# Change the world gravity and the quality of the solver.
from Range import constraints

constraints.setGravity(0.0, 0.0, -3.7)
constraints.setNumIterations(20)
```

```python
# See the collision shapes while testing.
from Range import constraints

constraints.setDebugMode(constraints.DBG_DRAWWIREFRAME)
```

```python
# Remove a constraint by its id.
from Range import constraints

constraints.removeConstraint(hinge.constraint_id)
```

### Examples

> **Tip:**
For more examples of Bullet physics and how to use them
see the [pybullet forum](https://pybullet.org/Bullet/phpBB3/viewforum.php?f=17)_.

### Functions

#### createConstraint( \

physicsid_1, physicsid_2, constraint_type, \
pivot_x=0.0, pivot_y=0.0, pivot_z=0.0, \
axis_x=0.0, axis_y=0.0, axis_z=0.0, flag=0)

Creates a constraint.

- **`physicsid_1`**: The physics id of the first object in constraint.
  - type: int
- **`physicsid_2`**: The physics id of the second object in constraint.
  - type: int
- **`constraint_type`**: The type of the constraint, see `Create Constraint Constants`_.
  - type: int
- **`pivot_x`**: Pivot X position. (optional)
  - type: float
- **`pivot_y`**: Pivot Y position. (optional)
  - type: float
- **`pivot_z`**: Pivot Z position. (optional)
  - type: float
- **`axis_x`**: X axis angle in degrees. (optional)
  - type: float
- **`axis_y`**: Y axis angle in degrees. (optional)
  - type: float
- **`axis_z`**: Z axis angle in degrees. (optional)
  - type: float
- **`flag`**: 128 to disable collision between linked bodies. (optional)
  - type: int

**Returns:** A constraint wrapper.

**Return type:** `KX_ConstraintWrapper`

#### createVehicle(physicsid)

Creates a vehicle constraint.

- **`physicsid`**: The physics id of the chassis object in constraint.
  - type: int

**Returns:** A vehicle constraint wrapper.

**Return type:** `KX_VehicleWrapper`

#### exportBulletFile(filename)

Exports a file representing the dynamics world (usually using `.bullet` extension).

See [Bullet binary serialization](http://bulletphysics.org/mediawiki-1.5.8/index.php/Bullet_binary_serialization)_.

- **`filename`**: File path.
  - type: str

#### getAppliedImpulse(constraintId)

- **`constraintId`**: The id of the constraint.
  - type: int

**Returns:** The most recent applied impulse.

**Return type:** float

#### getVehicleConstraint(constraintId)

- **`constraintId`**: The id of the vehicle constraint.
  - type: int

**Returns:** A vehicle constraint object.

**Return type:** `KX_VehicleWrapper`

#### getCharacter(gameobj)

- **`gameobj`**: The game object with the character physics.
  - type: `KX_GameObject`

**Returns:** Character wrapper.

**Return type:** `KX_CharacterWrapper`

#### removeConstraint(constraintId)

Removes a constraint.

- **`constraintId`**: The id of the constraint to be removed.
  - type: int

#### setCcdMode(ccdMode)

> **Note:**
Very experimental, not recommended

Sets the CCD (Continous Colision Detection) mode in the Physics Environment.

- **`ccdMode`**: The new CCD mode.
  - type: int

#### setContactBreakingTreshold(breakingTreshold)

> **Note:**
Reasonable default is 0.02 (if units are meters)

Sets tresholds to do with contact point management.

- **`breakingTreshold`**: The new contact breaking treshold.
  - type: float

#### setDeactivationAngularTreshold(angularTreshold)

Sets the angular velocity treshold.

- **`angularTreshold`**: New deactivation angular treshold.
  - type: float

#### setDeactivationLinearTreshold(linearTreshold)

Sets the linear velocity treshold.

- **`linearTreshold`**: New deactivation linear treshold.
  - type: float

#### setDeactivationTime(time)

Sets the time after which a resting rigidbody gets deactived.

- **`time`**: The deactivation time.
  - type: float

#### setDebugMode(mode)

Sets the debug mode.

- **`mode`**: The new debug mode, see `Debug Mode Constants`_.
  - type: int

#### setGravity(x, y, z)

Sets the gravity force.

- **`x`**: Gravity X force.
  - type: float
- **`y`**: Gravity Y force.
  - type: float
- **`z`**: Gravity Z force.
  - type: float

#### setLinearAirDamping(damping)

> **Note:**
Not implemented

Sets the linear air damping for rigidbodies.

#### setNumIterations(numiter)

Sets the number of iterations for an iterative constraint solver.

- **`numiter`**: New number of iterations.
  - type: int

#### setLinearSlop(slop)

Sets the contact penetration tolerance for the active physics scene.
A positive value allows objects to overlap by up to `slop` Blender units
before the Bullet solver applies positional correction. The default is `0.0`.

This is a scene-wide solver setting: it affects every physical contact in
the active scene. It does not change an object's collision margin or the
point at which collisions are detected. Use small values appropriate to the
scene scale.

- **`slop`**: Penetration tolerance in Blender units. Use a finite, non-negative value.
  - type: float

#### setNumTimeSubSteps(numsubstep)

Sets the number of substeps for each physics proceed. Tradeoff quality for performance.

- **`numsubstep`**: New number of substeps.
  - type: int

#### setSolverDamping(damping)

> **Note:**
Very experimental, not recommended

Sets the damper constant of a penalty based solver.

- **`damping`**: New damping for the solver.
  - type: float

#### setSolverTau(tau)

> **Note:**
Very experimental, not recommended

Sets the spring constant of a penalty based solver.

- **`tau`**: New tau for the solver.
  - type: float

#### setSolverType(solverType)

> **Note:**
Very experimental, not recommended

Sets the solver type.

- **`solverType`**: The new type of the solver.
  - type: int

#### setSorConstant(sor)

> **Note:**
Very experimental, not recommended

Sets the successive overrelaxation constant.

- **`sor`**: New sor value.
  - type: float

#### setUseEpa(epa)

> **Note:**
Not implemented

### Constants

#### error

Symbolic constant string that indicates error.

**Type:** str

### Debug Mode Constants

Debug mode to be used with `setDebugMode`.

#### DBG_NODEBUG

No debug.

#### DBG_DRAWWIREFRAME

Draw wireframe in debug.

#### DBG_DRAWAABB

Draw Axis Aligned Bounding Box in debug.

#### DBG_DRAWFREATURESTEXT

Draw features text in debug.

#### DBG_DRAWCONTACTPOINTS

Draw contact points in debug.

#### DBG_NOHELPTEXT

Debug without help text.

#### DBG_DRAWTEXT

Draw text in debug.

#### DBG_PROFILETIMINGS

Draw profile timings in debug.

#### DBG_ENABLESATCOMPARISION

Enable sat comparision in debug.

#### DBG_DISABLEBULLETLCP

Disable Bullet LCP.

#### DBG_ENABLECCD

Enable Continous Collision Detection in debug.

#### DBG_DRAWCONSTRAINTS

Draw constraints in debug.

#### DBG_DRAWCONSTRAINTLIMITS

Draw constraint limits in debug.

#### DBG_FASTWIREFRAME

Draw a fast wireframe in debug.

### Create Constraint Constants

Constraint type to be used with `createConstraint`.

#### POINTTOPOINT_CONSTRAINT

.. to do

#### LINEHINGE_CONSTRAINT

.. to do

#### ANGULAR_CONSTRAINT

.. to do

#### CONETWIST_CONSTRAINT

.. to do

#### VEHICLE_CONSTRAINT

.. to do

#### GENERIC_6DOF_CONSTRAINT

.. to do

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### setErp(value)

 `function`

Physics solver ERP: how much of the penetration between objects is corrected per step (default 0.2).

#### setErp2(value)

 `function`

ERP used with split impulse (default 0.8).

#### setGlobalCfm(value)

 `function`

Global CFM: makes contacts and joints "softer" (default 0.0).

#### setMaxGyroscopicForce(value)

 `function`

Gyroscopic force limit (explicit mode only).

#### setSplitImpulse(enabled)

 `function`

Solves contact position and velocity separately. Avoids objects "popping" when separating.

#### setSplitImpulsePenetrationThreshold(value)

 `function`

Penetration from which split impulse is used (default -0.04).

#### setSplitImpulseTurnErp(value)

 `function`

Split impulse rotation correction (default 0.1).

#### setWarmstartingFactor(value)

 `function`

How much the solver reuses the previous frame result (0.0 to 1.0).

---

## Range.events

> **See also:**
[`KX_PythonKeyboard`](#kx_pythonkeyboard), [`KX_PythonMouse`](#kx_pythonmouse), [`SCA_InputEvent`](#sca_inputevent), [`SCA_KeyboardSensor`](#sca_keyboardsensor)

```python
# Do something once, on the frame the key was pressed.
import Range

keys = Range.logic.keyboard.inputs

if keys[Range.events.SPACEKEY].activated:
    print("Jump")
```

```python
# Read the mouse buttons in the same way.
import Range

buttons = Range.logic.mouse.inputs

if buttons[Range.events.LEFTMOUSE].active:
    print("Shooting")
```

```python
# Show the name of each key held down.
import Range

for code in Range.logic.keyboard.activeInputs:
    print(Range.events.EventToString(code))
```

### Intro

This module holds key constants for the SCA_KeyboardSensor.

```python

# Set a connected keyboard sensor to accept F1
import Range

co = Range.logic.getCurrentController()
# 'Keyboard' is a keyboard sensor
sensor = co.sensors["Keyboard"]
sensor.key = Range.events.F1KEY
```

```python

# Do the all keys thing
import Range

co = Range.logic.getCurrentController()
# 'Keyboard' is a keyboard sensor
sensor = co.sensors["Keyboard"]

for key, input in sensor.inputs:
	# key[0] == Range.events.keycode = event.type, key[1] = input
	if Range.logic.KX_INPUT_JUST_ACTIVATED in input.queue:
		if key == Range.events.WKEY:
			# Activate Forward!
		if key == Range.events.SKEY:
			# Activate Backward!
		if key == Range.events.AKEY:
			# Activate Left!
		if key == Range.events.DKEY:
			# Activate Right!
```

```python

# The all keys thing without a keyboard sensor (but you will
# need an always sensor with pulse mode on)
import Range

# Just shortening names here
keyboard = Range.logic.keyboard
JUST_ACTIVATED = Range.logic.KX_INPUT_JUST_ACTIVATED

if JUST_ACTIVATED in keyboard.inputs[Range.events.WKEY].queue:
	print("Activate Forward!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.SKEY].queue:
	print("Activate Backward!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.AKEY].queue:
	print("Activate Left!")
if JUST_ACTIVATED in keyboard.inputs[Range.events.DKEY].queue:
	print("Activate Right!")
```

### Functions

#### EventToString(event)

Return the string name of a key event. Will raise a ValueError error if its invalid.

- **`event`**: key event constant from `Range.events` or the keyboard sensor.
  - type: int

**Return type:** string

#### EventToCharacter(event, shift)

Return the string name of a key event. Returns an empty string if the event cant be represented as a character.

  - type: int
- **`event`**: key event constant from `Range.events` or the keyboard sensor.
  - type: bool
- **`shift`**: set to true if shift is held.

**Return type:** string

### Keys (Constants)

### Mouse Keys

#### LEFTMOUSE

Left mouse button.

#### MIDDLEMOUSE

Middle mouse button (wheel click).

#### RIGHTMOUSE

Right mouse button.

#### WHEELUPMOUSE

Mouse wheel scrolled up.

#### WHEELDOWNMOUSE

Mouse wheel scrolled down.

#### LEFTTHUMBMOUSE

Back side mouse button.

#### RIGHTTHUMBMOUSE

Forward side mouse button.

#### BUTTON6MOUSE

Extra mouse button 6.

#### BUTTON7MOUSE

Extra mouse button 7.

#### MOUSEX

Horizontal mouse movement.

#### MOUSEY

### Keyboard Keys

### Alphabet keys

#### AKEY

A key.

#### BKEY

B key.

#### CKEY

C key.

#### DKEY

D key.

#### EKEY

E key.

#### FKEY

F key.

#### GKEY

G key.

#### HKEY

H key.

#### IKEY

I key.

#### JKEY

J key.

#### KKEY

K key.

#### LKEY

L key.

#### MKEY

M key.

#### NKEY

N key.

#### OKEY

O key.

#### PKEY

P key.

#### QKEY

Q key.

#### RKEY

R key.

#### SKEY

S key.

#### TKEY

T key.

#### UKEY

U key.

#### VKEY

V key.

#### WKEY

W key.

#### XKEY

X key.

#### YKEY

Y key.

#### ZKEY

### Number keys

#### ZEROKEY

0 key on the number row (not the numpad).

#### ONEKEY

1 key on the number row (not the numpad).

#### TWOKEY

2 key on the number row (not the numpad).

#### THREEKEY

3 key on the number row (not the numpad).

#### FOURKEY

4 key on the number row (not the numpad).

#### FIVEKEY

5 key on the number row (not the numpad).

#### SIXKEY

6 key on the number row (not the numpad).

#### SEVENKEY

7 key on the number row (not the numpad).

#### EIGHTKEY

8 key on the number row (not the numpad).

#### NINEKEY

### Modifiers Keys

#### CAPSLOCKKEY

Caps Lock key.

#### LEFTCTRLKEY

Left Ctrl key.

#### LEFTALTKEY

Left Alt key.

#### RIGHTALTKEY

Right Alt key (AltGr).

#### RIGHTCTRLKEY

Right Ctrl key.

#### RIGHTSHIFTKEY

Right Shift key.

#### LEFTSHIFTKEY

### Arrow Keys

#### LEFTARROWKEY

Left arrow.

#### DOWNARROWKEY

Down arrow.

#### RIGHTARROWKEY

Right arrow.

#### UPARROWKEY

### Numberpad Keys

#### PAD0

Numpad 0 key.

#### PAD1

Numpad 1 key.

#### PAD2

Numpad 2 key.

#### PAD3

Numpad 3 key.

#### PAD4

Numpad 4 key.

#### PAD5

Numpad 5 key.

#### PAD6

Numpad 6 key.

#### PAD7

Numpad 7 key.

#### PAD8

Numpad 8 key.

#### PAD9

Numpad 9 key.

#### PADPERIOD

Numpad period key.

#### PADSLASHKEY

Numpad / key.

#### PADASTERKEY

Numpad * key.

#### PADMINUS

Numpad - key.

#### PADENTER

Numpad Enter key.

#### PADPLUSKEY

### Function Keys

#### F1KEY

F1 key.

#### F2KEY

F2 key.

#### F3KEY

F3 key.

#### F4KEY

F4 key.

#### F5KEY

F5 key.

#### F6KEY

F6 key.

#### F7KEY

F7 key.

#### F8KEY

F8 key.

#### F9KEY

F9 key.

#### F10KEY

F10 key.

#### F11KEY

F11 key.

#### F12KEY

F12 key.

#### F13KEY

F13 key.

#### F14KEY

F14 key.

#### F15KEY

F15 key.

#### F16KEY

F16 key.

#### F17KEY

F17 key.

#### F18KEY

F18 key.

#### F19KEY

### Other Keys

#### ACCENTGRAVEKEY

Grave accent key (`).

#### BACKSLASHKEY

Backslash key (\).

#### BACKSPACEKEY

Backspace key.

#### COMMAKEY

Comma key (,).

#### DELKEY

Delete key.

#### ENDKEY

End key.

#### EQUALKEY

Equal key (=).

#### ESCKEY

Esc key.

#### HOMEKEY

Home key.

#### INSERTKEY

Insert key.

#### LEFTBRACKETKEY

Left bracket key ([).

#### LINEFEEDKEY

Line Feed key (rare on modern keyboards).

#### MINUSKEY

Minus key (-).

#### PAGEDOWNKEY

Page Down key.

#### PAGEUPKEY

Page Up key.

#### PAUSEKEY

Pause key.

#### PERIODKEY

Period key (.).

#### QUOTEKEY

Quote key (').

#### RIGHTBRACKETKEY

Right bracket key (]).

#### RETKEY (Deprecated: use bge.events.ENTERKEY)

#### ENTERKEY

Enter key.

#### SEMICOLONKEY

Semicolon key (;).

#### SLASHKEY

Slash key (/).

#### SPACEKEY

Space bar.

#### TABKEY

Tab key.

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### JOYSTICKA

 `constant`

Gamepad A button.

#### JOYSTICKB

 `constant`

Gamepad B button.

#### JOYSTICKBACK

 `constant`

Gamepad Back/Select button.

#### JOYSTICKGUIDE

 `constant`

Gamepad Guide (center) button.

#### JOYSTICKLEFTSHOUDER

 `constant`

Gamepad left shoulder button (LB).

#### JOYSTICKLEFTSTICK

 `constant`

Gamepad left stick click.

#### JOYSTICKPADDOWN

 `constant`

Gamepad D-pad down.

#### JOYSTICKPADLEFT

 `constant`

Gamepad D-pad left.

#### JOYSTICKPADRIGHT

 `constant`

Gamepad D-pad right.

#### JOYSTICKPADUP

 `constant`

Gamepad D-pad up.

#### JOYSTICKRIGHTSHOUDER

 `constant`

Gamepad right shoulder button (RB).

#### JOYSTICKRIGHTSTICK

 `constant`

Gamepad right stick click.

#### JOYSTICKX

 `constant`

Gamepad X button.

#### JOYSTICKY

 `constant`

Gamepad Y button.

#### OSKEY

 `constant`

System key (Windows/Command).

---

## Range.imgui

> **See also:**
[`Range.render`](#rangerender), [`Range.logic`](#rangelogic)

Anastacio Engine module `Range.imgui`. Also available as `bge.imgui`.

```python
# A pause window, drawn every frame by a component.
import Range
import Range.imgui as imgui

class PauseMenu(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        self.volume = 0.5
        imgui.set_game_ui_open(True)

    def update(self):
        w, h = imgui.get_display_size()
        imgui.set_next_window_size(300, 200, imgui.COND_FIRST_USE_EVER)
        imgui.set_next_window_pos(w / 2 - 150, h / 2 - 100)

        is_open, want_close = imgui.begin("Pause", closable=True)
        if is_open:
            changed, self.volume = imgui.slider_float("Volume", self.volume, 0.0, 1.0)
            imgui.separator()
            if imgui.button("Quit", width=240):
                Range.logic.endGame()
        imgui.end()
```

```python
# Common widgets return if they changed and the new value.
changed, self.fullscreen = imgui.checkbox("Full screen", self.fullscreen)
changed, self.quality = imgui.slider_int("Quality", self.quality, 0, 3)
imgui.same_line()
imgui.text("Level: {}".format(self.quality))
```

```python
# Change the color of one button.
imgui.push_style_color(imgui.COL_BUTTON, 0.8, 0.2, 0.2, 1.0)
imgui.button("Delete save")
imgui.pop_style_color()
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### begin(name, closable=False)

 `function`

Opens a window titled `name`. Everything you draw until `end()` goes inside it. With `closable=True` the window gets the X button, and `want_close` becomes True when it is clicked. Always call `end()` afterwards, even if `is_open` is False.

**Returns:** `(is_open, want_close)`

#### begin_popup_modal(name, closable=False)

 `function`

Draws the modal popup opened before with `open_popup(name)`. Only call `end_popup()` when `is_open` is True.

**Returns:** `(is_open, want_close)`

#### button(label, width=0, height=0)

 `function`

Button with the text `label`. Returns True on the frame it is clicked. Width and height 0 fit the text.

**Returns:** `bool`

#### checkbox(label, value)

 `function`

Checkbox. Pass the current value in `value` and keep `new_value`; `changed` is True when the player clicked.

**Returns:** `(changed, new_value)`

#### close_current_popup()

 `function`

Closes the open popup.

#### color_edit3(label, r, g, b)

 `function`

RGB color picker (values from 0 to 1). Returns the new color.

**Returns:** `(changed, r, g, b)`

#### color_edit4(label, r, g, b, a)

 `function`

RGBA color picker with transparency (values from 0 to 1).

**Returns:** `(changed, r, g, b, a)`

#### combo(label, current_item, items)

 `function`

Dropdown list. `items` is a list of strings and `current_item` the chosen index.

**Returns:** `(changed, new_item)`

#### draw_rect_filled(x1, y1, x2, y2, r, g, b, a)

 `function`

-- drawn above every window, for fades

#### end()

 `function`

Closes the window started with `begin()`.

#### end_popup()

 `function`

Closes a popup block.

#### get_cursor_pos()

 `function`

Where the next item will be drawn, relative to the current window.

**Returns:** `(x, y)`

#### get_cursor_screen_pos()

 `function`

Where the next item will be drawn, in screen pixels.

**Returns:** `(x, y)`

#### get_display_size()

 `function`

Size of the drawing area in pixels. Useful to place windows and HUD.

**Returns:** `(width, height)`

#### get_io_want_capture_keyboard()

 `function`

True when the interface is using the keyboard (e.g. typing in a field). Use it to not move the character at that moment.

**Returns:** `bool`

#### get_io_want_capture_mouse()

 `function`

True when the mouse is over the interface. Use it to ignore game clicks at that moment.

**Returns:** `bool`

#### image(texture_id, w, h)

 `function`

-- texture_id is a raw OpenGL bind code

#### input_text(label, value, max_length=256)

 `function`

Editable text field. `max_length` limits the number of characters.

**Returns:** `(changed, new_value)`

#### invisible_button(label, width, height)

 `function`

Clickable area with no drawing. Good to place over an image. Returns True when clicked.

**Returns:** `bool`

#### listbox(label, current_item, items, height_items=-1)

 `function`

Scrolling list. `height_items` is how many lines show (-1 = automatic).

**Returns:** `(changed, new_item)`

#### load_default_font(size)

*(new in Anastacio)* `function`

**Returns:** `font_id or None -- engine font with icons; None until built next frame`

#### load_font(path, size)

 `function`

Loads a .ttf/.otf font at the given size. Call it only once; the font is ready on the next frame. Use the id in `push_font()`.

**Returns:** `font_id`

#### open_popup(name)

 `function`

Opens the popup with that name.

#### pop_font()

 `function`

Goes back to the font before `push_font()`.

#### pop_item_width()

*(new in Anastacio)* `function`

Goes back to the width before `push_item_width()`.

#### pop_style_color(count=1)

 `function`

Undoes the last `count` colors from `push_style_color()`.

#### pop_style_var(count=1)

*(new in Anastacio)* `function`

Undoes the last `count` styles from `push_style_var()`.

#### push_font(font_id)

 `function`

Uses another font until `pop_font()`.

#### push_item_width(width)

*(new in Anastacio)* `function`

-- >0 pixels, <0 right-aligned to the window edge (-1 = full width)

#### push_style_color(idx, r, g, b, a)

 `function`

-- idx is one of the imgui.COL_* constants

#### push_style_var(idx, value)

*(new in Anastacio)* `function`

or push_style_var(idx, x, y) -- idx is one of imgui.STYLE_*

#### radio_button(label, active)

 `function`

Option button. `active` says whether it is the chosen one; when `pressed` is True, store this option as the group choice.

**Returns:** `pressed`

#### same_line()

 `function`

Puts the next item on the same line as the previous one.

#### separator()

 `function`

Draws a separator line.

#### set_cursor_pos(x, y)

 `function`

-- position relative to the current window

#### set_game_ui_open(open)

 `function`

-- enable/disable input + free mouse for Python-drawn game UI

#### set_next_item_width(width)

*(new in Anastacio)* `function`

-- same convention as push_item_width, next widget only

#### set_next_window_pos(x, y, cond=COND_ALWAYS)

 `function`

Position of the next window, in pixels.

#### set_next_window_size(w, h, cond=COND_ALWAYS)

 `function`

Size of the next window, in pixels.

#### slider_float(label, value, min, max)

 `function`

Slider for a float between `min` and `max`.

**Returns:** `(changed, new_value)`

#### slider_int(label, value, min, max)

 `function`

Slider for an integer between `min` and `max`.

**Returns:** `(changed, new_value)`

#### text(text)

 `function`

Shows a text.

---

## Range.logic

> **See also:**
[`KX_GameObject`](#kx_gameobject), [`KX_Scene`](#kx_scene), [`Range.events`](#rangeevents), [`SCA_PythonController`](#sca_pythoncontroller)

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

### Introduction

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

### Variables

#### globalDict

A dictionary that is saved between loading blend files so you can use it to store inventory and other variables you want to store between scenes and blend files.
It can also be written to a file and loaded later on with the game load/save actuators.

> **Note:**
only python built in types such as int/string/bool/float/tuples/lists can be saved, GameObjects, Actuators etc will not work as expected.

#### keyboard

The current keyboard wrapped in an `SCA_PythonKeyboard` object.

#### mouse

The current mouse wrapped in an `SCA_PythonMouse` object.

#### motion

Device motion sensors (gyroscope, accelerometer, tilt) wrapped in a `KX_PythonMotion` object.

#### joysticks

A list of attached `SCA_PythonJoystick`.
The list size is the maximum number of supported joysticks.
If no joystick is available for a given slot, the slot is set to None.

#### inputSystem

The input maps of the game, a `KX_InputSystem`. They are loaded from the JSON files in the KeyMapping folder, next to the game file.

### General functions

#### getCurrentController()

Gets the Python controller associated with this Python script.

**Return type:** `Range.types.SCA_PythonController`

#### getCurrentScene()

Gets the current Scene.

**Return type:** `Range.types.KX_Scene`

#### getSceneList()

Gets a list of the current scenes loaded in the game engine.

**Return type:** list of `Range.types.KX_Scene`

> **Note:**
Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes.

#### getInactiveSceneNames()

Gets a list of the scene's names not loaded in the game engine.

**Return type:** list of string

#### loadGlobalDict()

Loads Range.logic.globalDict from a file.

#### saveGlobalDict()

Saves Range.logic.globalDict to a file.

#### startGame(blend)

Loads the blend file.

- **`blend`**: The name of the blend file
  - type: string

#### endGame()

Ends the current game.

#### restartGame()

Restarts the current game by reloading the .blend file (the last saved version, not what is currently running).

#### LibLoad(blend, type, data, load_actions=False, verbose=False, load_scripts=True, asynchronous=False, scene=None)

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

#### LibNew(name, type, data)

Uses existing datablock data and loads in as a new library.

- **`name`**: A unique library name used for removal later
  - type: string
- **`type`**: The datablock type (currently only "Mesh" is supported)
  - type: string
- **`data`**: A list of names of the datablocks to load
  - type: list of strings

#### LibFree(name)

Frees a library, removing all objects and meshes from the currently active scenes.

- **`name`**: The name of the library to free (the name used in LibNew)
  - type: string

#### LibList()

Returns a list of currently loaded libraries.

**Return type:** list [str]

#### setLibLoadFrameBudget([ms])

Time per frame, in milliseconds, that asynchronous LibLoad may spend merging loaded libraries into the
scene (textures, shaders, objects). The default of 8 keeps the game frame rate; a loading screen can raise
it (e.g. 30) to finish sooner at a lower frame rate, then set it back.

- **`ms`**: New budget; omitted, only returns the current one.
  - type: float

**Returns:** The current budget in milliseconds.

**Return type:** float

#### addScene(name, overlay=1, asynchronous=False)

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

#### sendMessage(subject, body="", to="", message_from="")

Sends a message to sensors in any active scene.

- **`subject`**: The subject of the message
  - type: string
- **`body`**: The body of the message (optional)
  - type: string
- **`to`**: The name of the object to send the message to (optional)
  - type: string
- **`message_from`**: The name of the object that the message is coming from (optional)
  - type: string

#### setGravity(gravity)

Sets the world gravity.

- **`gravity`**: gravity vector
  - type: Vector((fx, fy, fz))

#### getSpectrum() (Deprecated)

Returns a 512 point list from the sound card.
This only works if the fmod sound driver is being used.

**Return type:** list [float], len(getSpectrum()) == 512

#### getMaxLogicFrame()

Gets the maximum number of logic frames per render frame.

**Returns:** The maximum number of logic frames per render frame

**Return type:** integer

#### setMaxLogicFrame(maxlogic)

Sets the maximum number of logic frames that are executed per render frame.
This does not affect the physic system that still runs at full frame rate.

- **`maxlogic`**: The new maximum number of logic frames per render frame. Valid values: 1..5
  - type: integer

#### ~~getMaxPhysicsFrame()~~

> **Deprecated :**
No scheduler in the engine consumes this limit; the value set here has no effect.
Kept only for compatibility with existing scripts. It also no longer controls shadow
culling, which used to alias this same underlying setting.

Gets the value last passed to `setMaxPhysicsFrame`.

**Returns:** The value last set (default: 5)

**Return type:** integer

#### ~~setMaxPhysicsFrame(maxphysics)~~

> **Deprecated :**
No scheduler in the engine consumes this limit; calling this has no effect on physics
or on shadows. Kept only for compatibility with existing scripts.

Stores the value for later retrieval via `getMaxPhysicsFrame`. Historically documented
as the maximum number of physics timesteps executed per render frame, but no code path in
the engine reads it for that purpose.

- **`maxphysics`**: The new maximum number of physics timestep per render frame. Valid values: 1..5.
  - type: integer

#### getLogicTicRate()

Gets the logic update frequency.

**Returns:** The logic frequency in Hz

**Return type:** float

#### setLogicTicRate(ticrate)

Sets the logic update frequency.

The logic update frequency is the number of times logic bricks are executed every second.
The default is 60 Hz.

- **`ticrate`**: The new logic update frequency (in Hz).
  - type: float

#### getPhysicsTicRate()

Gets the physics update frequency

**Returns:** The physics update frequency in Hz

**Return type:** float

#### setPhysicsTicRate(ticrate)

Sets the physics update frequency

The physics update frequency is the number of times the physics system is executed every second.
The default is 60 Hz.

- **`ticrate`**: The new update frequency (in Hz).
  - type: float

#### getExitKey()

Gets the key used to exit the game engine

**Returns:** The key (defaults to `Range.events.ESCKEY`)

**Return type:** int

#### setExitKey(key)

Sets the key used to exit the game engine

- **`key`**: A key constant from `Range.events`
  - type: int

#### NextFrame()

Render next frame (if Python has control)

#### setRender(render)

Sets the global flag that controls the render of the scene.
If True, the render is done after the logic frame.
If False, the render is skipped and another logic frame starts immediately.

> **Note:**
GPU VSync no longer limits the number of frame per second when render is off,
but the *Use Frame Rate* option still regulates the fps. To run as many frames
as possible, untick this option (Render Properties, System panel).

- **`render`**: the render flag
  - type: bool

#### getRender()

Get the current value of the global render flag

**Returns:** The flag value

**Return type:** bool

### Time related functions

#### getClockTime()

Get the current BGE render time, in seconds. The BGE render time is the
simulation time corresponding to the next scene that will be rendered.

**Return type:** double

#### getFrameTime()

Get the current BGE frame time, in seconds. The BGE frame time is the
simulation time corresponding to the current call of the logic system.
Generally speaking, it is what the user is interested in.

**Return type:** double

#### getRealTime()

Get the number of real (system-clock) seconds elapsed since the beginning
of the simulation.

**Return type:** double

#### getTimeScale()

Get the time multiplier between real-time and simulation time. The default
value is 1.0. A value greater than 1.0 means that the simulation is going
faster than real-time, a value lower than 1.0 means that the simulation is
going slower than real-time.

**Return type:** double

#### setTimeScale(time_scale)

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

#### setAnimationsUseTimeScale(use)

Choose whether actions follow `setTimeScale`. With `False` the
animation clock advances by the unscaled logic step, so actions play at
full speed while physics, timers and logic stay scaled. Default `True`.

- **`use`**: `True` to scale animations, `False` to keep them at full speed.
  - type: bool

#### getAnimationsUseTimeScale()

**Returns:** `True` if actions follow the time scale.

**Return type:** bool

#### ~~getUseExternalClock()~~

> **Deprecated 0.5.5:**
The flag has no effect; the simulation always uses its own clock.

**Return type:** bool

#### ~~setUseExternalClock(use_external_clock)~~

> **Deprecated 0.5.5:**
Has no effect on the simulation and emits a `DeprecationWarning`.

- **`use_external_clock`**: the new setting

#### setClockTime(new_time)

Set the next value of the simulation clock. It is preferable to use this
method from a custom main function in python, as calling it in the logic
block can easily lead to a blocked system (if the time does not advance
enough to run at least the next logic step).

- **`new_time`**: the next value of the BGE clock (in second).

### Utility functions

#### expandPath(path)

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

#### getAverageFrameRate()

Gets the estimated/average framerate for all the active scenes, not only the current scene.

**Returns:** The estimated average framerate in frames per second

**Return type:** float

#### getBlendFileList(path = "//")

Returns a list of blend files in the same directory as the open blend file, or from using the option argument.

- **`path`**: Optional directory argument, will be expanded (like expandPath) into the full path.
  - type: string

**Returns:** A list of filenames, with no directory prefix

**Return type:** list

#### getRandomFloat()

Returns a random floating point value in the range [0 - 1)

#### PrintGLInfo()

Prints GL Extension Info into the console

#### PrintMemInfo()

Prints engine statistics into the console

#### getProfileInfo()

Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time.

#### getRenderStats()

Returns a Python dictionary of integer counters from the last completed frame, the same numbers the Debug Mode render queries show. Unlike the frame times from `getProfileInfo`, these do not depend on the hardware or the clock, so they are what A/B tests should compare.

Rasterizer counters, covering every pass of the frame (main camera, shadows, 2D filters):

* `drawCalls` -- draw calls issued.
* `materialBinds` -- material (shader program) binds.
* `lightBinds` -- uploads of the scene light and shadow lamp uniforms. The light set is constant per light layer, so this counts how often the same values were re-uploaded.

Counters of the active scene:

* `cullingTotal`, `cullingTested`, `cullingVisible` -- objects in the render list, tested against the frustum/DBVT, and found visible, from the last main-camera culling pass.
* `lightsTotal`, `lightsShadowUpdated`, `shadowPasses` -- lights in the scene, lights whose shadow buffer was refreshed, and shadow passes rendered (each cascade split counts as one).
* `sensors`, `controllersTriggered`, `actuatorsUpdated` -- registered sensors, and controllers/actuators run on the logic frame. Beware that these two are counted as the frame runs, and a Python controller calling this function is itself part of that frame: it sees only what ran before it, so from a controller the value is usually 0. The Debug Mode overlay reads them after the frame and shows the complete count. The rasterizer and culling counters above have no such caveat -- they are always from the last completed frame.

### Constants

#### KX_TRUE

True value used by some modules.

#### KX_FALSE

False value used by some modules.

### Sensors

### Sensor Status

#### KX_SENSOR_INACTIVE

Sensor state: off.

#### KX_SENSOR_JUST_ACTIVATED

Sensor state: just turned on this frame.

#### KX_SENSOR_ACTIVE

Sensor state: still on.

#### KX_SENSOR_JUST_DEACTIVATED

### Armature Sensor

See `Range.types.KX_ArmatureSensor.type`

#### KX_ARMSENSOR_STATE_CHANGED

Detect that the constraint is changing state (active/inactive)

**Value:** `0`

#### KX_ARMSENSOR_LIN_ERROR_BELOW

Detect that the constraint linear error is above a threshold

**Value:** `1`

#### KX_ARMSENSOR_LIN_ERROR_ABOVE

Detect that the constraint linear error is below a threshold

**Value:** `2`

#### KX_ARMSENSOR_ROT_ERROR_BELOW

Detect that the constraint rotation error is above a threshold

**Value:** `3`

#### KX_ARMSENSOR_ROT_ERROR_ABOVE

Detect that the constraint rotation error is below a threshold

**Value:** `4`

### Property Sensor

#### KX_PROPSENSOR_EQUAL

Activate when the property is equal to the sensor value.

**Value:** `1`

#### KX_PROPSENSOR_NOTEQUAL

Activate when the property is not equal to the sensor value.

**Value:** `2`

#### KX_PROPSENSOR_INTERVAL

Activate when the property is between the specified limits.

**Value:** `3`

#### KX_PROPSENSOR_CHANGED

Activate when the property changes

**Value:** `4`

#### KX_PROPSENSOR_EXPRESSION

Activate when the expression matches

**Value:** `5`

#### KX_PROPSENSOR_LESSTHAN

Activate when the property is less than the sensor value

**Value:** `6`

#### KX_PROPSENSOR_GREATERTHAN

Activate when the property is greater than the sensor value

**Value:** `7`

### Radar Sensor

See `Range.types.KX_RadarSensor`

#### KX_RADAR_AXIS_POS_X

Radar sensor: cone pointing along the object +X axis.

#### KX_RADAR_AXIS_POS_Y

Radar sensor: cone pointing along the object +Y axis.

#### KX_RADAR_AXIS_POS_Z

Radar sensor: cone pointing along the object +Z axis.

#### KX_RADAR_AXIS_NEG_X

Radar sensor: cone pointing along the object -X axis.

#### KX_RADAR_AXIS_NEG_Y

Radar sensor: cone pointing along the object -Y axis.

#### KX_RADAR_AXIS_NEG_Z

### Ray Sensor

See `Range.types.KX_RaySensor`

#### KX_RAY_AXIS_POS_X

Ray sensor: ray cast along the object +X axis.

#### KX_RAY_AXIS_POS_Y

Ray sensor: ray cast along the object +Y axis.

#### KX_RAY_AXIS_POS_Z

Ray sensor: ray cast along the object +Z axis.

#### KX_RAY_AXIS_NEG_X

Ray sensor: ray cast along the object -X axis.

#### KX_RAY_AXIS_NEG_Y

Ray sensor: ray cast along the object -Y axis.

#### KX_RAY_AXIS_NEG_Z

### Actuators

### Action Actuator

See `Range.types.BL_ActionActuator`

#### KX_ACTIONACT_PLAY

Action actuator: plays the animation once.

#### KX_ACTIONACT_PINGPONG

Action actuator: plays forward and, on the next activation, backward.

#### KX_ACTIONACT_FLIPPER

Action actuator: plays while active and goes back to the start when turned off.

#### KX_ACTIONACT_LOOPSTOP

Action actuator: loops while the sensor is active.

#### KX_ACTIONACT_LOOPEND

Action actuator: loops and, when turned off, finishes the current loop.

#### KX_ACTIONACT_PROPERTY

### Armature Actuator

See `Range.types.BL_ArmatureActuator.type`

#### KX_ACT_ARMATURE_RUN

Just make sure the armature will be updated on the next graphic frame.
This is the only persistent mode of the actuator:
it executes automatically once per frame until stopped by a controller

**Value:** `0`

#### KX_ACT_ARMATURE_ENABLE

Enable the constraint.

**Value:** `1`

#### KX_ACT_ARMATURE_DISABLE

Disable the constraint (runtime constraint values are not updated).

**Value:** `2`

#### KX_ACT_ARMATURE_SETTARGET

Change target and subtarget of constraint.

**Value:** `3`

#### KX_ACT_ARMATURE_SETWEIGHT

Change weight of constraint (IK only).

**Value:** `4`

#### KX_ACT_ARMATURE_SETINFLUENCE

Change influence of constraint.

**Value:** `5`

### Constraint Actuator

See `Range.types.KX_ConstraintActuator.option`

* Applicable to Distance constraint:

#### KX_CONSTRAINTACT_NORMAL

Activate alignment to surface

#### KX_CONSTRAINTACT_DISTANCE

Activate distance control

#### KX_CONSTRAINTACT_LOCAL

Direction of the ray is along the local axis

* Applicable to Force field constraint:

#### KX_CONSTRAINTACT_DOROTFH

Force field act on rotation as well

* Applicable to both:

#### KX_CONSTRAINTACT_MATERIAL

Detect material rather than property

#### KX_CONSTRAINTACT_PERMANENT

No deactivation if ray does not hit target

See `Range.types.KX_ConstraintActuator.limit`

#### KX_CONSTRAINTACT_LOCX

Limit X coord.

#### KX_CONSTRAINTACT_LOCY

Limit Y coord

#### KX_CONSTRAINTACT_LOCZ

Limit Z coord

#### KX_CONSTRAINTACT_ROTX

Limit X rotation

#### KX_CONSTRAINTACT_ROTY

Limit Y rotation

#### KX_CONSTRAINTACT_ROTZ

Limit Z rotation

#### KX_CONSTRAINTACT_DIRNX

Set distance along negative X axis

#### KX_CONSTRAINTACT_DIRNY

Set distance along negative Y axis

#### KX_CONSTRAINTACT_DIRNZ

Set distance along negative Z axis

#### KX_CONSTRAINTACT_DIRPX

Set distance along positive X axis

#### KX_CONSTRAINTACT_DIRPY

Set distance along positive Y axis

#### KX_CONSTRAINTACT_DIRPZ

Set distance along positive Z axis

#### KX_CONSTRAINTACT_ORIX

Set orientation of X axis

#### KX_CONSTRAINTACT_ORIY

Set orientation of Y axis

#### KX_CONSTRAINTACT_ORIZ

Set orientation of Z axis

#### KX_CONSTRAINTACT_FHNX

Set force field along negative X axis

#### KX_CONSTRAINTACT_FHNY

Set force field along negative Y axis

#### KX_CONSTRAINTACT_FHNZ

Set force field along negative Z axis

#### KX_CONSTRAINTACT_FHPX

Set force field along positive X axis

#### KX_CONSTRAINTACT_FHPY

Set force field along positive Y axis

#### KX_CONSTRAINTACT_FHPZ

Set force field along positive Z axis

### Dynamic Actuator

See `Range.types.KX_SCA_DynamicActuator`

#### KX_DYN_RESTORE_DYNAMICS

Dynamic actuator: turns physics back on.

#### KX_DYN_DISABLE_DYNAMICS

Dynamic actuator: turns off the object physics.

#### KX_DYN_ENABLE_RIGID_BODY

Dynamic actuator: turns on rigid body mode (physics rotation).

#### KX_DYN_DISABLE_RIGID_BODY

Dynamic actuator: turns off rigid body mode.

#### KX_DYN_SET_MASS

### Game Actuator

See `Range.types.KX_GameActuator`

#### KX_GAME_LOAD

Game actuator: loads another game file.

#### KX_GAME_START

Game actuator: starts another game file.

#### KX_GAME_RESTART

Game actuator: restarts the game.

#### KX_GAME_QUIT

Game actuator: quits the game.

#### KX_GAME_SAVECFG

Game actuator: saves the global properties to a file.

#### KX_GAME_LOADCFG

### Mouse Actuator

#### KX_ACT_MOUSE_OBJECT_AXIS_X

Mouse (look) actuator: rotates around the object X axis.

#### KX_ACT_MOUSE_OBJECT_AXIS_Y

Mouse (look) actuator: rotates around the object Y axis.

#### KX_ACT_MOUSE_OBJECT_AXIS_Z

### Parent Actuator

#### KX_PARENT_REMOVE

Parent actuator: removes the object from its parent.

#### KX_PARENT_SET

### Random Distributions

See `Range.types.SCA_RandomActuator`

#### KX_RANDOMACT_BOOL_CONST

Random actuator: fixed true/false.

#### KX_RANDOMACT_BOOL_UNIFORM

Random actuator: true or false, 50% chance each.

#### KX_RANDOMACT_BOOL_BERNOUILLI

Random actuator: true with the chance you set.

#### KX_RANDOMACT_INT_CONST

Random actuator: fixed integer.

#### KX_RANDOMACT_INT_UNIFORM

Random actuator: integer picked between a minimum and a maximum.

#### KX_RANDOMACT_INT_POISSON

Random actuator: integer with a Poisson distribution (given mean).

#### KX_RANDOMACT_FLOAT_CONST

Random actuator: fixed float.

#### KX_RANDOMACT_FLOAT_UNIFORM

Random actuator: float picked between a minimum and a maximum.

#### KX_RANDOMACT_FLOAT_NORMAL

Random actuator: float with a normal distribution (mean and deviation).

#### KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL

### Scene Actuator

See `Range.types.KX_SceneActuator`

#### KX_SCENE_RESTART

Scene actuator: restarts the scene.

#### KX_SCENE_SET_SCENE

Scene actuator: switches to another scene.

#### KX_SCENE_SET_CAMERA

Scene actuator: changes the active camera.

#### KX_SCENE_ADD_FRONT_SCENE

Scene actuator: adds a scene on top (overlay, like a HUD).

#### KX_SCENE_ADD_BACK_SCENE

Scene actuator: adds a scene behind (background).

#### KX_SCENE_REMOVE_SCENE

Scene actuator: removes a scene.

#### KX_SCENE_SUSPEND

Scene actuator: pauses a scene.

#### KX_SCENE_RESUME

### Sound Actuator

See `Range.types.KX_SoundActuator`

#### KX_SOUNDACT_PLAYSTOP

Sound actuator: plays while the sensor is active and stops when it turns off.

**Value:** `1`

#### KX_SOUNDACT_PLAYEND

Sound actuator: plays the whole sound once.

**Value:** `2`

#### KX_SOUNDACT_LOOPSTOP

Sound actuator: loops while the sensor is active.

**Value:** `3`

#### KX_SOUNDACT_LOOPEND

Sound actuator: loops and, when turned off, finishes the current loop.

**Value:** `4`

#### KX_SOUNDACT_LOOPBIDIRECTIONAL

Sound actuator: plays forward and backward in a loop.

**Value:** `5`

#### KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP

**Value:** `6`

### Steering Actuator

See `Range.types.KX_SteeringActuator.behavior`

#### KX_STEERING_SEEK

Steering actuator: goes to the target.

**Value:** `1`

#### KX_STEERING_FLEE

Steering actuator: runs away from the target.

**Value:** `2`

#### KX_STEERING_PATHFOLLOWING

**Value:** `3`

### TrackTo Actuator

See `Range.types.KX_TrackToActuator`

#### KX_TRACK_UPAXIS_POS_X

Track To actuator: the object +X axis points up.

#### KX_TRACK_UPAXIS_POS_Y

Track To actuator: the object +Y axis points up.

#### KX_TRACK_UPAXIS_POS_Z

Track To actuator: the object +Z axis points up.

#### KX_TRACK_TRAXIS_POS_X

Track To actuator: the object +X axis points at the target.

#### KX_TRACK_TRAXIS_POS_Y

Track To actuator: the object +Y axis points at the target.

#### KX_TRACK_TRAXIS_POS_Z

Track To actuator: the object +Z axis points at the target.

#### KX_TRACK_TRAXIS_NEG_X

Track To actuator: the object -X axis points at the target.

#### KX_TRACK_TRAXIS_NEG_Y

Track To actuator: the object -Y axis points at the target.

#### KX_TRACK_TRAXIS_NEG_Z

### Various

### 2D Filter

#### RAS_2DFILTER_BLUR

2D Filter actuator: blur.

**Value:** `2`

#### RAS_2DFILTER_CUSTOMFILTER

Customer filter, the code code is set via shaderText property.

**Value:** `12`

#### RAS_2DFILTER_DILATION

2D Filter actuator: dilation (brightens edges).

**Value:** `4`

#### RAS_2DFILTER_DISABLED

Disable the filter that is currently active

**Value:** `-1`

#### RAS_2DFILTER_ENABLED

Enable the filter that was previously disabled

**Value:** `-2`

#### RAS_2DFILTER_EROSION

2D Filter actuator: erosion (darkens edges).

**Value:** `5`

#### RAS_2DFILTER_GRAYSCALE

2D Filter actuator: grayscale.

**Value:** `9`

#### RAS_2DFILTER_INVERT

2D Filter actuator: inverted colors.

**Value:** `11`

#### RAS_2DFILTER_LAPLACIAN

2D Filter actuator: edge detection (Laplace).

**Value:** `6`

#### RAS_2DFILTER_MOTIONBLUR

Create and enable preset filters

**Value:** `1`

#### RAS_2DFILTER_NOFILTER

Disable and destroy the filter that is currently active

**Value:** `0`

#### RAS_2DFILTER_PREWITT

2D Filter actuator: edge detection (Prewitt).

**Value:** `8`

#### RAS_2DFILTER_SEPIA

2D Filter actuator: sepia.

**Value:** `10`

#### RAS_2DFILTER_SHARPEN

2D Filter actuator: sharpen.

**Value:** `3`

#### RAS_2DFILTER_SOBEL

**Value:** `7`

#### RAS_2DFILTER_SOBEL

**Value:** `14`

### Armature Channel

See `Range.types.BL_ArmatureChannel.rotation_mode`

.. note:
euler mode are named as in Blender UI but the actual axis order is reversed

#### ROT_MODE_QUAT

Use quaternion in rotation attribute to update bone rotation.

**Value:** `0`

#### ROT_MODE_XYZ

Use euler_rotation and apply angles on bone's Z, Y, X axis successively.

**Value:** `1`

#### ROT_MODE_XZY

Use euler_rotation and apply angles on bone's Y, Z, X axis successively.

**Value:** `2`

#### ROT_MODE_YXZ

Use euler_rotation and apply angles on bone's Z, X, Y axis successively.

**Value:** `3`

#### ROT_MODE_YZX

Use euler_rotation and apply angles on bone's X, Z, Y axis successively.

**Value:** `4`

#### ROT_MODE_ZXY

Use euler_rotation and apply angles on bone's Y, X, Z axis successively.

**Value:** `5`

#### ROT_MODE_ZYX

Use euler_rotation and apply angles on bone's X, Y, Z axis successively.

**Value:** `6`

### Armature Constraint

See `Range.types.BL_ArmatureConstraint.type`

#### CONSTRAINT_TYPE_TRACKTO

Bone constraint type: Track To (points at a target).

#### CONSTRAINT_TYPE_KINEMATIC

Bone constraint type: IK (inverse kinematics).

#### CONSTRAINT_TYPE_ROTLIKE

Bone constraint type: Copy Rotation.

#### CONSTRAINT_TYPE_LOCLIKE

Bone constraint type: Copy Location.

#### CONSTRAINT_TYPE_MINMAX

Bone constraint type: Floor (min/max limit).

#### CONSTRAINT_TYPE_SIZELIKE

Bone constraint type: Copy Scale.

#### CONSTRAINT_TYPE_LOCKTRACK

Bone constraint type: Locked Track.

#### CONSTRAINT_TYPE_STRETCHTO

Bone constraint type: Stretch To.

#### CONSTRAINT_TYPE_CLAMPTO

Bone constraint type: Clamp To (sticks to a curve).

#### CONSTRAINT_TYPE_TRANSFORM

Bone constraint type: Transformation.

#### CONSTRAINT_TYPE_DISTLIMIT

See `Range.types.BL_ArmatureConstraint.ik_type`

#### CONSTRAINT_IK_COPYPOSE

constraint is trying to match the position and eventually the rotation of the target.

**Value:** `0`

#### CONSTRAINT_IK_DISTANCE

Constraint is maintaining a certain distance to target subject to ik_mode

**Value:** `1`

See `Range.types.BL_ArmatureConstraint.ik_flag`

#### CONSTRAINT_IK_FLAG_TIP

Set when the constraint operates on the head of the bone and not the tail

**Value:** `1`

#### CONSTRAINT_IK_FLAG_ROT

Set when the constraint tries to match the orientation of the target

**Value:** `2`

#### CONSTRAINT_IK_FLAG_STRETCH

Set when the armature is allowed to stretch (only the bones with stretch factor > 0.0)

**Value:** `16`

#### CONSTRAINT_IK_FLAG_POS

Set when the constraint tries to match the position of the target.

**Value:** `32`

See `Range.types.BL_ArmatureConstraint.ik_mode`

#### CONSTRAINT_IK_MODE_INSIDE

The constraint tries to keep the bone within ik_dist of target

**Value:** `0`

#### CONSTRAINT_IK_MODE_OUTSIDE

The constraint tries to keep the bone outside ik_dist of the target

**Value:** `1`

#### CONSTRAINT_IK_MODE_ONSURFACE

The constraint tries to keep the bone exactly at ik_dist of the target.

**Value:** `2`

### Blender Material

#### BL_DST_ALPHA

Material blend factor: destination alpha. Used in setBlending().

#### BL_DST_COLOR

Material blend factor: destination color. Used in setBlending().

#### BL_ONE

Material blend factor: one (full color). Used in setBlending().

#### BL_ONE_MINUS_DST_ALPHA

Material blend factor: one minus destination alpha. Used in setBlending().

#### BL_ONE_MINUS_DST_COLOR

Material blend factor: one minus destination color. Used in setBlending().

#### BL_ONE_MINUS_SRC_ALPHA

Material blend factor: one minus source alpha. Used in setBlending().

#### BL_ONE_MINUS_SRC_COLOR

Material blend factor: one minus source color. Used in setBlending().

#### BL_SRC_ALPHA

Material blend factor: source alpha. Used in setBlending().

#### BL_SRC_ALPHA_SATURATE

Material blend factor: saturated source alpha. Used in setBlending().

#### BL_SRC_COLOR

Material blend factor: source color. Used in setBlending().

#### BL_ZERO

### Input Status

See `Range.types.SCA_PythonKeyboard`, `Range.types.SCA_PythonMouse`, `Range.types.SCA_MouseSensor`, `Range.types.SCA_KeyboardSensor`

#### KX_INPUT_NONE

Key/button state: released.

#### KX_INPUT_JUST_ACTIVATED

Key/button state: just pressed.

#### KX_INPUT_ACTIVE

Key/button state: held down.

#### KX_INPUT_JUST_RELEASED

### KX_GameObject

See `Range.types.KX_GameObject.playAction`

#### KX_ACTION_MODE_PLAY

Play the action once.

**Value:** `0`

#### KX_ACTION_MODE_LOOP

Loop the action (repeat it).

**Value:** `1`

#### KX_ACTION_MODE_PING_PONG

Play the action one direct then back the other way when it has completed.

**Value:** `2`

#### KX_ACTION_BLEND_BLEND

Blend layers using linear interpolation

**Value:** `0`

#### KX_ACTION_BLEND_ADD

Adds the layers together

**Value:** `1`

### Mouse Buttons

See `Range.types.SCA_MouseSensor`

#### KX_MOUSE_BUT_LEFT

Left mouse button (for the mouse sensor).

#### KX_MOUSE_BUT_MIDDLE

Middle mouse button (for the mouse sensor).

#### KX_MOUSE_BUT_RIGHT

### Navigation Mesh Draw Modes

#### RM_WALLS

Draw only the walls.

#### RM_POLYS

Draw only polygons.

#### RM_TRIS

Draw triangle mesh.

### Shader

#### VIEWMATRIX

Shader uniform with the view (world → camera) matrix. Used in setUniformDef().

#### VIEWMATRIX_INVERSE

Shader uniform with the view (world → camera) matrix, inverse. Used in setUniformDef().

#### VIEWMATRIX_INVERSETRANSPOSE

Shader uniform with the view (world → camera) matrix, inverse transposed. Used in setUniformDef().

#### VIEWMATRIX_TRANSPOSE

Shader uniform with the view (world → camera) matrix, transposed. Used in setUniformDef().

#### MODELMATRIX

Shader uniform with the model (object → world) matrix. Used in setUniformDef().

#### MODELMATRIX_INVERSE

Shader uniform with the model (object → world) matrix, inverse. Used in setUniformDef().

#### MODELMATRIX_INVERSETRANSPOSE

Shader uniform with the model (object → world) matrix, inverse transposed. Used in setUniformDef().

#### MODELMATRIX_TRANSPOSE

Shader uniform with the model (object → world) matrix, transposed. Used in setUniformDef().

#### MODELVIEWMATRIX

Shader uniform with the model × view matrix. Used in setUniformDef().

#### MODELVIEWMATRIX_INVERSE

Shader uniform with the model × view matrix, inverse. Used in setUniformDef().

#### MODELVIEWMATRIX_INVERSETRANSPOSE

Shader uniform with the model × view matrix, inverse transposed. Used in setUniformDef().

#### MODELVIEWMATRIX_TRANSPOSE

Shader uniform with the model × view matrix, transposed. Used in setUniformDef().

#### CAM_POS

Current camera position

#### CONSTANT_TIMER

Shader uniform with the game time, for animated effects.

#### EYE

User a timer for the uniform value.

#### SHD_TANGENT

### States

See `Range.types.KX_StateActuator`

#### KX_STATE1

Mask for logic brick state 1.

#### KX_STATE2

Mask for logic brick state 2.

#### KX_STATE3

Mask for logic brick state 3.

#### KX_STATE4

Mask for logic brick state 4.

#### KX_STATE5

Mask for logic brick state 5.

#### KX_STATE6

Mask for logic brick state 6.

#### KX_STATE7

Mask for logic brick state 7.

#### KX_STATE8

Mask for logic brick state 8.

#### KX_STATE9

Mask for logic brick state 9.

#### KX_STATE10

Mask for logic brick state 10.

#### KX_STATE11

Mask for logic brick state 11.

#### KX_STATE12

Mask for logic brick state 12.

#### KX_STATE13

Mask for logic brick state 13.

#### KX_STATE14

Mask for logic brick state 14.

#### KX_STATE15

Mask for logic brick state 15.

#### KX_STATE16

Mask for logic brick state 16.

#### KX_STATE17

Mask for logic brick state 17.

#### KX_STATE18

Mask for logic brick state 18.

#### KX_STATE19

Mask for logic brick state 19.

#### KX_STATE20

Mask for logic brick state 20.

#### KX_STATE21

Mask for logic brick state 21.

#### KX_STATE22

Mask for logic brick state 22.

#### KX_STATE23

Mask for logic brick state 23.

#### KX_STATE24

Mask for logic brick state 24.

#### KX_STATE25

Mask for logic brick state 25.

#### KX_STATE26

Mask for logic brick state 26.

#### KX_STATE27

Mask for logic brick state 27.

#### KX_STATE28

Mask for logic brick state 28.

#### KX_STATE29

Mask for logic brick state 29.

#### KX_STATE30

See `Range.types.KX_StateActuator.operation`

#### KX_STATE_OP_CLR

Substract bits to state mask

**Value:** `0`

#### KX_STATE_OP_CPY

Copy state mask

**Value:** `1`

#### KX_STATE_OP_NEG

Invert bits to state mask

**Value:** `2`

#### KX_STATE_OP_SET

Add bits to state mask

**Value:** `3`

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### deltaTime()

 `function`

Time in seconds since the previous frame. Multiply movement by it so it doesn't depend on FPS.

**Returns:** `float`

#### freeUnconvertedData(scene)

*(new in Anastacio)* `function`

Exported game only: frees geometry used only by scene objects left out by the **Convert** option. They can no longer be converted. Returns the bytes freed.

**Returns:** `int`

#### getAnimationRate()

 `function`

Animation update rate (times per second).

**Returns:** `float`

#### getGraphicsCardRenderer()

 `function`

Graphics card name.

**Returns:** `str`

#### getGraphicsCardVendor()

 `function`

Graphics card vendor.

**Returns:** `str`

#### getLoadLog(clear=False)

*(new in Anastacio)* `function`

Report of the latest scene loads: dicts with `scene`, `stage`, `ms`, `detail` and `total`. With `clear=True`, clears it after reading.

**Returns:** `list`

#### getMessages(to, subject='')

*(new in Anastacio)* `function`

Messages `(subject, body)` that a Message sensor of object `to` receives this frame.

**Returns:** `list`

#### getObjectConvert(scene, object)

*(new in Anastacio)* `function`

Value of the object **Convert** option in the scene.

**Returns:** `bool`

#### getProcessorName()

 `function`

Processor name.

**Returns:** `str`

#### getRangeFileList(path='')

 `function`

`.range` files in the current game folder (or in `path`).

**Returns:** `list`

#### getRasecFileList(path='')

 `function`

`.rasec` files in the current game folder (or in `path`).

**Returns:** `list`

#### getRenderRate()

 `function`

Render rate (times per second).

**Returns:** `float`

#### preloadScene(name)

*(new in Anastacio)* `function`

Converts a scene ahead of time, at the end of this frame (shaders and textures included), without adding it. A later `addScene` or `replaceScene` of it only inserts the ready scene, without stalling. Call it while a loading screen is showing. Returns `False` if the scene doesn't exist.

**Returns:** `bool`

#### setAnimationRate(rate)

 `function`

Changes the animation update rate.

#### setNeedsParents(count)

 `function`

How many times per frame the parent hierarchy is updated (going from 3 to 1 saves CPU).

#### setObjectConvert(scene, object, convert, children=True)

*(new in Anastacio)* `function`

Changes the **Convert** option of an object in a scene not loaded yet. Returns how many objects changed.

**Returns:** `int`

#### setRenderRate(rate)

 `function`

Changes the render rate.

#### KX_GAME_SCREENSHOT

 `constant`

Game actuator mode: takes a screenshot.

#### KX_JOYSTICK_BUT_A

 `constant`

Gamepad A button.

#### KX_JOYSTICK_BUT_B

 `constant`

Gamepad B button.

#### KX_JOYSTICK_BUT_BACK

 `constant`

Gamepad Back/Select button.

#### KX_JOYSTICK_BUT_GUIDE

 `constant`

Gamepad Guide (center) button.

#### KX_JOYSTICK_BUT_LEFTSHOUDER

 `constant`

Gamepad left shoulder button (LB).

#### KX_JOYSTICK_BUT_LEFTSTICK

 `constant`

Gamepad left stick click.

#### KX_JOYSTICK_BUT_PADDOWN

 `constant`

Gamepad D-pad down.

#### KX_JOYSTICK_BUT_PADLEFT

 `constant`

Gamepad D-pad left.

#### KX_JOYSTICK_BUT_PADRIGHT

 `constant`

Gamepad D-pad right.

#### KX_JOYSTICK_BUT_PADUP

 `constant`

Gamepad D-pad up.

#### KX_JOYSTICK_BUT_RIGHTSHOUDER

 `constant`

Gamepad right shoulder button (RB).

#### KX_JOYSTICK_BUT_RIGHTSTICK

 `constant`

Gamepad right stick click.

#### KX_JOYSTICK_BUT_X

 `constant`

Gamepad X button.

#### KX_JOYSTICK_BUT_Y

 `constant`

Gamepad Y button.

#### KX_MOUSE_BUT_BUTTON6

 `constant`

Mouse button 6.

#### KX_MOUSE_BUT_BUTTON7

 `constant`

Mouse button 7.

#### KX_MOUSE_BUT_LEFTTHUMBMOUSE

 `constant`

Left side mouse button (thumb).

#### KX_MOUSE_BUT_RIGHTTHUMBMOUSE

 `constant`

Right side mouse button (thumb).

#### KX_MOVEMENT_ALL_AXIS

 `constant`

Movement sensor: watches all axes.

#### KX_MOVEMENT_AXIS_NEG_X

 `constant`

Movement sensor: -X axis.

#### KX_MOVEMENT_AXIS_NEG_Y

 `constant`

Movement sensor: -Y axis.

#### KX_MOVEMENT_AXIS_NEG_Z

 `constant`

Movement sensor: -Z axis.

#### KX_MOVEMENT_AXIS_POS_X

 `constant`

Movement sensor: +X axis.

#### KX_MOVEMENT_AXIS_POS_Y

 `constant`

Movement sensor: +Y axis.

#### KX_MOVEMENT_AXIS_POS_Z

 `constant`

Movement sensor: +Z axis.

#### RAS_2DFILTER_BLOOM

 `constant`

2D filter: Bloom.

#### RAS_2DFILTER_FXAA

 `constant`

2D filter: FXAA.

#### RAS_2DFILTER_LIGHTSCATTER

 `constant`

2D filter: light scattering (light rays).

#### RAS_2DFILTER_OUTLINE

 `constant`

2D filter: outline.

#### RAS_2DFILTER_SSAO

 `constant`

2D filter: ambient occlusion (SSAO).

#### RAS_2DFILTER_SSR

 `constant`

2D filter: screen-space reflections (SSR).

#### RAS_2DFILTER_TONEMAP

 `constant`

2D filter: tonemap.

---

## Range.network

> **See also:**
`Range.network.steam`, [`KX_GameObject`](#kx_gameobject), [`KX_Scene`](#kx_scene)

Anastacio Engine module `Range.network`. Also available as `bge.network`.

```python
# Open a room, or enter one by its address.
from Range import network

def connected(client_id):
    print("Connected as", client_id)

def refused(reason, detail):
    print("Refused:", reason, detail)

network.on_connect(connected)
network.on_reject(refused)

# On the host:
network.host(port=7777, max_players=4, room_name="Friends")

# On the client:
network.join("192.168.0.10:7777")
```

```python
# Sync the position and the life of an object. Call it before host() or join().
import Range
from Range import network

own = Range.logic.getCurrentController().owner
network.replicate(own, ["life"], transform=True, velocity=True)
```

```python
# Only the server creates the player of whoever joins.
from Range import network

def player_joined(client_id, name):
    print(name, "joined")
    network.spawn("Player", owner=client_id, position=(0.0, 0.0, 1.0))

network.on_player_join(player_joined)
```

```python
# Only the owner of the object reads the keyboard.
import Range
from Range import network

own = Range.logic.getCurrentController().owner

if network.is_owner(own):
    pressed = Range.logic.keyboard.inputs[Range.events.WKEY].active
    network.set_input(bytes([1 if pressed else 0]))
```

```python
# Lobby chat.
from Range import network

def message(client_id, text):
    print(client_id, text)

network.on_chat(message)
network.send_chat("Ready!")
network.set_ready(True)
```

```python
# Call a function on every player. Register it the same way on all of them.
from Range import network

@network.rpc(target="all")
def say_hello(text):
    print(text)

network.call("say_hello", "Hello!")
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### call(name, *args, obj=None)

*(new in Anastacio)* `function`

Calls a game RPC registered with `@rpc`. With `obj`, it becomes an object call (target `'owner'` and `owner_only` use its owner). `False` when refused locally (no session, wrong target...).

**Returns:** `bool`

#### change_scene(name)

*(new in Anastacio)* `function`

Server only: changes the session scene during the match. Clients load the same scene and receive everything again when it finishes loading.

#### despawn(obj)

*(new in Anastacio)* `function`

Server only: removes a replicated object on every player.

**Returns:** `bool`

#### disconnect()

*(new in Anastacio)* `function`

Leaves the session. On the host, closes the room for everyone.

#### discover_lan()

*(new in Anastacio)* `function`

Looks for rooms on the local network without stalling the game. Call about once a second; each item is a dict with the room data.

**Returns:** `list`

#### host(port=0, max_players=0, room_name='', password='', dedicated=False, websocket_port=-1, transport='enet')

*(new in Anastacio)* `function`

Opens a server (room). Zero or empty values use the scene Network panel. `dedicated=True` creates no local player; `websocket_port` accepts Web clients; `transport` is `'enet'` (LAN/IP) or `'steam'`.

**Returns:** `bool`

#### input(client)

*(new in Anastacio)* `function`

Server only: the client input applied this tick (0 = host), or `None`.

**Returns:** `bytes`

#### input_stats(client)

*(new in Anastacio)* `function`

Server only: how the client inputs arrived (late, repeated, missing...), or `None`.

**Returns:** `dict`

#### is_owner(obj)

*(new in Anastacio)* `function`

`True` if this player owns the object.

**Returns:** `bool`

#### join(address, password='', transport='enet')

*(new in Anastacio)* `function`

Joins a room. `address` accepts `'host'`, `'host:port'` or `'[ipv6]:port'`. The result arrives through `on_connect` or `on_reject`.

**Returns:** `bool`

#### net_id(obj)

*(new in Anastacio)* `function`

Network id of the object; 0 when it is not replicated.

**Returns:** `int`

#### on_chat(fn)

*(new in Anastacio)* `function`

Registers `fn(client_id, text)`, called for each lobby chat message.

#### on_connect(fn)

*(new in Anastacio)* `function`

Registers `fn(client_id)`, called on connecting (client) or when the room opens (host, with 0).

#### on_disconnect(fn)

*(new in Anastacio)* `function`

Registers `fn(reason, detail)`, called when leaving the session. `reason` is a `DISCONNECT_*` constant (1 to 5).

#### on_lobby(fn)

*(new in Anastacio)* `function`

Registers `fn()`, called when the host takes the session back to the lobby.

#### on_player_join(fn)

*(new in Anastacio)* `function`

Server only: registers `fn(client_id, name)`, called when a player joins.

#### on_player_leave(fn)

*(new in Anastacio)* `function`

Server only: registers `fn(client_id)`, called when a player leaves.

#### on_reject(fn)

*(new in Anastacio)* `function`

Registers `fn(reason, detail)`, called when the server refuses the connection. `reason` is a `REJECT_*` constant (1 to 6).

#### on_scene(fn)

*(new in Anastacio)* `function`

Registers `fn(scene_name)`, called when the session changed scene and it finished loading (server and clients).

#### on_start(fn)

*(new in Anastacio)* `function`

Registers `fn()`, called when the host starts the match.

#### owner(obj)

*(new in Anastacio)* `function`

Id of the client that owns the object, or `None` if it is not replicated.

**Returns:** `int`

#### predict(obj, fn)

*(new in Anastacio)* `function`

`fn(obj, input)` moves the object one tick with the owner's input (bytes): on the server every tick and on the owning client ahead of the server (prediction, corrected by snapshots). Register it on every player; `None` turns it off.

**Returns:** `bool`

#### prediction_stats(obj)

*(new in Anastacio)* `function`

Client only: prediction statistics for the object (corrections etc.), or `None`.

**Returns:** `dict`

#### raycast_past(origin, direction, distance=100.0, client=-1, ignore=None, max_rewind_ms=400)

*(new in Anastacio)* `function`

Server only: ray against the hitboxes as the client saw them (lag compensation, up to 1 s back); `client=-1` uses the current moment. Returns `(obj, point, distance)` or `None`.

**Returns:** `tuple`

#### replicate(obj, props, transform=True, velocity=False, angular_velocity=False, always_relevant=False, priority=1.0, quantize=None)

*(new in Anastacio)* `function`

Same as the **Replicate** checkbox: syncs the object over the network. Call it before `host()`/`join()`, in the same order on every player. `props` lists the game properties sent (may be empty); `quantize={name: (min, max, bits)}` sends Float properties with fewer bits. Returns the network id.

**Returns:** `int`

#### return_to_lobby()

*(new in Anastacio)* `function`

Host only: ends the match, clears the players' "ready" flag and notifies clients (`on_lobby`). Changing scenes is up to the game.

**Returns:** `bool`

#### send_chat(text)

*(new in Anastacio)* `function`

Sends a lobby chat message, up to 200 bytes in UTF-8. Received by `on_chat`.

**Returns:** `bool`

#### set_client_view(client, center=None, radius=None)

*(new in Anastacio)* `function`

Server only: relevance center (object or position) and radius of a client; objects outside the radius are not sent. Radius 0 sends everything. Without a center, uses the client's first object. All `None` goes back to the scene **Relevance Radius**.

#### set_hitbox(obj, radius, half_height=0.0)

*(new in Anastacio)* `function`

Server only: sphere (or capsule on local Z) kept with 1 s of history for `raycast_past()`. Radius 0 removes it.

**Returns:** `bool`

#### set_input(data)

*(new in Anastacio)* `function`

Local player input (bytes, up to 57), sent every tick until it changes, together with the moment remote objects were being drawn (lag compensation). Call it every frame.

#### set_owner(obj, client)

*(new in Anastacio)* `function`

Server only: gives the object to another owner (client id; 0 = host).

**Returns:** `bool`

#### set_ready(ready)

*(new in Anastacio)* `function`

In the lobby, marks this player as ready (`True`) or not (`False`).

#### set_simulation(latency_ms, jitter_ms, loss_percent)

*(new in Anastacio)* `function`

Simulates a bad network (delay, jitter and packet loss) on the next `host()`/`join()`. Useful for testing.

#### spawn(prototype, owner=0, position=None, orientation=None)

*(new in Anastacio)* `function`

Server only: creates a copy of the inactive object `prototype` (name) and replicates it to everyone. `owner` is the owning client id (0 = host).

**Returns:** `KX_GameObject`

#### start_game()

*(new in Anastacio)* `function`

Host only: starts the match. Returns `False` if some player is not ready. Clients receive `on_start`.

**Returns:** `bool`

#### view_time(client=0)

*(new in Anastacio)* `function`

On the client: the moment `(tick, alpha)` remote objects are drawn at. On the server: the moment the client sent with its last input. `None` without a session.

**Returns:** `tuple`

---

## Range.network.steam

> **See also:**
[`Range.network`](#rangenetwork)

Anastacio Engine module `Range.network.steam`. Also available as `bge.network.steam`.

```python
# Load Steam and see who is playing.
import Range
from Range.network import steam

dll = Range.logic.expandPath("//AnastacioSteam.dll")
steam.initialize(dll, 480)

info = steam.status()
if info["ready"]:
    print("Steam id:", info["steam_id"], steam.language())
```

```python
# Unlock an achievement.
from Range.network import steam

if not steam.achievement("FIRST_WIN"):
    steam.achievement("FIRST_WIN", unlock=True)
```

```python
# Handle lobby events and invites.
from Range.network import steam

for event in steam.poll_events():
    print(event["type"], event["name"], event["members"])
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### achievement(name, unlock=False)

*(new in Anastacio)* `function`

Checks a Steam achievement by its API name; with `unlock=True`, unlocks it.

**Returns:** `bool`

#### connection_routes()

*(new in Anastacio)* `function`

Route of each connected player: dicts with `peer`, `steam_id` and `route` (`'direct'`, `'relay'` or `'unknown'`). Empty without players.

**Returns:** `list`

#### force_relay(force)

*(new in Anastacio)* `function`

With `True`, turns off direct connection and forces Steam relay servers. Call after `initialize()` and before opening the session.

#### initialize(absolute_dll_path, app_id)

*(new in Anastacio)* `function`

Loads the optional `AnastacioSteam.dll` add-on (absolute path) with the game AppID (1 to 4294967295). Windows 64-bit only, with the game running; not available on the Web. The multiplayer component does this by itself when **enable_steam** is on.

#### language()

*(new in Anastacio)* `function`

Game language chosen in Steam (e.g. `'brazilian'`); empty without Steam.

**Returns:** `str`

#### poll_events()

*(new in Anastacio)* `function`

Takes the pending lobby and invite events. Each item is a dict with `type`, `lobby_id`, `host_id`, `port`, `members`, `capacity`, `name` and `detail`.

**Returns:** `list`

#### shutdown()

*(new in Anastacio)* `function`

Unloads Steam. Disconnect the session first. Closing the game also unloads it.

#### status()

*(new in Anastacio)* `function`

`{'loaded': bool, 'ready': bool, 'steam_id': int}`: whether the DLL loaded, whether Steam is ready, and the player SteamID.

**Returns:** `dict`

---

## Range.render

> **See also:**
[`KX_Camera`](#kx_camera), [`KX_2DFilterManager`](#kx_2dfiltermanager), [`Range.logic`](#rangelogic)

```python
# Show the mouse and use a lighter setup on weak machines.
import Range

Range.render.showMouse(True)
Range.render.setAnisotropicFiltering(4)
Range.render.setVsync(Range.render.VSYNC_ON)
```

```python
# Lower the resolution by itself when the frame rate falls.
import Range

Range.render.setDynamicResolution(True, targetFPS=60, minScale=50, maxScale=100, step=5)
print("Scale:", Range.render.getRenderScale())
```

```python
# Draw a red line from the object to the world origin.
import Range

own = Range.logic.getCurrentController().owner
Range.render.drawLine(own.worldPosition, (0.0, 0.0, 0.0), (1.0, 0.0, 0.0))
```

```python
# Change the window and save a screenshot.
import Range

Range.render.setWindowSize(1280, 720)
print(Range.render.getWindowWidth(), Range.render.getWindowHeight())
Range.render.makeScreenshot("//screenshot_#.png")
```

```python
# Control the general volume from an options menu.
import Range

Range.render.setMasterVolume(0.5)
print(Range.render.getMasterVolume())
```

### Intro

Example of using a `Range.types.SCA_MouseSensor`,
and two `Range.types.KX_ObjectActuator` to implement MouseLook:

> **Note:**
This can also be achieved with the `Range.types.KX_MouseActuator`.

```python

# To use a mouse movement sensor "Mouse" and a
# motion actuator to mouse look:
import Range

# scale sets the speed of motion
scale = 1.0, 0.5

co = Range.logic.getCurrentController()
obj = co.owner
mouse = co.sensors["Mouse"]
lmotion = co.actuators["LMove"]
wmotion = co.actuators["WMove"]

# Transform the mouse coordinates to see how far the mouse has moved.
def mousePos():
   x = (Range.render.getWindowWidth() / 2 - mouse.position[0]) * scale[0]
   y = (Range.render.getWindowHeight() / 2 - mouse.position[1]) * scale[1]
   return (x, y)

pos = mousePos()

# Set the amount of motion: X is applied in world coordinates...
wmotion.useLocalTorque = False
wmotion.torque = ((0.0, 0.0, pos[0]))

# ...Y is applied in local coordinates
lmotion.useLocalTorque = True
lmotion.torque = ((-pos[1], 0.0, 0.0))

# Activate both actuators
co.activate(lmotion)
co.activate(wmotion)

# Centre the mouse
Range.render.setMousePosition(int(Range.render.getWindowWidth() / 2), int(Range.render.getWindowHeight() / 2))
```

### Constants

#### KX_TEXFACE_MATERIAL

Deprecated.

Materials as defined by the texture face settings.

#### KX_BLENDER_MULTITEX_MATERIAL

Deprecated.

Materials approximating blender materials with multitexturing.

#### KX_BLENDER_GLSL_MATERIAL

Deprecated.

Materials approximating blender materials with GLSL.

Disables vsync
Enables vsync
Enables adaptive vsync if supported.
Adaptive vsync enables vsync if the framerate is above the monitors refresh rate.
Otherwise, vsync is diabled if the framerate is too low.

#### LEFT_EYE

Left eye being used during stereoscopic rendering.

#### RIGHT_EYE

Right eye being used during stereoscopic rendering.

### HDR

#### HDR_NONE

Use 8 bit per channel image format.

#### HDR_HALF_FLOAT

Use 16 bit float per channel image format.

#### HDR_FULL_FLOAT

Use 32 bit float per channel image format.

### Functions

#### getWindowWidth()

Gets the width of the window (in pixels)

**Return type:** integer

#### getWindowHeight()

Gets the height of the window (in pixels)

**Return type:** integer

#### setWindowSize(width, height)

Set the width and height of the window (in pixels). This also works for fullscreen applications.

> **Note:**
Only works in the standalone player, not the Blender-embedded player.

- **`width`**: width in pixels
  - type: integer
- **`height`**: height in pixels
  - type: integer

#### setFullScreen(enable)

Set whether or not the window should be fullscreen.

> **Note:**
Only works in the standalone player, not the Blender-embedded player.

- **`enable`**: `True` to set full screen, `False` to set windowed.
  - type: bool

#### getFullScreen()

Returns whether or not the window is fullscreen.

> **Note:**
Only works in the standalone player, not the Blender-embedded player; there it always returns False.

**Return type:** bool

#### getDisplayDimensions()

Get the display dimensions, in pixels, of the display (e.g., the
monitor). Can return the size of the entire view, so the
combination of all monitors; for example, `(3840, 1080)` for two
side-by-side 1080p monitors.

**Return type:** tuple (width, height)

#### makeScreenshot(filename)

Writes an image file with the displayed image at the frame end.

The image is written to *'filename'*.
The path may be absolute (eg. `/home/foo/image`) or relative when started with
`//` (eg. `//image`). Note that absolute paths are not portable between platforms.
If the filename contains a `#`,
it will be replaced by an incremental index so that screenshots can be taken multiple
times without overwriting the previous ones (eg. `image-#`).

Settings for the image are taken from the render settings (file format and respective settings,
gamma and colospace conversion, etc).
The image resolution matches the framebuffer, meaning, the window size and aspect ratio.
When running from the standalone player, instead of the embedded player, only PNG files are supported.
Additional color conversions are also not supported.

- **`filename`**: path and name of the file to write
  - type: string

#### enableVisibility(visible)

Deprecated; doesn't do anything.

#### showMouse(visible)

Enables or disables the operating system mouse cursor.

- **`visible`**: 
  - type: boolean

#### setMousePosition(x, y)

Sets the mouse cursor position.

- **`x`**: X-coordinate in screen pixel coordinates.
  - type: integer
- **`y`**: Y-coordinate in screen pixel coordinates.
  - type: integer

#### setBackgroundColor(rgba)

Deprecated and no longer functional. Use `Range.types.KX_WorldInfo.horizonColor` or `Range.types.KX_WorldInfo.zenithColor` instead.

#### setEyeSeparation(eyesep)

Sets the eye separation for stereo mode. Usually Focal Length/30 provides a confortable value.

- **`eyesep`**: The distance between the left and right eye.
  - type: float

#### getEyeSeparation()

Gets the current eye separation for stereo mode.

**Return type:** float

#### setFocalLength(focallength)

Sets the focal length for stereo mode. It uses the current camera focal length as initial value.

- **`focallength`**: The focal length.
  - type: float

#### getFocalLength()

Gets the current focal length for stereo mode.

**Return type:** float

#### getStereoEye()

Gets the current stereoscopy eye being rendered.
This function is mainly used in a `Range.types.KX_Scene.pre_draw` callback
function to customize the camera projection matrices for each
stereoscopic eye.

**Return type:** LEFT_EYE, RIGHT_EYE

#### setMaterialMode(mode)

Deprecated and no longer functional.

Set the material mode to use for OpenGL rendering.

- **`mode`**: material mode
  - type: KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

> **Note:**
Changes will only affect newly created scenes.

#### getMaterialMode(mode)

Deprecated and no longer functional.

Get the material mode to use for OpenGL rendering.

**Return type:** KX_TEXFACE_MATERIAL, KX_BLENDER_MULTITEX_MATERIAL, KX_BLENDER_GLSL_MATERIAL

#### setGLSLMaterialSetting(setting, enable)

Enables or disables a GLSL material setting.

- **`setting`**: 
  - type: string (lights, shaders, shadows, ramps, nodes, extra_textures)
- **`enable`**: 
  - type: boolean

#### getGLSLMaterialSetting(setting)

Get the state of a GLSL material setting.

- **`setting`**: 
  - type: string (lights, shaders, shadows, ramps, nodes, extra_textures)

**Return type:** boolean

#### setAnisotropicFiltering(level)

Set the anisotropic filtering level for textures.

- **`level`**: The new anisotropic filtering level to use
  - type: integer (must be one of 1, 2, 4, 8, 16)

> **Note:**
clamped to the maximum of the graphics card. The exported game starts with 8.

#### getAnisotropicFiltering()

Get the anisotropic filtering level used for textures.

**Return type:** integer (one of 1, 2, 4, 8, 16)

#### setAntiAliasing(level)

Set the anti aliasing level.

- **`level`**: The new anti aliasing level to use
  - type: integer (must be one of 0, 2, 4, 8, 16)

> **Note:**
Changing this value cause all off screens to be recreated, which can be slow.

#### getAntiAliasing()

Get the anti aliasing level setting.

**Return type:** integer (one of 0, 2, 4, 8, 16)

#### setMipmapping(value)

Change how to use mipmapping.

  - type: RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

> **Note:**
Switching between NEAREST and LINEAR or turning them off only changes the filters.
With mipmaps off textures are displayed unfiltered (nearest), useful for pixel art.

#### getMipmapping()

Get the current mipmapping setting.

**Return type:** RAS_MIPMAP_NONE, RAS_MIPMAP_NEAREST, RAS_MIPMAP_LINEAR

#### setTextureQuality(level)

Texture quality of a graphics menu: keep only the high resolution texture in the project and
drop its largest mipmap levels when it is sent to the graphics card.

* `0`: full size
* `1`: half size (1/4 of the video memory)
* `2`: quarter size (1/16 of the video memory)

Textures never go below 256 pixels on their larger side, and textures without mipmaps
(or with mipmapping off) keep their size. DDS files skip the levels stored in the file.

- **`level`**: 0, 1 or 2
  - type: integer

> **Note:**
menu, not every frame. In the editor the value is restored when the game ends.

#### getTextureQuality()

**Returns:** the current texture quality (0 full, 1 half, 2 quarter).

**Return type:** integer

#### drawLine(fromVec,toVec,color)

Draw a line in the 3D scene.

- **`fromVec`**: the origin of the line
  - type: list [x, y, z]
- **`toVec`**: the end of the line
  - type: list [x, y, z]
- **`color`**: the color of the line
  - type: list [r, g, b, a]

#### enableMotionBlur(factor)

Enable the motion blur effect.

- **`factor`**: the ammount of motion blur to display.
  - type: float [0.0 - 1.0]

#### disableMotionBlur()

Disable the motion blur effect.

#### showFramerate(enable)

Show or hide the framerate.

- **`enable`**: 
  - type: boolean

#### showProfile(enable)

Show or hide the profile.

- **`enable`**: 
  - type: boolean

#### showProperties(enable)

Show or hide the debug properties.

- **`enable`**: 
  - type: boolean

#### autoDebugList(enable)

Enable or disable auto adding debug properties to the debug list.

- **`enable`**: 
  - type: boolean

#### clearDebugList()

Clears the debug property list.

#### setVsync(value)

Set the vsync value

- **`value`**: One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE
  - type: integer

#### getVsync()

Get the current vsync value

**Return type:** One of VSYNC_OFF, VSYNC_ON, VSYNC_ADAPTIVE

#### setDynamicResolution(enabled, targetFPS=60, minScale=50, maxScale=100, step=5)

Runtime version of the scene's Dynamic Resolution settings. The 3D scene is rendered at a
scale of the window size and stretched to the screen; the window itself does not change.
With dynamic resolution the scale goes down by `step` when the GPU time of a frame is above
the target and back up when there is time left. `minScale == maxScale` gives a fixed render
scale. Paused while "Show Render Queries" is on (both use a GPU timer query).

- **`enabled`**: False renders at 100%.
  - type: boolean
- **`targetFPS`**: Frame rate the GPU time is compared to.
  - type: integer
- **`minScale`**: Lowest scale, in percent (25-100).
  - type: integer
- **`maxScale`**: Highest scale, in percent (25-100).
  - type: integer
- **`step`**: Scale change per adjustment, in percent (1-25).
  - type: integer

#### getRenderScale()

Current render scale, 1.0 = full resolution.

**Return type:** float

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### getMasterVolume()

 `function`

Overall game sound volume, from 0 to 1. See `setMasterVolume()`.

**Returns:** `volume`

#### getStereoMode()

*(new in Anastacio)* `function`

get the stereo mode

#### getVRChromaticAberration()

*(new in Anastacio)* `function`

get the VR lens chromatic aberration correction

#### getVRLensStrength()

*(new in Anastacio)* `function`

get the VR lens distortion strength

#### setCustomMouse(path)

 `function`

Uses the image at `path` as the mouse cursor.

#### setMasterVolume(volume)

 `function`

-- volume in [0, 1], applies to the engine's actual audio device

#### setStereoMode()

*(new in Anastacio)* `function`

set the stereo mode (STEREO_* constants)

#### setVRChromaticAberration()

*(new in Anastacio)* `function`

set the VR lens chromatic aberration correction (0..0.1, default 0.01)

#### setVRLensStrength()

*(new in Anastacio)* `function`

set the VR lens distortion strength (0..1, default 0.3)

#### showDebugPhysics(enabled)

 `function`

Shows or hides the physics collision shapes.

#### RAS_MIPMAP_LINEAR

 `constant`

Linear mipmap (smoother).

#### RAS_MIPMAP_NEAREST

 `constant`

Nearest mipmap.

#### RAS_MIPMAP_NONE

 `constant`

No mipmap.

#### STEREO_ABOVEBELOW

 `constant`

Stereo: one image above the other.

#### STEREO_ANAGLYPH

 `constant`

Stereo: anaglyph (red/cyan glasses).

#### STEREO_INTERLACED

 `constant`

Stereo: interlaced lines.

#### STEREO_NOSTEREO

 `constant`

No stereo.

#### STEREO_SIDEBYSIDE

 `constant`

Stereo: side by side.

#### VSYNC_ADAPTIVE

 `constant`

Adaptive VSync: syncs, but doesn't stall when FPS drops.

#### VSYNC_OFF

 `constant`

VSync off.

#### VSYNC_ON

 `constant`

VSync on.

---

## Range.texture

> **See also:**
[`Texture`](#texture), [`KX_BlenderMaterial`](#kx_blendermaterial), [`BL_Texture`](#bl_texture)

```python
# Show a video on the material of the object.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

if "video" not in own:
    matID = texture.materialID(own, "MAscreen")
    tex = texture.Texture(own, matID)
    tex.source = texture.VideoFFmpeg(Range.logic.expandPath("//movie.mp4"))
    tex.source.play()
    own["video"] = tex

own["video"].refresh(True)
```

```python
# Swap the image of a material while the game runs.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageFFmpeg(Range.logic.expandPath("//poster.png"))
tex.refresh(False)
own["poster"] = tex
```

```python
# Make a mirror image with another camera.
import Range
from Range import texture

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageRender(scene, scene.objects["SecurityCamera"])
own["monitor"] = tex
own["monitor"].refresh(True)
```

### Introduction

The `Range.texture` module allows you to manipulate textures during the game.
Several sources for texture are possible: video files, image files, video capture,
memory buffer, camera render or a mix of that.
The video and image files can be loaded from the Internet using a URL instead of a file name.
In addition, you can apply filters on the images before sending them to the GPU,
allowing video effect: blue screen, color band, gray, normal map.
`Range.texture` uses FFmpeg to load images and videos.
All the formats and codecs that FFmpeg supports are supported by `Range.texture`,
including but not limited to:

* AVI
* Ogg
* Xvid
* Theora
* dv1394 camera
* video4linux capture card (this includes many webcams)
* videoForWindows capture card (this includes many webcams)
* JPG

### How it works

The principle is simple: first you identify a texture on an existing object using the
`materialID` function, then you create a new texture with dynamic content
and swap the two textures in the GPU.

The game engine is not aware of the substitution and continues to display the object as always,
except that you are now in control of the texture.

When the texture object is deleted, the new texture is deleted and the old texture restored.

### Game Preparation

Before you can use the `Range.texture` module,
you must have objects with textures applied appropriately.

Imagine you want to have a television showing live broadcast programs in the game.
You will create a television object and UV-apply a different texture at the place of the screen,
for example `tv.png`. What this texture looks like is not important;
probably you want to make it dark gray to simulate power-off state.
When the television must be turned on, you create a dynamic texture from a video capture card
and use it instead of `tv.png`: the TV screen will come to life.

You have two ways to define textures that `Range.texture` can grab:

- Simple UV texture.
- Blender material with image texture channel.

Because `Range.texture` works at texture level, it is compatible with all
the Blender Game Engine's fancy texturing features: GLSL, multi-texture, custom shaders, etc.

### Examples

### Video classes

### Class `VideoFFmpeg(file, capture=-1, rate=25.0, width=0, height=0)`

FFmpeg video source, used for video files, video captures, or video streams.

- **`file`**: Path to the video to load; if capture >= 0 on Windows, this parameter will not be used.
  - type: str
- **`capture`**: Capture device number; if >= 0, the corresponding webcam will be used. (optional)
  - type: int
- **`rate`**: Capture rate. (optional, used only if capture >= 0)
  - type: float
- **`width`**: Capture width. (optional, used only if capture >= 0)
  - type: int
- **`height`**: Capture height. (optional, used only if capture >= 0)
  - type: int

#### status

Video status. (readonly)

**Type:** int

**Value:** `see `FFmpeg Video and Image Status`_.`

#### range

The start and stop time of the video playback, expressed in seconds from beginning.
By default the entire video.

**Type:** sequence of two floats

#### repeat

Number of times to replay the video, -1 for infinite repeat.

**Type:** int

#### framerate

Relative frame rate, <1.0 for slow, >1.0 for fast.

**Type:** float

#### valid

Tells if an image is available. (readonly)

**Type:** bool

#### image

Image data. (readonly)

**Type:** `Buffer` or None

#### size

Image size. (readonly)

**Type:** tuple of two ints

#### scale

Set to True to activate fast nearest neighbor scaling algorithm.
Texture width and height must be a power of 2.
If the video picture size is not a power of 2, rescaling is required.
By default `Range.texture` uses the precise but slow `gluScaleImage()` function.
Best is to rescale the video offline so that no scaling is necessary at runtime!

**Type:** bool

#### flip

If True the imaged will be flipped vertically.
FFmpeg always delivers the image upside down, so this attribute is set to True by default.

**Type:** bool

#### filter

An additional filter that is applied on the video before sending it to the GPU.

**Type:** one of: * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### preseek

Number of frames of preseek.

**Type:** int

#### deinterlace

Deinterlace image.

**Type:** bool

#### play()

Play (restart) video.

**Returns:** Whether the video was ready or stopped.

**Return type:** bool

#### pause()

Pause video.

**Returns:** Whether the video was playing.

**Return type:** bool

#### stop()

Stop video (play will replay it from start).

**Returns:** Whether the video was playing.

**Return type:** bool

#### refresh(buffer=None, format="RGBA", timestamp=-1.0)

Refresh video - get its status and optionally copy the frame to an external buffer.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str
- **`timestamp`**: An optional timestamp (in seconds from the start of the movie) of the frame to be copied to the buffer.
  - type: float

**Returns:** see `FFmpeg Video and Image Status`_.

**Return type:** int

### Image classes

### Class `ImageFFmpeg(file)`

FFmpeg image source, used for image files and web based images.

- **`file`**: Path to the image to load.
  - type: str

#### status

Image status. (readonly)

**Type:** int

**Value:** `see `FFmpeg Video and Image Status`_.`

#### valid

Tells if an image is available. (readonly)

**Type:** bool

#### image

Image data. (readonly)

**Type:** `Buffer` or None

#### size

Image size. (readonly)

**Type:** tuple of two ints

#### scale

Fast scale of image (near neighbour).

**Type:** bool

#### flip

Flip image vertically.

**Type:** bool

#### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### refresh(buffer=None, format="RGBA")

Refresh image, get its status and optionally copy the frame to an external buffer.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

**Returns:** see `FFmpeg Video and Image Status`_.

**Return type:** int

#### reload(newname=None)

Reload image, i.e. reopen it.

- **`newname`**: Path to a new image. (optional)
  - type: str

### Class `ImageBuff(width, height, color=0, scale=False)`

Image from application memory.
For computer generated images, drawing applications.

- **`width`**: Width of the image.
  - type: int
- **`height`**: Height of the image.
  - type: int
- **`color`**: Value to initialize RGB channels with. The initialized buffer will have all pixels set to (color, color, color, 255). (optional)
  - type: int in [0, 255]
- **`scale`**: Image uses scaling. (optional)
  - type: bool

#### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Flip image vertically.

**Type:** bool

#### image

Image data. (readonly)

**Type:** `Buffer` or None

#### load(imageBuffer, width, height)

Load image from buffer.

- **`imageBuffer`**: Buffer to load the image from.
  - type: `Buffer` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Width of the image to load.
  - type: int
- **`height`**: Height of the image to load.
  - type: int

#### plot(imageBuffer, width, height, positionX, positionY, mode=IMB_BLEND_COPY)

Update image buffer.

- **`imageBuffer`**: Buffer to load the new data from.
  - type: `Buffer`, `ImageBuff` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Width of the data to load.
  - type: int
- **`height`**: Height of the data to load.
  - type: int
- **`positionX`**: Left boundary of the region to be drawn on.
  - type: int
- **`positionY`**: Upper boundary of the region to be drawn on.
  - type: int
- **`mode`**: Drawing mode, see `Image Blending Modes`_.
  - type: int

#### scale

Fast scale of image (near neighbour).

**Type:** bool

#### size

Image size. (readonly)

**Type:** tuple of two ints

#### valid

Tells if an image is available. (readonly)

**Type:** bool

### Class `ImageMirror(scene, observer, mirror, material=0, width, height, samples, hdr)`

Image source from mirror.

- **`scene`**: Scene in which the image has to be taken.
  - type: `KX_Scene`
- **`observer`**: Reference object for the mirror (the object from which the mirror has to be looked at, for example a camera).
  - type: `KX_GameObject`
- **`mirror`**: Object holding the mirror.
  - type: `KX_GameObject`
- **`material`**: ID of the mirror's material to be used for mirroring. (optional)
  - type: int
- **`width`**: Off-screen render buffer width (optional).
  - type: integer
- **`height`**: Off-screen render buffer height (optional).
  - type: integer
- **`samples`**: Off-screen render buffer samples (optional).
  - type: integer
- **`hdr`**: Off-screen image format (optional).
  - type: One of `these constants`

#### alpha

Use alpha in texture.

**Type:** bool

#### horizon

Horizon color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

#### zenith

Zenith color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

#### background

**Type:** float list [r, g, b, a] in [0.0, 1.0]

Deprecated use :py`Range.texture.ImageMirror.horizon` or :py`Range.texture.ImageMirror.zenith` instead.

#### updateShadow

Choose to force shadow buffer update if there is a gap beetween image rendered and shadows.

**Type:** bool

#### colorBindCode

Off-screen color texture bind code.

**Type:** integer

#### capsize

Size of render area.

**Type:** sequence of two ints

#### clip

Clipping distance.

**Type:** float in [0.01, 5000.0]

#### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Flip image vertically.

**Type:** bool

#### image

Image data. (readonly)

**Type:** `Buffer` or None

#### refresh(buffer=None, format="RGBA")

Refresh image - render and copy the image to an external buffer (optional)
then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is rendered and copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

#### scale

Fast scale of image (near neighbour).

**Type:** bool

#### size

Image size (readonly).

**Type:** tuple of two ints

#### valid

Tells if an image is available. (readonly)

**Type:** bool

#### whole

Use whole viewport to render.

**Type:** bool

### Class `ImageMix`

Image mixer used to mix multiple image sources together.

#### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Flip image vertically.

**Type:** bool

#### getSource(id)

Get image source.

- **`id`**: Identifier of the source to get.
  - type: str

**Returns:** Image source.

**Return type:** one of... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

#### getWeight(id)

Get image source weight.

- **`id`**: Identifier of the source.
  - type: str

**Returns:** Weight of the source.

**Return type:** int

#### image

Image data. (readonly)

**Type:** `Buffer` or None

#### refresh(buffer=None, format="RGBA")

Refresh image - calculate and copy the image to an external buffer (optional)
then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is calculated and copied to the buffer, which must be big enough or an exception is thrown.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

#### scale

Fast scale of image (near neighbour).

**Type:** bool

#### size

Image size. (readonly)

**Type:** tuple of two ints

#### setSource(id, image)

Set image source - all sources must have the same size.

- **`id`**: Identifier of the source to set.
  - type: str
- **`image`**: Image source of type... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

#### setWeight(id, weight)

Set image source weight - the sum of the weights should be 256 to get full color intensity in the output.

- **`id`**: Identifier of the source.
  - type: str
- **`weight`**: Weight of the source.
  - type: int

#### valid

Tells if an image is available. (readonly)

**Type:** bool

### Class `ImageRender(scene, camera, width, height, samples, hdr)`

Image source from a render of a non active camera.
The render is done on a custom framebuffer object if fbo is specified,
otherwise on the default framebuffer.

- **`scene`**: Scene in which the image has to be taken.
  - type: `KX_Scene`
- **`camera`**: Camera from which the image has to be taken.
  - type: `KX_Camera`
- **`width`**: Off-screen render buffer width (optional).
  - type: integer
- **`height`**: Off-screen render buffer height (optional).
  - type: integer
- **`samples`**: Off-screen render buffer samples (optional).
  - type: integer
- **`hdr`**: Off-screen image format (optional).
  - type: One of `these constants`

#### alpha

Use alpha in texture.

**Type:** bool

#### horizon

Horizon color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

#### zenith

Zenith color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

#### background

Background color.

**Type:** float list [r, g, b, a] in [0.0, 1.0]

Deprecated use :py`Range.texture.ImageRender.horizon` or :py`Range.texture.ImageRender.zenith` instead.

#### updateShadow

Choose to force shadow buffer update if there is a gap beetween image rendered and shadows.

**Type:** bool

#### colorBindCode

Off-screen color texture bind code.

**Type:** integer

#### capsize

Size of render area.

**Type:** sequence of two ints

#### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Flip image vertically.

**Type:** bool

#### image

Image data. (readonly)

**Type:** `Buffer` or None

#### scale

Fast scale of image (near neighbour).

**Type:** bool

#### size

Image size. (readonly)

**Type:** tuple of two ints

#### valid

Tells if an image is available. (readonly)

**Type:** bool

#### whole

Use whole viewport to render.

**Type:** bool

#### depth

Use depth component of render as array of float - not suitable for texture source,
should only be used with Range.texture.imageToArray(mode='F').

**Type:** bool

#### zbuff

Use depth component of render as grayscale color - suitable for texture source.

**Type:** bool

#### render()

Render the scene but do not extract the pixels yet.
The function returns as soon as the render commands have been send to the GPU.
The render will proceed asynchronously in the GPU while the host can perform other tasks.
To complete the render, you can either call `refresh`
directly of refresh the texture of which this object is the source.
This method is useful to implement asynchronous render for optimal performance: call render()
on frame n and refresh() on frame n+1 to give as much as time as possible to the GPU
to render the frame while the game engine can perform other tasks.

**Returns:** True if the render was initiated, False if the render cannot be performed (e.g. the camera is active)

**Return type:** bool

#### refresh()

#### refresh(buffer, format="RGBA")

Refresh video - render and optionally copy the image to an external buffer then invalidate its current content.
The render may have been started earlier with the `render` method,
in which case this function simply waits for the render operations to complete.
When called without argument, the pixels are not extracted but the render is guaranteed
to be completed when the function returns.
This only makes sense with offscreen render on texture target (see `offScreenCreate`).

- **`buffer`**: An object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` and no filter is set.
  - type: any buffer type of sufficient size
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

**Returns:** True if the render is complete, False if the render cannot be performed (e.g. the camera is active)

**Return type:** bool

### Class `ImageViewport`

Image source from viewport rendered by the active camera.
To render from a non active camera see `ImageRender`.

#### alpha

Use alpha in texture.

**Type:** bool

#### capsize

Size of viewport area being captured.

**Type:** sequence of two ints

#### filter

Pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

#### flip

Flip image vertically.

**Type:** bool

#### image

Image data. (readonly)

**Type:** `Buffer` or None

#### position

Upper left corner of the captured area.

**Type:** sequence of two ints

#### refresh(buffer=None, format="RGBA")

Refresh video - copy the viewport to an external buffer (optional) then invalidate its current content.

- **`buffer`**: An optional object that implements the buffer protocol. If specified, the image is copied to the buffer, which must be big enough or an exception is thrown. The transfer to the buffer is optimal if no processing of the image is needed. This is the case if `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` and no filter is set.
  - type: any buffer type
- **`format`**: An optional image format specifier for the image that will be copied to the buffer. Only valid values are "RGBA" or "BGRA"
  - type: str

#### scale

Fast scale of image (near neighbour).

**Type:** bool

#### size

Image size. (readonly)

**Type:** tuple of two ints

#### valid

Tells if an image is available. (readonly)

**Type:** bool

#### whole

Use whole viewport to capture.

**Type:** bool

#### depth

Use depth component of viewport as array of float - not suitable for texture source,
should only be used with `Range.texture.imageToArray(mode='F')`.

**Type:** bool

#### zbuff

Use depth component of viewport as grayscale color - suitable for texture source.

**Type:** bool

### Class `VideoDeckLink(format, capture=0)`

Image source from an external video stream captured with a DeckLink video card from
Black Magic Design.
Before this source can be used, a DeckLink hardware device must be installed, it can be a PCIe card
or a USB device, and the 'Desktop Video' software package (version 10.4 or above must be installed)
on the host as described in the DeckLink documentation.
If in addition you have a recent nVideo Quadro card, you can benefit from the 'GPUDirect' technology
to push the captured video frame very efficiently to the GPU. For this you need to install the
'DeckLink SDK' version 10.4 or above and copy the 'dvp.dll' runtime library to Blender's
installation directory or to any other place where Blender can load a DLL from.

- **`format`**: string describing the video format to be captured.
  - type: str
- **`capture`**: Card number from which the input video must be captured.
  - type: int
The format argument must be written as `<displayMode>/<pixelFormat>[/3D][:<cacheSize>]`
where `<displayMode>` describes the frame size and rate and <pixelFormat> the encoding of the pixels.
The optional `/3D` suffix is to be used if the video stream is stereo with a left and right eye feed.
The optional `:<cacheSize>` suffix determines the number of the video frames kept in cache, by default 8.
Some DeckLink cards won't work below a certain cache size. The default value 8 should be sufficient for all cards.
You may try to reduce the cache size to reduce the memory footprint. For example the The 4K Extreme is known
to work with 3 frames only, the Extreme 2 needs 4 frames and the Intensity Shuttle needs 6 frames, etc.
Reducing the cache size may be useful when Decklink is used in conjunction with GPUDirect:
all frames must be locked in memory in that case and that puts a lot of pressure on memory.
If you reduce the cache size too much, you'll get no error but no video feed either.

The valid `<displayMode>` values are copied from the `BMDDisplayMode` enum in the DeckLink API
without the 'bmdMode' prefix. In case a mode that is not in this list is added in a later version
of the SDK, it is also possible to specify the 4 letters of the internal code for that mode.
You will find the internal code in the `DeckLinkAPIModes.h` file that is part of the SDK.
Here is for reference the full list of supported display modes with their equivalent internal code:

Internal Codes
- NTSC 'ntsc'
- NTSC2398 	'nt23'
- PAL		'pal '
- NTSCp		'ntsp'
- PALp		'palp'
HD 1080 Modes
- HD1080p2398	'23ps'
- HD1080p24	'24ps'
- HD1080p25	'Hp25'
- HD1080p2997	'Hp29'
- HD1080p30	'Hp30'
- HD1080i50	'Hi50'
- HD1080i5994	'Hi59'
- HD1080i6000	'Hi60'
- HD1080p50	'Hp50'
- HD1080p5994	'Hp59'
- HD1080p6000	'Hp60'
HD 720 Modes
- HD720p50	'hp50'
- HD720p5994	'hp59'
- HD720p60	'hp60'
2k Modes
- 2k2398	'2k23'
- 2k24		'2k24'
- 2k25		'2k25'
4k Modes
- 4K2160p2398	'4k23'
- 4K2160p24	'4k24'
- 4K2160p25	'4k25'
- 4K2160p2997	'4k29'
- 4K2160p30	'4k30'
- 4K2160p50	'4k50'
- 4K2160p5994	'4k59'
- 4K2160p60	'4k60'

Most of names are self explanatory. If necessary refer to the DeckLink API documentation for more information.

Similarly, <pixelFormat> is copied from the BMDPixelFormat enum.

Here is for reference the full list of supported pixel format and their equivalent internal code:

Pixel Formats
- 8BitYUV	'2vuy'
- 10BitYUV	'v210'
- 8BitARGB	* no equivalent code *
- 8BitBGRA	'BGRA'
- 10BitRGB	'r210'
- 12BitRGB	'R12B'
- 12BitRGBLE	'R12L'
- 10BitRGBXLE	'R10l'
- 10BitRGBX	'R10b'

Refer to the DeckLink SDK documentation for a full description of these pixel format.
It is important to understand them as the decoding of the pixels is NOT done in VideoTexture
for performance reason. Instead a specific shader must be used to decode the pixel in the GPU.
Only the '8BitARGB', '8BitBGRA' and '10BitRGBXLE' pixel formats are mapped directly to OpenGL RGB float textures.
The '8BitYUV' and '10BitYUV' pixel formats are mapped to openGL RGB float texture but require a shader to decode.
The other pixel formats are sent as a `GL_RED_INTEGER` texture (i.e. a texture with only the
red channel coded as an unsigned 32 bit integer) and are not recommended for use.

Example: `HD1080p24/10BitYUV/3D:4` is equivalent to `24ps/v210/3D:4`
and represents a full HD stereo feed at 24 frame per second and 4 frames cache size.

Although video format auto detection is possible with certain DeckLink devices, the corresponding
API is NOT implemented in the BGE. Therefore it is important to specify the format string that
matches exactly the video feed. If the format is wrong, no frame will be captured.
It should be noted that the pixel format that you need to specify is not necessarily the actual
format in the video feed. For example, the 4K Extreme card delivers 8bit RGBs pixels in the
'10BitRGBXLE' format. Use the 'Media Express' application included in 'Desktop Video' to discover
which pixel format works for a particular video stream.

#### status

Status of the capture: 1=ready to use, 2=capturing, 3=stopped

**Type:** int

#### framerate

Capture frame rate as computed from the video format.

**Type:** float

#### valid

Tells if the image attribute can be used to retrieve the image.
Always False in this implementation (the image is not available at python level)

**Type:** bool

#### image

The image data. Always None in this implementation.

**Type:** `Buffer` or None

#### size

The size of the frame in pixel.
Stereo frames have double the height of the video frame, i.e. 3D is delivered to the GPU
as a single image in top-bottom order, left eye on top.

**Type:** (int,int)

#### scale

Not used in this object.

**Type:** bool

#### flip

Not used in this object.

**Type:** bool

#### filter

Not used in this object.

#### play()

Kick-off the capture after creation of the object.

**Returns:** True if the capture could be started, False otherwise.

**Return type:** bool

#### pause()

Temporary stops the capture. Use play() to restart it.

**Returns:** True if the capture could be paused, False otherwise.

**Return type:** bool

#### stop()

Stops the capture.

**Returns:** True if the capture could be stopped, False otherwise.

**Return type:** bool

### Texture classes

### Class `Texture(gameObj, materialID=0, textureID=0, textureObj=None)`

Class that creates the `Texture` object that loads the dynamic texture on the GPU.

- **`gameObj`**: Game object to be created a video texture on.
  - type: `KX_GameObject`
- **`materialID`**: Material ID default, 0 is the first material. (optional)
  - type: int
- **`textureID`**: Texture index in case of multi-texture channel, 0 = first channel by default. In case of UV texture, this parameter should always be 0. (optional)
  - type: int
- **`textureObj`**: Reference to another `Texture` object with shared bindId which he user might want to reuse the texture. If this argument is used, you should not create any source on this texture and there is no need to refresh it either: the other `Texture` object will provide the texture for both materials/textures.(optional)
  - type: `Texture`

#### bindId

OpenGL Bind Name. (readonly)

**Type:** int

#### close()

Close dynamic texture and restore original.

#### mipmap

Mipmap texture.

**Type:** bool

#### refresh(refresh_source, timestamp=-1.0)

Refresh texture from source.

- **`refresh_source`**: Whether to also refresh the image source of the texture.
  - type: bool
- **`timestamp`**: If the texture controls a VideoFFmpeg object: timestamp (in seconds from the start of the movie) of the frame to be loaded; this can be used for video-sound synchonization by passing `time` to it. (optional)
  - type: float

#### source

Source of texture.

**Type:** one of... * `VideoFFmpeg` * `VideoDeckLink` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

### Class `DeckLink(cardIdx=0, format="")`

Certain DeckLink devices can be used to playback video: the host sends video frames regularly
for immediate or scheduled playback. The video feed is outputted on HDMI or SDI interfaces.
This class supports the immediate playback mode: it has a source attribute that is assigned
one of the source object in the Range.texture module. Refreshing the DeckLink object causes
the image source to be computed and sent to the DeckLink device for immediate transmission
on the output interfaces.  Keying is supported: it allows to composite the frame with an
input video feed that transits through the DeckLink card.

- **`cardIdx`**: Number of the card to be used for output (0=first card). It should be noted that DeckLink devices are usually half duplex: they can either be used for capture or playback but not both at the same time.
  - type: int
- **`format`**: String representing the display mode of the output feed.
  - type: str
The default value of the format argument is reserved for auto detection but it is currently
not supported (it will generate a runtime error) and thus the video format must be explicitly
specified. If keying is the goal (see keying attributes), the format must match exactly the
input video feed, otherwise it can be any format supported by the device (there will be a
runtime error if not).
The format of the string is `<displayMode>[/3D]`.

Refer to `VideoDeckLink` to get the list of acceptable `<displayMode>`.
The optional `/3D` suffix is used to create a stereo 3D feed.
In that case the 'right' attribute must also be set to specify the image source for the right eye.

Note: The pixel format is not specified here because it is always BGRA. The alpha channel is
used in keying to mix the source with the input video feed, otherwise it is not used.
If a conversion is needed to match the native video format, it is done inside the DeckLink driver
or device.

#### source

This attribute must be set to one of the image sources. If the image size does not fit exactly
the frame size, the extend attribute determines what to do.

For best performance, the source image should match exactly the size of the output frame.
A further optimization is achieved if the image source object is ImageViewport or ImageRender
set for whole viewport, flip disabled and no filter: the GL frame buffer is copied directly
to the image buffer and directly from there to the DeckLink card (hence no buffer to buffer
copy inside VideoTexture).

**Type:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

#### right

If the video format is stereo 3D, this attribute should be set to an image source object
that will produce the right eye images.  If the goal is to render the BGE scene in 3D,
it can be achieved with 2 cameras, one for each eye, used by 2 ImageRender with an offscreen
render buffer that is just the size of the video frame.

**Type:** one of... - `VideoFFmpeg` - `VideoDeckLink` - `ImageFFmpeg` - `ImageBuff` - `ImageMirror` - `ImageMix` - `ImageRender` - `ImageViewport`

#### keying

Specify if keying is enabled. False (default): the output frame is sent unmodified on
the output interface (in that case no input video is required). True: the output frame
is mixed with the input video, using the alpha channel to blend the two images and the
combination is sent on the output interface.

**Type:** bool

#### level

If keying is enabled, sets the keying level from 0 to 255. This value is a global alpha value
that multiplies the alpha channel of the image source. Use 255 (the default) to keep the alpha
channel unmodified, 0 to make the output frame totally transparent.

**Type:** int

#### extend

Determines how the image source should be mapped if the size does not fit the video frame size.
* False (the default): map the image pixel by pixel.
If the image size is smaller than the frame size, extra space around the image is filled with
0-alpha black. If it is larger, the image is cropped to fit the frame size.
* True: the image is scaled by the nearest neighbor algorithm to fit the frame size.
The scaling is fast but poor quality. For best results, always adjust the image source to
match the size of the output video.

**Type:** bool

#### close()

Close the DeckLink device and release all resources. After calling this method,
the object cannot be reactivated, it must be destroyed and a new DeckLink object
created from fresh to restart the output.

#### refresh(refresh_source,ts)

This method must be called frequently to update the output frame in the DeckLink device.

- **`refresh_source`**: True if the source objects image buffer should be invalidated after being used to compute the output frame. This triggers the recomputing of the source image on next refresh, which is normally the desired effect. False if the image source buffer should stay valid and reused on next refresh. Note that the DeckLink device stores the output frame and replays until a new frame is sent from the host. Thus, it is not necessary to refresh the DeckLink object if it is known that the image source has not changed.
  - type: bool
- **`ts`**: The timestamp value passed to the image source object to compute the image. If unspecified, the BGE clock is used.
  - type: float

### Filter classes

### Class `FilterBGR24`

Source filter BGR24.

### Class `FilterBlueScreen`

Filter for Blue Screen.
The RGB channels of the color are left unchanged, while the output alpha is obtained as follows:

- if the square of the euclidian distance between the RGB color
and the filter's reference color is smaller than the filter's lower limit,
the output alpha is set to 0;
- if that square is bigger than the filter's upper limit, the output alpha is set to 255;
- otherwise the output alpha is linarly extrapoled between 0 and 255 in the interval of the limits.

#### color

Reference color.

**Type:** sequence of three ints

**default:** (0, 0, 255)

#### limits

Reference color limits.

**Type:** sequence of two ints

**default:** (64, 64)

#### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Class `FilterColor`

Filter for color calculations.
The output color is obtained by multiplying the reduced 4x4 matrix with the input color
and adding the remaining column to the result.

#### matrix

Matrix [4][5] for color calculation.

**Type:** sequence of four sequences of five ints

**default:** ((256, 0, 0, 0, 0), (0, 256, 0, 0, 0), (0, 0, 256, 0, 0), (0, 0, 0, 256, 0))

#### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Class `FilterGray`

Filter for grayscale effect.
Proportions of R, G and B contributions in the output grayscale are 28:151:77.

#### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Class `FilterLevel`

Filter for levels calculations. Each output color component is obtained as follows:

* if it is smaller than its corresponding min value, it is set to 0;

* if it is bigger than its corresponding max value, it is set to 255;

* Otherwise it is linearly extrapoled between 0 and 255 in the (min, max) interval.

#### levels

Levels matrix [4] (min, max).

**Type:** sequence of four sequences of two ints

**default:** ((0, 255), (0, 255), (0, 255), (0, 255))

#### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Class `FilterNormal`

Normal map filter.

#### colorIdx

Index of color used to calculate normal (0 - red, 1 - green, 2 - blue, 3 - alpha).

**Type:** int in [0, 3]

**default:** 0

#### depth

Depth of relief.

**Type:** float

**default:** 4.0

#### previous

Previous pixel filter.

**Type:** one of... * `FilterBGR24` * `FilterBlueScreen` * `FilterColor` * `FilterGray` * `FilterLevel` * `FilterNormal` * `FilterRGB24` * `FilterRGBA32`

### Class `FilterRGB24`

Returns a new input filter object to be used with `ImageBuff` object when the image passed
to the `ImageBuff.load` function has the 3-bytes pixel format BGR.

### Class `FilterRGBA32`

Source filter RGBA32.

### Functions

#### getLastError()

Last error that occurred in a Range.texture function.

**Returns:** The description of the last error occurred in a Range.texture function.

**Return type:** str

#### imageToArray(image, mode)

Returns a `Buffer` corresponding to the current image stored in a texture source object.

- **`image`**: Image source object of type: * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`
- **`mode`**: Optional argument representing the pixel format. - You can use the characters R, G, B for the 3 color channels, A for the alpha channel, 0 to force a fixed 0 color channel and 1 to force a fixed 255 color channel. Examples: - "BGR" will return 3 bytes per pixel with the Blue, Green and Red channels in that order. - "RGB1" will return 4 bytes per pixel with the Red, Green, Blue channels in that order and the alpha channel forced to 255. - A special mode "F" allows to return the image as an array of float. This mode should only be used to retrieve the depth buffer of the class:`ImageViewport` and `ImageRender` objects. The default mode is "RGBA".
  - type: str

**Returns:** An object representing the image as one dimensional array of bytes of size (pixel_size*width*height), line by line starting from the bottom of the image. The pixel size and format is determined by the mode parameter. For mode 'F', the array is a one dimensional array of float of size (width*height).

**Return type:** `Buffer`

#### materialID(object, name)

Returns a numeric value that can be used in `Texture` to create a dynamic texture.

The value corresponds to an internal material number that uses the texture identified
by name. name is a string representing a texture name with `IM` prefix if you want to
identify the texture directly. This method works for basic tex face and for material,
provided the material has a texture channel using that particular texture in first
position of the texture stack. name can also have `MA` prefix if you want to identify
the texture by material. In that case the material must have a texture channel in first
position.

If the object has no material that matches name, it generates a runtime error.
Use try/except to catch the exception.

Ex: `Range.texture.materialID(obj, 'IMvideo.png')`

- **`object`**: The game object that uses the texture you want to make dynamic.
  - type: `KX_GameObject`
- **`name`**: Name of the texture/material you want to make dynamic.
  - type: str

**Returns:** The internal material number.

**Return type:** int

#### setLogFile(filename)

Sets the name of a text file in which runtime error messages will be written,
in addition to the printing of the messages on the Python console.
Only the runtime errors specific to the VideoTexture module are written in that file,
ordinary runtime time errors are not written.

- **`filename`**: Name of the error log file.
  - type: str

**Returns:** -1 if the parameter name is invalid (not of type string), else 0.

**Return type:** int

### Constants

### FFmpeg Video and Image Status

#### SOURCE_ERROR

#### SOURCE_EMPTY

#### SOURCE_READY

#### SOURCE_PLAYING

#### SOURCE_STOPPED

### Image Blending Modes

See Wikipedia's [Blend Modes](https://en.wikipedia.org/wiki/Blend_modes) for reference.

#### IMB_BLEND_MIX

#### IMB_BLEND_ADD

#### IMB_BLEND_SUB

#### IMB_BLEND_MUL

#### IMB_BLEND_LIGHTEN

#### IMB_BLEND_DARKEN

#### IMB_BLEND_ERASE_ALPHA

#### IMB_BLEND_ADD_ALPHA

#### IMB_BLEND_OVERLAY

#### IMB_BLEND_HARDLIGHT

#### IMB_BLEND_COLORBURN

#### IMB_BLEND_LINEARBURN

#### IMB_BLEND_COLORDODGE

#### IMB_BLEND_SCREEN

#### IMB_BLEND_SOFTLIGHT

#### IMB_BLEND_PINLIGHT

#### IMB_BLEND_VIVIDLIGHT

#### IMB_BLEND_LINEARLIGHT

#### IMB_BLEND_DIFFERENCE

#### IMB_BLEND_EXCLUSION

#### IMB_BLEND_HUE

#### IMB_BLEND_SATURATION

#### IMB_BLEND_LUMINOSITY

#### IMB_BLEND_COLOR

#### IMB_BLEND_COPY

#### IMB_BLEND_COPY_RGB

#### IMB_BLEND_COPY_ALPHA

---

## Range.track

Baked track data of the Track Tool (`Range.track`, alias `bge.track`).

The editor tool bakes one table per sample of a track layout into the Text datablock
`TRACK_<name>.json` (format version 1, see `docs/plano-track-tool.md`). In the game the engine
reads that Text from the loaded file (and from files loaded with `Range.logic.LibLoad`) the
first time `get` asks for it, keeps it by name and answers the queries in C++.
The results match the pure Python reference `range_track.runtime` (scripts/modules) within 1 mm.

Units are meters and radians. "Left" is the positive lateral side.

```python

import Range

track = Range.track.get("Pista_4")
s, side, dist = track.project(own.worldPosition, near=own.get("track_s"))
own["track_s"] = s
lap_progress = s / track.length
target = track.racingLine(s + 15.0)
```

#### get(name)

Track baked in the Text `TRACK_<name>.json` of the game file or of a LibLoaded file.
The Text name itself (`"TRACK_Pista_4.json"`) is accepted too. Read once and cached; the cache
follows LibLoad/LibFree and is cleared when the game ends.

- **`name`**: track name (the name of the track layout object).
  - type: str

**Returns:** the track, or None when there is no such Text.

**Return type:** `Track` or None

**Raises:** the Text is not a valid track (the message says what is wrong).

#### names()

Names of the tracks available in the loaded files (Texts `TRACK_*.json`).

**Return type:** list of str

#### fromJson(text, name="")

Track built from a JSON string in the baked format (version 1), for data kept elsewhere.

- **`text`**: JSON text.
  - type: str
- **`name`**: name used when the JSON has no `name`.
  - type: str

**Return type:** `Track`

#### reload()

Forget the cached tracks: the next `get` reads the Text again.

### Class `Track`

Baked track. Get one with `get`; it stays valid after the file that held it is freed.

Positions may be a `mathutils.Vector` or a sequence of numbers. With only `(x, y)` the
height is ignored; with `z` the height picks the right level on bridges and crossings.
`s` wraps around on a closed circuit and is clamped to `[0, length]` on an open track.

#### project(pos, near=None)

Projection of a position on the track.

Pass the `s` of the previous frame as `near` for cars: the search stays within 50 m of it,
so a car never jumps to another stretch of the track that passes close by (hairpins, parallel
straights). When the position is more than 15 m away from that stretch (respawn, teleport)
the whole track is searched, as without `near`.

```python

s, side, dist = track.project(own.worldPosition, near=own.get("track_s"))
own["track_s"] = s
```

**Returns:** `(s, side, dist)`: meters along the track, `1` left / `-1` right of the center line and lateral distance from it (>= 0).

**Return type:** tuple (float, int, float)

#### pointAt(s)

Center line point at `s`.

**Return type:** `mathutils.Vector`

#### tangentAt(s)

Unit 3D direction of travel at `s`.

**Return type:** `mathutils.Vector`

#### lateralAt(s)

Horizontal unit vector to the left at `s`.

**Return type:** `mathutils.Vector`

#### bankAt(s)

Banking at `s` in radians (positive: the left edge is lower).

**Return type:** float

#### widthAt(s)

Asphalt half widths at `s`.

**Returns:** `(left, right)`

**Return type:** tuple of 2 floats

#### edgeAt(s)

Lateral distance of the outer border band (wall, guard rail) at `s`.

**Returns:** `(left, right)`

**Return type:** tuple of 2 floats

#### racingLine(s)

Racing line point at `s`, on the banked surface.

**Return type:** `mathutils.Vector`

#### isOnRoad(pos)

True when `pos` is over the asphalt (inside the half widths) and up to 3 m from the
surface (height ignored without `z`). Past the start or the end of an open track: False.

**Return type:** bool

#### surfaceAt(s)

Surface name of the sample that starts the stretch at `s` (`""` when the track has no
surface names).

**Return type:** str

#### name

Track name.

**Type:** str

#### length

Track length in meters.

**Type:** float

#### cyclic

True for a closed circuit.

**Type:** bool

#### count

Number of baked samples.

**Type:** int

#### surfaces

Surface names.

**Type:** list of str

---

# Types

---

## BL_ActionActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

> **See also:**
[`KX_GameObject`](#kx_gameobject), [`BL_ArmatureObject`](#bl_armatureobject), [`KX_AnimationEventManager`](#kx_animationeventmanager)

Action Actuators apply an action to an actor.

```python
# Play part of an action on a separate layer.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Action"]

act.action = "Wave"
act.frameStart = 1
act.frameEnd = 30
act.layer = 1
act.mode = Range.logic.KX_ACTIONACT_PLAY
cont.activate(act)
```

#### action

The name of the action to set as the current action.

**Type:** string

#### frameStart

Specifies the starting frame of the animation.

**Type:** float

#### frameEnd

Specifies the ending frame of the animation.

**Type:** float

#### blendIn

Specifies the number of frames of animation to generate when making transitions between actions.

**Type:** float

#### priority

Sets the priority of this actuator. Actuators will lower priority numbers will override actuators with higher numbers.

**Type:** integer

#### frame

Sets the current frame for the animation.

**Type:** float

#### propName

Sets the property to be used in FromProp playback mode.

**Type:** string

#### mode

The operation mode of the actuator. Can be one of `these constants`.

**Type:** integer

#### useContinue

The actions continue option, True or False. When True, the action will always play from where last left off,
otherwise negative events to this actuator will reset it to its start frame.

**Type:** boolean

#### framePropName

The name of the property that is set to the current frame number.

**Type:** string

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### layer

 `attribute`

Animation layer (0 to 7) the actuator plays the action on. Different layers play at the same time.

#### layerWeight

 `attribute`

Layer weight, from 0.0 to 1.0: how much this action blends with the layers below.

---

## BL_ArmatureActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Armature Actuators change constraint condition on armatures.

```python
# Change the target of a bone constraint.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Armature"]

act.type = Range.logic.KX_ACT_ARMATURE_SETTARGET
act.target = Range.logic.getCurrentScene().objects["Ball"]
cont.activate(act)
```

```python
# Fade the influence of the constraint.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Armature"]

act.type = Range.logic.KX_ACT_ARMATURE_SETINFLUENCE
act.influence = 0.5
cont.activate(act)
```

#### type

The type of action that the actuator executes when it is active.

Can be one of `these constants`

**Type:** integer

#### constraint

The constraint object this actuator is controlling.

**Type:** `BL_ArmatureConstraint`

#### target

The object that this actuator will set as primary target to the constraint it controls.

**Type:** `KX_GameObject`

#### subtarget

The object that this actuator will set as secondary target to the constraint it controls.

**Type:** `KX_GameObject`.

> **Note:**
Currently, the only secondary target is the pole target for IK constraint.

#### weight

The weight this actuator will set on the constraint it controls.

**Type:** float.

> **Note:**
Currently only the IK constraint has a weight. It must be a value between 0 and 1.

> **Note:**
A weight of 0 disables a constraint while still updating constraint runtime values (see `BL_ArmatureConstraint`)

#### influence

The influence this actuator will set on the constraint it controls.

**Type:** float.

---

## BL_ArmatureBone

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Proxy to Blender bone structure. All fields are read-only and comply to RNA names.
All space attribute correspond to the rest pose.

```python
# List the bones with their length and parent.
import Range

armature = Range.logic.getCurrentController().owner

for channel in armature.channels:
    bone = channel.bone
    parent = bone.parent.name if bone.parent else "-"
    print(bone.name, bone.length, parent)
```

#### name

bone name.

**Type:** string

#### connected

true when the bone head is struck to the parent's tail.

**Type:** boolean

#### hinge

true when bone doesn't inherit rotation or scale from parent bone.

**Type:** boolean

#### inherit_scale

true when bone inherits scaling from parent bone.

**Type:** boolean

#### bbone_segments

number of B-bone segments.

**Type:** integer

#### roll

bone rotation around head-tail axis.

**Type:** float

#### head

location of head end of the bone in parent bone space.

**Type:** vector [x, y, z]

#### tail

location of head end of the bone in parent bone space.

**Type:** vector [x, y, z]

#### length

bone length.

**Type:** float

#### arm_head

location of head end of the bone in armature space.

**Type:** vector [x, y, z]

#### arm_tail

location of tail end of the bone in armature space.

**Type:** vector [x, y, z]

#### arm_mat

matrix of the bone head in armature space.

**Type:** matrix [4][4]

> **Note:**
This matrix has no scale part.

#### bone_mat

rotation matrix of the bone in parent bone space.

**Type:** matrix [3][3]

#### parent

parent bone, or None for root bone.

**Type:** `BL_ArmatureBone`

#### children

list of bone's children.

**Type:** list of `BL_ArmatureBone`

---

## BL_ArmatureChannel

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`BL_ArmatureObject`](#bl_armatureobject), [`BL_ArmatureBone`](#bl_armaturebone)

Proxy to armature pose channel. Allows to read and set armature pose.
The attributes are identical to RNA attributes, but mostly in read-only mode.

```python
# Turn the head of the character by script.
import Range

armature = Range.logic.getCurrentController().owner
head = armature.channels["Head"]

head.rotation_mode = Range.logic.ROT_MODE_XYZ
head.rotation_euler = (0.0, 0.0, 0.5)
armature.update()
```

```python
# Find where a bone is in the world.
import Range

armature = Range.logic.getCurrentController().owner
hand = armature.channels["Hand.R"]

print(armature.worldTransform * hand.pose_tail)
```

#### name

channel name (=bone name), read-only.

**Type:** string

#### bone

return the bone object corresponding to this pose channel, read-only.

**Type:** `BL_ArmatureBone`

#### parent

return the parent channel object, None if root channel, read-only.

**Type:** `BL_ArmatureChannel`

#### has_ik

true if the bone is part of an active IK chain, read-only.
This flag is not set when an IK constraint is defined but not enabled (miss target information for example).

**Type:** boolean

#### ik_dof_x

true if the bone is free to rotation in the X axis, read-only.

**Type:** boolean

#### ik_dof_y

true if the bone is free to rotation in the Y axis, read-only.

**Type:** boolean

#### ik_dof_z

true if the bone is free to rotation in the Z axis, read-only.

**Type:** boolean

#### ik_limit_x

true if a limit is imposed on X rotation, read-only.

**Type:** boolean

#### ik_limit_y

true if a limit is imposed on Y rotation, read-only.

**Type:** boolean

#### ik_limit_z

true if a limit is imposed on Z rotation, read-only.

**Type:** boolean

#### ik_rot_control

true if channel rotation should applied as IK constraint, read-only.

**Type:** boolean

#### ik_lin_control

true if channel size should applied as IK constraint, read-only.

**Type:** boolean

#### location

displacement of the bone head in armature local space, read-write.

**Type:** vector [X, Y, Z].

> **Note:**
You can only move a bone if it is unconnected to its parent. An action playing on the armature may change the value. An IK chain does not update this value, see joint_rotation.

> **Note:**
Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see `BL_ArmatureObject.update`).

#### scale

scale of the bone relative to its parent, read-write.

**Type:** vector [sizeX, sizeY, sizeZ].

> **Note:**
An action playing on the armature may change the value.  An IK chain does not update this value, see joint_rotation.

> **Note:**
Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see `BL_ArmatureObject.update`)

#### rotation_quaternion

rotation of the bone relative to its parent expressed as a quaternion, read-write.

**Type:** vector [qr, qi, qj, qk].

> **Note:**
This field is only used if rotation_mode is 0. An action playing on the armature may change the value.  An IK chain does not update this value, see joint_rotation.

> **Note:**
Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see `BL_ArmatureObject.update`)

#### rotation_euler

rotation of the bone relative to its parent expressed as a set of euler angles, read-write.

**Type:** vector [X, Y, Z].

> **Note:**
This field is only used if rotation_mode is > 0. You must always pass the angles in [X, Y, Z] order; the order of applying the angles to the bone depends on rotation_mode. An action playing on the armature may change this field.  An IK chain does not update this value, see joint_rotation.

> **Note:**
Changing this field has no immediate effect, the pose is updated when the armature is updated during the graphic render (see `BL_ArmatureObject.update`)

#### rotation_mode

Method of updating the bone rotation, read-write.

**Type:** integer (one of `these constants`)

#### channel_matrix

pose matrix in bone space (deformation of the bone due to action, constraint, etc), Read-only.
This field is updated after the graphic render, it represents the current pose.

**Type:** matrix [4][4]

#### pose_matrix

pose matrix in armature space, read-only,
This field is updated after the graphic render, it represents the current pose.

**Type:** matrix [4][4]

#### pose_head

position of bone head in armature space, read-only.

**Type:** vector [x, y, z]

#### pose_tail

position of bone tail in armature space, read-only.

**Type:** vector [x, y, z]

#### ik_min_x

minimum value of X rotation in degree (<= 0) when X rotation is limited (see ik_limit_x), read-only.

**Type:** float

#### ik_max_x

maximum value of X rotation in degree (>= 0) when X rotation is limited (see ik_limit_x), read-only.

**Type:** float

#### ik_min_y

minimum value of Y rotation in degree (<= 0) when Y rotation is limited (see ik_limit_y), read-only.

**Type:** float

#### ik_max_y

maximum value of Y rotation in degree (>= 0) when Y rotation is limited (see ik_limit_y), read-only.

**Type:** float

#### ik_min_z

minimum value of Z rotation in degree (<= 0) when Z rotation is limited (see ik_limit_z), read-only.

**Type:** float

#### ik_max_z

maximum value of Z rotation in degree (>= 0) when Z rotation is limited (see ik_limit_z), read-only.

**Type:** float

#### ik_stiffness_x

bone rotation stiffness in X axis, read-only.

**Type:** float between 0 and 1

#### ik_stiffness_y

bone rotation stiffness in Y axis, read-only.

**Type:** float between 0 and 1

#### ik_stiffness_z

bone rotation stiffness in Z axis, read-only.

**Type:** float between 0 and 1

#### ik_stretch

ratio of scale change that is allowed, 0=bone can't change size, read-only.

**Type:** float

#### ik_rot_weight

weight of rotation constraint when ik_rot_control is set, read-write.

**Type:** float between 0 and 1

#### ik_lin_weight

weight of size constraint when ik_lin_control is set, read-write.

**Type:** float between 0 and 1

#### joint_rotation

Control bone rotation in term of joint angle (for robotic applications), read-write.

When writing to this attribute, you pass a [x, y, z] vector and an appropriate set of euler angles or quaternion is calculated according to the rotation_mode.

When you read this attribute, the current pose matrix is converted into a [x, y, z] vector representing the joint angles.

The value and the meaning of the x, y, z depends on the ik_dof_x/ik_dof_y/ik_dof_z attributes:

* 1DoF joint X, Y or Z: the corresponding x, y, or z value is used an a joint angle in radiant
* 2DoF joint X+Y or Z+Y: treated as 2 successive 1DoF joints: first X or Z, then Y. The x or z value is used as a joint angle in radiant along the X or Z axis, followed by a rotation along the new Y axis of y radiants.
* 2DoF joint X+Z: treated as a 2DoF joint with rotation axis on the X/Z plane. The x and z values are used as the coordinates of the rotation vector in the X/Z plane.
* 3DoF joint X+Y+Z: treated as a revolute joint. The [x, y, z] vector represents the equivalent rotation vector to bring the joint from the rest pose to the new pose.

**Type:** vector [x, y, z]

> **Note:**
The bone must be part of an IK chain if you want to set the ik_dof_x/ik_dof_y/ik_dof_z attributes via the UI, but this will interfere with this attribute since the IK solver will overwrite the pose. You can stay in control of the armature if you create an IK constraint but do not finalize it (e.g. don't set a target) the IK solver will not run but the IK panel will show up on the UI for each bone in the chain.

> **Note:**
[0, 0, 0] always corresponds to the rest pose.

> **Note:**
You must request the armature pose to update and wait for the next graphic frame to see the effect of setting this attribute (see `BL_ArmatureObject.update`).

> **Note:**
You can read the result of the calculation in rotation or euler_rotation attributes after setting this attribute.

---

## BL_ArmatureConstraint

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Proxy to Armature Constraint. Allows to change constraint on the fly.
Obtained through `BL_ArmatureObject`.constraints.

> **Note:**
Not all armature constraints are supported in the GE.

```python
# Turn off every constraint of one bone.
import Range

armature = Range.logic.getCurrentController().owner

for constraint in armature.constraints:
    if constraint.name.startswith("Hand.L"):
        constraint.enforce = 0.0
```

```python
# Change the target and the weight of an IK.
import Range

armature = Range.logic.getCurrentController().owner
ik = armature.constraints["Foot.L:IK"]

ik.target = Range.logic.getCurrentScene().objects["FootTarget"]
ik.ik_weight = 1.0
```

#### type

Type of constraint, (read-only).

Use one of `these constants`.

**Type:** integer, one of CONSTRAINT_TYPE_* constants

#### name

Name of constraint constructed as <bone_name>:<constraint_name>. constraints list.

**Type:** string

This name is also the key subscript on `BL_ArmatureObject`.

#### enforce

fraction of constraint effect that is enforced. Between 0 and 1.

**Type:** float

#### headtail

Position of target between head and tail of the target bone: 0=head, 1=tail.

**Type:** float.

> **Note:**
Only used if the target is a bone (i.e target object is an armature.

#### lin_error

runtime linear error (in Blender units) on constraint at the current frame.

This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.

**Type:** float

#### rot_error

Runtime rotation error (in radiant) on constraint at the current frame.

**Type:** float.

This is a runtime value updated on each frame by the IK solver. Only available on IK constraint and iTaSC solver.

It is only set if the constraint has a rotation part, for example, a CopyPose+Rotation IK constraint.

#### target

Primary target object for the constraint. The position of this object in the GE will be used as target for the constraint.

**Type:** `KX_GameObject`.

#### subtarget

Secondary target object for the constraint. The position of this object in the GE will be used as secondary target for the constraint.

**Type:** `KX_GameObject`.

Currently this is only used for pole target on IK constraint.

#### active

True if the constraint is active.

**Type:** boolean

> **Note:**
An inactive constraint does not update lin_error and rot_error.

#### ik_weight

Weight of the IK constraint between 0 and 1.

Only defined for IK constraint.

**Type:** float

#### ik_type

Type of IK constraint, (read-only).

Use one of `these constants`.

**Type:** integer.

#### ik_flag

Combination of IK constraint option flags, read-only.

Use one of `these constants`.

**Type:** integer

#### ik_dist

Distance the constraint is trying to maintain with target, only used when ik_type=CONSTRAINT_IK_DISTANCE.

**Type:** float

#### ik_mode

Use one of `these constants`.

Additional mode for IK constraint. Currently only used for Distance constraint:

**Type:** integer

---

## BL_ArmatureObject

Base class: [`KX_GameObject`](#kx_gameobject)

> **See also:**
[`BL_ArmatureChannel`](#bl_armaturechannel), [`BL_ArmatureBone`](#bl_armaturebone), [`BL_ArmatureConstraint`](#bl_armatureconstraint), [`BL_ActionActuator`](#bl_actionactuator)

An armature object.

```python
# Offset a bone on top of the animation.
import Range

armature = Range.logic.getCurrentController().owner

armature.setBoneRotationOffset("Spine", (0.2, 0.0, 0.0))
```

```python
# Give the bone back to the animation.
import Range

armature = Range.logic.getCurrentController().owner

armature.clearBoneRotationOffset("Spine")
```

```python
# List the channels.
import Range

armature = Range.logic.getCurrentController().owner

for channel in armature.channels:
    print(channel.name)
```

#### constraints

The list of armature constraint defined on this armature.
Elements of the list can be accessed by index or string.
The key format for string access is '<bone_name>:<constraint_name>'.

**Type:** list of `BL_ArmatureConstraint`

#### channels

The list of armature channels.
Elements of the list can be accessed by index or name the bone.

**Type:** list of `BL_ArmatureChannel`

#### update()

Ensures that the armature will be updated on next graphic frame.

This action is unecessary if a KX_ArmatureActuator with mode run is active
or if an action is playing. Use this function in other cases. It must be called
on each frame to ensure that the armature is updated continously.

#### draw()

Draw lines that represent armature to view it in real time.

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### clearBoneRotationOffset(bone=None)

 `method`

Removes the extra rotation of one bone, or of all bones when `bone` is omitted.

#### setBoneRotationOffset(bone, rotation)

 `method`

Extra rotation for a bone on top of the playing actions, in the bone's local space. `rotation`: euler XYZ (3 floats, radians) or quaternion (4 floats, w x y z). Stays until `clearBoneRotationOffset()`.

---

## BL_Shader

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`KX_BlenderMaterial`](#kx_blendermaterial), [`KX_2DFilter`](#kx_2dfilter)

BL_Shader is a class used to compile and use custom shaders scripts. It supports vertex, fragment and geometry shader scripts.
The shader is compiled with a generated header for the three shaders scripts.
This header set the `#version` directive, so the user must not define his own `#version`.

```python
# Replace the shader of a material and send it a value.
import Range

VERTEX = """
void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
"""

FRAGMENT = """
uniform float brightness;

void main()
{
    gl_FragColor = vec4(vec3(brightness), 1.0);
}
"""

own = Range.logic.getCurrentController().owner
material = own.meshes[0].materials[0]
shader = material.getShader()

if shader is not None and not shader.isValid():
    shader.setSource(VERTEX, FRAGMENT, True)

shader.setUniform1f("brightness", 0.8)
```

```python
# Let the engine fill a matrix or the camera position on its own.
import Range

own = Range.logic.getCurrentController().owner
shader = own.meshes[0].materials[0].getShader()

shader.setUniformDef("cameraPosition", Range.logic.CAM_POS)
```

#### enabled

Set shader enabled to use.

**Type:** boolean

#### objectCallbacks

The list of python callbacks executed when the shader is used to render an object.
All the functions can expect as argument the object currently rendered.

```python

def callback(object):
    print("render object %r" % object.name)
```

**Type:** list of functions and/or methods

#### bindCallbacks

The list of python callbacks executed when the shader is begin used to render.

**Type:** list of functions and/or methods

#### setUniformfv(name, fList)

Set a uniform with a list of float values

- **`name`**: the uniform name
  - type: string
- **`fList`**: a list (2, 3 or 4 elements) of float values
  - type: list[float]

#### delSource()

Clear the shader. Use this method before the source is changed with `setSource`.

#### getFragmentProg()

Returns the fragment program.

**Returns:** The fragment program.

**Return type:** string

#### getVertexProg()

Get the vertex program.

**Returns:** The vertex program.

**Return type:** string

#### isValid()

Check if the shader is valid.

**Returns:** True if the shader is valid

**Return type:** boolean

#### setAttrib(enum)

Set attribute location. (The parameter is ignored a.t.m. and the value of "tangent" is always used.)

- **`enum`**: attribute location value
  - type: integer

#### setSampler(name, index)

Set uniform texture sample index.

- **`name`**: Uniform name
  - type: string
- **`index`**: Texture sample index.
  - type: integer

#### setSource(vertexProgram, fragmentProgram, apply)

Set the vertex and fragment programs

- **`vertexProgram`**: Vertex program
  - type: string
- **`fragmentProgram`**: Fragment program
  - type: string
- **`apply`**: Enable the shader.
  - type: boolean

#### setSourceList(sources, apply)

Set the vertex, fragment and geometry shader programs.

- **`sources`**: Dictionary of all programs. The keys `vertex`, `fragment` and `geometry` represent shader programs of the same name. `geometry` is an optional program. This dictionary can be similar to: .. code-block:: python sources = { "vertex" : vertexProgram, "fragment" : fragmentProgram, "geometry" : geometryProgram }
  - type: dict
- **`apply`**: Enable the shader.
  - type: boolean

#### setUniform1f(name, fx)

Set a uniform with 1 float value.

- **`name`**: the uniform name
  - type: string
- **`fx`**: Uniform value
  - type: float

#### setUniform1i(name, ix)

Set a uniform with an integer value.

- **`name`**: the uniform name
  - type: string
- **`ix`**: the uniform value
  - type: integer

#### setUniform2f(name, fx, fy)

Set a uniform with 2 float values

- **`name`**: the uniform name
  - type: string
- **`fx`**: first float value
  - type: float
- **`fy`**: second float value
  - type: float

#### setUniform2i(name, ix, iy)

Set a uniform with 2 integer values

- **`name`**: the uniform name
  - type: string
- **`ix`**: first integer value
  - type: integer
- **`iy`**: second integer value
  - type: integer

#### setUniform3f(name, fx, fy, fz)

Set a uniform with 3 float values.

- **`name`**: the uniform name
  - type: string
- **`fx`**: first float value
  - type: float
- **`fy`**: second float value
  - type: float
- **`fz`**: third float value
  - type: float

#### setUniform3i(name, ix, iy, iz)

Set a uniform with 3 integer values

- **`name`**: the uniform name
  - type: string
- **`ix`**: first integer value
  - type: integer
- **`iy`**: second integer value
  - type: integer
- **`iz`**: third integer value
  - type: integer

#### setUniform4f(name, fx, fy, fz, fw)

Set a uniform with 4 float values.

- **`name`**: the uniform name
  - type: string
- **`fx`**: first float value
  - type: float
- **`fy`**: second float value
  - type: float
- **`fz`**: third float value
  - type: float
- **`fw`**: fourth float value
  - type: float

#### setUniform4i(name, ix, iy, iz, iw)

Set a uniform with 4 integer values

- **`name`**: the uniform name
  - type: string
- **`ix`**: first integer value
  - type: integer
- **`iy`**: second integer value
  - type: integer
- **`iz`**: third integer value
  - type: integer
- **`iw`**: fourth integer value
  - type: integer

#### setUniformDef(name, type)

Define a new uniform

- **`name`**: the uniform name
  - type: string
- **`type`**: uniform type, one of `these constants`
  - type: integer

#### setUniformMatrix3(name, mat, transpose)

Set a uniform with a 3x3 matrix value

- **`name`**: the uniform name
  - type: string
- **`mat`**: A 3x3 matrix [[f, f, f], [f, f, f], [f, f, f]]
  - type: 3x3 matrix
- **`transpose`**: set to True to transpose the matrix
  - type: boolean

#### setUniformMatrix4(name, mat, transpose)

Set a uniform with a 4x4 matrix value

- **`name`**: the uniform name
  - type: string
- **`mat`**: A 4x4 matrix [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
  - type: 4x4 matrix
- **`transpose`**: set to True to transpose the matrix
  - type: boolean

#### setUniformiv(name, iList)

Set a uniform with a list of integer values

- **`name`**: the uniform name
  - type: string
- **`iList`**: a list (2, 3 or 4 elements) of integer values
  - type: list[integer]

#### setUniformEyef(name)

Set a uniform with a float value that reflects the eye being render in stereo mode:
0.0 for the left eye, 0.5 for the right eye. In non stereo mode, the value of the uniform
is fixed to 0.0. The typical use of this uniform is in stereo mode to sample stereo textures
containing the left and right eye images in a top-bottom order.

- **`name`**: the uniform name
  - type: string

#### validate()

Validate the shader object.

---

## BL_Texture

Base class: [`EXP_Value`](#exp_value)

A texture object that contains attributes of a material texture.

```python
# Make the first texture of the material scroll.
import Range

own = Range.logic.getCurrentController().owner
texture = own.meshes[0].materials[0].textures[0]

offset = texture.uvOffset
offset.x += 0.01
texture.uvOffset = offset
```

```python
# Control how much the texture affects the color.
import Range

own = Range.logic.getCurrentController().owner
texture = own.meshes[0].materials[0].textures[0]

texture.diffuseFactor = 0.5
texture.emit = 1.0
```

#### diffuseIntensity

Amount texture affects diffuse reflectivity.

**Type:** float

#### diffuseFactor

Amount texture affects diffuse color.

**Type:** float

#### alpha

Amount texture affects alpha.

**Type:** float

#### specularIntensity

Amount texture affects specular reflectivity.

**Type:** float

#### specularFactor

Amount texture affects specular color.

**Type:** float

#### hardness

Amount texture affects hardness.

**Type:** float

#### emit

Amount texture affects emission.

**Type:** float

#### mirror

Amount texture affects mirror color.

**Type:** float

#### normal

Amount texture affects normal values.

**Type:** float

#### parallaxBump

Height of parallax occlusion mapping.

**Type:** float

#### parallaxStep

Number of steps to achieve parallax effect.

**Type:** float

#### lodBias

Amount bias on mipmapping.

**Type:** float

#### bindCode

Texture bind code/Id/number.

**Type:** integer

#### renderer

Texture renderer of this texture.

**Type:** `KX_CubeMap`, `KX_PlanarMap` or None

#### ior

Index Of Refraction used to compute refraction.

**Type:** float (1.0 to 50.0)

#### refractionRatio

Amount refraction mixed with reflection.

**Type:** float (0.0 to 1.0)

#### uvOffset

Offset applied to texture UV coordinates (mainly translation on U and V axis).

**Type:** `mathutils.Vector`

#### uvSize

Scale applied to texture UV coordinates.

**Type:** `mathutils.Vector`

#### uvRotation

Rotation applied to texture UV coordinates.

**Type:** float (radians)

---

## EXP_BaseListValue

Class `Range.types.EXP_BaseListValue`.

```python
# Look for an object without an error if it does not exist.
import Range

objects = Range.logic.getCurrentScene().objects

door = objects.get("Door")
if door is not None:
    print(objects.index(door))
```

```python
# Filter by name and property. Both are regular expressions.
import Range

objects = Range.logic.getCurrentScene().objects

for enemy in objects.filter("Enemy.*", "life"):
    print(enemy.name)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### append(item)

 `method`

Adds an item at the end of the list. Only works on lists created by the script; internal engine lists (e.g. `scene.objects`) can't be changed.

#### count(item)

 `method`

How many times the item appears in the list.

**Returns:** `int`

#### filter(name, prop='')

 `method`

New list with only the items whose name contains `name` and that have the game property `prop`. At least one of the two must be given.

**Returns:** `EXP_ListValue`

#### from_id(id)

 `method`

Finds the item by its Python `id()`. Useful to store a reference to an object as a number.

**Returns:** `object`

#### get(key, default=None)

 `method`

Item with that name, or `default` if it doesn't exist. E.g. `scene.objects.get('Player')`.

**Returns:** `object`

#### index(item)

 `method`

Position of the item in the list. Raises an error if it isn't there.

**Returns:** `int`

#### reverse()

 `method`

Reverses the list order. Only on lists created by the script.

---

## EXP_BaseListWrapper

Class `Range.types.EXP_BaseListWrapper`.

```python
# These lists work by name or by index, like sensors or channels.
import Range

armature = Range.logic.getCurrentController().owner

head = armature.channels.get("Head")
first = armature.channels[0]
print(head, first)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### get(key, default=None)

 `method`

Item with that name, or `default` if it doesn't exist.

**Returns:** `object`

---

## EXP_ListValue

Base class: [`EXP_PropValue`](#exp_propvalue)

This is a list like object used in the game engine internally that behaves similar to a python list in most ways.

As well as the normal index lookup (`val= clist[i]`), EXP_ListValue supports string lookups (`val= scene.objects["Cube"]`)

Other operations such as `len(clist)`, `list(clist)`, `clist[0:10]` are also supported.

```python
# Walk through the objects of the scene.
import Range

objects = Range.logic.getCurrentScene().objects

for obj in objects:
    print(obj.name)
```

```python
# Find one with a default value.
import Range

objects = Range.logic.getCurrentScene().objects

print(objects.get("Player", None))
print(len(objects.filter("Coin.*")))
```

#### append(val)

Add an item to the list (like pythons append)

> **Caution:**
Appending values to the list can cause crashes when the list is used internally by the game engine.

#### count(val)

Count the number of instances of a value in the list.

**Returns:** number of instances

**Return type:** integer

#### index(val)

Return the index of a value in the list.

**Returns:** The index of the value in the list.

**Return type:** integer

#### reverse()

Reverse the order of the list.

#### get(key, default=None)

Return the value matching key, or the default value if its not found.

**Returns:** The key value or a default.

#### filter(name, prop)

Return a list of items with name matching `name` regex and with a property matching `prop` regex.
If `name` is empty every items are checked, if `prop` is empty no property check is proceeded.

**Returns:** The list of matching items.

#### from_id(id)

This is a funtion especially for the game engine to return a value with a spesific id.

Since object names are not always unique, the id of an object can be used to get an object from the EXP_ValueList.

Example:

```python

myObID=id(gameObject)
ob= scene.objects.from_id(myObID)
```

Where `myObID` is an int or long from the id function.

This has the advantage that you can store the id in places you could not store a gameObject.

> **Caution:**
The id is derived from a memory location and will be different each time the game engine starts.

> **Caution:**
The id can't be stored as an integer in game object properties, as those only have a limited range that the id may not be contained in. Instead an id can be stored as a string game property and converted back to an integer for use in from_id lookups.

---

## EXP_PropValue

Base class: [`EXP_Value`](#exp_value)

This class has no python functions

```python
# This is an internal base class and is not available in Range.types. Check the public base class instead.
import Range

own = Range.logic.getCurrentController().owner

print(isinstance(own, Range.types.EXP_Value))
```

---

## EXP_PyObjectPlus

EXP_PyObjectPlus base class of most other types in the Game Engine.

```python
# Check that an object was not removed before using a saved reference.
import Range

own = Range.logic.getCurrentController().owner
target = own.get("target")

if target is not None and not target.invalid:
    print(target.worldPosition)
```

#### invalid

Test if the object has been freed by the game engine and is no longer valid.

Normally this is not a problem but when storing game engine data in the GameLogic module,
KX_Scenes or other KX_GameObjects its possible to hold a reference to invalid data.
Calling an attribute or method on an invalid object will raise a SystemError.

The invalid attribute allows testing for this case without exception handling.

**Type:** boolean

---

## EXP_Value

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

This class is a basis for other classes.

```python
# Every value with a name has the name attribute.
import Range

cont = Range.logic.getCurrentController()

print(cont.owner.name)
print(cont.name)
```

#### name

The name of this EXP_Value derived object (read-only).

**Type:** string

---

## KX_2DFilter

Base class: [`BL_Shader`](#bl_shader)

> **See also:**
[`KX_2DFilterManager`](#kx_2dfiltermanager), [`KX_2DFilterOffScreen`](#kx_2dfilteroffscreen), [`BL_Shader`](#bl_shader)

2D filter shader object. Can be alterated with `BL_Shader`'s functions.

> **Caution:**
The vertex shader must not apply modelview and projection transformation. It should be similar to:

```glsl

void main()
{
    gl_Position = gl_Vertex;
}
```

#### mipmap

Request mipmap generation of the render `bgl_RenderedTexture` texture. Accessing mipmapping level is similar to:

```glsl

uniform sampler2D bgl_RenderedTexture;

void main()
{
    float level = 2.0; // mipmap level
    gl_FragColor = textureLod(bgl_RenderedTexture, gl_TexCoord[0].st, level);
}
```

**Type:** boolean

#### offScreen

The custom off screen the filter render to (read-only).

**Type:** `Range.types.KX_2DFilterOffScreen` or None

#### setTexture(index, bindCode, samplerName="")

Set specified texture bind code `bindCode` in specified slot `index`. Any call to `setTexture`
should be followed by a call to `BL_Shader.setSampler` with the same `index` if `sampleName` is not specified.

- **`index`**: The texture slot.
  - type: integer
- **`bindCode`**: The texture bind code/Id.
  - type: integer
- **`samplerName`**: The shader sampler name set to `index` if `samplerName` is passed in the function. (optional)
  - type: string

#### setCubeMap(index, bindCode, samplerName="")

Set specified cube map texture bind code `bindCode` in specified slot `index`. Any call to `setCubeMap`
should be followed by a call to `BL_Shader.setSampler` with the same `index` if `sampleName` is not specified.

- **`index`**: The texture slot.
  - type: integer
- **`bindCode`**: The cube map texture bind code/Id.
  - type: integer
- **`samplerName`**: The shader sampler name set to `index` if `samplerName` is passed in the function. (optional)
  - type: string

#### addOffScreen(slots, depth=False, width=-1, height=-1, hdr=bge.render.HDR_NONE, mipmap=False)

Register a custom off screen to render the filter to.

- **`slots`**: The number of color texture attached to the off screen, between 0 and 8 excluded.
  - type: integer
- **`depth`**: True of the off screen use a depth texture (optional).
  - type: boolean
- **`width`**: The off screen width, -1 if it can be resized dynamically when the viewport dimensions changed (optional).
  - type: integer
- **`height`**: The off screen height, -1 if it can be resized dynamically when the viewport dimensions changed (optional).
  - type: integer
- **`hdr`**: The image quality HDR of the color textures (optional).
  - type: one of `these constants`
- **`mipmap`**: True if the color texture generate mipmap at the end of the filter rendering (optional).
  - type: boolean

> **Note:**
If the off screen is created using a dynamic size (`width` and `height` to -1) its bind codes will be unavailable before
the next render of the filter and the it can change when the viewport is resized.

#### removeOffScreen()

Unregister the custom off screen the filter render to.

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### recompile(fragmentProgram=None)

 `method`

Compiles new GLSL code. Without an argument, rereads the external text file (if the filter came from one) or recompiles the current code. Returns `True` on success; otherwise see `compileLog`.

**Returns:** `bool`

#### setUniform(name, value)

 `method`

Sets a shader uniform by name. The type comes from the shader (float, vec2-4, int, ivec2-4, bool, mat3, mat4 or arrays of them). The value stays after a `recompile()`.

#### activeUniforms

*(new in Anastacio)* `attribute · read-only`

List of the uniforms used by the shader, as `(name, type, size)` tuples.

#### compileLog

*(new in Anastacio)* `attribute · read-only`

Messages from the last shader compile (errors and warnings). Empty when it compiled without problems.

#### sourceName

*(new in Anastacio)* `attribute · read-only`

Name of the text or file the filter code came from.

#### sourcePath

*(new in Anastacio)* `attribute · read-only`

Path of the filter external `.glsl` file; empty when the code is inside the `.range`.

---

## KX_2DFilterManager

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`KX_2DFilter`](#kx_2dfilter), [`KX_2DFilterOffScreen`](#kx_2dfilteroffscreen), [`KX_Camera`](#kx_camera)

2D filter manager used to add, remove and find filters in a scene.

```python
# Add a built-in filter, then a custom one.
import Range

manager = Range.logic.getCurrentScene().filterManager

manager.addFilter(0, Range.logic.RAS_2DFILTER_SEPIA)

GLSL = """
uniform sampler2D bgl_RenderedTexture;
in vec4 bgl_TexCoord;
out vec4 fragColor;

void main()
{
    fragColor = texture(bgl_RenderedTexture, bgl_TexCoord.xy) * 0.5;
}
"""
manager.addFilter(1, Range.logic.RAS_2DFILTER_CUSTOMFILTER, GLSL)
```

```python
# Remove a filter.
import Range

manager = Range.logic.getCurrentScene().filterManager

if manager.getFilter(0) is not None:
    manager.removeFilter(0)
```

```python
# Adjust the effects of the graphics options.
import Range

manager = Range.logic.getCurrentScene().filterManager

manager.changeBloomValues(True, 0.6, 0.8)
manager.changeFxaaValues(True)
manager.changeGrainValues(True, 0.1)
```

#### addFilter(index, type, fragmentProgram="", owner=None, mipmap=False)

Add a filter to the pass index `index`, type `type` and fragment program if custom filter.

- **`index`**: The filter pass index.
  - type: integer
- **`type`**: The filter type, one of: * `Range.logic.RAS_2DFILTER_BLUR` * `Range.logic.RAS_2DFILTER_DILATION` * `Range.logic.RAS_2DFILTER_EROSION` * `Range.logic.RAS_2DFILTER_SHARPEN` * `Range.logic.RAS_2DFILTER_LAPLACIAN` * `Range.logic.RAS_2DFILTER_PREWITT` * `Range.logic.RAS_2DFILTER_SOBEL` * `Range.logic.RAS_2DFILTER_GRAYSCALE` * `Range.logic.RAS_2DFILTER_SEPIA` * `Range.logic.RAS_2DFILTER_OUTLINE` * `Range.logic.RAS_2DFILTER_CUSTOMFILTER`
  - type: integer
- **`fragmentProgram`**: The filter shader fragment program. Used only if `type` is `Range.logic.RAS_2DFILTER_CUSTOMFILTER`, if empty or not specified the filter is created without shader, waiting call to `BL_Shader.setSourceList`. (optional)
  - type: string
- **`owner`**: Object whose game properties feed the uniforms of the same name, like the Filter 2D actuator. (optional)
  - type: `KX_GameObject`
- **`mipmap`**: Generate mipmaps of the filter input. (optional)
  - type: boolean

**Returns:** The 2D Filter.

**Return type:** `KX_2DFilter`

#### setBuiltinFilterEnabled(type, enabled=True)

Turn a built-in filter on or off with its current values, like the Filter 2D actuator.

- **`type`**: `Range.logic.RAS_2DFILTER_FXAA`, `RAS_2DFILTER_BLOOM`, `RAS_2DFILTER_TONEMAP`, `RAS_2DFILTER_SSAO`, `RAS_2DFILTER_LIGHTSCATTER` or `RAS_2DFILTER_SSR`.
  - type: integer
- **`enabled`**: The new state.
  - type: boolean

**Returns:** False when the filter is unavailable.

**Return type:** boolean

#### removeFilter(index)

Remove filter to the pass index `index`.

- **`index`**: The filter pass index.
  - type: integer

#### getFilter(index)

Return filter to the pass index `index`.

**warning:** If the 2D Filter is added with a `SCA_2DFilterActuator`, the filter will be available only after the 2D Filter program is linked. The python script to get the filter has to be executed one frame later. A delay sensor can be used.

- **`index`**: The filter pass index.
  - type: integer

**Returns:** The filter in the specified pass index or None.

**Return type:** `KX_2DFilter` or None

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### changeBloomValues(enabled, intensity, threshold)

 `method`

Turns the scene Bloom on/off and changes intensity and brightness threshold.

#### changeFxaaValues(enabled)

 `method`

Turns the scene FXAA (anti-aliasing) on or off.

#### changeGrainValues(enabled, strength)

 `method`

Turns film grain on/off and changes its strength.

#### changeLightScatterValues(enabled, step_max, step_size, threshold, intensity)

 `method`

Turns light scattering (light rays) on/off and changes steps, step size, threshold and intensity.

#### changeSSAOValues(enabled, samples, strength, distance, attenuation)

 `method`

Turns ambient occlusion (SSAO) on/off and changes samples, strength, distance and attenuation.

#### changeSSGIValues(enabled, radius=3.0, strength=1.0, rays=4, steps=8, thickness=0.1, divisor=0)

 `method`

Turns screen-space global illumination (SSGI) on/off and changes its parameters. `divisor` 1, 2 or 4 changes the tracing resolution; 0 keeps it. SSGI must be enabled in the scene before Play.

#### changeSSRValues(enabled, step_max, bias, max_distance)

 `method`

Turns screen-space reflections (SSR) on/off and changes steps, bias and maximum distance.

#### changeTonemapValues(enabled, exposure, gamma)

 `method`

Turns tonemapping on/off and changes exposure and gamma.

#### compositor

*(new in Anastacio)* `attribute · read-only`

Filter generated from the scene's Compositor tree (Use Nodes). Value and RGB nodes change live with `compositor.setUniform()`. Read-only.

#### fxaaEdgeThreshold

*(new in Anastacio)* `attribute`

Minimum relative contrast for an edge to get FXAA, from 0.0 to 1.0. Lower values smooth more edges.

#### fxaaEdgeThresholdMin

*(new in Anastacio)* `attribute`

Minimum absolute contrast for FXAA to act, from 0.0 to 1.0. Avoids processing dark areas.

#### fxaaEnabled

*(new in Anastacio)* `attribute`

Turns the scene FXAA on or off (Scene > Post-process). `True` or `False`.

#### fxaaSearchSteps

*(new in Anastacio)* `attribute`

Number of FXAA edge search steps (integer, 2 or more). More steps catch longer edges and cost more.

#### fxaaSubpix

*(new in Anastacio)* `attribute`

How much FXAA smooths details smaller than a pixel, from 0.0 to 1.0.

#### grainEnabled

*(new in Anastacio)* `attribute`

Turns the scene film grain on or off.

#### grainStrength

*(new in Anastacio)* `attribute`

Film grain strength, from 0.0 to 1.0.

#### taaEnabled

*(new in Anastacio)* `attribute`

Turns the scene TAA (temporal anti-aliasing) on or off (Render > TAA). `True` or `False`. Smooths edges by blending frames with a slightly shifted camera. In split screen and stereo only the sharpening runs.

#### taaSharpen

*(new in Anastacio)* `attribute`

Sharpening applied after TAA, from 0.0 to 1.0 (default 0.25). Makes up for the slight blur of frame blending.

---

## KX_2DFilterOffScreen

Base class: [`EXP_Value`](#exp_value)

2D filter custom off screen.

```python
# Read the size of the image a filter writes to.
import Range

manager = Range.logic.getCurrentScene().filterManager
offScreen = manager.getFilter(0).offScreen

if offScreen is not None:
    print(offScreen.width, offScreen.height)
    print(offScreen.colorBindCodes, offScreen.depthBindCode)
```

#### width

The off screen width, -1 if the off screen can be resized dynamically (read-only).

**Type:** integer

#### height

The off screen height, -1 if the off screen can be resized dynamically (read-only).

**Type:** integer

#### colorBindCodes

The bind code of the color textures attached to the off screen (read-only).

> **Caution:**
If the off screen can be resized dynamically (:data:`width` of :data:`height` equal to -1), the bind codes may change.

**Type:** list of 8 integers

#### depthBindCode

The bind code of the depth texture attached to the off screen (read-only).

> **Caution:**
If the off screen can be resized dynamically (:data:`width` of :data:`height` equal to -1), the bind code may change.

**Type:** integer

---

## KX_AddObjectActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Edit Object Actuator (in Add Object Mode)

> **Caution:**
An Add Object actuator will be ignored if at game start, the linked object doesn't exist (or is empty) or the linked object is in an active layer.

```text

Error: GameObject 'Name' has a AddObjectActuator 'ActuatorName' without object (in 'nonactive' layer)
```

#### object

the object this actuator adds.

**Type:** `KX_GameObject` or None

#### objectLastCreated

the last added object from this actuator (read-only).

**Type:** `KX_GameObject` or None

#### time

the lifetime of added objects, in frames. Set to 0 to disable automatic deletion.

**Type:** float

#### linearVelocity

the initial linear velocity of added objects.

**Type:** list [vx, vy, vz]

#### angularVelocity

the initial angular velocity of added objects.

**Type:** list [vx, vy, vz]

#### instantAddObject()

adds the object without needing to calling SCA_PythonController.activate()

> **Note:**
Use objectLastCreated to get the newly created object.

---

## KX_AnimationEvent

Class `Range.types.KX_AnimationEvent`.

```python
# See how many times each event of the animation fired.
import Range

own = Range.logic.getCurrentController().owner

for event in own.animationEventManager.events:
    print(event.triggers, event.getFireCount())
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### getFireCount(index=-1)

 `method`

How many times trigger number `index` fired. With -1, adds up all triggers.

**Returns:** `int`

#### triggers

 `attribute · read-only`

List of the animation frames where the event fires.

---

## KX_AnimationEventManager

> **See also:**
[`KX_AnimationEvent`](#kx_animationevent), [`SCA_AnimationEventSensor`](#sca_animationeventsensor)

Class `Range.types.KX_AnimationEventManager`.

```python
# Play a step sound on the frames marked in the animation.
import Range

cont = Range.logic.getCurrentController()
own = cont.owner

fired = sum(event.getFireCount() for event in own.animationEventManager.events)

if fired != own.get("steps", 0):
    own["steps"] = fired
    cont.activate("StepSound")
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### events

 `attribute · read-only`

List of the object animation events (`KX_AnimationEvent`).

---

## KX_ArmatureSensor

Base class: [`SCA_ISensor`](#sca_isensor)

Armature sensor detect conditions on armatures.

```python
# React when the IK error gets too big.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Armature"]

sensor.type = Range.logic.KX_ARMSENSOR_LIN_ERROR_ABOVE
sensor.value = 0.1

if sensor.positive:
    print("Bone cannot reach the target:", sensor.constraint.name)
```

#### type

The type of measurement that the sensor make when it is active.

Can be one of `these constants`

**Type:** integer.

#### constraint

The constraint object this sensor is watching.

**Type:** `BL_ArmatureConstraint`

#### value

The threshold used in the comparison with the constraint error
The linear error is only updated on CopyPose/Distance IK constraint with iTaSC solver
The rotation error is only updated on CopyPose+rotation IK constraint with iTaSC solver
The linear error on CopyPose is always >= 0: it is the norm of the distance between the target and the bone
The rotation error on CopyPose is always >= 0: it is the norm of the equivalent rotation vector between the bone and the target orientations
The linear error on Distance can be positive if the distance between the bone and the target is greater than the desired distance, and negative if the distance is smaller.

**Type:** float

---

## KX_BatchGroup

Base class: [`EXP_Value`](#exp_value)

The batch group is class containing a mesh resulting of the merging of meshes used by objects.
The meshes are merged with the transformation of the objects using it.
An instance of this class is not owned by one object but shared between objects.
In consideration an instance of `KX_BatchGroup` have to instanced with as argument a list of at least one object containing the meshes to merge.
This can be done in a way similar to:

```python

import Range

scene = Range.logic.getCurrentScene()

batchGroup = Range.types.KX_BatchGroup([scene.objects["Cube"], scene.objects["Plane"]])
```

> **Caution:**
Rendering settings unique to objects such as `KX_GameObject.layer` and `KX_GameObject.color` are shared when using batch groups.
These settings are taken from object `referenceObject`.

```python

# Merge every object with the rock property to draw them in fewer calls.
import Range

scene = Range.logic.getCurrentScene()
rocks = [obj for obj in scene.objects if "rock" in obj]

group = Range.types.KX_BatchGroup(rocks)
print(len(group.objects))
```

```python

# Take one object out of its group before changing it alone.
import Range

obj = Range.logic.getCurrentController().owner

if obj.batchGroup is not None:
    obj.batchGroup.split([obj])
```

```python

# Undo the group and give every object its original mesh back.
import Range

obj = Range.logic.getCurrentController().owner

if obj.batchGroup is not None:
    obj.batchGroup.destruct()
```

#### objects

The list of the objects merged. (read only)

**Type:** `EXP_ListValue` of `KX_GameObject`

#### referenceObject

The object used for object rendering settings (layer, color...).

#### merge(objects)

Merge meshes using the transformation of the objects using them.

- **`objects`**: The objects to merge.
  - type: `EXP_ListValue` of `KX_GameObject`

#### split(objects)

Split the meshes of the objects using them and restore their original meshes.

- **`objects`**: The objects to unmerge.
  - type: `EXP_ListValue` of `KX_GameObject`

#### destruct()

Destruct the batch group and restore all the objects to their original meshes.

---

## KX_BlenderMaterial

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`BL_Shader`](#bl_shader), [`BL_Texture`](#bl_texture), [`KX_Mesh`](#kx_mesh)

This is the interface to materials in the game engine.

Materials define the render state to be applied to mesh objects.

The example below shows a simple GLSL shader setup allowing to dynamically mix two texture channels
in a material. All materials of the object executing this script should have two textures using
separate UV maps in the two first texture channels.

The code works for both Multitexture and GLSL rendering modes.

```python

from Range import logic

vertex_shader = """

void main(void)
{
   // simple projection of the vertex position to view space
   gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
   // coordinate of the 1st texture channel
   gl_TexCoord[0] = gl_MultiTexCoord0;
   // coordinate of the 2nd texture channel
   gl_TexCoord[1] = gl_MultiTexCoord1;
}
"""

fragment_shader ="""

uniform sampler2D texture_0;
uniform sampler2D texture_1;
uniform float factor;

void main(void)
{
   vec4 color_0 = texture2D(texture_0, gl_TexCoord[0].st);
   vec4 color_1 = texture2D(texture_1, gl_TexCoord[1].st);
   gl_FragColor = mix(color_0, color_1, factor);
}
"""

object = logic.getCurrentController().owner

for mesh in object.meshes:
    for material in mesh.materials:
        shader = material.getShader()
        if shader is not None:
            if not shader.isValid():
                shader.setSource(vertex_shader, fragment_shader, True)

            # get the first texture channel of the material
            shader.setSampler('texture_0', 0)
            # get the second texture channel of the material
            shader.setSampler('texture_1', 1)
            # pass another uniform to the shader
            shader.setUniform1f('factor', 0.3)
```

#### shader

The material's shader.

**Type:** `BL_Shader`

#### blending

Ints used for pixel blending, (src, dst), matching the setBlending method.

**Type:** (integer, integer)

#### getShader()

Returns the material's shader.

**Returns:** the material's shader

**Return type:** `BL_Shader`

#### ~~getTextureBindcode(textureslot)~~

Returns the material's texture OpenGL bind code/id/number/name.

> **Deprecated use :py:meth:`bge.types.BL_Texture.bindCode`:**

- **`textureslot`**: Specifies the texture slot number
  - type: integer

**Returns:** the material's texture OpenGL bind code/id/number/name

**Return type:** integer

#### alpha

The material's alpha transparency.

**Type:** float between 0.0 and 1.0 inclusive

#### hardness

How hard (sharp) the material's specular reflection is.

**Type:** integer between 1 and 511 inclusive

#### emit

Amount of light to emit.

**Type:** float between 0.0 and 2.0 inclusive

#### ambient

Amount of ambient light on the material.

**Type:** float between 0.0 and 1.0 inclusive

#### specularAlpha

Alpha transparency for specular areas.

**Type:** float between 0.0 and 1.0 inclusive (alpha must be < 1.0)

#### specularIntensity

How intense (bright) the material's specular reflection is.

**Type:** float between 0.0 and 1.0 inclusive

#### diffuseIntensity

The material's amount of diffuse reflection.

**Type:** float between 0.0 and 1.0 inclusive

#### specularColor

The material's specular color.

**Type:** `mathutils.Color`

#### diffuseColor

The material's diffuse color.

**Type:** `mathutils.Color`

#### textures

List of all material's textures.

**Type:** List of `BL_Texture` (read only)

#### setScriptUniform(name, value)

Set a `u_` uniform declared in the Text of the GLSL Script nodes of this material
(`uniform float u_speed;`). The value is sent to the GPU on the next draw, the shader is not
compiled again. A uniform whose socket is linked to another node is not affected.

- **`name`**: Name of the uniform, as written in the Text (`"u_speed"`).
  - type: string
- **`value`**: A number, or a sequence of up to 4 numbers for vec2/vec3/vec4.
  - type: float or sequence of floats

**Returns:** True when the material has that uniform.

**Return type:** boolean

#### getScriptUniform(name)

Current value of a `u_` uniform of the GLSL Script nodes of this material.

- **`name`**: Name of the uniform.
  - type: string

**Returns:** A float, a tuple (3 values for vec2/vec3, 4 for vec4) or None when there is no such uniform.

#### setBlending(src, dest)

Set the pixel color arithmetic functions.

- **`src`**: Specifies how the red, green, blue, and alpha source blending factors are computed, one of... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - type: int
- **`dest`**: Specifies how the red, green, blue, and alpha destination blending factors are computed, one of... * `GL_ZERO` * `GL_ONE` * `GL_SRC_COLOR` * `GL_ONE_MINUS_SRC_COLOR` * `GL_DST_COLOR` * `GL_ONE_MINUS_DST_COLOR` * `GL_SRC_ALPHA` * `GL_ONE_MINUS_SRC_ALPHA` * `GL_DST_ALPHA` * `GL_ONE_MINUS_DST_ALPHA` * `GL_SRC_ALPHA_SATURATE`
  - type: int

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### passIndex

 `attribute`

Material Pass Index, used to separate materials in filters and effects.

---

## KX_BoundingBox

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

A bounding volume box of a game object. Used to get and alterate the volume box or AABB.

```python

from Range import logic
from mathutils import Vector

owner = logic.getCurrentController().owner
box = owner.cullingBox

# Disable auto update to allow modify the box.
box.autoUpdate = False

print(box)
# Increase the height of the box of 1.
box.max = box.max + Vector((0, 0, 1))

print(box)
```

```python

# Read the size of the box of the object.
import Range

box = Range.logic.getCurrentController().owner.cullingBox

size = box.max - box.min
print("Size:", size)
print("Center:", box.center)
print("Radius:", box.radius)
print("Volume:", box.volume)
```

#### min

The minimal point in x, y and z axis of the bounding box.

**Type:** `mathutils.Vector`

#### max

The maximal point in x, y and z axis of the bounding box.

**Type:** `mathutils.Vector`

#### center

The center of the bounding box. (read only)

**Type:** `mathutils.Vector`

#### radius

The radius of the bounding box. (read only)

**Type:** float

#### autoUpdate

Allow to update the bounding box if the mesh is modified.

**Type:** boolean

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### volume

 `attribute · read-only`

Bounding box volume (width × height × depth).

---

## KX_Camera

Base class: [`KX_GameObject`](#kx_gameobject)

> **See also:**
[`KX_Scene`](#kx_scene), [`KX_2DFilterManager`](#kx_2dfiltermanager), [`KX_GameObject`](#kx_gameobject), [`Range.render`](#rangerender)

A Camera object.

```python

# Pick the object under the mouse.
import Range

scene = Range.logic.getCurrentScene()
x, y = Range.logic.mouse.position

hit = scene.active_camera.getScreenRay(x, y, 100.0)

if hit is not None:
    print(hit.name)
```

```python

# Check whether an object is inside the view of the camera.
import Range

scene = Range.logic.getCurrentScene()
cam = scene.active_camera
enemy = scene.objects["Enemy"]

if cam.sphereInsideFrustum(enemy.worldPosition, 1.0) != cam.OUTSIDE:
    print("Enemy on screen")
```

```python

# Shake the camera for half a second, as in an explosion.
import Range

cam = Range.logic.getCurrentScene().active_camera
cam.shake(0.8, 0.5)
```

```python

# Zoom in by closing the field of view.
import Range

cam = Range.logic.getCurrentScene().active_camera
cam.fov = 30.0
```

```python

# Split screen: this camera takes the left half of the window.
import Range

cam = Range.logic.getCurrentController().owner
width = Range.render.getWindowWidth()
height = Range.render.getWindowHeight()

cam.useViewport = True
cam.setViewport(0, 0, width // 2, height)
```

#### INSIDE

See `sphereInsideFrustum` and `boxInsideFrustum`

#### INTERSECT

See `sphereInsideFrustum` and `boxInsideFrustum`

#### OUTSIDE

See `sphereInsideFrustum` and `boxInsideFrustum`

#### lens

The camera's lens value.

**Type:** float

#### lodDistanceFactor

The factor to multiply distance to camera to adjust levels of detail.
A float < 1.0f will make the distance to camera used to compute
levels of detail decrease.

**Type:** float

#### fov

The camera's field of view value.

**Type:** float

#### ortho_scale

The camera's view scale when in orthographic mode.

**Type:** float

#### near

The camera's near clip distance.

**Type:** float

#### far

The camera's far clip distance.

**Type:** float

#### shift_x

The camera's horizontal shift.

**Type:** float

#### shift_y

The camera's vertical shift.

**Type:** float

#### perspective

True if this camera has a perspective transform, False for an orthographic projection.

**Type:** boolean

#### frustum_culling

True if this camera is frustum culling.

**Type:** boolean

#### activityCulling

True if this camera is used to compute object distance for object activity culling.

**Type:** boolean

#### projection_matrix

This camera's 4x4 projection matrix.

> **Note:**
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).

**Type:** 4x4 Matrix [[float]]

#### projectionMatrixLeft

This camera's 4x4 left eye projection matrix.

> **Note:**
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).

**Type:** 4x4 Matrix [[float]]

#### projectionMatrixRight

This camera's 4x4 right eye projection matrix.

> **Note:**
This is the identity matrix prior to rendering the first frame (any Python done on frame 1).

**Type:** 4x4 Matrix [[float]]

#### modelview_matrix

This camera's 4x4 model view matrix. (read-only).

**Type:** 4x4 Matrix [[float]]

> **Note:**
This matrix is regenerated every frame from the camera's position and orientation. Also, this is the identity matrix prior to rendering the first frame (any Python done on frame 1).

#### camera_to_world

This camera's camera to world transform. (read-only).

**Type:** 4x4 Matrix [[float]]

> **Note:**
This matrix is regenerated every frame from the camera's position and orientation.

#### world_to_camera

This camera's world to camera transform. (read-only).

**Type:** 4x4 Matrix [[float]]

> **Note:**
Regenerated every frame from the camera's position and orientation.

> **Note:**
This is camera_to_world inverted.

#### useViewport

True when the camera is used as a viewport, set True to enable a viewport for this camera.

**Type:** boolean

#### viewport

The viewport rectangle used for the last render of this camera, in pixels (read-only).
Ratios set in the editor are already resolved against the window.

**Type:** list [left, bottom, right, top]

#### sphereInsideFrustum(centre, radius)

Tests the given sphere against the view frustum.

- **`centre`**: The centre of the sphere (in world coordinates.)
  - type: list [x, y, z]
- **`radius`**: the radius of the sphere
  - type: float

**Returns:** `INSIDE`, `OUTSIDE` or `INTERSECT`

**Return type:** integer

> **Note:**
When the camera is first initialized the result will be invalid because the projection matrix has not been set.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# A sphere of radius 4.0 located at [x, y, z] = [1.0, 1.0, 1.0]
if (cam.sphereInsideFrustum([1.0, 1.0, 1.0], 4) != cam.OUTSIDE):
    # Sphere is inside frustum !
    # Do something useful !
else:
    # Sphere is outside frustum
```

#### boxInsideFrustum(box)

Tests the given box against the view frustum.

- **`box`**: Eight (8) corner points of the box (in world coordinates), or a `KX_GameObject` to test its world bounding box.
  - type: list of lists or `KX_GameObject`

**Returns:** `INSIDE`, `OUTSIDE` or `INTERSECT`

> **Note:**
When the camera is first initialized the result will be invalid because the projection matrix has not been set.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Box to test...
box = []
box.append([-1.0, -1.0, -1.0])
box.append([-1.0, -1.0,  1.0])
box.append([-1.0,  1.0, -1.0])
box.append([-1.0,  1.0,  1.0])
box.append([ 1.0, -1.0, -1.0])
box.append([ 1.0, -1.0,  1.0])
box.append([ 1.0,  1.0, -1.0])
box.append([ 1.0,  1.0,  1.0])

if (cam.boxInsideFrustum(box) != cam.OUTSIDE):
  # Box is inside/intersects frustum !
  # Do something useful !
else:
  # Box is outside the frustum !
```

To test a game object, pass the object itself. It is the same as passing its world corners
from `getBoundBoxCorners`:

```python

if cam.boxInsideFrustum(obj) != cam.OUTSIDE:
    print(obj.name, "is visible (at least partly)")

# same result:
cam.boxInsideFrustum(obj.getBoundBoxCorners('WORLD'))
```

#### pointInsideFrustum(point)

Tests the given point against the view frustum.

- **`point`**: The point to test (in world coordinates.)
  - type: 3D Vector

**Returns:** True if the given point is inside this camera's viewing frustum.

**Return type:** boolean

> **Note:**
When the camera is first initialized the result will be invalid because the projection matrix has not been set.

```python

from Range import logic
cont = logic.getCurrentController()
cam = cont.owner

# Test point [0.0, 0.0, 0.0]
if (cam.pointInsideFrustum([0.0, 0.0, 0.0])):
  # Point is inside frustum !
  # Do something useful !
else:
  # Box is outside the frustum !
```

#### getCameraToWorld()

Returns the camera-to-world transform.

**Returns:** the camera-to-world transform matrix.

**Return type:** matrix (4x4 list)

#### getWorldToCamera()

Returns the world-to-camera transform.

This returns the inverse matrix of getCameraToWorld().

**Returns:** the world-to-camera transform matrix.

**Return type:** matrix (4x4 list)

#### setOnTop()

Set this cameras viewport ontop of all other viewport.

#### setViewport(left, bottom, right, top)

Sets the region of this viewport on the screen in pixels.

Use `Range.render.getWindowHeight` and `Range.render.getWindowWidth` to calculate values relative to the entire display.

- **`left`**: left pixel coordinate of this viewport
  - type: integer
- **`bottom`**: bottom pixel coordinate of this viewport
  - type: integer
- **`right`**: right pixel coordinate of this viewport
  - type: integer
- **`top`**: top pixel coordinate of this viewport
  - type: integer

#### getScreenPosition(object)

Gets the position of an object projected on screen space.

```python

# For an object in the middle of the screen, coord = [0.5, 0.5]
coord = camera.getScreenPosition(object)
```

- **`object`**: object name or list [x, y, z]
  - type: `KX_GameObject` or 3D Vector

**Returns:** the object's position in screen coordinates.

**Return type:** list [x, y]

#### getScreenVect(x, y)

Gets the vector from the camera position in the screen coordinate direction.

- **`x`**: X Axis
  - type: float
- **`y`**: Y Axis
  - type: float

**Return type:** 3D Vector

**Returns:** The vector from screen coordinate.

```python

# Gets the vector of the camera front direction:
m_vect = camera.getScreenVect(0.5, 0.5)
```

#### getScreenRay(x, y, dist, property="", xray=False, mask=0xFFFF)

Look towards a screen coordinate (x, y) and find first object hit within dist that matches prop.
The ray is similar to KX_GameObject->rayCastTo.

- **`x`**: X Axis
  - type: float
- **`y`**: Y Axis
  - type: float
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
  - type: float
- **`property`**: property name that object must have; can be omitted => detect any object
  - type: string
- **`xray`**: the ray goes through objects without the property, like the X-Ray option of the Mouse sensor
  - type: boolean
- **`mask`**: collision mask, only objects of these collision groups are hit
  - type: bitfield

**Return type:** `KX_GameObject`

**Returns:** the first object hit or None if no object or object does not match prop

```python

# Gets an object with a property "wall" in front of the camera within a distance of 100:
target = camera.getScreenRay(0.5, 0.5, 100, "wall")
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### shake(trauma, duration=0.0)

 `method`

Shakes the camera. `trauma` goes from 0 to 1 and adds to the World earthquake. With `duration`, the shake fades in that time; without it, it decreases at `shakeDecay` per second.

#### cameraSpeed

*(new in Anastacio)* `attribute · read-only`

Current camera speed (units per second), used by speed-based effects.

#### catEyeStrength

*(new in Anastacio)* `attribute`

Strength of the "cat eye" bokeh of the depth of field (DOF), from 0.0 to 1.0: circles get flattened near the edges.

#### chromaticStrength

*(new in Anastacio)* `attribute`

Chromatic aberration strength, from 0.0 to 5.0.

#### directionalBlurMax

*(new in Anastacio)* `attribute`

Directional blur limit (trail when turning the camera), from 0.0 to 0.2.

#### directionalBlurStrength

*(new in Anastacio)* `attribute`

Directional blur strength, from 0.0 to 2.0.

#### dofBlur

*(new in Anastacio)* `attribute`

Maximum depth of field (DOF) blur size, from 0 to 32.

#### dofQuality

*(new in Anastacio)* `attribute`

DOF quality: 0 low, 1 medium, 2 high.

#### droneAmplitude

*(new in Anastacio)* `attribute`

Sway amplitude of the Drone tracking mode (0 to 20).

#### droneFrequency

*(new in Anastacio)* `attribute`

Sway frequency of the Drone mode (0 to 20).

#### fisheyeStrength

*(new in Anastacio)* `attribute`

Fisheye distortion, from -1.0 (pincushion) to 1.0 (barrel).

#### focusDistance

*(new in Anastacio)* `attribute · read-only`

Focus distance used this frame, after smoothing.

#### focusManualDistance

*(new in Anastacio)* `attribute`

Focus distance when `focusMode` is 0 (manual).

#### focusMode

*(new in Anastacio)* `attribute`

How focus is chosen: 0 manual (`focusManualDistance`), 1 object (`focusObject`), 2 property (`focusProperty`), 3 automatic (ray at the screen point).

#### focusObject

*(new in Anastacio)* `attribute`

Object in focus when `focusMode` is 1. `None` for none.

#### focusPosition

*(new in Anastacio)* `attribute · read-only`

World position of the focus point, or `None`.

#### focusProperty

*(new in Anastacio)* `attribute`

Name of the game property used when `focusMode` is 2: focuses the closest object that has it true.

#### focusRange

*(new in Anastacio)* `attribute`

Distance range around the focus that stays sharp.

#### focusScreenPosition

*(new in Anastacio)* `attribute · read-only`

Screen position (0 to 1) of the focus point.

#### focusSmooth

*(new in Anastacio)* `attribute`

Focus change smoothing, from 0 (instant) to 10.

#### focusTarget

*(new in Anastacio)* `attribute · read-only`

Object in focus right now, or `None`.

#### focusValid

*(new in Anastacio)* `attribute · read-only`

`True` when focus found a target this frame.

#### gazeDirection

*(new in Anastacio)* `attribute · read-only`

Direction the camera is looking at, in world space.

#### shakeAmplitude

*(new in Anastacio)* `attribute`

Maximum shake amplitude (0 to 0.5).

#### shakeDecay

*(new in Anastacio)* `attribute`

How much the shake decreases per second (0 to 20).

#### shakeFrequency

*(new in Anastacio)* `attribute`

Shake frequency (0 to 60).

#### shakeTrauma

*(new in Anastacio)* `attribute · read-only`

Current shake trauma (0 to 1).

#### speedBlurMaxSpeed

*(new in Anastacio)* `attribute`

Speed at which the speed blur reaches its maximum.

#### speedBlurStrength

*(new in Anastacio)* `attribute`

Speed blur strength, from 0.0 to 2.0.

#### speedOverride

*(new in Anastacio)* `attribute`

Speed used by the effects instead of the real speed. -1 turns it off and goes back to the real one.

#### trackBank

*(new in Anastacio)* `attribute`

Camera side tilt in tracking turns (0 to 5).

#### trackDeadzone

*(new in Anastacio)* `attribute`

Tracking dead zone: the target can move within this screen margin without the camera turning (0 to 0.5).

#### trackLimit

*(new in Anastacio)* `attribute`

Maximum angle, in radians, tracking can turn the camera.

#### trackMode

*(new in Anastacio)* `attribute`

Tracking mode: 0 off, 1 look at target, 2 drone.

#### trackOrientation

*(new in Anastacio)* `attribute · read-only`

Orientation computed by tracking this frame.

#### trackScreenOffset

*(new in Anastacio)* `attribute`

Target offset `[x, y]` on screen, from -0.5 to 0.5.

#### trackSpeed

*(new in Anastacio)* `attribute`

How fast the camera turns to the target (0 to 10).

#### useBlurProtect

*(new in Anastacio)* `attribute`

Protects the center of the screen from blurs.

#### useCatEye

*(new in Anastacio)* `attribute`

Turns on cat eye bokeh in the DOF.

#### useChromatic

*(new in Anastacio)* `attribute`

Turns on chromatic aberration.

#### useChromaticSpeed

*(new in Anastacio)* `attribute`

Makes chromatic aberration grow with speed.

#### useDirectionalBlur

*(new in Anastacio)* `attribute`

Turns on directional blur.

#### useDof

*(new in Anastacio)* `attribute`

Turns on depth of field (DOF).

#### useShakeRoll

*(new in Anastacio)* `attribute`

The shake also rolls the camera around the view axis.

#### useSpeedBlur

*(new in Anastacio)* `attribute`

Turns on speed blur.

#### useTrackUpLock

*(new in Anastacio)* `attribute`

Keeps the camera "up" fixed during tracking.

#### useVignette

*(new in Anastacio)* `attribute`

Turns on the vignette (dark edges).

#### vignetteRadius

*(new in Anastacio)* `attribute`

Vignette radius (0 to 2).

#### vignetteStrength

*(new in Anastacio)* `attribute`

Vignette strength (0 to 1).

---

## KX_CameraActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Applies changes to a camera.

```python
# Make the camera follow another object, at a set distance.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Camera"]

act.object = Range.logic.getCurrentScene().objects["Car"]
act.min = 4.0
act.max = 8.0
act.height = 2.5
act.damping = 0.1
cont.activate(act)
```

#### damping

strength of of the camera following movement.

**Type:** float

#### axis

The camera axis (0, 1, 2) for positive `XYZ`, (3, 4, 5) for negative `XYZ`.

**Type:** int

#### min

minimum distance to the target object maintained by the actuator.

**Type:** float

#### max

maximum distance to stay from the target object.

**Type:** float

#### height

height to stay above the target object.

**Type:** float

#### object

the object this actuator tracks.

**Type:** `KX_GameObject` or None

---

## KX_ChangeColorActuator

Class `Range.types.KX_ChangeColorActuator`.

```python
# Fade the color of the object to red.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["ChangeColor"]

act.color = [1.0, 0.0, 0.0, 1.0]
act.useLerp = True
act.lerp = 0.2
cont.activate(act)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### color

 `attribute`

Color `[r, g, b, a]` applied by the actuator.

#### lerp

 `attribute`

Color transition speed when `useLerp` is on (0.1 to 1.0).

#### useLerp

 `attribute`

Makes the color change gradually instead of all at once.

---

## KX_CharacterWrapper

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`KX_GameObject`](#kx_gameobject), [`Range.constraints`](#rangeconstraints)

A wrapper to expose character physics options.

> **Note:**
When the character's object is removed, every method and attribute of the wrapper raises
`ReferenceError`. Suspending physics keeps the character, so the wrapper still works.

```python
# Walk and jump with a Character object.
import Range
from Range import constraints

own = Range.logic.getCurrentController().owner
character = constraints.getCharacter(own)
keys = Range.logic.keyboard.inputs

speed = 0.1 if keys[Range.events.WKEY].active else 0.0
character.walkDirection = (0.0, speed, 0.0)

if keys[Range.events.SPACEKEY].activated and character.onGround:
    character.jump()
```

```python
# Crouch, and stand up when there is room.
import Range
from Range import constraints

own = Range.logic.getCurrentController().owner
character = constraints.getCharacter(own)
crouch = Range.logic.keyboard.inputs[Range.events.LEFTCTRLKEY].active

if crouch:
    character.posture = "CROUCH"
elif character.canStand:
    character.posture = "STAND"
```

```python
# Allow a double jump.
import Range
from Range import constraints

character = constraints.getCharacter(Range.logic.getCurrentController().owner)

character.maxJumps = 2
character.jumpSpeed = 8.0
```

#### onGround

Whether or not the character is on the ground. (read-only)

**Type:** boolean

#### gravity

The gravity value used for the character.

**Type:** float

#### fallSpeed

The character falling speed.

**Type:** float

#### maxJumps

The maximum number of jumps a character can perform before having to touch the ground. By default this is set to 1. 2 allows for a double jump, etc.

**Type:** int in [0, 255], default 1

#### jumpCount

The current jump count. This can be used to have different logic for a single jump versus a double jump. For example, a different animation for the second jump.

**Type:** int

#### jumpSpeed

The character jumping speed.

**Type:** float

#### maxSlope

The maximum slope which the character can climb.

**Type:** float

#### walkDirection

The speed and direction the character is traveling in using world coordinates. This should be used instead of applyMovement() to properly move the character.

**Type:** Vector((x, y, z))

#### jump()

The character jumps based on it's jump speed.

#### jumpDirection

The direction the character is jumping.

**Type:** Vector((x, y, z))

#### setVelocity(velocity, time, local=False)

Sets the character's linear velocity for a given period.

This method sets character's velocity through it's center of mass during a period.

- **`velocity`**: Linear velocity vector.
  - type: 3D Vector
- **`time`**: Period while applying linear velocity.
  - type: float
- **`local`**:  * False: you get the "global" velocity ie: relative to world orientation. * True: you get the "local" velocity ie: relative to object orientation.
  - type: boolean

#### smoothMovement

Smooth movement caused by walking direction.

**Type:** float (0.0 to 1.0)

#### posture

Current posture (the collision shape in use). Setting it asks for a new posture;
standing up waits until there is room above the character (see `canStand`).

**Type:** string, one of `'STAND'`, `'CROUCH'`, `'CRAWL'`, `'JUMP_TUCK'`

#### canStand

True when there is room to stand up from the current posture.

**Type:** boolean (read-only)

#### running

Run mode: while True the character walks with the object's Run Speed factor.

**Type:** boolean

#### reset()

Resets the character velocity and walk direction.

---

## KX_CollisionContactPoint

Base class: [`EXP_Value`](#exp_value)

A collision contact point passed to the collision callbacks.

```python

import Range

def oncollision(object, point, normal, points):
    print("Hit by", object)
    for point in points:
        print(point.localPointA)
        print(point.localPointB)
        print(point.worldPoint)
        print(point.normal)
        print(point.combinedFriction)
        print(point.combinedRestitution)
        print(point.appliedImpulse)

cont = Range.logic.getCurrentController()
own = cont.owner
own.collisionCallbacks = [oncollision]
```

#### localPointA

The contact point in the owner object space.

**Type:** `mathutils.Vector`

#### localPointB

The contact point in the collider object space.

**Type:** `mathutils.Vector`

#### worldPoint

The contact point in world space.

**Type:** `mathutils.Vector`

#### normal

The contact normal in owner object space.

**Type:** `mathutils.Vector`

#### combinedFriction

The combined friction of the owner and collider object.

**Type:** float

#### combinedRollingFriction

The combined rolling friction of the owner and collider object.

**Type:** float

#### combinedRestitution

The combined restitution of the owner and collider object.

**Type:** float

#### appliedImpulse

The applied impulse to the owner object.

**Type:** float

---

## KX_CollisionSensor

Base class: [`SCA_ISensor`](#sca_isensor)

Collision sensor detects collisions between objects.

```python
# See what hit the object.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Collision"]

if sensor.positive:
    for obj in sensor.hitObjectList:
        print(obj.name)
```

```python
# Only detect objects with the coin property.
import Range

sensor = Range.logic.getCurrentController().sensors["Collision"]

sensor.propName = "coin"
sensor.useMaterial = False
```

#### propName

The property or material to collide with.

**Type:** string

#### useMaterial

Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property.

**Type:** boolean

#### usePulseCollision

When enabled, changes to the set of colliding objects generate a pulse.

**Type:** boolean

#### hitObject

The last collided object. (read-only).

**Type:** `KX_GameObject` or None

#### hitObjectList

A list of colliding objects. (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`

#### hitMaterial

The material of the object in the face hit by the ray. (read-only).

**Type:** string

---

## KX_ConstraintActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

A constraint actuator limits the position, rotation, distance or orientation of an object.

```python
# Keep the object at a distance from the ground.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Constraint"]

act.distance = 1.5
act.rayLength = 5.0
act.damp = 10
cont.activate(act)
```

#### damp

Time constant of the constraint expressed in frame (not use by Force field constraint).

**Type:** integer

#### rotDamp

Time constant for the rotation expressed in frame (only for the distance constraint), 0 = use damp for rotation as well.

**Type:** integer

#### direction

The reference direction in world coordinate for the orientation constraint.

**Type:** `mathutils.Vector`

#### option

Binary combination of `these constants`

**Type:** integer

#### time

activation time of the actuator. The actuator disables itself after this many frame. If set to 0, the actuator is not limited in time.

**Type:** integer

#### propName

the name of the property or material for the ray detection of the distance constraint.

**Type:** string

#### min

The lower bound of the constraint. For the rotation and orientation constraint, it represents radiant.

**Type:** float

#### distance

the target distance of the distance constraint.

**Type:** float

#### max

the upper bound of the constraint. For rotation and orientation constraints, it represents radiant.

**Type:** float

#### rayLength

the length of the ray of the distance constraint.

**Type:** float

#### limit

type of constraint. Use one of the `these constants`

**Type:** integer.

---

## KX_ConstraintWrapper

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

KX_ConstraintWrapper

> **Note:**
When the constraint is deleted (`Range.constraints.removeConstraint` or removing one of
its objects), every method and attribute of the wrapper raises `ReferenceError`.
Suspending physics keeps the constraint, so the wrapper still works.

```python
# Limit how far a hinge can open.
import math
import Range
from Range import constraints

scene = Range.logic.getCurrentScene()
door = scene.objects["Door"]
frame = scene.objects["Frame"]

hinge = constraints.createConstraint(
    door.getPhysicsId(), frame.getPhysicsId(),
    constraints.LINEHINGE_CONSTRAINT)

hinge.setParam(3, 0.0, math.radians(90.0))
```

```python
# Break the connection when the force is too strong.
hinge.breakingThreshold = 50.0
print(hinge.constraint_id, hinge.enabled)
```

#### getConstraintId(val)

Returns the contraint ID

**Returns:** the constraint ID

**Return type:** integer

#### setParam(axis, value0, value1)

Set the contraint limits

- **`axis`**: 
  - type: integer

> **Note:**
* Lowerlimit == Upperlimit -> axis is locked
* Lowerlimit > Upperlimit -> axis is free
* Lowerlimit < Upperlimit -> axis it limited in that range

For PHY_LINEHINGE_CONSTRAINT = 2 or PHY_ANGULAR_CONSTRAINT = 3:

axis = 3 is a constraint limit, with low/high limit value
* 3: X axis angle

- **`value0 (min)`**: Set the minimum limit of the axis
  - type: float
- **`value1 (max)`**: Set the maximum limit of the axis
  - type: float
For PHY_CONE_TWIST_CONSTRAINT = 4:

axis = 3..5 are constraint limits, high limit values
* 3: X axis angle
* 4: Y axis angle
* 5: Z axis angle

- **`value0 (min)`**: Set the minimum limit of the axis
  - type: float
- **`value1 (max)`**: Set the maximum limit of the axis
  - type: float
For PHY_GENERIC_6DOF_CONSTRAINT = 12:

axis = 0..2 are constraint limits, with low/high limit value
* 0: X axis position
* 1: Y axis position
* 2: Z axis position

axis = 3..5 are relative constraint (Euler) angles in radians
* 3: X axis angle
* 4: Y axis angle
* 5: Z axis angle

- **`value0 (min)`**: Set the minimum limit of the axis
  - type: float
- **`value1 (max)`**: Set the maximum limit of the axis
  - type: float
axis = 6..8 are translational motors, with value0=target velocity, value1 = max motor force
* 6: X axis position
* 7: Y axis position
* 8: Z axis position

axis = 9..11 are rotational motors, with value0=target velocity, value1 = max motor force
* 9: X axis angle
* 10: Y axis angle
* 11: Z axis angle

- **`value0 (speed)`**: Set the linear velocity of the axis
  - type: float Range: -10,000.00 to 10,000.00
- **`value1 (force)`**: Set the maximum force limit of the axis
  - type: float Range: -10,000.00 to 10,000.00
axis = 12..14 are for linear springs on each of the position of freedom
* 12: X axis position
* 13: Y axis position
* 14: Z axis position

axis = 15..17 are for angular springs on each of the angle of freedom in radians
* 15: X axis angle
* 16: Y axis angle
* 17: Z axis angle

- **`value0 (stiffness)`**: Set the stiffness of the spring
  - type: float
- **`value1 (damping)`**: Tendency of the spring to return to it's original position
  - type: float 1.0 = springs back to original position (no damping) 0.0 = don't springs back

#### getParam(axis)

Get the contraint position or euler angle of a generic 6DOF constraint

- **`axis`**: 
  - type: integer
axis = 0..2 are linear constraint values
* 0: X axis position
* 1: Y axis position
* 2: Z axis position

**Returns:** position

**Return type:** float

axis = 3..5 are relative constraint (Euler) angles in radians
* 3: X axis angle
* 4: Y axis angle
* 5: Z axis angle

**Returns:** angle

**Return type:** float

#### constraint_id

Returns the contraint ID  (read only)

**Type:** integer

#### constraint_type

Returns the contraint type (read only)

**Type:** integer - `POINTTOPOINT_CONSTRAINT` - `LINEHINGE_CONSTRAINT` - `ANGULAR_CONSTRAINT` - `CONETWIST_CONSTRAINT` - `VEHICLE_CONSTRAINT` - `GENERIC_6DOF_CONSTRAINT`

#### breakingThreshold

The impulse threshold breaking the constraint, if the constraint is broken `enabled` is set to `False`.

**Type:** float greater or equal to 0

#### enabled

The status of the constraint. Set to `True` to restore a constraint after breaking.

**Type:** boolean

---

## KX_CubeMap

Base class: [`KX_TextureRenderer`](#kx_texturerenderer)

> **See also:**
[`KX_PlanarMap`](#kx_planarmap), [`KX_TextureRenderer`](#kx_texturerenderer)

Python API for realtime cube map textures.

```python

import Range

scene = Range.logic.getCurrentScene()
# The object using a realtime cube map in its material.
obj = scene.objects["Suzanne"]

mat = obj.meshes[0].materials[0]
# Obtain the realtime cube map from the material texture.
cubemap = mat.textures[0].renderer

# Set the render position to the "Cube" object position.
cubemap.viewpointObject = scene.objects["Cube"]

# Change the culling clip start and clip end.
cubemap.clipStart = 5.0
cubemap.clipEnd = 20.0

# Disable render on third layer.
cubemap.ignoreLayers = (1 << 2)

# Disable per frame update.
cubemap.autoUpdate = False
# Ask to update for this frame only.
cubemap.update()
```

---

## KX_DynamicActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Dynamic Actuator.

```python
# Change the mass of the object.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Dynamics"]

act.mode = Range.logic.KX_DYN_SET_MASS
act.mass = 5.0
cont.activate(act)
```

```python
# Turn the physics of the object off.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Dynamics"]

act.mode = Range.logic.KX_DYN_DISABLE_DYNAMICS
cont.activate(act)
```

#### mode

**Type:** integer

the type of operation of the actuator, 0-4

* KX_DYN_RESTORE_DYNAMICS(0)
* KX_DYN_DISABLE_DYNAMICS(1)
* KX_DYN_ENABLE_RIGID_BODY(2)
* KX_DYN_DISABLE_RIGID_BODY(3)
* KX_DYN_SET_MASS(4)

#### mass

the mass value for the KX_DYN_SET_MASS operation.

**Type:** float

---

## KX_EndObjectActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Edit Object Actuator (in End Object mode)

This actuator has no python methods.

```python
# Remove the object when its life runs out.
import Range

cont = Range.logic.getCurrentController()

if cont.owner["life"] <= 0:
    cont.activate(cont.actuators["EndObject"])
```

---

## KX_FontObject

Base class: [`KX_GameObject`](#kx_gameobject)

A Font object.

```python

# Display a message about the exit key using a Font object.
import Range

co = Range.logic.getCurrentController()
font = co.owner

exit_key = Range.events.EventToString(Range.logic.getExitKey())

if exit_key.endswith("KEY"):
    exit_key = exit_key[:-3]

font.text = "Press key '%s' to quit the game." % exit_key
```

```python

# Show the score stored in a game property.
import Range

font = Range.logic.getCurrentController().owner
font.text = "Score: %d" % font["score"]
```

```python

# Center the text on the X axis, using its current width.
import Range

font = Range.logic.getCurrentController().owner
font.text = "Game Over"
font.localPosition.x = -font.dimensions.x / 2
```

```python

# Reveal the text one letter at a time. Run it every frame (Always sensor with True Pulse).
import Range

font = Range.logic.getCurrentController().owner

if font.visibleCharacters < font.characterCount:
    font.visibleCharacters += 1
```

```python

# Add a dark shadow behind the text.
import Range

font = Range.logic.getCurrentController().owner
font.useShadows = True
font.shadowColor = [0.0, 0.0, 0.0, 0.8]
font.shadowOffset = [0.02, -0.02]
```

#### text

The text displayed by this Font object.

**Type:** string

#### resolution

The resolution of the font police.

> **Caution:**
High resolution can use a lot of memory and may crash.

**Type:** float (0.1 to 50.0)

#### size

The size (scale factor) of the font object, scaled from font object origin (affects text resolution).

> **Caution:**
High size can use a lot of memory and may crash.

**Type:** float (0.0001 to 40.0)

#### dimensions

The size (width and height) of the current text in Blender Units.

**Type:** `mathutils.Vector`

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### atlas

*(new in Anastacio)* `attribute`

Name of the text data holding the Bitmap Atlas used for drawing, `""` for the text's own atlas, or `None` for no atlas.

#### characterCount

*(new in Anastacio)* `attribute · read-only`

Total number of characters in the text. Read-only.

#### font

*(new in Anastacio)* `attribute`

Name of the text's font (as shown in the Text properties), or `None`. Changing it redraws the text immediately; an unknown name raises `ValueError`.

#### lines

*(new in Anastacio)* `attribute · read-only`

List of the text lines after wrapping. Read-only.

#### page

*(new in Anastacio)* `attribute`

Current page of the text box, from 0. Out-of-range values are clamped to the last valid page.

#### pageCount

*(new in Anastacio)* `attribute · read-only`

Number of pages in the text box. Read-only.

#### shadowColor

 `attribute`

Text shadow color `[r, g, b, a]`.

#### shadowOffset

 `attribute`

Text shadow offset `[x, y]`.

#### textBox

*(new in Anastacio)* `attribute`

Size `(width, height)` of the text box. The text wraps and splits into pages to fit it; `(0, 0)` turns it off.

#### translationKey

*(new in Anastacio)* `attribute`

Key in the language table (`locale/translations.csv`). With a key, the text shows the translation for the current `Range.locale` language and updates by itself when the language changes. `""` turns it off.

#### useLanguageFont

*(new in Anastacio)* `attribute`

When `True`, the text uses the font and atlas set for the current language in `locale/locale.json` (useful for Russian, Japanese, etc.).

#### useShadows

 `attribute`

Turns on the text shadow.

#### visibleCharacters

*(new in Anastacio)* `attribute`

How many characters are shown, for the typewriter effect. `-1` shows everything.

---

## KX_GameActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

The game actuator loads a new .blend file, restarts the current .blend file or quits the game.

```python
# Restart the game.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Game"]

act.mode = Range.logic.KX_GAME_RESTART
cont.activate(act)
```

```python
# Open another game file.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Game"]

act.mode = Range.logic.KX_GAME_START
act.fileName = "//level2.range"
cont.activate(act)
```

#### fileName

the new .blend file to load.

**Type:** string

#### mode

The mode of this actuator. Can be on of `these constants`

**Type:** Int

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### extensionName

 `attribute`

File extension used by the save/load game modes.

#### saveLocation

 `attribute`

Folder where the actuator saves and loads the game.

---

## KX_GameObject

Base class: [`SCA_IObject`](#sca_iobject)

> **See also:**
[`KX_Scene`](#kx_scene), [`KX_Mesh`](#kx_mesh), [`KX_PythonComponent`](#kx_pythoncomponent), [`KX_VehicleWrapper`](#kx_vehiclewrapper), [`KX_ParticleSystem`](#kx_particlesystem)

All game objects are derived from this class.

Properties assigned to game objects are accessible as attributes of this class.

> **Note:**
Calling ANY method or attribute on an object that has been removed from a scene will raise a SystemError,
if an object may have been removed since last accessing it use the `invalid` attribute to check.

KX_GameObject can be subclassed to extend functionality. For example:

```python

import Range

class CustomGameObject(Range.types.KX_GameObject):
    RATE = 0.05

    def __init__(self, old_owner):
        # "old_owner" can just be ignored. At this point, "self" is
        # already the object in the scene, and "old_owner" has been
        # destroyed.

        # New attributes can be defined - but we could also use a game
        # property, like "self['rate']".
        self.rate = CustomGameObject.RATE

    def update(self):
        self.worldPosition.z += self.rate

        # switch direction
        if self.worldPosition.z > 1.0:
            self.rate = -CustomGameObject.RATE
        elif self.worldPosition.z < 0.0:
            self.rate = CustomGameObject.RATE

# Called first
def mutate(cont):
    old_object = cont.owner
    mutated_object = CustomGameObject(cont.owner)

    # After calling the constructor above, references to the old object
    # should not be used.
    assert(old_object is not mutated_object)
    assert(old_object.invalid)
    assert(mutated_object is cont.owner)

# Called later - note we are now working with the mutated object.
def update(cont):
    cont.owner.update()
```

When subclassing objects other than empties and meshes, the specific type
should be used - e.g. inherit from `BL_ArmatureObject` when the object
to mutate is an armature.

```python

# Move and turn the object with W and A. Run it every frame (Always sensor with True Pulse).
import Range

obj = Range.logic.getCurrentController().owner
keys = Range.logic.keyboard.events

if keys[Range.events.WKEY]:
    obj.applyMovement((0, 0.1, 0), True)
if keys[Range.events.AKEY]:
    obj.applyRotation((0, 0, 0.05), True)
```

```python

# Read and change game properties.
import Range

obj = Range.logic.getCurrentController().owner

obj["health"] = obj.get("health", 100) - 10

if obj["health"] <= 0:
    obj.endObject()
```

```python

# Look for the ground under the object.
import Range

obj = Range.logic.getCurrentController().owner
below = obj.worldPosition - obj.getAxisVect((0, 0, 1))

hit, point, normal = obj.rayCast(below, obj, 10.0)

if hit is not None:
    print(hit.name, point)
```

```python

# Chase the player when it comes close.
import Range

scene = Range.logic.getCurrentScene()
obj = Range.logic.getCurrentController().owner
player = scene.objects["Player"]

if obj.getDistanceTo(player) < 15.0:
    distance, direction, local = obj.getVectTo(player)
    obj.alignAxisToVect(direction, 1, 0.1)
    obj.applyMovement((0, 0.05, 0), True)
```

```python

# Play the frames 1 to 30 of an action.
import Range

obj = Range.logic.getCurrentController().owner

if not obj.isPlayingAction():
    obj.playAction("Walk", 1, 30)
```

```python

# Attach the object to a hand, and release it later.
import Range

scene = Range.logic.getCurrentScene()
obj = Range.logic.getCurrentController().owner

obj.setParent(scene.objects["Hand"])

# Later:
obj.removeParent()
```

#### name

The object's name.

**Type:** string

#### mass

The object's mass

**Type:** float

> **Note:**
The object must have a physics controller for the mass to be applied, otherwise the mass value will be returned as 0.0.

#### friction

The object's friction

**Type:** float

#### isSuspendDynamics

The object's dynamic state (read-only).

**Type:** boolean

> **Tip:**
:py:meth:`suspendDynamics` and :py:meth:`restoreDynamics` allow you to change the state.

#### linearDamping

The object's linear damping, also known as translational damping. Can be set simultaneously with angular damping using the :py`setDamping` method.

**Type:** float between 0 and 1 inclusive.

> **Note:**
The object must have a physics controller for the linear damping to be applied, otherwise the value will be returned as 0.0.

#### angularDamping

The object's angular damping, also known as rotationation damping. Can be set simultaneously with linear damping using the :py`setDamping` method.

**Type:** float between 0 and 1 inclusive.

> **Note:**
The object must have a physics controller for the angular damping to be applied, otherwise the value will be returned as 0.0.

#### linVelocityMin

Enforces the object keeps moving at a minimum velocity.

**Type:** float

> **Note:**
Applies to dynamic and rigid body objects only.

> **Note:**
A value of 0.0 disables this option.

> **Note:**
While objects are stationary the minimum velocity will not be applied.

#### linVelocityMax

Clamp the maximum linear velocity to prevent objects moving beyond a set speed.

**Type:** float

> **Note:**
Applies to dynamic and rigid body objects only.

> **Note:**
A value of 0.0 disables this option (rather than setting it stationary).

#### angularVelocityMin

Enforces the object keeps rotating at a minimum velocity. A value of 0.0 disables this.

**Type:** non-negative float

> **Note:**
Applies to dynamic and rigid body objects only.
While objects are stationary the minimum velocity will not be applied.

#### angularVelocityMax

Clamp the maximum angular velocity to prevent objects rotating beyond a set speed.
A value of 0.0 disables clamping; it does not stop rotation.

**Type:** non-negative float

> **Note:**
Applies to dynamic and rigid body objects only.

#### localInertia

the object's inertia vector in local coordinates. Read only.

**Type:** Vector((ix, iy, iz))

#### parent

The object's parent object. (read-only).

**Type:** `KX_GameObject` or None

#### groupMembers

Returns the list of group members if the object is a group object (dupli group instance), otherwise None is returned.

**Type:** `EXP_ListValue` of `KX_GameObject` or None

#### groupObject

Returns the group object (dupli group instance) that the object belongs to or None if the object is not part of a group.

**Type:** `KX_GameObject` or None

#### collisionGroup

The object's collision group.

**Type:** bitfield

#### collisionMask

The object's collision mask.

**Type:** bitfield

#### collisionCallbacks

A list of functions to be called when a collision occurs.

**Type:** list of functions and/or methods

Callbacks should either accept one argument `(object)`, or four
arguments `(object, point, normal, points)`. For simplicity, per
colliding object the first collision point is reported in second
and third argument.

```python

# Function form
def callback_four(object, point, normal, points):
    print('Hit by %r with %i contacts points' % (object.name, len(points)))

def callback_three(object, point, normal):
    print('Hit by %r at %s with normal %s' % (object.name, point, normal))

def callback_one(object):
    print('Hit by %r' % object.name)

def register_callback(controller):
    controller.owner.collisionCallbacks.append(callback_four)
    controller.owner.collisionCallbacks.append(callback_three)
    controller.owner.collisionCallbacks.append(callback_one)

# Method form
class YourGameEntity(Range.types.KX_GameObject):
    def __init__(self, old_owner):
        self.collisionCallbacks.append(self.on_collision_four)
        self.collisionCallbacks.append(self.on_collision_three)
        self.collisionCallbacks.append(self.on_collision_one)

    def on_collision_four(self, object, point, normal, points):
        print('Hit by %r with %i contacts points' % (object.name, len(points)))

    def on_collision_three(self, object, point, normal):
        print('Hit by %r at %s with normal %s' % (object.name, point, normal))

    def on_collision_one(self, object):
        print('Hit by %r' % object.name)
```

> **Note:**
For backward compatibility, a callback with variable number of
arguments (using `*args`) will be passed only the `object`
argument. Only when there is more than one fixed argument (not
counting `self` for methods) will the four-argument form be
used.

#### scene

The object's scene. (read-only).

**Type:** `KX_Scene` or None

#### visible

visibility flag.

**Type:** boolean

> **Note:**
Game logic will still run for invisible objects.

#### layer

The layer mask used for shadow and real-time cube map render.

**Type:** bitfield

#### cullingBox

The object's bounding volume box used for culling.

**Type:** `KX_BoundingBox`

#### culled

Returns True if the object is culled, else False.

> **Caution:**
This variable returns an invalid value if it is called outside the scene's callbacks `KX_Scene.pre_draw` and `KX_Scene.post_draw`.

**Type:** boolean (read only)

#### color

The object color of the object. [r, g, b, a]

**Type:** `mathutils.Vector`

#### occlusion

occlusion capability flag.

**Type:** boolean

#### physicsCulling

True if the object suspends its physics depending on its nearest distance to any camera.

**Type:** boolean

#### physicsCullingVelocity

Stop physics after the object stops.

**Type:** boolean

#### logicCulling

True if the object suspends its logic and animation depending on its nearest distance to any camera.

**Type:** boolean

#### logicCullingComponents

No Suspend execution of object components.

**Type:** boolean

#### physicsCullingRadius

Suspend object's physics if this radius is smaller than its nearest distance to any camera
and `physicsCulling` set to `True`.

**Type:** float

#### logicCullingRadius

Suspend object's logic and animation if this radius is smaller than its nearest distance to any camera
and `logicCulling` set to `True`.

**Type:** float

#### ~~position~~

The object's position. [x, y, z] On write: local position, on read: world position

> **Deprecated use :data:`localPosition` and :data:`worldPosition`.:**

**Type:** `mathutils.Vector`

#### ~~orientation~~

The object's orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector. On write: local orientation, on read: world orientation

> **Deprecated use :data:`localOrientation` and :data:`worldOrientation`.:**

**Type:** `mathutils.Matrix`

#### ~~scaling~~

The object's scaling factor. [sx, sy, sz] On write: local scaling, on read: world scaling

> **Deprecated use :data:`localScale` and :data:`worldScale`.:**

**Type:** `mathutils.Vector`

#### localOrientation

The object's local orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector.

**Type:** `mathutils.Matrix`

#### worldOrientation

The object's world orientation. 3x3 Matrix.

**Type:** `mathutils.Matrix`

#### localScale

The object's local scaling factor. [sx, sy, sz]

**Type:** `mathutils.Vector`

#### worldScale

The object's world scaling factor. [sx, sy, sz]

**Type:** `mathutils.Vector`

#### localPosition

The object's local position. [x, y, z]

**Type:** `mathutils.Vector`

#### worldPosition

The object's world position. [x, y, z]

**Type:** `mathutils.Vector`

#### localTransform

The object's local space transform matrix. 4x4 Matrix.

**Type:** `mathutils.Matrix`

#### worldTransform

The object's world space transform matrix. 4x4 Matrix.

**Type:** `mathutils.Matrix`

#### localLinearVelocity

The object's local linear velocity. [x, y, z]

**Type:** `mathutils.Vector`

#### worldLinearVelocity

The object's world linear velocity. [x, y, z]

**Type:** `mathutils.Vector`

#### localAngularVelocity

The object's local angular velocity. [x, y, z]

**Type:** `mathutils.Vector`

#### worldAngularVelocity

The object's world angular velocity. [x, y, z]

**Type:** `mathutils.Vector`

#### gravity

The object's gravity. [x, y, z]

**Type:** `mathutils.Vector`

#### timeOffset

adjust the slowparent delay at runtime.

**Type:** float

#### state

the game object's state bitmask, using the first 30 bits, one bit must always be set.

**Type:** int

#### meshes

a list meshes for this object.

**Type:** list of `KX_Mesh`

> **Note:**
Most objects use only 1 mesh.

> **Note:**
Changes to this list will not update the KX_GameObject.

#### batchGroup

The object batch group containing the batched mesh.

**Type:** `KX_BatchGroup`

#### sensors

a sequence of `SCA_ISensor` objects with string/index lookups and iterator support.

**Type:** list

> **Note:**
This attribute is experimental and may be removed (but probably wont be).

> **Note:**
Changes to this list will not update the KX_GameObject.

#### controllers

a sequence of `SCA_IController` objects with string/index lookups and iterator support.

**Type:** list of `SCA_ISensor`

> **Note:**
This attribute is experimental and may be removed (but probably wont be).

> **Note:**
Changes to this list will not update the KX_GameObject.

#### actuators

a list of `SCA_IActuator` with string/index lookups and iterator support.

**Type:** list

> **Note:**
This attribute is experemental and may be removed (but probably wont be).

> **Note:**
Changes to this list will not update the KX_GameObject.

#### attrDict

get the objects internal python attribute dictionary for direct (faster) access.

**Type:** dict

#### components

All python components.

**Type:** `EXP_ListValue` of `KX_PythonComponent`'s

#### children

direct children of this object, (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`'s

#### childrenRecursive

all children of this object including children's children, (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`'s

#### life

The number of frames until the object ends, assumes one frame is 1/50 second (read-only).

**Type:** float

#### debug

If true, the object's debug properties will be displayed on screen.

**Type:** boolean

#### debugRecursive

If true, the object's and children's debug properties will be displayed on screen.

**Type:** boolean

#### currentLodLevel

The index of the level of detail (LOD) currently used by this object (read-only).

**Type:** int

#### lodManager

Return the lod manager of this object.
Needed to access to lod manager to set attributes of levels of detail of this object.
The lod manager is shared between instance objects and can be changed to use the lod levels of an other object.
If the lod manager is set to `None` the object's mesh backs to the mesh of the previous first lod level.

**Type:** `KX_LodManager`

#### isDestructible

True if Physics > Destruction is enabled on this object, also for objects on an inactive layer (read-only).

**Type:** boolean

#### isExplosive

True if Physics > Explosive is enabled on this object, also for objects on an inactive layer (read-only).

**Type:** boolean

#### breakImpulse

The impulse that breaks this destructible object, from a collision or from `KX_Scene.explode`.
Starts with the panel's Break Impulse; changing it affects only this instance.
Reads 0.0 on objects that are not destructible, and setting it on them raises AttributeError.

**Type:** float

#### fuse

Seconds left before this explosive object detonates. The fuse counts from the moment the object enters
the game (scene start or `KX_Scene.addObject`). 0.0 means no fuse; setting a value lights it.
Setting it on an object that is not explosive raises AttributeError.

**Type:** float

#### explosionRadius

Radius of the blast of this explosive object, in meters. Like every attribute of the
Explosive panel below, setting it on an object that is not explosive raises AttributeError.

**Type:** float

#### explosionForce

Impulse of the blast at its center; it falls to 0 at `explosionRadius`.

**Type:** float

#### upBias

Extra upward push of the blast (0 to 5), so objects fly up instead of sliding on the floor.

**Type:** float

#### useOcclusion

Static geometry between the blast and an object shields it.

**Type:** bool

#### explosionEffect

Object of an inactive layer added at the blast (fire, smoke, a sound). It must be an object of the scene file.

**Type:** `KX_GameObject` or None

#### effectLife

Seconds `explosionEffect` lives (0 = until its own logic removes it).

**Type:** float

#### useParticleExplosion

Built-in GPU particle explosion (core, smoke and debris) at the blast.

**Type:** bool

#### particleSize

Size preset of the particle explosion: `'TINY'`, `'SMALL'`, `'MEDIUM'`, `'LARGE'` or `'HUGE'`.
It also scales the ground mark.

**Type:** str

#### particleStyle

What the particle explosion is made of: `'FIRE'`, `'ELECTRIC'`, `'CONCRETE'` or `'WATER'`.
Setting it resets `fireColor`, `smokeColor` and `sparkColor` to the colors of the style.

**Type:** str

#### fireColor

Tint of the core of the particle explosion (white = the natural colors of the style).

**Type:** Vector((r, g, b))

#### smokeColor

Color of the smoke (dust cloud, mist) of the particle explosion when it is born.

**Type:** Vector((r, g, b))

#### sparkColor

Color of the sparks (debris, droplets) of the particle explosion.

**Type:** Vector((r, g, b))

#### fireAmount

How many core particles, relative to the size preset (0 to 4, 0 = none).

**Type:** float

#### smokeAmount

How much smoke, relative to the size preset (0 to 4, 0 = none).

**Type:** float

#### sparkAmount

How many sparks, relative to the size preset (0 to 4, 0 = none).

**Type:** float

#### smokeDuration

How long the smoke lasts, relative to the style (0.2 to 4).

**Type:** float

#### blastSpeed

How hard the particles are thrown out, relative to the size preset (0.2 to 4).

**Type:** float

#### useGroundMark

Paint the material of `groundMark` on the static surface under the blast.

**Type:** bool

#### useMarkNearby

With `useGroundMark`: also paint a smaller mark on the objects around the blast (12 closest).

**Type:** bool

#### groundMark

Mesh object of an inactive layer whose material is the ground mark. It must be an object of the scene file.

**Type:** `KX_GameObject` or None

#### markSize

Size of the ground mark, relative to `particleSize` (0.1 to 4).

**Type:** float

#### markLife

Seconds the ground mark stays (0 = forever).

**Type:** float

#### onBreak

A list of functions called when this object breaks, with the arguments `(object, fragments)`.
They run right after the fragments enter the scene, before any explosion pushes them.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Type:** list of functions and/or methods

```python

def on_break(obj, fragments):
    print('%s broke into %d pieces' % (obj.name, len(fragments)))

controller.owner.onBreak.append(on_break)
```

#### onExplode

A list of functions called when this object explodes, with the arguments `(object, position)`.
On an object that is both destructible and explosive, they run after `onBreak`.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Type:** list of functions and/or methods

#### onDent

A list of functions called when this deformable object dents (collision, explosion or
`dent`), with the arguments `(object, point, impulse)`: world hit point (the blast center
for an explosion) and hit strength, e.g. to play a metal sound or spawn sparks there.
Callbacks set on an object of an inactive layer are copied to every object added from it.

**Type:** list of functions and/or methods

#### endObject()

Delete this object, can be used in place of the EndObject Actuator.

The actual removal of the object from the scene is delayed.

#### shatter(origin=None, burst=None)

Break this destructible object now, replacing it by the pieces of its Fragments group.
On an object that is also explosive, it detonates as well.

- **`origin`**: The point the pieces fly away from, the object's position by default.
  - type: 3D Vector
- **`burst`**: The speed given to the pieces away from origin, the panel's Burst Speed by default.
  - type: float

**Returns:** The new pieces, an empty list if the object is not destructible or has already broken.

**Return type:** list of `KX_GameObject`

#### detonate()

Make this explosive object explode now: a blast like `KX_Scene.explode` with the panel's settings,
the Effect object, and the removal of the object. A destructible explosive breaks as well.

**Returns:** False if the object is not explosive or has already exploded.

**Return type:** boolean

#### dent(point, direction, impulse)

Dent this deformable object (Deformation panel) as a hit of the given strength: the vertices within
the panel's Radius of point move along direction (into the object) by
(impulse - Dent Impulse) * Depth, limited by Max Depth. Only this instance changes, other objects
sharing the mesh keep their shape.

- **`point`**: hit point in world space.
  - type: 3D vector
- **`direction`**: hit direction in world space, flipped to point into the object.
  - type: 3D vector
- **`impulse`**: hit strength (N*s), compared with Dent Impulse.
  - type: float

**Returns:** False if the object is not deformable, the impulse is too weak or no vertex moved.

**Return type:** boolean

#### resetDent()

Restore the shape of a dented object.

**Returns:** False if the object was never dented.

**Return type:** boolean

#### replaceMesh(mesh, useDisplayMesh=True, usePhysicsMesh=False)

Replace the mesh of this object with a new mesh. This works the same was as the actuator.

- **`mesh`**: mesh to replace or the meshes name.
  - type: `MeshProxy` or string
- **`useDisplayMesh`**: when enabled the display mesh will be replaced (optional argument).
  - type: boolean
- **`usePhysicsMesh`**: when enabled the physics mesh will be replaced (optional argument).
  - type: boolean

#### setVisible(visible[, recursive])

Sets the game object's visible flag.

- **`visible`**: the visible state to set.
  - type: boolean
- **`recursive`**: optional argument to set all childrens visibility flag too, defaults to False if no value passed.
  - type: boolean

#### setOcclusion(occlusion[, recursive])

Sets the game object's occlusion capability.

- **`occlusion`**: the state to set the occlusion to.
  - type: boolean
- **`recursive`**: optional argument to set all childrens occlusion flag too, defaults to False if no value passed.
  - type: boolean

#### alignAxisToVect(vect, axis=2, factor=1.0)

Aligns any of the game object's axis along the given vector.

- **`vect`**: a vector to align the axis.
  - type: 3D vector
- **`axis`**: The axis you want to align * 0: X axis * 1: Y axis * 2: Z axis
  - type: integer
- **`factor`**: Only rotate a feaction of the distance to the target vector (0.0 - 1.0)
  - type: float

#### getAxisVect(vect)

Returns the axis vector rotates by the object's worldspace orientation.
This is the equivalent of multiplying the vector by the orientation matrix.

- **`vect`**: a vector to align the axis.
  - type: 3D Vector

**Returns:** The vector in relation to the objects rotation.

**Return type:** 3d vector.

#### applyMovement(movement[, local])

Sets the game object's movement.

- **`movement`**: movement vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" movement ie: relative to world orientation. * True: get the "local" movement ie: relative to object orientation. Default to False if not passed.
- **`local`**: boolean

#### applyRotation(rotation[, local])

Sets the game object's rotation.

- **`rotation`**: rotation vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" rotation ie: relative to world orientation. * True: get the "local" rotation ie: relative to object orientation. Default to False if not passed.
- **`local`**: boolean

#### applyForce(force[, local])

Sets the game object's force.

This requires a dynamic object.

- **`force`**: force vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" force ie: relative to world orientation. * True: get the "local" force ie: relative to object orientation. Default to False if not passed.
  - type: boolean

#### applyTorque(torque[, local])

Sets the game object's torque.

This requires a dynamic object.

- **`torque`**: torque vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" torque ie: relative to world orientation. * True: get the "local" torque ie: relative to object orientation. Default to False if not passed.
  - type: boolean

#### getLinearVelocity([local])

Gets the game object's linear velocity.

This method returns the game object's velocity through it's center of mass, ie no angular velocity component.

- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - type: boolean

**Returns:** the object's linear velocity.

**Return type:** Vector((vx, vy, vz))

#### setLinearVelocity(velocity[, local])

Sets the game object's linear velocity.

This method sets game object's velocity through it's center of mass,
ie no angular velocity component.

This requires a dynamic object.

- **`velocity`**: linear velocity vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - type: boolean

#### getAngularVelocity([local])

Gets the game object's angular velocity.

- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.
  - type: boolean

**Returns:** the object's angular velocity.

**Return type:** Vector((vx, vy, vz))

#### setAngularVelocity(velocity[, local])

Sets the game object's angular velocity.

This requires a dynamic object.

- **`velocity`**: angular velocity vector.
  - type: boolean
- **`local`**:  * False: get the "global" velocity ie: relative to world orientation. * True: get the "local" velocity ie: relative to object orientation. Default to False if not passed.

#### getVelocity([point])

Gets the game object's velocity at the specified point.

Gets the game object's velocity at the specified point, including angular
components.

- **`point`**: optional point to return the velocity for, in local coordinates, defaults to (0, 0, 0) if no value passed.
  - type: 3D Vector

**Returns:** the velocity at the specified point.

**Return type:** Vector((vx, vy, vz))

#### getReactionForce()

Gets the game object's reaction force.

The reaction force is the force applied to this object over the last simulation timestep.
This also includes impulses, eg from collisions.

**Returns:** the reaction force of this object.

**Return type:** Vector((fx, fy, fz))

> **Note:**
This is not implimented at the moment.

#### applyImpulse(point, impulse[, local])

Applies an impulse to the game object.

This will apply the specified impulse to the game object at the specified point.
If point != position, applyImpulse will also change the object's angular momentum.
Otherwise, only linear momentum will change.

- **`point`**: the point to apply the impulse to (in world or local coordinates)
  - type: point [ix, iy, iz] the point to apply the impulse to (in world or local coordinates)
- **`impulse`**: impulse vector.
  - type: 3D Vector
- **`local`**:  * False: get the "global" impulse ie: relative to world coordinates with world orientation. * True: get the "local" impulse ie: relative to local coordinates with object orientation. Default to False if not passed.
  - type: boolean

#### setDamping(linear_damping, angular_damping)

Sets both the :py`linearDamping` and :py`angularDamping` simultaneously. This is more efficient than setting both properties individually.

- **`linear_damping`**: Linear ("translational") damping factor.
  - type: float ∈ [0, 1]
- **`angular_damping`**: Angular ("rotational") damping factor.
  - type: float ∈ [0, 1]

#### suspendPhysics([freeConstraints])

Suspends physics for this object.

- **`freeConstraints`**: When set to `True` physics constraints used by the object are deleted. Else when `False` (the default) constraints are restored when restoring physics.
  - type: bool

#### restorePhysics()

Resumes physics for this object. Also reinstates collisions.

#### suspendDynamics([ghost])

Suspends dynamics physics for this object.

- **`ghost`**: When set to `True`, collisions with the object will be ignored, similar to the "ghost" checkbox in Blender. When `False` (the default), the object becomes static but still collide with other objects.
  - type: bool

> **Tip:**
:py:attr:`isSuspendDynamics` allows you to inspect whether the object is in a suspended state.

#### restoreDynamics()

Resumes dynamics physics for this object. Also reinstates collisions; the object will no longer be a ghost.

> **Note:**
The objects linear velocity will be applied from when the dynamics were suspended.

#### enableRigidBody()

Enables rigid body physics for this object.

Rigid body physics allows the object to roll on collisions.

#### disableRigidBody()

Disables rigid body physics for this object.

#### setParent(parent, compound=True, ghost=True)

Sets this object's parent.
Control the shape status with the optional compound and ghost parameters:

In that case you can control if it should be ghost or not:

- **`parent`**: new parent object.
  - type: `KX_GameObject`
- **`compound`**: whether the shape should be added to the parent compound shape. * True: the object shape should be added to the parent compound shape. * False: the object should keep its individual shape.
  - type: boolean
- **`ghost`**: whether the object should be ghost while parented. * True: if the object should be made ghost while parented. * False: if the object should be solid while parented.
  - type: boolean

> **Note:**
If the object type is sensor, it stays ghost regardless of ghost parameter

#### removeParent()

Removes this objects parent.

#### getPhysicsId()

Returns the user data object associated with this game object's physics controller.

#### getPropertyNames()

Gets a list of all property names.

**Returns:** All property names for this object.

**Return type:** list

#### getBoundBoxSize()

Size of the bounding box (`cullingBox`) along the object's own axes, with its world scale.

**Returns:** width, depth and height.

**Return type:** `mathutils.Vector`

#### getBoundBoxCorners(space='WORLD')

The 8 corners of the bounding box. Corner `i` uses the max X when bit 0 is set, max Y for bit 1
and max Z for bit 2, so `[0]` is the minimum corner and `[7]` the maximum one.

- **`space`**: `'WORLD'` (positions in the world), `'OFFSET'` (from `worldPosition`, with rotation and scale) or `'LOCAL'` (object space, without scale).
  - type: string

**Return type:** list of `mathutils.Vector`

The `'WORLD'` corners can be passed straight to
`boxInsideFrustum` to test if the object is in the camera view.

#### getBoundBoxVolume()

Compatibility with Range 1.x scripts: returns `[volume, corner1, ..., corner8]`. The volume uses
the world scale and the corners are the `'OFFSET'` ones of `getBoundBoxCorners`, so
`obj.worldPosition + box[i]` is a corner in the world.

**Return type:** list

#### getDistanceTo(other)

- **`other`**: a point or another `KX_GameObject` to measure the distance to.
  - type: `KX_GameObject` or list [x, y, z]

**Returns:** distance to another object or point.

**Return type:** float

#### getVectTo(other)

Returns the vector and the distance to another object or point.
The vector is normalized unless the distance is 0, in which a zero length vector is returned.

- **`other`**: a point or another `KX_GameObject` to get the vector and distance to.
  - type: `KX_GameObject` or list [x, y, z]

**Returns:** (distance, globalVector(3), localVector(3))

**Return type:** 3-tuple (float, 3-tuple (x, y, z), 3-tuple (x, y, z))

#### rayCastTo(other, dist=0, prop="")

Look towards another point/object and find first object hit within dist that matches prop.

The ray is always casted from the center of the object, ignoring the object itself.
The ray is casted towards the center of another object or an explicit [x, y, z] point.
Use rayCast() if you need to retrieve the hit point

- **`other`**: [x, y, z] or object towards which the ray is casted
  - type: `KX_GameObject` or 3-tuple
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
  - type: float
- **`prop`**: property name that object must have; can be omitted => detect any object
  - type: string

**Returns:** the first object hit or None if no object or object does not match prop

**Return type:** `KX_GameObject`

#### rayCast(objto, objfrom=None, dist=0, prop="", face=False, xray=False, poly=0, mask=0xFFFF)

Look from a point/object to another point/object and find first object hit within dist that matches prop.
if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit.
if poly is 1, returns a 4-tuple with in addition a `KX_PolyProxy` as 4th element.
if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.

```python

# shoot along the axis gun-gunAim (gunAim should be collision-free)
obj, point, normal = gun.rayCast(gunAim, None, 50)
if obj:
   # do something
   pass
```

The face parameter determines the orientation of the normal.

* 0 => hit normal is always oriented towards the ray origin (as if you casted the ray from outside)
* 1 => hit normal is the real face normal (only for mesh object, otherwise face has no effect)

The ray has X-Ray capability if xray parameter is 1, otherwise the first object hit (other than self object) stops the ray.
The prop and xray parameters interact as follow.

* prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray.
* prop off, xray on : idem.
* prop on, xray off: return closest hit if it matches prop, no hit otherwise.
* prop on, xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray.

The `KX_PolyProxy` 4th element of the return tuple when poly=1 allows to retrieve information on the polygon hit by the ray.
If there is no hit or the hit object is not a static mesh, None is returned as 4th element.

The ray ignores collision-free objects and faces that dont have the collision flag enabled, you can however use ghost objects.

- **`objto`**: [x, y, z] or object to which the ray is casted
  - type: `KX_GameObject` or 3-tuple
- **`objfrom`**: [x, y, z] or object from which the ray is casted; None or omitted => use self object center
  - type: `KX_GameObject` or 3-tuple or None
- **`dist`**: max distance to look (can be negative => look behind); 0 or omitted => detect up to to
  - type: float
- **`prop`**: property name that object must have; can be omitted or "" => detect any object
  - type: string
- **`face`**: normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
  - type: integer
- **`xray`**: X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
  - type: integer
- **`poly`**: polygon option: 0, 1 or 2 to return a 3-, 4- or 5-tuple with information on the face hit. * 0 or omitted: return value is a 3-tuple (object, hitpoint, hitnormal) or (None, None, None) if no hit * 1: return value is a 4-tuple and the 4th element is a `KX_PolyProxy` or None if no hit or the object doesn't use a mesh collision shape. * 2: return value is a 5-tuple and the 5th element is a 2-tuple (u, v) with the UV mapping of the hit point or None if no hit, or the object doesn't use a mesh collision shape, or doesn't have a UV mapping.
  - type: integer
- **`mask`**: collision mask: The collision mask (16 layers mapped to a 16-bit integer) is combined with each object's collision group, to hit only a subset of the objects in the scene. Only those objects for which `collisionGroup & mask` is true can be hit.
  - type: bitfield

**Returns:** (object, hitpoint, hitnormal) or (object, hitpoint, hitnormal, polygon) or (object, hitpoint, hitnormal, polygon, hituv). * object, hitpoint and hitnormal are None if no hit. * polygon is valid only if the object is valid and is a static object, a dynamic object using mesh collision shape or a soft body object, otherwise it is None * hituv is valid only if polygon is valid and the object has a UV mapping, otherwise it is None

**Return type:**  * 3-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz)) * or 4-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`) * or 5-tuple (`KX_GameObject`, 3-tuple (x, y, z), 3-tuple (nx, ny, nz), `KX_PolyProxy`, 2-tuple (u, v))

> **Note:**
The ray ignores the object on which the method is called. It is casted from/to object center or explicit [x, y, z] points.

#### collide(obj)

Test if this object collides object `obj`.

- **`obj`**: the object to test collision with
  - type: string or `KX_GameObject`

**Returns:** (collide, points) * collide, True if this object collides object `obj` * points, contact point data of the collision or None

**Return type:** 2-tuple (boolean, list of `KX_CollisionContactPoint` or None)

#### setCollisionMargin(margin)

Set the objects collision margin.

- **`margin`**: the collision margin distance in blender units.
  - type: float

> **Note:**
If this object has no physics controller (a physics ID of zero), this function will raise RuntimeError.

#### sendMessage(subject, body="", to="")

Sends a message.

- **`subject`**: The subject of the message
  - type: string
- **`body`**: The body of the message (optional)
  - type: string
- **`to`**: The name of the object to send the message to (optional)
  - type: string

#### reinstancePhysicsMesh(gameObject, meshObject, dupli)

Updates the physics system with the changed mesh.

If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.

- **`gameObject`**: optional argument, set the physics shape from this gameObjets mesh.
  - type: string, `KX_GameObject` or None
- **`meshObject`**: optional argument, set the physics shape from this mesh.
  - type: string, `MeshProxy` or None
- **`dupli`**: optional argument, duplicate the physics shape.
  - type: boolean

**Returns:** True if reinstance succeeded, False if it failed.

**Return type:** boolean

> **Note:**
If this object has instances the other instances will be updated too.

> **Note:**
The gameObject argument has an advantage that it can convert from a mesh with modifiers applied (such as the Subdivision Surface modifier).

> **Caution:**
Only triangle mesh and convex hull type objects are supported currently.

> **Caution:**
If the object is a part of a compound object it will fail (parent or child)

> **Caution:**
Rebuilding the physics mesh can be slow, running many times per second will give a performance hit.

> **Caution:**
Duplicate the physics mesh can use much more memory, use this option only for duplicated meshes else use :py`replacePhysicsShape`.

#### replacePhysicsShape(gameObject)

Replace the current physics shape.

- **`gameObject`**: set the physics shape from this gameObjets.
  - type: string, `KX_GameObject`

**Returns:** True if replace succeeded, False if it failed.

**Return type:** boolean

> **Caution:**
Triangle mesh shapes are not supported.

#### get(key[, default])

Return the value matching key, or the default value if its not found.
- **`key`**: the matching key
  - type: string
- **`default`**: optional default value is the key isn't matching, defaults to None if no value passed.

**Returns:** The key value or a default.

#### playAction(name, start_frame, end_frame, layer=0, priority=0, blendin=0, play_mode=KX_ACTION_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0, blend_mode=KX_ACTION_BLEND_BLEND)

Plays an action.

- **`name`**: the name of the action
  - type: string
- **`start`**: the start frame of the action
  - type: float
- **`end`**: the end frame of the action
  - type: float
- **`layer`**: the layer the action will play in (actions in different layers are added/blended together)
  - type: integer
- **`priority`**: only play this action if there isn't an action currently playing in this layer with a higher (lower number) priority
  - type: integer
- **`blendin`**: the amount of blending between this animation and the previous one on this layer
  - type: float
- **`play_mode`**: the play mode
  - type: one of `these constants`
- **`layer_weight`**: how much of the previous layer to use for blending
  - type: float
- **`ipo_flags`**: flags for the old IPO behaviors (force, etc)
  - type: int bitfield
- **`speed`**: the playback speed of the action as a factor (1.0 = normal speed, 2.0 = 2x speed, etc)
  - type: float
- **`blend_mode`**: how to blend this layer with previous layers
  - type: one of `these constants`

#### stopAction([layer])

Stop playing the action on the given layer.

- **`layer`**: The layer to stop playing, defaults to 0 if no value passed.
  - type: integer

#### getActionFrame([layer])

Gets the current frame of the action playing in the supplied layer.

- **`layer`**: The layer that you want to get the frame from, defaults to 0 if no value passed.
  - type: integer

**Returns:** The current frame of the action

**Return type:** float

#### getActionName([layer])

Gets the name of the current action playing in the supplied layer.

- **`layer`**: The layer that you want to get the action name from, defaults to 0 if no value passed.
  - type: integer

**Returns:** The name of the current action

**Return type:** string

#### setActionFrame(frame[, layer])

Set the current frame of the action playing in the supplied layer.

- **`layer`**: The layer where you want to set the frame, default to 0 if no value passed.
  - type: integer
- **`frame`**: The frame to set the action to
  - type: float

#### isPlayingAction([layer])

Checks to see if there is an action playing in the given layer.

- **`layer`**: The layer to check for a playing action, defaults to 0 if no value passed.
  - type: integer

**Returns:** Whether or not the action is playing

**Return type:** boolean

#### playNLA(speed=1.0, loop=True)

Plays the NLA tracks of an armature, like the NLA Editor does. Muted tracks and strips are skipped,
Solo is respected and the tracks are blended from the bottom up (Replace and Add, influence, blend
in/out, repeat, scale, reverse and extrapolation). Actions played with `playAction` are
blended on top of the NLA result.

Calling it again while the NLA is playing with the same arguments keeps it going, so it can be
called every frame.

Not supported yet: transition and meta strips, Subtract/Multiply modes (played as Replace),
strip time curves and NLA on objects that are not armatures.

- **`speed`**: Playback speed (1.0 = scene animation frame rate, 0.0 = stopped, use `setNLAFrame`; negative plays backwards from the last frame).
  - type: float
- **`loop`**: Restart from the first strip after the last one ends, else hold the last frame.
  - type: boolean

**Returns:** True when the NLA started (the object is an armature with at least one strip).

**Return type:** boolean

#### stopNLA()

Stops the NLA playback. The armature keeps its current pose.

#### isPlayingNLA()

**Returns:** True while the NLA is playing (False after a non-looping NLA reached its end).

**Return type:** boolean

#### getNLAFrame()

**Returns:** The current NLA frame.

**Return type:** float

#### setNLAFrame(frame)

Jumps the NLA to the given frame, clamped to the range of the strips.

- **`frame`**: The NLA frame.
  - type: float

#### addDebugProperty (name[, debug])

Adds a single debug property to the debug list.

- **`name`**: name of the property that added to the debug list.
  - type: string
- **`debug`**: the debug state, default to True is no value passed.
  - type: boolean

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### getCurvePoints()

 `method`

`getCurvePoints(world=True)`: points of the first spline of a Curve object, as a list of `Vector`. World space by default; `world=False` returns local space. Empty list if the object is not a curve.

#### getTurnTo(other)

 `method`

Local vector from this object to another object or point. Useful to know which way to turn.

**Returns:** `Vector`

#### getVehicle()

*(new in Anastacio)* `method`

The vehicle created by this object's Vehicle panel, or `None`.

**Returns:** `KX_VehicleWrapper`

#### getVehicleGearboxType()

*(new in Anastacio)* `method`

Gearbox type set in the Vehicle panel.

**Returns:** `int`

#### getVehicleGearRatios()

*(new in Anastacio)* `method`

Gear ratios set in the Vehicle panel.

**Returns:** `tuple`

#### getVehicleMaxRPM()

*(new in Anastacio)* `method`

Maximum engine RPM set in the Vehicle panel.

**Returns:** `float`

#### getVehicleMaxTorque()

*(new in Anastacio)* `method`

Maximum engine torque set in the Vehicle panel.

**Returns:** `float`

#### getVehicleSteeringWheel()

*(new in Anastacio)* `method`

Steering wheel object set in the Vehicle panel, or `None`.

**Returns:** `KX_GameObject`

#### is_playing_take()

 `method`

`True` while a Rec Play take moves this object.

**Returns:** `bool`

#### lookAt(vect, axis=2, factor=1.0)

*(new in Anastacio)* `method`

Turns the object so its `axis` (0=X, 1=Y, 2=Z) points along `vect`. A `factor` below 1 turns only part of the way (smoothing).

#### play_take(name)

 `method`

Plays what a Rec Play take recorded of this object. `False` if it recorded nothing of it.

**Returns:** `bool`

#### resumeAnimations()

*(new in Anastacio)* `method`

Resumes the animations paused by `suspendAnimations()`.

#### setActionLayerSpeed(layer, speed)

 `method`

Changes the speed of the action playing on layer `layer`.

#### setActionLayerWeight(layer, layerWeight)

 `method`

Changes the weight (0 to 1) of animation layer `layer`.

#### setCcdMotionThreshold(threshold)

*(new in Anastacio)* `method`

Speed above which continuous collision detection (CCD) kicks in, so fast objects don't pass through walls.

#### setCcdSweptSphereRadius(radius)

*(new in Anastacio)* `method`

Radius of the sphere used by continuous collision detection (CCD).

#### setHalfAnimations(enabled)

*(new in Anastacio)* `method`

With `True`, updates the object animations every other frame to save CPU.

#### setSoftAnchorsHardness(value)

*(new in Anastacio)* `method`

Soft body physics: anchor hardness.

#### setSoftAngularStiffness(value)

*(new in Anastacio)* `method`

Soft body physics: angular stiffness.

#### setSoftClusterSolverIterations(iterations)

*(new in Anastacio)* `method`

Soft body physics: cluster solver iterations.

#### setSoftContactsHardness(value)

*(new in Anastacio)* `method`

Soft body physics: contact hardness.

#### setSoftDampingCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: damping.

#### setSoftDragCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: air drag.

#### setSoftDriftSolverIterations(iterations)

*(new in Anastacio)* `method`

Soft body physics: drift solver iterations.

#### setSoftDynamicFrictionCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: dynamic friction.

#### setSoftKineticContactsHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness of contact with kinematic objects.

#### setSoftLiftCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: lift.

#### setSoftLinearStiffness(value)

*(new in Anastacio)* `method`

Soft body physics: linear stiffness.

#### setSoftPoseMatching(enabled)

*(new in Anastacio)* `method`

Soft body physics: tries to go back to the original shape.

#### setSoftPoseMatchingCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: how strongly it goes back to the original shape.

#### setSoftPositionSolverIterations(iterations)

*(new in Anastacio)* `method`

Soft body physics: position solver iterations.

#### setSoftPressureCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: internal pressure (balloon effect).

#### setSoftRigidContactsHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness of contact with rigid bodies.

#### setSoftVelocitiesCorrectionFactor(value)

*(new in Anastacio)* `method`

Soft body physics: velocity correction factor.

#### setSoftVelocitySolverIterations(iterations)

*(new in Anastacio)* `method`

Soft body physics: velocity solver iterations.

#### setSoftVolume(volume)

*(new in Anastacio)* `method`

Soft body physics: volume the body tries to keep.

#### setSoftVolumeConversationCoefficient(value)

*(new in Anastacio)* `method`

Soft body physics: volume conservation.

#### setSoftVsKineticHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness against kinematic bodies (clusters).

#### setSoftVsKineticImpulseSplitCluster(value)

*(new in Anastacio)* `method`

Soft body physics: impulse split against kinematic bodies (clusters).

#### setSoftVsRigidHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness against rigid bodies (clusters).

#### setSoftVsRigidImpulseSplitCluster(value)

*(new in Anastacio)* `method`

Soft body physics: impulse split against rigid bodies (clusters).

#### setSoftVsSoftHardness(value)

*(new in Anastacio)* `method`

Soft body physics: hardness against other soft bodies (clusters).

#### setSoftVsSoftImpulseSplitCluster(value)

*(new in Anastacio)* `method`

Soft body physics: impulse split against other soft bodies (clusters).

#### setVehicleGearRatios(ratios)

*(new in Anastacio)* `method`

Replaces the vehicle gear ratios. Takes a list of numbers, one per gear.

#### setVehicleMaxRPM(value)

*(new in Anastacio)* `method`

Changes the maximum engine RPM of the vehicle at runtime (number >= 0).

#### setVehicleMaxTorque(value)

*(new in Anastacio)* `method`

Changes the maximum engine torque of this object's vehicle at runtime (number >= 0).

#### stop_take()

 `method`

Stops the take of this object and gives it back to its logic and physics.

#### strikeLightning(bolt=True)

 `method`

a lightning strike now (rain must be on)

#### suspendAnimations()

*(new in Anastacio)* `method`

Pauses all object animations until `resumeAnimations()`.

#### activitycullingdistance

*(new in Anastacio)* `attribute · read-only`

Distance from this object to the camera, computed by Activity Culling.

#### angularVelocity

*(new in Anastacio)* `attribute`

Angular velocity. Read in local coordinates, written in world coordinates.

#### animationEventManager

*(new in Anastacio)* `attribute · read-only`

Manager of the object animation events (`KX_AnimationEventManager`).

#### anisotropicFriction

*(new in Anastacio)* `attribute`

Turns on per-axis (anisotropic) friction.

#### anisotropicFrictionCoefficients

*(new in Anastacio)* `attribute`

Friction `[x, y, z]` on each axis when `anisotropicFriction` is on.

#### bendAngle

*(new in Anastacio)* `attribute`

How much the object bends on each impact.

#### bendAxis

*(new in Anastacio)* `attribute`

Axis the object bends on: `'X'`, `'Y'` or `'Z'`.

#### bendMaxAngle

*(new in Anastacio)* `attribute`

Maximum angle the object can bend.

#### burstSpeed

*(new in Anastacio)* `attribute`

Speed at which fragments fly out when the object breaks.

#### debrisLifetime

*(new in Anastacio)* `attribute`

Lifetime of the fragments after breaking.

#### decal

*(new in Anastacio)* `attribute`

Object used as a scratch decal on collisions, or `None`. It must be an object in the scene file.

#### decalLife

*(new in Anastacio)* `attribute`

Lifetime of each decal.

#### decalSize

*(new in Anastacio)* `attribute`

Decal size.

#### dentImpulse

*(new in Anastacio)* `attribute`

Minimum collision impulse to dent the object.

#### fragments

*(new in Anastacio)* `attribute`

Name of the group with the fragments used when the object breaks, or `None`. Only on destructible objects; otherwise raises `AttributeError`.

#### hiddenFromCamera

*(new in Anastacio)* `attribute`

Camera that must not show this object (e.g. your own car in split screen), or `None`.

#### impactImpulse

*(new in Anastacio)* `attribute`

Minimum collision impulse for an explosive object to detonate.

#### isDeformable

*(new in Anastacio)* `attribute · read-only`

`True` if the object has the deformation settings on (dent, bend, decals).

#### linearVelocity

*(new in Anastacio)* `attribute`

Linear velocity. Read in local coordinates, written in world coordinates.

#### maxDecals

*(new in Anastacio)* `attribute`

Maximum number of decals on this object at the same time.

#### parentRecursive

*(new in Anastacio)* `attribute · read-only`

List of all parents above the object, from closest to farthest.

#### particles

*(new in Anastacio)* `attribute · read-only`

Object particle system (`KX_ParticleSystem`), or `None`.

#### particlesMix

*(new in Anastacio)* `attribute · read-only`

Second (mix) particle system of the object, or `None`.

#### passIndex

*(new in Anastacio)* `attribute`

Object Pass Index, used to separate objects in filters and effects.

#### useBreakOnCollision

*(new in Anastacio)* `attribute`

Whether the object breaks on collision.

#### useChainReaction

*(new in Anastacio)* `attribute`

Whether this object explosion detonates other explosives nearby.

#### useDentOnCollision

*(new in Anastacio)* `attribute`

Whether the object dents on collision.

#### useExplodeOnImpact

*(new in Anastacio)* `attribute`

Whether the explosive object detonates on an impact above `impactImpulse`.

#### useInheritVelocity

*(new in Anastacio)* `attribute`

Whether fragments inherit the object velocity when it breaks.

---

## KX_InputSystem

> **See also:**
[`KX_InputTable`](#kx_inputtable), [`KX_PythonKeyboard`](#kx_pythonkeyboard), [`KX_PythonJoystick`](#kx_pythonjoystick)

Class `Range.types.KX_InputSystem`.

```python
# List the maps and the actions that were loaded.
import Range

for mapName, tables in Range.logic.inputSystem.inputMaps.items():
    print(mapName, list(tables))
```

```python
# Save a new sensitivity chosen in the options menu. Arguments: map, action, binding, value.
import Range

system = Range.logic.inputSystem

if system.changeSensitivity("Player", "Jump", "keyboard", 0.5):
    system.reloadInputMaps()
```

```python
# Change the key of an action. The map is the file KeyMapping/Player.json, next to the game.
import Range

system = Range.logic.inputSystem

if system.changeKeyMap("Player", "Jump", "keyboard", "BUTTON", Range.events.SPACEKEY):
    system.reloadInputMaps()
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### changeJoystickIndex(inputMap, inputTable, name, value)

 `method`

Changes which gamepad (joystick index) an action uses.

#### changeKeyMap(inputMap, inputTable, name, keyType, value)

 `method`

Changes the key or button bound to an action. Use it for "rebind controls" menus.

#### changeSensitivity(inputMap, inputTable, name, value)

 `method`

Changes an action sensitivity (e.g. mouse or analog stick).

#### reloadInputMaps()

 `method`

Reloads the input maps from the file. It is slow; avoid calling it repeatedly.

#### inputMaps

 `attribute · read-only`

Dictionary `{map: {table: KX_InputTable}}` with all loaded input maps.

---

## KX_InputTable

> **See also:**
[`KX_InputSystem`](#kx_inputsystem)

Class `Range.types.KX_InputTable`.

```python
# Use an action without knowing which key is connected to it.
import Range

maps = Range.logic.inputSystem.inputMaps
jump = maps["Player"]["Jump"]

if jump.activated:
    print("Jump")
```

```python
# Read an axis.
import Range

move = Range.logic.inputSystem.inputMaps["Player"]["Move"]

if move.active:
    print(move.values)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### activated

 `attribute · read-only`

`True` on the frame the action was just triggered.

#### active

 `attribute · read-only`

`True` while the action is triggered.

#### released

 `attribute · read-only`

`True` on the frame the action was just released.

#### values

 `attribute · read-only`

Current action values: `True`/`False` on a simple button (`VECTOR1D`); tuple with 2 or 3 numbers on 2D or 3D axes.

---

## KX_LibLoadStatus

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

An object providing information about a LibLoad() operation.

```python

# Print a message when an async LibLoad is done
import Range

def finished_cb(status):
    print("Library (%s) loaded in %.2fms." % (status.libraryName, status.timeTaken))

Range.logic.LibLoad('myblend.blend', 'Scene', asynchronous=True).onFinish = finished_cb
```

```python

# Loading screen: show the progress. Run update every frame (Always sensor with True Pulse).
import Range

status = Range.logic.LibLoad("//level2.range", "Scene", asynchronous=True)

def update(cont):
    cont.owner.text = "Loading %d%%" % (status.progress * 100)

    if status.finished:
        cont.owner.text = "Ready"
```

```python

# Add an object as soon as its file finishes loading.
import Range

def finished(status):
    print(status.libraryName, status.timeTaken)
    Range.logic.getCurrentScene().addObject("Enemy")

status = Range.logic.LibLoad("//enemies.range", "Scene", asynchronous=True)
status.onFinish = finished
```

#### onFinish

A callback that gets called when the lib load is done.

**Type:** callable

#### finished

The current status of the lib load.

**Type:** boolean

#### progress

The current progress of the lib load as a normalized value from 0.0 to 1.0.

**Type:** float

#### libraryName

The name of the library being loaded (the first argument to LibLoad).

**Type:** string

#### timeTaken

The amount of time, in seconds, the lib load took (0 until the operation is complete).

**Type:** float

---

## KX_LightningActuator

Class `Range.types.KX_LightningActuator`.

```python
# Fire a flash with a visible bolt.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Lightning"]

act.bolt = True
cont.activate(act)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### bolt

*(new in Anastacio)* `attribute`

Turns on the visible lightning bolt, besides the flash.

---

## KX_LightObject

Base class: [`KX_GameObject`](#kx_gameobject)

> **See also:**
[`KX_WorldInfo`](#kx_worldinfo), [`KX_Scene`](#kx_scene)

!Lamp panel in the editor, with the Point, Sun, Spot, Hemi and Area types

A light in the game: the **Lamp** object of the editor (Add > Lamp). The type chosen in the Lamp panel is read in Python with `type`:

- **Point**: `NORMAL`, shines in all directions from one point, like a light bulb.
- **Sun**: `SUN`, parallel light from far away, for daylight.
- **Spot**: `SPOT`, a cone of light, like a flashlight.
- **Hemi**: `HEMI`, soft light from a half sphere, without shadows.
- **Area**: has no type of its own in the game and reads as `NORMAL`.

**Fake (GPU Particle)**, in the same Add > Lamp menu, is not a light: it is a mesh with one glowing particle, so it is not a `KX_LightObject`.

```python

# Check the type of the lamp, or change it during the game.
import Range

light = Range.logic.getCurrentController().owner

if light.type == light.NORMAL:
    print("Point lamp")
elif light.type == light.SUN:
    print("Sun lamp")
elif light.type == light.SPOT:
    print("Spot lamp")
elif light.type == light.HEMI:
    print("Hemi lamp")

light.type = light.SPOT  # turn it into a Spot lamp
```

```python

# Turn on a red alert light.
import Range

co = Range.logic.getCurrentController()
light = co.owner

light.energy = 1.0
light.color = [1.0, 0.0, 0.0]
```

```python

# Flicker like a torch. Run it every frame (Always sensor with True Pulse).
import random
import Range

light = Range.logic.getCurrentController().owner
light.energy = random.uniform(0.8, 1.2)
```

```python

# Turn the light on or off. An invisible light does not update its shadow.
import Range

light = Range.logic.getCurrentController().owner
light.visible = not light.visible
```

```python

# Shadow quality option. Bigger sizes look sharper but use more video memory.
# Point lamps keep the Size set in the editor.
import Range

light = Range.logic.getCurrentController().owner
light.shadowMapSize = 1024  # for example 512, 1024, 2048 or 4096
```

```python

# Stop redrawing the shadow every frame when the scene rarely changes.
import Range

light = Range.logic.getCurrentController().owner
light.staticShadow = True

# Later, after moving something that casts a shadow, redraw it once.
light.updateShadow()
```

```python

# Narrow the cone of a spot light and soften its edge.
import Range

light = Range.logic.getCurrentController().owner
if light.type == light.SPOT:
    light.spotsize = 45.0  # cone angle in degrees
    light.spotblend = 0.3  # edge softness, from 0 to 1
```

#### SPOT

A spot light source. See attribute `type`

#### SUN

A point light source with no attenuation. See attribute `type`

#### NORMAL

A point light source. See attribute `type`

#### HEMI

A hemi light source. See attribute `type`

#### type

The type of light - must be SPOT, SUN or NORMAL

#### energy

The brightness of this light.

**Type:** float

#### shadowClipStart

The shadowmap clip start, below which objects will not generate shadows.

**Type:** float (read only)

#### shadowClipEnd

The shadowmap clip end, beyond which objects will not generate shadows.

**Type:** float (read only)

#### shadowFrustumSize

Size of the frustum used for creating the shadowmap.

**Type:** float (read only)

#### shadowBindId

The OpenGL shadow texture bind number/id.

**Type:** int (read only)

#### shadowMapType

The shadow shadow map type (0 -> Simple; 1 -> Variance)

**Type:** int (read only)

#### shadowBias

The shadow buffer sampling bias.

**Type:** float (read only)

#### shadowBleedBias

The bias for reducing light-bleed on variance shadow maps.

**Type:** float (read only)

#### useShadow

Returns True if the light has Shadow option activated, else returns False.

**Type:** boolean (read only)

#### shadowColor

The color of this light shadows. Black = (0.0, 0.0, 0.0), White = (1.0, 1.0, 1.0).

**Type:** `mathutils.Color` (read only)

#### shadowMatrix

Matrix that converts a vector in camera space to shadow buffer depth space.

Computed as:
mat4_perspective_to_depth * mat4_lamp_to_perspective * mat4_world_to_lamp * mat4_cam_to_world.

mat4_perspective_to_depth is a fixed matrix defined as follow:

0.5 0.0 0.0 0.5
0.0 0.5 0.0 0.5
0.0 0.0 0.5 0.5
0.0 0.0 0.0 1.0

.. note:

There is one matrix of that type per lamp casting shadow in the scene.

**Type:** Matrix4x4 (read only)

#### distance

The maximum distance this light can illuminate. (SPOT and NORMAL lights only).

**Type:** float

#### color

The color of this light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].

**Type:** list [r, g, b]

#### lin_attenuation

The linear component of this light's attenuation. (SPOT and NORMAL lights only).

**Type:** float

#### quad_attenuation

The quadratic component of this light's attenuation (SPOT and NORMAL lights only).

**Type:** float

#### spotsize

The cone angle of the spot light, in degrees (SPOT lights only).

**Type:** float in [0 - 180].

#### spotblend

Specifies the intensity distribution of the spot light (SPOT lights only).

**Type:** float in [0 - 1]

> **Note:**
Higher values result in a more focused light source.

#### shadowMapSize

Shadow map resolution in pixels (the lamp's Size). Setting it resizes the shadow buffer on
the fly without recompiling shaders, for a shadow quality option (e.g. 512 / 1024 / 2048).
Cascaded shadow maps keep their ratio to it. Reads 0 when the lamp has no shadow buffer.
Point lamps keep their own size.

**Type:** integer from 64 to 16384 (clamped to the graphics card maximum).

#### staticShadow

Enables static shadows. By default (staticShadow=False) the shadow cast by the lamp is recalculated every frame. When this is not needed, set staticShadow=True. In that case, call :py`updateShadow` to request a shadow update.

**Type:** boolean.

#### updateShadow()

Set the shadow to be updated next frame if the lamp uses a static shadow, see `staticShadow`.

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### autoShadowUpdate

*(new in Anastacio)* `attribute`

When `False`, this light shadow stops being recomputed every frame (saves GPU in static scenes).

---

## KX_LodLevel

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

A single lod level for a game object lod manager.

```python

# List the levels of detail of the object.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    for lod in obj.lodManager.levels:
        print(lod.level, lod.distance, lod.useMesh, lod.useMaterial)
```

```python

# See which level the object is using right now.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    lod = obj.lodManager.levels[obj.currentLodLevel]
    print(lod.level, lod.mesh)
```

#### mesh

The mesh used for this lod level. (read only)

**Type:** `RAS_MeshObject`

#### level

The number of the lod level. (read only)

**Type:** integer

#### distance

Distance to begin using this level of detail. (read only)

**Type:** float (0.0 to infinite)

#### hysteresis

Minimum distance factor change required to transition to the previous level of detail in percent. (read only)

**Type:** float [0.0 to 100.0]

#### useMesh

Return True if the lod level uses a different mesh than the original object mesh. (read only)

**Type:** boolean

#### useMaterial

Return True if the lod level uses a different material than the original object mesh material. (read only)

**Type:** boolean

#### useHysteresis

Return true if the lod level uses hysteresis override. (read only)

**Type:** boolean

---

## KX_LodManager

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

This class contains a list of all levels of detail used by a game object.

```python

# Graphics option: values above 1.0 switch to the simpler levels sooner.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    obj.lodManager.distanceFactor = 2.0
```

```python

# Use the same levels of detail in another object.
import Range

scene = Range.logic.getCurrentScene()
scene.objects["TreeB"].lodManager = scene.objects["TreeA"].lodManager
```

```python

# Also switch the physics mesh when the level changes.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    obj.lodManager.updatePhysics = True
```

#### levels

Return the list of all levels of detail of the lod manager.

**Type:** list of `KX_LodLevel`

#### distanceFactor

Method to multiply the distance to the camera.

**Type:** float

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### updatePhysics

 `attribute`

Also changes the physics mesh when the level of detail (LOD) changes.

---

## KX_Mesh

Base class: [`EXP_Value`](#exp_value)

> **See also:**
[`KX_MeshBuilder`](#kx_meshbuilder), [`KX_PolyProxy`](#kx_polyproxy), [`KX_VertexProxy`](#kx_vertexproxy), [`KX_BlenderMaterial`](#kx_blendermaterial)

A mesh object.

You can only change the vertex properties of a mesh object, not the mesh topology.

To use mesh objects effectively, you should know a bit about how the game engine handles them.

#. Mesh Objects are converted from Blender at scene load.
#. The Converter groups polygons by Material.  This means they can be sent to the renderer efficiently.  A material holds:

#. The texture.
#. The Blender material.
#. The Tile properties
#. The face properties - (From the "Texture Face" panel)
#. Transparency & z sorting
#. Light layer
#. Polygon shape (triangle/quad)
#. Game Object

#. Vertices will be split by face if necessary.  Vertices can only be shared between faces if:

#. They are at the same position
#. UV coordinates are the same
#. Their normals are the same (both polygons are "Set Smooth")
#. They are the same color, for example: a cube has 24 vertices: 6 faces with 4 vertices per face.

The correct method of iterating over every `KX_VertexProxy` in a game object

```python

from Range import logic

cont = logic.getCurrentController()
object = cont.owner

for mesh in object.meshes:
   for m_index in range(len(mesh.materials)):
      for v_index in range(mesh.getVertexArrayLength(m_index)):
         vertex = mesh.getVertex(m_index, v_index)
         # Do something with vertex here...
         # ... eg: color the vertex red.
         vertex.color = [1.0, 0.0, 0.0, 1.0]
```

#### materials

**Type:** list of `KX_BlenderMaterial` type

#### numPolygons

**Type:** integer

#### numMaterials

**Type:** integer

#### polygons

Returns the list of polygons of this mesh.

**Type:** `KX_PolyProxy` list (read only)

#### getMaterialName(matid)

Gets the name of the specified material.

- **`matid`**: the specified material.
  - type: integer

**Returns:** the attached material name.

**Return type:** string

#### getTextureName(matid)

Gets the name of the specified material's texture.

- **`matid`**: the specified material
  - type: integer

**Returns:** the attached material's texture name.

**Return type:** string

#### getVertexArrayLength(matid)

Gets the length of the vertex array associated with the specified material.

There is one vertex array for each material.

- **`matid`**: the specified material
  - type: integer

**Returns:** the number of verticies in the vertex array.

**Return type:** integer

#### getVertex(matid, index)

Gets the specified vertex from the mesh object.

- **`matid`**: the specified material
  - type: integer
- **`index`**: the index into the vertex array.
  - type: integer

**Returns:** a vertex object.

**Return type:** `KX_VertexProxy`

#### getPolygon(index)

Gets the specified polygon from the mesh.

- **`index`**: polygon number
  - type: integer

**Returns:** a polygon object.

**Return type:** `KX_PolyProxy`

#### transform(matid, matrix)

Transforms the vertices of a mesh.

- **`matid`**: material index, -1 transforms all.
  - type: integer
- **`matrix`**: transformation matrix.
  - type: 4x4 matrix [[float]]

#### transformUV(matid, matrix, uv_index=-1, uv_index_from=-1)

Transforms the vertices UV's of a mesh.

- **`matid`**: material index, -1 transforms all.
  - type: integer
- **`matrix`**: transformation matrix.
  - type: 4x4 matrix [[float]]
- **`uv_index`**: optional uv index, -1 for all, otherwise 0 or 1.
  - type: integer
- **`uv_index_from`**: optional uv index to copy from, -1 to transform the current uv.
  - type: integer

#### replaceMaterial(matid, material)

Replace the material in slot `matid` by the material `material`.

- **`matid`**: The material index.
  - type: integer
- **`material`**: The material replacement.
  - type: `KX_BlenderMaterial`

> **Caution:**
Changing the material of a mesh used by many objects can be slow. This function should be not called every frames

#### copy()

Return a duplicated mesh.

**Returns:** a duplicated mesh of the current used.

**Return type:** `KX_Mesh`.

#### constructBvh(transform=mathutils.Matrix.Identity(4), epsilon=0)

Return a BVH tree based on mesh geometry. Indices of tree elements match polygons indices.

- **`transform`**: The transform 4x4 matrix applied to vertices.
  - type: `mathutils.Matrix`
- **`epsilon`**: The tree distance epsilon.
  - type: float

**Returns:** A BVH tree based on mesh geometry.

**Return type:** `mathutils.bvhtree.BVHTree`

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### destruct()

 `method`

Deletes the mesh from memory. Use only on script-created meshes no object uses anymore.

---

## KX_MeshBuilder

> **See also:**
[`KX_MeshBuilderSlot`](#kx_meshbuilderslot), [`KX_Mesh`](#kx_mesh), [`KX_GameObject`](#kx_gameobject)

Class `Range.types.KX_MeshBuilder`.

```python
# Create a triangle by script and put it on the object.
import Range

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

builder = Range.types.KX_MeshBuilder("Triangle", scene, ["UVMap"], ["Col"])
slot = builder.addSlot(own.meshes[0].materials[0])

a = slot.addVertex((0.0, 0.0, 0.0))
b = slot.addVertex((1.0, 0.0, 0.0))
c = slot.addVertex((0.0, 1.0, 0.0))
slot.addIndex([a, b, c])
slot.recalculateNormals()

own.replaceMesh(builder.finish())
```

```python
# Copy an existing mesh to change it. Keep the builder in a variable while you use its slots.
import Range

own = Range.logic.getCurrentController().owner

builder = Range.types.KX_MeshBuilder.FromMesh("Copy", own.meshes[0])
print(len(builder.slots))
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### addSlot(material, primitive=0)

 `method`

Creates a mesh part with the given material. `primitive`: 0 triangles (default), 1 points, 2 lines.

**Returns:** `KX_MeshBuilderSlot`

#### finish()

 `method`

Builds the mesh from the slots and registers it in the scene. Then use `obj.replaceMesh()` to put it on an object.

**Returns:** `KX_Mesh`

#### FromMesh(name, mesh)

 `method`

Creates a builder from an existing mesh, to copy and edit it.

**Returns:** `KX_MeshBuilder`

#### slots

 `attribute · read-only`

List of the mesh slots (`KX_MeshBuilderSlot`).

---

## KX_MeshBuilderSlot

> **See also:**
[`KX_MeshBuilder`](#kx_meshbuilder), [`KX_Mesh`](#kx_mesh)

Class `Range.types.KX_MeshBuilderSlot`.

```python
# Add a square made of two triangles.
points = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
ids = [slot.addVertex(point) for point in points]

slot.addIndex([ids[0], ids[1], ids[2]])
slot.addIndex([ids[0], ids[2], ids[3]])
slot.recalculateNormals()
```

```python
# See what the slot has.
print(len(slot.vertices), len(slot.indices))
print(slot.uvCount, slot.colorCount)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### addIndex(indices)

 `method`

Adds vertex indices (list of integers) to the primitives and, for triangle meshes, to the triangles.

#### addPrimitiveIndex(indices)

 `method`

Adds indices only to the primitive (drawing) list.

#### addTriangleIndex(indices)

 `method`

Adds indices only to the triangle list (physics and rays).

#### addVertex(position, normal=None, tangent=None, uvs=None, colors=None)

 `method`

Adds a vertex. `uvs` and `colors` are lists, one entry per layer.

**Returns:** `int`

#### recalculateNormals()

 `method`

Recomputes vertex normals from the triangles.

#### removePrimitiveIndex(start, end=-1)

 `method`

Removes primitive indices from `start` to `end`.

#### removeTriangleIndex(start, end=-1)

 `method`

Removes triangle indices from `start` to `end`.

#### removeVertex(start, end=-1)

 `method`

Removes vertices from `start` to `end`.

#### colorCount

 `attribute · read-only`

How many vertex color layers the slot has.

#### indices

 `attribute · read-only`

List of primitive indices.

#### material

 `attribute`

Slot material.

#### primitive

 `attribute · read-only`

Slot primitive type (points, lines or triangles).

#### triangleIndices

 `attribute · read-only`

List of triangle indices.

#### uvCount

 `attribute · read-only`

How many UV layers the slot has.

#### vertices

 `attribute · read-only`

List of the slot vertices.

---

## KX_MicrophoneSensor

Class `Range.types.KX_MicrophoneSensor`.

```python
# Open the mouth of the character while the player talks.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Microphone"]
cont.owner["mouth"] = sensor.level
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### hold

*(new in Anastacio)* `attribute`

Seconds, 0 to 60: how long talking stays positive, or how much silence is needed.

#### level

*(new in Anastacio)* `attribute · read-only`

Voice level now (read-only).

#### mode

*(new in Anastacio)* `attribute`

Mode: `0` talking (level above `threshold`), `1` peak (one pulse, like a clap or blow), `2` silence (after `hold` seconds below `threshold`).

#### peak

*(new in Anastacio)* `attribute · read-only`

Voice peak (read-only).

#### propName

*(new in Anastacio)* `attribute`

Name of the object property tied to the sensor.

#### threshold

*(new in Anastacio)* `attribute`

Voice level that triggers the sensor, 0 to 1.

---

## KX_MouseActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

The mouse actuator gives control over the visibility of the mouse cursor and rotates the parent object according to mouse movement.

```python
# First-person view with limits to look up and down.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Mouse"]

act.sensitivity = [2.0, 2.0]
act.limit_y = [-80.0, 80.0]
act.visible = False
cont.activate(act)
```

```python
# Center the view again.
import Range

act = Range.logic.getCurrentController().actuators["Mouse"]
act.reset()
```

#### reset()

Undoes the rotation caused by the mouse actuator.

#### visible

The visibility of the mouse cursor.

**Type:** boolean

#### use_axis_x

Mouse movement along the x axis effects object rotation.

**Type:** boolean

#### use_axis_y

Mouse movement along the y axis effects object rotation.

**Type:** boolean

#### threshold

Amount of movement from the mouse required before rotation is triggered.

**Type:** `mathutils.Vector`

The values in the list should be between 0.0 and 0.5.

#### reset_x

Mouse is locked to the center of the screen on the x axis.

**Type:** boolean

#### reset_y

Mouse is locked to the center of the screen on the y axis.

**Type:** boolean

#### object_axis

The object's 3D axis to rotate with the mouse movement. ([x, y])

**Type:** list (vector of 2 integers from 0 to 2)

* KX_ACT_MOUSE_OBJECT_AXIS_X
* KX_ACT_MOUSE_OBJECT_AXIS_Y
* KX_ACT_MOUSE_OBJECT_AXIS_Z

#### local_x

Rotation caused by mouse movement along the x axis is local.

**Type:** boolean

#### local_y

Rotation caused by mouse movement along the y axis is local.

**Type:** boolean

#### sensitivity

The amount of rotation caused by mouse movement along the x and y axis.

**Type:** `mathutils.Vector`

Negative values invert the rotation.

#### limit_x

The minimum and maximum angle of rotation caused by mouse movement along the x axis in degrees.
limit_x[0] is minimum, limit_x[1] is maximum.

**Type:** `mathutils.Vector`

#### limit_y

The minimum and maximum angle of rotation caused by mouse movement along the y axis in degrees.
limit_y[0] is minimum, limit_y[1] is maximum.

**Type:** `mathutils.Vector`

#### angle

The current rotational offset caused by the mouse actuator in degrees.

**Type:** `mathutils.Vector`

---

## KX_MouseFocusSensor

Base class: [`SCA_MouseSensor`](#sca_mousesensor)

The mouse focus sensor detects when the mouse is over the current game object.

The mouse focus sensor works by transforming the mouse coordinates from 2d device
space to 3d space then raycasting away from the camera.

```python
# Select what is under the mouse.
import Range

sensor = Range.logic.getCurrentController().sensors["MouseOver"]

if sensor.positive:
    print(sensor.hitObject.name, sensor.hitPosition)
```

#### raySource

The worldspace source of the ray (the view position).

**Type:** list (vector of 3 floats)

#### rayTarget

The worldspace target of the ray.

**Type:** list (vector of 3 floats)

#### rayDirection

The `rayTarget` - `raySource` normalized.

**Type:** list (normalized vector of 3 floats)

#### hitObject

the last object the mouse was over.

**Type:** `KX_GameObject` or None

#### hitPosition

The worldspace position of the ray intersecton.

**Type:** list (vector of 3 floats)

#### hitNormal

the worldspace normal from the face at point of intersection.

**Type:** list (normalized vector of 3 floats)

#### hitUV

the UV coordinates at the point of intersection.

**Type:** list (vector of 2 floats)

If the object has no UV mapping, it returns [0, 0].

The UV coordinates are not normalized, they can be < 0 or > 1 depending on the UV mapping.

#### usePulseFocus

When enabled, moving the mouse over a different object generates a pulse. (only used when the 'Mouse Over Any' sensor option is set).

**Type:** boolean

#### useXRay

If enabled it allows the sensor to see through game objects that don't have the selected property or material.

**Type:** boolean

#### mask

The collision mask (16 layers mapped to a 16-bit integer) combined with each object's collision group, to hit only a subset of the
objects in the scene. Only those objects for which `collisionGroup & mask` is true can be hit.

**Type:** bitfield

#### propName

The property or material the sensor is looking for.

**Type:** string

#### useMaterial

Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property.

**Type:** boolean

---

## KX_MovementSensor

Class `Range.types.KX_MovementSensor`.

```python
# Fire when the object moves on any axis.
import Range

sensor = Range.logic.getCurrentController().sensors["Movement"]

sensor.axis = 6
sensor.threshold = 0.05

if sensor.positive:
    print("Moving")
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### axis

 `attribute`

Watched axis: 0 to 2 = +X, +Y, +Z; 3 to 5 = -X, -Y, -Z; 6 = all.

#### threshold

 `attribute`

How much the object must move for the sensor to fire.

---

## KX_NavMeshObject

Base class: [`KX_GameObject`](#kx_gameobject)

> **See also:**
[`KX_SteeringActuator`](#kx_steeringactuator)

Python interface for using and controlling navigation meshes.

A navigation mesh with a Boolean game property `dynamic_navmesh` set to True is built in tiles when the
game starts, so obstacles can carve it at runtime. Objects with "Create Obstacle" carve it automatically;
`addObstacle` adds any other object. Paths may differ slightly from the static navigation mesh.

```python

# Find a path from the object to the player.
import Range

scene = Range.logic.getCurrentScene()
owner = Range.logic.getCurrentController().owner

navmesh = scene.objects["Navmesh"]
player = scene.objects["Player"]

path = navmesh.findPath(owner.worldPosition, player.worldPosition)
print(len(path), "points")
```

```python

# Check for a wall on the way to the player: a factor below 1.0 means the ray stopped early.
import Range

scene = Range.logic.getCurrentScene()
owner = Range.logic.getCurrentController().owner

navmesh = scene.objects["Navmesh"]
player = scene.objects["Player"]

if navmesh.raycast(owner.worldPosition, player.worldPosition) < 1.0:
    print("Something is in the way")
```

```python

# Draw the navigation mesh to debug it. Run it every frame (Always sensor with True Pulse).
import Range

navmesh = Range.logic.getCurrentScene().objects["Navmesh"]
navmesh.draw(Range.logic.RM_TRIS)
```

```python

# Dynamic navigation mesh: a crate blocks the way, then frees it.
import Range

scene = Range.logic.getCurrentScene()
navmesh = scene.objects["Navmesh"]
crate = scene.objects["Crate"]

if navmesh.dynamic:
    navmesh.addObstacle(crate, 1.5)

# Later, when the crate is gone:
navmesh.removeObstacle(crate)
```

#### dynamic

True when the navigation mesh was built in tiles and obstacles can carve it (read-only).

**Type:** boolean

#### version

Incremented when the navigation mesh is rebuilt or finishes changing because of obstacles
(read-only). Paths found with an older version may cross new obstacles.

**Type:** integer

#### findPath(start, goal)

Finds the path from start to goal points.

- **`start`**: the start point
- **`start`**: 3D Vector
- **`goal`**: the goal point
- **`start`**: 3D Vector

**Returns:** a path as a list of points

**Return type:** list of points

#### raycast(start, goal)

Raycast from start to goal points.

- **`start`**: the start point
- **`start`**: 3D Vector
- **`goal`**: the goal point
- **`start`**: 3D Vector

**Returns:** the hit factor

**Return type:** float

#### draw(mode)

Draws a debug mesh for the navigation mesh.
On a dynamic navigation mesh, the obstacle cylinders are drawn in yellow.

- **`mode`**: the drawing mode (one of `these constants`)
- **`mode`**: integer

**Returns:** None

#### rebuild()

Rebuild the navigation mesh.

**Returns:** None

#### addObstacle(object, radius=0.0)

Makes the object carve every dynamic navigation mesh of its scene, following it when it moves.
Calling it again changes the radius. It has no effect on static navigation meshes.

- **`object`**: the obstacle, in the same scene as the navigation mesh
  - type: `KX_GameObject` or string
- **`radius`**: the world radius of the obstacle cylinder, 0.0 uses the object "Create Obstacle" radius or half its bounding box size
  - type: float

**Returns:** None

#### removeObstacle(object)

Stops the object carving the dynamic navigation meshes, including objects with "Create Obstacle".

- **`object`**: the obstacle
  - type: `KX_GameObject` or string

**Returns:** None

---

## KX_NearSensor

Base class: [`KX_CollisionSensor`](#kx_collisionsensor)

A near sensor is a specialised form of touch sensor.

```python
# Open the door when someone gets close, and only close it further away.
import Range

sensor = Range.logic.getCurrentController().sensors["Near"]

sensor.distance = 3.0
sensor.resetDistance = 5.0

if sensor.positive:
    print(sensor.hitObject.name, "is near")
```

#### distance

The near sensor activates when an object is within this distance.

**Type:** float

#### resetDistance

The near sensor deactivates when the object exceeds this distance.

**Type:** float

---

## KX_NetworkMessageActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Message Actuator

```python
# Send a message to objects in the scene.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Message"]

act.subject = "door_open"
act.body = "north"
act.usePropBody = False
cont.activate(act)
```

#### propName

Messages will only be sent to objects with the given property name.

**Type:** string

#### subject

The subject field of the message.

**Type:** string

#### body

The body of the message.

**Type:** string

#### usePropBody

Send a property instead of a regular body message.

**Type:** boolean

---

## KX_NetworkMessageSensor

Base class: [`SCA_ISensor`](#sca_isensor)

The Message Sensor logic brick.

Currently only loopback (local) networks are supported.

```python
# Read the messages that arrived on this frame.
import Range

sensor = Range.logic.getCurrentController().sensors["Message"]

if sensor.positive:
    for subject, body in zip(sensor.subjects, sensor.bodies):
        print(subject, body)
```

#### subject

The subject the sensor is looking for.

**Type:** string

#### frameMessageCount

The number of messages received since the last frame. (read-only).

**Type:** integer

#### subjects

The list of message subjects received. (read-only).

**Type:** list of strings

#### bodies

The list of message bodies received. (read-only).

**Type:** list of strings

---

## KX_ObjectActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

The object actuator ("Motion Actuator") applies force, torque, displacement, angular displacement,
velocity, or angular velocity to an object.
Servo control allows to regulate force to achieve a certain speed target.

```python
# Move forward with a constant speed.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Motion"]

act.linV = (0.0, 5.0, 0.0)
act.useLocalLinV = True
cont.activate(act)
```

```python
# Push the object and turn it.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Motion"]

act.force = (0.0, 0.0, 50.0)
act.torque = (0.0, 0.0, 2.0)
cont.activate(act)
```

#### force

The force applied by the actuator.

**Type:** Vector((x, y, z))

#### useLocalForce

A flag specifying if the force is local.

**Type:** boolean

#### torque

The torque applied by the actuator.

**Type:** Vector((x, y, z))

#### useLocalTorque

A flag specifying if the torque is local.

**Type:** boolean

#### dLoc

The displacement vector applied by the actuator.

**Type:** Vector((x, y, z))

#### useLocalDLoc

A flag specifying if the dLoc is local.

**Type:** boolean

#### dRot

The angular displacement vector applied by the actuator

**Type:** Vector((x, y, z))

> **Note:**
Since the displacement is applied every frame, you must adjust the displacement based on the frame rate, or you game experience will depend on the player's computer speed.

#### useLocalDRot

A flag specifying if the dRot is local.

**Type:** boolean

#### linV

The linear velocity applied by the actuator.

**Type:** Vector((x, y, z))

#### useLocalLinV

A flag specifying if the linear velocity is local.

**Type:** boolean

> **Note:**
This is the target speed for servo controllers.

#### angV

The angular velocity applied by the actuator.

**Type:** Vector((x, y, z))

#### useLocalAngV

A flag specifying if the angular velocity is local.

**Type:** boolean

#### damping

The damping parameter of the servo controller.

**Type:** short

#### forceLimitX

The min/max force limit along the X axis and activates or deactivates the limits in the servo controller.

**Type:** list [min(float), max(float), bool]

#### forceLimitY

The min/max force limit along the Y axis and activates or deactivates the limits in the servo controller.

**Type:** list [min(float), max(float), bool]

#### forceLimitZ

The min/max force limit along the Z axis and activates or deactivates the limits in the servo controller.

**Type:** list [min(float), max(float), bool]

#### pid

The PID coefficients of the servo controller.

**Type:** list of floats [proportional, integral, derivate]

#### reference

The object that is used as reference to compute the velocity for the servo controller.

**Type:** `KX_GameObject` or None

---

## KX_ParentActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

The parent actuator can set or remove an objects parent object.

```python
# Attach the object to another one.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Parent"]

act.mode = Range.logic.KX_PARENT_SET
act.object = Range.logic.getCurrentScene().objects["Hand"]
act.ghost = True
cont.activate(act)
```

```python
# Release it.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Parent"]

act.mode = Range.logic.KX_PARENT_REMOVE
cont.activate(act)
```

#### object

the object this actuator sets the parent too.

**Type:** `KX_GameObject` or None

#### mode

The mode of this actuator.

**Type:** integer from 0 to 1.

#### compound

Whether the object shape should be added to the parent compound shape when parenting.

Effective only if the parent is already a compound shape.

**Type:** boolean

#### ghost

Whether the object should be made ghost when parenting
Effective only if the shape is not added to the parent compound shape.

**Type:** boolean

---

## KX_ParticleSystem

> **See also:**
[`KX_GameObject`](#kx_gameobject), [`KX_Scene`](#kx_scene)

Class `Range.types.KX_ParticleSystem`.

```python
# Change the fire of the object while the game runs.
import Range

own = Range.logic.getCurrentController().owner
particles = own.particles

if particles is not None:
    particles.particleCount = 200
    particles.lifetime = 1.5
    particles.blendMode = "ADDITIVE"
```

```python
# A single explosion.
import Range

particles = Range.logic.getCurrentController().owner.particles

particles.emissionMode = "BURST"
particles.burst()
```

```python
# Stop emitting.
import Range

particles = Range.logic.getCurrentController().owner.particles
particles.enabled = False
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### burst()

 `method`

Releases all particles at once on the next frame. Only on emitters with `burstMode` on.

#### billboardMode

*(new in Anastacio)* `attribute`

How particles face the camera: `'FULL'` or `'VERTICAL'` (rotates only on the vertical axis).

#### blendMode

*(new in Anastacio)* `attribute`

How particles blend with the scene: `'ALPHA'` or `'ADDITIVE'`. An unknown value raises `ValueError`.

#### burstInterval

*(new in Anastacio)* `attribute`

Interval in seconds between automatic bursts in burst mode.

#### burstMode

*(new in Anastacio)* `attribute`

`True` emits in bursts (explosions); `False` emits continuously.

#### collisionBounce

 `attribute`

How much a particle bounces when it hits (0 = no bounce).

#### collisionFriction

 `attribute`

Particle friction when sliding after a hit.

#### collisionHeight

 `attribute`

Ground plane height when `collisionMode` is 1.

#### collisionMode

 `attribute`

Particle collision: 0 none, 1 ground plane, 2 with what is on screen (screen-space).

#### color

 `attribute`

Initial particle color `[r, g, b, a]`.

#### debugUI

 `attribute · read-only`

`True` when the particle system debug panel is open.

#### drag

*(new in Anastacio)* `attribute`

Air resistance: how much particles slow down over time.

#### emissionAngle

 `attribute`

Emission cone opening, in degrees.

#### emissionDirection

 `attribute`

Direction `[x, y, z]` particles are emitted in.

#### emissionMode

*(new in Anastacio)* `attribute`

Emission mode: `'CONTINUOUS'` or `'BURST'` (all at once). `burstMode` follows this value.

#### emitterPosition

 `attribute`

Emitter position `[x, y, z]` relative to the object.

#### emitterRadius

 `attribute`

Radius of the area particles spawn from.

#### enabled

 `attribute`

Turns emission on or off.

#### endColor

 `attribute`

Particle color `[r, g, b, a]` at the end of its life (the color fades from `color` to it).

#### endSize

 `attribute`

Particle size at the end of its life.

#### flipbook

*(new in Anastacio)* `attribute`

#### fragmentShaderPath

 `attribute`

Path to your own `.glsl` to draw the particles. Empty goes back to the default look.

#### gravity

 `attribute`

Gravity applied to particles.

#### lifetime

 `attribute`

Lifetime of each particle, in seconds.

#### particleCount

 `attribute`

Maximum number of live particles.

#### size

 `attribute`

Initial particle size.

#### texture

 `attribute`

Path of the image used on particles. Empty removes the texture.

#### useBackfaceCulling

*(new in Anastacio)* `attribute`

Whether particles stop being drawn when seen from behind.

#### useDebugUi

*(new in Anastacio)* `attribute`

Shows the emitter debug panel during the game.

#### useObjectRotation

*(new in Anastacio)* `attribute`

#### useVortex

*(new in Anastacio)* `attribute`

Turns on the vortex: particles rise spinning around the emitter.

#### velocity

 `attribute`

Initial particle velocity.

#### velocityRandomness

 `attribute`

Random variation of the initial velocity (0 = all the same).

#### vortexHeight

*(new in Anastacio)* `attribute`

Vortex height.

#### vortexRadiusTop

*(new in Anastacio)* `attribute`

Vortex radius at the top.

#### vortexRotationSpeed

*(new in Anastacio)* `attribute`

Vortex rotation speed.

---

## KX_PlanarMap

Base class: [`KX_TextureRenderer`](#kx_texturerenderer)

> **See also:**
[`KX_CubeMap`](#kx_cubemap), [`KX_TextureRenderer`](#kx_texturerenderer)

Python API for realtime planar map textures.

```python
# Update a mirror only when needed.
import Range

own = Range.logic.getCurrentController().owner
mirror = own.meshes[0].materials[0].textures[0].renderer

mirror.autoUpdate = False
mirror.update()
print(mirror.normal)
```

#### normal

Plane normal used to compute the reflection or refraction orientation of the render camera.

**Type:** `mathutils.Vector`

---

## KX_PolyProxy

Base class: [`SCA_IObject`](#sca_iobject)

A polygon holds the index of the vertex forming the poylgon.

Note:
The polygon attributes are read-only, you need to retrieve the vertex proxy if you want
to change the vertex settings.

```python
# Find the material of the face hit by a ray.
import Range

own = Range.logic.getCurrentController().owner
hit, point, normal, poly = own.rayCast((0, 0, -10), own, 20.0, "", 0, 0, 1)

if poly is not None:
    print(poly.material_name, poly.getNumVertex())
```

```python
# Read the vertices of the first face of a mesh.
import Range

mesh = Range.logic.getCurrentController().owner.meshes[0]
poly = mesh.getPolygon(0)

for i in range(poly.getNumVertex()):
    print(poly.getVertexIndex(i))
```

#### material_name

The name of polygon material, empty if no material.

**Type:** string

#### material

The material of the polygon.

**Type:** `KX_BlenderMaterial`

#### texture_name

The texture name of the polygon.

**Type:** string

#### material_id

The material index of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Type:** integer

#### v1

vertex index of the first vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Type:** integer

#### v2

vertex index of the second vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Type:** integer

#### v3

vertex index of the third vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

**Type:** integer

#### ~~v4~~

> **Deprecated polygons are triangles.:**

**Type:** integer

#### visible

visible state of the polygon: 1=visible, 0=invisible.

**Type:** integer

#### collide

collide state of the polygon: 1=receives collision, 0=collision free.

**Type:** integer

#### vertices

Returns the list of vertices of this polygon.

**Type:** `KX_VertexProxy` list (read only)

#### getMaterialName()

Returns the polygon material name with MA prefix

**Returns:** material name

**Return type:** string

#### getMaterial()

**Returns:** The polygon material

**Return type:** `KX_BlenderMaterial`

#### getTextureName()

**Returns:** The texture name

**Return type:** string

#### getMaterialIndex()

Returns the material bucket index of the polygon.
This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from `MeshProxy`.

**Returns:** the material index in the mesh

**Return type:** integer

#### getNumVertex()

Returns the number of vertex of the polygon.

**Returns:** number of vertex.

**Return type:** integer

#### isVisible()

Returns whether the polygon is visible or not

**Returns:** 0=invisible, 1=visible

**Return type:** boolean

#### isCollider()

Returns whether the polygon is receives collision or not

**Returns:** 0=collision free, 1=receives collision

**Return type:** integer

#### getVertexIndex(vertex)

Returns the mesh vertex index of a polygon vertex
This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from `MeshProxy`.

- **`vertex`**: index of the vertex in the polygon: 0->2
- **`vertex`**: integer

**Returns:** mesh vertex index

**Return type:** integer

#### getMesh()

Returns a mesh proxy

**Returns:** mesh proxy

**Return type:** `MeshProxy`

---

## KX_PythonComponent

Base class: [`EXP_Value`](#exp_value)

> **See also:**
[`KX_GameObject`](#kx_gameobject), [`SCA_PythonController`](#sca_pythoncontroller)

Python component can be compared to python logic bricks with parameters.
The python component is a script loaded in the UI, this script defined a component class by inheriting from `KX_PythonComponent`.
This class must contain a dictionary of properties: `args` and two default functions: `start` and `update`.

The script must have .py extension.

The component properties are loaded from the `args` attribute from the UI at loading time.
When the game start the function `start` is called with as arguments a dictionary of the properties' name and value.
The `update` function is called every frames during the logic stage before running logics bricks,
the goal of this function is to handle and process everything.

The following component example moves and rotates the object when pressing the keys W, A, S and D.

```python

import Range
from collections import OrderedDict

class ThirdPerson(Range.types.KX_PythonComponent):
    """Basic third person controls

    W: move forward
    A: turn left
    S: move backward
    D: turn right

    """

    #

    args = OrderedDict([
        ("Move Speed", 0.1),
        ("Turn Speed", 0.04)
    ])

    def start(self, args):
        self.move_speed = args['Move Speed']
        self.turn_speed = args['Turn Speed']

    def update(self):
        keyboard = Range.logic.keyboard.events

        move = 0
        rotate = 0

        if keyboard[Range.events.WKEY]:
            move += self.move_speed
        if keyboard[Range.events.SKEY]:
            move -= self.move_speed

        if keyboard[Range.events.AKEY]:
            rotate += self.turn_speed
        if keyboard[Range.events.DKEY]:
            rotate -= self.turn_speed

        self.object.applyMovement((0, move, 0), True)
        self.object.applyRotation((0, 0, rotate), True)
```

Since the components are loaded for the first time outside the bge, then `bge` is a fake module that contains only the class
`KX_PythonComponent` to avoid importing all the bge modules.
This behavior is safer but creates some issues at loading when the user want to use functions or attributes from the bge modules other
than the `KX_PythonComponent` class. The way is to not call these functions at loading outside the Range. To detect it, the bge
module contains the attribute `__component__` when it's imported outside the Range.

The following component example add a "Cube" object at initialization and move it along x for each update. It shows that the user can
use functions from scene and load the component outside the bge by setting global attributes in a condition at the beginning of the
script.

```python

import Range

if not hasattr(bge, "__component__"):
    global scene
    scene = Range.logic.getCurrentScene()

class Component(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        scene.addObject("Cube")

    def update(self):
        scene.objects["Cube"].worldPosition.x += 0.1
```

The property types supported are float, integer, boolean, string, set (for enumeration) and Vector 2D, 3D and 4D. The following example
show all of these property types.

```python

from Range import *
from mathutils import *
from collections import OrderedDict

class Component(types.KX_PythonComponent):
     args = OrderedDict([
         ("Float", 58.6),
         ("Integer", 150),
         ("Boolean", True),
         ("String", "Cube"),
         ("Enum", {"Enum 1", "Enum 2", "Enum 3"}),
         ("Vector 2D", Vector((0.8, 0.7))),
         ("Vector 3D", Vector((0.4, 0.3, 0.1))),
         ("Vector 4D", Vector((0.5, 0.2, 0.9, 0.6)))
     ])

     def start(self, args):
         print(args)

     def update(self):
         pass
```

```python

# Component that spins the object, with the speed set in the editor.
import Range
from collections import OrderedDict

class Spinner(Range.types.KX_PythonComponent):
    args = OrderedDict([
        ("Speed", 0.02),
    ])

    def start(self, args):
        self.speed = args["Speed"]

    def update(self):
        self.object.applyRotation((0, 0, self.speed), True)
```

```python

# Component that follows another object, chosen by name in the editor.
import Range
from collections import OrderedDict

class Follow(Range.types.KX_PythonComponent):
    args = OrderedDict([
        ("Target", "Player"),
        ("Speed", 0.05),
    ])

    def start(self, args):
        self.target = self.object.scene.objects[args["Target"]]
        self.speed = args["Speed"]

    def update(self):
        distance, direction, local = self.object.getVectTo(self.target)
        self.object.worldPosition += direction * self.speed

    def dispose(self):
        print("Component removed")
```

#### object

The object owner of the component.

**Type:** `KX_GameObject`

#### args

Dictionary of the component properties, the keys are string and the value can be: float, integer, Vector(2D/3D/4D), set, string.

**Type:** dict

#### start(args)

Initialize the component.

- **`args`**: The dictionary of the properties' name and value.
  - type: dict

> **Caution:**
This function must be inherited in the python component class.

#### update()

Process the logic of the component.

> **Caution:**
This function must be inherited in the python component class.

#### dispose()

Function called when the component is destroyed.

> **Caution:**
This function must be inherited in the python component class.

---

## KX_PythonJoystick

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`SCA_JoystickSensor`](#sca_joysticksensor), [`Range.events`](#rangeevents), [`KX_InputSystem`](#kx_inputsystem)

A Python interface to a joystick.

```python
# Move with the left stick and jump with a button.
import Range

joystick = Range.logic.joysticks[0]

if joystick is not None:
    x, y = joystick.axisValues[0], joystick.axisValues[1]
    print(x, y)

    if 0 in joystick.activeButtons:
        print("Jump")
```

```python
# Vibrate for half a second.
import Range

joystick = Range.logic.joysticks[0]

if joystick is not None and joystick.hasVibration:
    joystick.strengthLeft = 0.8
    joystick.strengthRight = 0.8
    joystick.duration = 500
    joystick.startVibration()
```

#### name

The name assigned to the joystick by the operating system. (read-only)

**Type:** string

#### activeButtons

A list of active button values. (read-only)

**Type:** list

#### axisValues

The state of the joysticks axis as a list of values `numAxis` long. (read-only).

**Type:** list of ints.

Each specifying the value of an axis between -1.0 and 1.0
depending on how far the axis is pushed, 0 for nothing.
The first 2 values are used by most joysticks and gamepads for directional control.
3rd and 4th values are only on some joysticks and can be used for arbitary controls.

* left:[-1.0, 0.0, ...]
* right:[1.0, 0.0, ...]
* up:[0.0, -1.0, ...]
* down:[0.0, 1.0, ...]

#### hatValues (Deprecated. Use :data:`activeButtons` instead)

The state of the joysticks hats as a list of values `numHats` long. (read-only).

**Type:** list of ints

Each specifying the direction of the hat from 1 to 12, 0 when inactive.

Hat directions are as follows...

* 0:None
* 1:Up
* 2:Right
* 4:Down
* 8:Left
* 3:Up - Right
* 6:Down - Right
* 12:Down - Left
* 9:Up - Left

#### numAxis

The number of axes for the joystick at this index. (read-only).

**Type:** integer

#### numButtons

The number of buttons for the joystick at this index. (read-only).

**Type:** integer

#### numHats (Deprecated. Use :data:`numButtons` instead)

The number of hats for the joystick at this index. (read-only).

**Type:** integer

#### startVibration()

Starts the vibration.

**Returns:** None

#### stopVibration()

Stops the vibration.

**Returns:** None

#### strengthLeft

Strength of the Low frequency joystick's motor (placed at left position usually).

**Type:** float (0.0 to 1.0)

#### strengthRight

Strength of the High frequency joystick's motor (placed at right position usually).

**Type:** float (0.0 to 1.0)

#### duration

Duration of the vibration in milliseconds.

**Type:** integer (0 to infinite)

#### isVibrating

Check status of joystick vibration

**Type:** bool (true vibrating and false stopped)

#### hasVibration

Check if the joystick supports vibration

**Type:** bool (true supported and false not supported)

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### stopVibration()

 `method`

Stops the gamepad vibration.

#### duration

 `attribute`

Vibration duration, in milliseconds.

#### hasVibration

 `attribute · read-only`

`True` if the gamepad supports vibration.

#### inputs

 `attribute · read-only`

Dictionary `{button: SCA_InputEvent}` with the state of each gamepad button.

#### isVibrating

 `attribute · read-only`

`True` while the gamepad is vibrating.

#### strengthLeft

 `attribute`

Left vibration motor strength (0 to 1).

#### strengthRight

 `attribute`

Right vibration motor strength (0 to 1).

---

## KX_PythonKeyboard

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`Range.events`](#rangeevents), [`SCA_InputEvent`](#sca_inputevent), [`KX_PythonMouse`](#kx_pythonmouse)

The current keyboard.

```python
# Check keys by state.
import Range

keyboard = Range.logic.keyboard

if keyboard.inputs[Range.events.ESCKEY].activated:
    print("Pause")
```

```python
# Read typed text and use the clipboard.
import Range

keyboard = Range.logic.keyboard

print(keyboard.text)
keyboard.setClipboard("Saved code: 1234")
print(keyboard.getClipboard())
```

#### inputs

A dictionary containing the input of each keyboard key. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~events~~

A dictionary containing the status of each keyboard event or key. (read-only).

> **Deprecated use :data:`inputs`:**

**Type:** dictionary {`keycode`:`status`, ...}

#### activeInputs

A dictionary containing the input of only the active keyboard keys. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~active_events~~

A dictionary containing the status of only the active keyboard events or keys. (read-only).

> **Deprecated use :data:`activeInputs`:**

**Type:** dictionary {`keycode`:`status`, ...}

#### text

The typed unicode text from the last frame.

**Type:** string

#### getClipboard()

Gets the clipboard text.

**Return type:** string

#### setClipboard(text)

Sets the clipboard text.

- **`text`**: New clipboard text
  - type: string

---

## KX_PythonMotion

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Motion sensors of the device (phone or tablet), available as `Range.logic.motion`.

Values come from the browser in the Web runtime (`DeviceMotionEvent` and `DeviceOrientationEvent`),
including the Android app, which runs the Web runtime inside a WebView. On other platforms there is no
sensor source yet: `available` is `False`, vectors are zero and `tilt` is `(0.0, 0.0)`, so the
same script runs everywhere.

Vectors use the axes of the screen as it is currently shown, in portrait or landscape: x to the right, y to
the top of the screen and z out of the screen, toward the player.

A tilt-controlled object:

```python

from Range import logic, events

def main(cont):
    own = cont.owner
    if logic.mouse.inputs[events.LEFTMOUSE].activated:  # a tap on the screen
        logic.motion.calibrate()
    x, y = logic.motion.tilt
    own.applyForce((x * 20.0, y * 20.0, 0.0))
```

#### available

`True` while the sensors are sending data. It becomes `False` when no reading arrived in the last
second (no sensor, desktop browser, page in background). (read-only).

**Type:** boolean

#### gyroscope

Rotation speed around each screen axis, in radians per second. (read-only).

**Type:** `mathutils.Vector`

#### accelerometer

Acceleration including gravity, in m/s². With the device lying still, face up, it is close to
`(0, 0, 9.8)`. (read-only).

**Type:** `mathutils.Vector`

#### gravity

Gravity alone, in m/s², pointing up as in `accelerometer`. When the device does not report
acceleration without gravity, it is estimated from `accelerometer` with a low-pass filter. (read-only).

**Type:** `mathutils.Vector`

#### orientation

Device orientation angles `(alpha, beta, gamma)` in degrees, exactly as given by the browser. They follow
the device axes, not the screen axes. (read-only).

**Type:** `mathutils.Vector`

#### tilt

How far the device is tilted from its neutral position, from -1.0 to 1.0 on each axis: the screen direction
a ball would roll to. `x` is positive when the right edge of the screen goes down, `y` when the top edge
goes down. The neutral position is the device lying flat until `calibrate` is called. (read-only).

**Type:** tuple (float, float)

#### calibrate()

Take the current position as neutral for `tilt`, so the player can hold the device the way they like.

**Returns:** `True` if there was a sensor reading to calibrate with, `False` otherwise.

**Return type:** boolean

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### recenter()

*(new in Anastacio)* `method`

Uses the current head direction (VR) as "forward". `False` if the sensor is not ready.

**Returns:** `bool`

#### headOrientation

*(new in Anastacio)* `attribute · read-only`

Head orientation (3×3 matrix), already recentered.

#### recenterTime

*(new in Anastacio)* `attribute`

Time in seconds to recenter by itself when the head stays still (0 turns it off).

#### smoothing

*(new in Anastacio)* `attribute`

Head movement smoothing (0 to 5).

---

## KX_PythonMouse

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`Range.events`](#rangeevents), [`SCA_InputEvent`](#sca_inputevent), [`KX_PythonKeyboard`](#kx_pythonkeyboard)

The current mouse.

> **Caution:**
Mouse normalization is using the maximum coordinate in width and height, whether `Range.render.getWindowWidth() - 1` or `Range.render.getWindowHeight() - 1`.

A script setting the mouse at center is similar to the following example:

```python

import Range

w, h = Range.render.getWindowWidth() - 1, Range.render.getWindowHeight() - 1
center_x, center_y = (w // 2) / w, (h // 2) / h

Range.logic.mouse.position = center_x, center_y
```

Note the usage of floor division to round an existing coordinate.

#### inputs

A dictionary containing the input of each mouse event. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~events~~

a dictionary containing the status of each mouse event. (read-only).

> **Deprecated use :data:`inputs`:**

**Type:** dictionary {`keycode`:`status`, ...}

#### activeInputs

A dictionary containing the input of only the active mouse events. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~active_events~~

a dictionary containing the status of only the active mouse events. (read-only).

> **Deprecated use :data:`activeInputs`:**

**Type:** dictionary {`keycode`:`status`, ...}

#### position

The normalized x and y position of the mouse cursor.

**Type:** tuple (x, y)

#### visible

The visibility of the mouse cursor.

**Type:** boolean

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### reCenter()

 `method`

Puts the cursor back in the window center (useful for first-person cameras).

#### deltaPosition

 `attribute · read-only`

How much the mouse moved since the last frame, `(x, y)`.

---

## KX_RadarSensor

Base class: [`KX_NearSensor`](#kx_nearsensor)

Radar sensor is a near sensor with a conical sensor object.

```python
# Detect enemies in the cone set in the editor. Distance and angle can only be read.
import Range

sensor = Range.logic.getCurrentController().sensors["Radar"]

print(sensor.distance, sensor.angle)

if sensor.positive:
    print(sensor.hitObject.name)
```

#### coneOrigin

The origin of the cone with which to test. The origin is in the middle of the cone. (read-only).

**Type:** `mathutils.Vector`

#### coneTarget

The center of the bottom face of the cone with which to test. (read-only).

**Type:** `mathutils.Vector`

#### distance

The height of the cone with which to test.

**Type:** float

#### angle

The angle of the cone (in degrees) with which to test.

**Type:** float

#### axis

The axis on which the radar cone is cast.

**Type:** integer from 0 to 5

KX_RADAR_AXIS_POS_X, KX_RADAR_AXIS_POS_Y, KX_RADAR_AXIS_POS_Z,
KX_RADAR_AXIS_NEG_X, KX_RADAR_AXIS_NEG_Y, KX_RADAR_AXIS_NEG_Z

---

## KX_RaySensor

Base class: [`SCA_ISensor`](#sca_isensor)

A ray sensor detects the first object in a given direction.

```python
# See what is ahead of the object.
import Range

sensor = Range.logic.getCurrentController().sensors["Ray"]

sensor.range = 10.0
sensor.axis = Range.logic.KX_RAY_AXIS_POS_Y

if sensor.positive:
    print(sensor.hitObject.name, sensor.hitPosition, sensor.hitNormal)
```

#### propName

The property the ray is looking for.

**Type:** string

#### range

The distance of the ray.

**Type:** float

#### useMaterial

Whether or not to look for a material (false = property).

**Type:** boolean

#### useXRay

Whether or not to use XRay.

**Type:** boolean

#### mask

The collision mask (16 layers mapped to a 16-bit integer) combined with each object's collision group, to hit only a subset of the
objects in the scene. Only those objects for which `collisionGroup & mask` is true can be hit.

**Type:** bitfield

#### hitObject

The game object that was hit by the ray. (read-only).

**Type:** `KX_GameObject`

#### hitPosition

The position (in worldcoordinates) where the object was hit by the ray. (read-only).

**Type:** `mathutils.Vector`

#### hitNormal

The normal (in worldcoordinates) of the object at the location where the object was hit by the ray. (read-only).

**Type:** `mathutils.Vector`

#### hitMaterial

The material of the object in the face hit by the ray. (read-only).

**Type:** string

#### rayDirection

The direction from the ray (in worldcoordinates). (read-only).

**Type:** `mathutils.Vector`

#### axis

The axis the ray is pointing on.

**Type:** integer from 0 to 5

* KX_RAY_AXIS_POS_X
* KX_RAY_AXIS_POS_Y
* KX_RAY_AXIS_POS_Z
* KX_RAY_AXIS_NEG_X
* KX_RAY_AXIS_NEG_Y
* KX_RAY_AXIS_NEG_Z

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### gazeAngle

*(new in Anastacio)* `attribute`

Gaze tolerance (0 to 1): how far off the ray center the target can be.

#### gazeProgress

*(new in Anastacio)* `attribute · read-only`

Fixed gaze progress, from 0 to 1. Reaches 1 after `gazeTime` seconds looking at the target.

#### gazeTime

*(new in Anastacio)* `attribute`

Time in seconds looking at the target for the sensor to fire (0 to 30).

---

## KX_ReplaceMeshActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Edit Object actuator, in Replace Mesh mode.

> **Caution:**
Replace mesh actuators will be ignored if at game start, the named mesh doesn't exist.

This will generate a warning in the console

```text

Error: GameObject 'Name' ReplaceMeshActuator 'ActuatorName' without object
```

```python

# Level-of-detail
# Switch a game object's mesh based on its depth in the camera view.
# +----------+     +-----------+     +-------------------------------------+
# | Always   +-----+ Python    +-----+ Edit Object (Replace Mesh) LOD.Mesh |
# +----------+     +-----------+     +-------------------------------------+
from Range import logic

# List detail meshes here
# Mesh (name, near, far)
# Meshes overlap so that they don't 'pop' when on the edge of the distance.
meshes = ((".Hi", 0.0, -20.0),
      (".Med", -15.0, -50.0),
      (".Lo", -40.0, -100.0)
    )

cont = logic.getCurrentController()
object = cont.owner
actuator = cont.actuators["LOD." + obj.name]
camera = logic.getCurrentScene().active_camera

def Depth(pos, plane):
  return pos[0]*plane[0] + pos[1]*plane[1] + pos[2]*plane[2] + plane[3]

# Depth is negative and decreasing further from the camera
depth = Depth(object.position, camera.world_to_camera[2])

newmesh = None
curmesh = None
# Find the lowest detail mesh for depth
for mesh in meshes:
  if depth < mesh[1] and depth > mesh[2]:
    newmesh = mesh
  if "ME" + object.name + mesh[0] == actuator.getMesh():
      curmesh = mesh

if newmesh != None and "ME" + object.name + newmesh[0] != actuator.mesh:
  # The mesh is a different mesh - switch it.
  # Check the current mesh is not a better fit.
  if curmesh == None or curmesh[1] < depth or curmesh[2] > depth:
    actuator.mesh = object.name + newmesh[0]
    cont.activate(actuator)
```

#### mesh

`MeshProxy` or the name of the mesh that will replace the current one.

Set to None to disable actuator.

**Type:** `MeshProxy` or None if no mesh is set

#### useDisplayMesh

when true the displayed mesh is replaced.

**Type:** boolean

#### usePhysicsMesh

when true the physics mesh is replaced.

**Type:** boolean

#### instantReplaceMesh()

Immediately replace mesh without delay.

---

## KX_Scene

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`KX_GameObject`](#kx_gameobject), [`KX_Camera`](#kx_camera), [`KX_WorldInfo`](#kx_worldinfo), [`KX_2DFilterManager`](#kx_2dfiltermanager), [`Range.logic`](#rangelogic)

An active scene that gives access to objects, cameras, lights and scene attributes.

The activity culling stuff is supposed to disable logic bricks when their owner gets too far
from the active camera.  It was taken from some code lurking at the back of KX_Scene - who knows
what it does!

```python

from Range import logic

# get the scene
scene = logic.getCurrentScene()

# print all the objects in the scene
for object in scene.objects:
   print(object.name)

# get an object named 'Cube'
object = scene.objects["Cube"]

# get the first object in the scene.
object = scene.objects[0]
```

```python

# Get the depth of an object in the camera view.
from Range import logic

object = logic.getCurrentController().owner
cam = logic.getCurrentScene().active_camera

# Depth is negative and decreasing further from the camera
depth = object.position[0]*cam.world_to_camera[2][0] + object.position[1]*cam.world_to_camera[2][1] + object.position[2]*cam.world_to_camera[2][2] + cam.world_to_camera[2][3]
```

@bug: All attributes are read only at the moment.

```python

# Add a bullet at the gun. It disappears after 120 frames.
import Range

scene = Range.logic.getCurrentScene()
gun = Range.logic.getCurrentController().owner

bullet = scene.addObject("Bullet", gun, 120)
bullet.worldLinearVelocity = gun.getAxisVect((0, 30, 0))
```

```python

# Switch to another camera.
import Range

scene = Range.logic.getCurrentScene()
scene.active_camera = scene.cameras["CameraBack"]
```

```python

# Pause or resume another scene, like the level behind a pause menu.
import Range

level = Range.logic.getSceneList()["Level"]

if level.suspended:
    level.resume()
else:
    level.suspend()
```

```python

# Find objects by property and go to the next level.
import Range

scene = Range.logic.getCurrentScene()
coins = [obj for obj in scene.objects if "coin" in obj]

if not coins:
    scene.replace("Level2")
```

```python

# Run a function right before each frame is drawn.
import Range

def before_draw():
    print("Drawing")

scene = Range.logic.getCurrentScene()
scene.pre_draw.append(before_draw)
```

#### name

The scene's name, (read-only).

**Type:** string

#### objects

A list of objects in the scene, (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`

#### objectsInactive

A list of objects on background layers (used for the addObject actuator), (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`

#### lights

A list of lights in the scene, (read-only).

**Type:** `EXP_ListValue` of `KX_LightObject`

#### cameras

A list of cameras in the scene, (read-only).

**Type:** `EXP_ListValue` of `KX_Camera`

#### texts

A list of texts in the scene, (read-only).

**Type:** `EXP_ListValue` of `KX_FontObject`

#### active_camera

The current active camera.

**Type:** `KX_Camera`

> **Note:**
This can be set directly from python to avoid using the `KX_SceneActuator`.

#### overrideCullingCamera

The override camera used for scene culling, if set to None the culling is proceeded with the camera used to render.

**Type:** `KX_Camera` or None

#### world

The current active world, (read-only).

**Type:** `KX_WorldInfo`

#### filterManager

The scene's 2D filter manager, (read-only).

**Type:** `KX_2DFilterManager`

#### suspended

True if the scene is suspended, (read-only).

**Type:** boolean

#### activityCulling

True if the scene allow object activity culling.

**Type:** boolean

#### dbvt_culling

True when Dynamic Bounding box Volume Tree is set (read-only).

**Type:** boolean

#### pre_draw

A list of callables to be run before the render step. The callbacks can take as argument the rendered camera.

**Type:** list

#### post_draw

A list of callables to be run after the render step.

**Type:** list

#### pre_draw_setup

A list of callables to be run before the drawing setup (i.e., before the model view and projection matrices are computed).
The callbacks can take as argument the rendered camera, the camera could be temporary in case of stereo rendering.

**Type:** list

#### onRemove

A list of callables to run when the scene is destroyed.

```python

@scene.onRemove.append
def callback(scene):
      print('exiting %s...' % scene.name)
```

**Type:** list

#### gravity

The scene gravity using the world x, y and z axis.

**Type:** Vector((gx, gy, gz))

#### maxDebris

The number of fragments of broken objects kept alive in the scene; past it the oldest are removed.
Starts with Scene > Game Physics > Max Debris. 0 means no limit. Lowering it removes the extra pieces at once.

**Type:** integer in [0, 100000]

#### explode(position, radius=5.0, force=20.0, upBias=0.3, occlusion=True, mask=0xFFFF, ignore=None)

Radial impulse on the dynamic objects around position, falling to zero at radius
(`force * (1 - distance / radius)`). Destructible objects hit above their `KX_GameObject.breakImpulse`
break and their pieces are pushed, sharing the impulse by mass. Explosive objects hit above their Impact
Impulse (with Chain Reaction on) detonate on the next frame.

- **`position`**: The center of the blast.
  - type: 3D Vector
- **`radius`**: The distance the blast reaches.
  - type: float
- **`force`**: The impulse at the center.
  - type: float
- **`upBias`**: How much the push is tilted upwards, 0.0 is straight away from the center.
  - type: float
- **`occlusion`**: If True, static geometry between the center and an object shields it.
  - type: boolean
- **`mask`**: The collision groups reached.
  - type: bitfield
- **`ignore`**: An object or a list of objects left out.
  - type: `KX_GameObject` or list

**Returns:** The objects reached (not the new pieces).

**Return type:** list of `KX_GameObject`

#### addObject(object, reference, time=0.0)

Adds an object to the scene like the Add Object Actuator would.

- **`object`**: The (name of the) object to add.
  - type: `KX_GameObject` or string
- **`reference`**: The (name of the) object which position, orientation, and scale to copy (optional), if the object to add is a light and there is not reference the light's layer will be the same that the active layer in the blender scene.
  - type: `KX_GameObject` or string
- **`time`**: The lifetime of the added object, in frames (assumes one frame is 1/50 second). A time of 0.0 means the object will last forever (optional).
  - type: float

**Returns:** The newly added object.

**Return type:** `KX_GameObject`

#### end()

Removes the scene from the game.

#### restart()

Restarts the scene.

#### replace(scene)

Replaces this scene with another one.

- **`scene`**: The name of the scene to replace this scene with.
  - type: string

**Returns:** True if the scene exists and was scheduled for addition, False otherwise.

**Return type:** boolean

#### suspend()

Suspends this scene.

#### resume()

Resume this scene.

#### get(key, default=None)

Return the value matching key, or the default value if its not found.

**Returns:** The key value or a default.

#### drawObstacleSimulation()

Draw debug visualization of obstacle simulation.

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### convertObject(name, children=True)

 `method`

Creates now an object that was left out at load time by the **Convert** option (and its unconverted children). It goes to `objects` if it is on an active layer, otherwise to `objectsInactive` (ready for `addObject`). An object already converted is returned as is.

**Returns:** `KX_GameObject`

#### getQualityPreset()

*(undocumented)* `method`

#### play_cutscene(sequence=0)

 `method`

Starts the scene native Cutscene. Returns `True` on success.

**Returns:** `bool`

#### play_take(name)

 `method`

Plays a Rec Play take on all its actors. `True` when the take exists.

**Returns:** `bool`

#### release_cutscene_trigger(name)

 `method`

Releases a Cutscene **Wait Trigger** event waiting for `name`. `True` if it was waiting right now; otherwise the trigger is kept for the next Wait Trigger with that name. A message with subject `name` does the same.

**Returns:** `bool`

#### restart_cutscene()

 `method`

Restarts the active Cutscene and removes the objects it created.

#### setQualityPreset()

*(undocumented)* `method`

#### skip_cutscene()

 `method`

Jumps to the end of the playing Cutscene: dialogs, waits, camera paths and fades are dropped; the other remaining events run (camera restore, unlock, scene change). Returns `False` when nothing was playing. Tab or the gamepad Start button do the same unless `Range.logic.globalDict["cutscene_skip"]` is `False`.

#### stop_cutscene()

 `method`

Stops the Cutscene and removes the objects it created.

#### speakers

 `attribute · read-only`

List of the scene sound objects (`KX_Speaker`).

#### takes

*(new in Anastacio)* `attribute · read-only`

Names of the scene's Rec Play takes (read-only).

#### thread_logic_1

 `attribute`

List of functions called every frame on the parallel logic thread. Same usage as `pre_draw`.

#### unconvertedObjects

*(new in Anastacio)* `attribute · read-only`

Names of the objects that can still be created with `convertObject()`.

#### visible

*(new in Anastacio)* `attribute`

#### worldSun

 `attribute · read-only`

Sun light linked to the World (sky sun position), or `None`.

---

## KX_SceneActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Scene Actuator logic brick.

> **Caution:**
Scene actuators that use a scene name will be ignored if at game start, the named scene doesn't exist or is empty

This will generate a warning in the console:

```text

Error: GameObject 'Name' has a SceneActuator 'ActuatorName' (SetScene) without scene
```

#### scene

the name of the scene to change to/overlay/underlay/remove/suspend/resume.

**Type:** string

#### camera

the camera to change to.

**Type:** `KX_Camera` on read, string or `KX_Camera` on write

> **Note:**
When setting the attribute, you can use either a `KX_Camera` or the name of the camera.

#### useRestart

Set flag to True to restart the sene.

**Type:** boolean

#### mode

The mode of the actuator.

**Type:** integer from 0 to 5.

---

## KX_SoundActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

> **See also:**
[`KX_Speaker`](#kx_speaker)

Sound Actuator.

The `startSound`, `pauseSound` and `stopSound` do not require the actuator to be activated - they act instantly provided that the actuator has been activated once at least.

```python
# Play a sound with a random pitch.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Sound"]

act.pitch = 0.9 + Range.logic.getRandomFloat() * 0.2
act.volume = 0.8
act.startSound()
```

```python
# Pause and stop it.
import Range

act = Range.logic.getCurrentController().actuators["Sound"]

act.pauseSound()
act.stopSound()
```

#### volume

The volume (gain) of the sound.

**Type:** float

#### time

The current position in the audio stream (in seconds).

**Type:** float

#### pitch

The pitch of the sound.

**Type:** float

#### mode

The operation mode of the actuator. Can be one of `these constants`

**Type:** integer

#### sound

The sound the actuator should play.

**Type:** Audaspace factory

#### is3D

Whether or not the actuator should be using 3D sound. (read-only)

**Type:** boolean

#### volume_maximum

The maximum gain of the sound, no matter how near it is.

**Type:** float

#### volume_minimum

The minimum gain of the sound, no matter how far it is away.

**Type:** float

#### distance_reference

The distance where the sound has a gain of 1.0.

**Type:** float

#### distance_maximum

The maximum distance at which you can hear the sound.

**Type:** float

#### attenuation

The influence factor on volume depending on distance.

**Type:** float

#### cone_angle_inner

The angle of the inner cone.

**Type:** float

#### cone_angle_outer

The angle of the outer cone.

**Type:** float

#### cone_volume_outer

The gain outside the outer cone (the gain in the outer cone will be interpolated between this value and the normal gain in the inner cone).

**Type:** float

#### startSound()

Starts the sound.

**Returns:** None

#### pauseSound()

Pauses the sound.

**Returns:** None

#### stopSound()

Stops the sound.

**Returns:** None

---

## KX_Speaker

> **See also:**
[`KX_SoundActuator`](#kx_soundactuator), [`KX_Scene`](#kx_scene)

Class `Range.types.KX_Speaker`.

```python
# Control a speaker of the scene.
import Range

scene = Range.logic.getCurrentScene()

for speaker in scene.speakers:
    speaker.volume = 0.5
    speaker.pitch = 1.0
    speaker.Play()
```

```python
# Pause, continue from the start or stop.
import Range

speaker = Range.logic.getCurrentScene().speakers[0]

speaker.Pause()
speaker.Restart()
speaker.Stop()
```

```python
# Sound that gets lower with distance.
import Range

speaker = Range.logic.getCurrentScene().speakers[0]

speaker.distance_reference = 2.0
speaker.distance_maximum = 40.0
speaker.attenuation = 1.0
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### GetActiveEffect()

 `method`

Active sound effect: 0 none, 1 reverb.

**Returns:** `int`

#### GetActiveEffectFilter()

 `method`

Active filter: 0 none, 1 low-pass, 2 high-pass, 3 band-pass.

**Returns:** `int`

#### Pause()

 `method`

Pauses the sound.

#### Play()

 `method`

Plays the sound.

#### RemoveEffect()

 `method`

Removes the sound effect.

#### Restart()

 `method`

Plays the sound from the beginning.

#### SetEffect(effectType, filterType=0)

 `method`

Applies an effect: `effectType` 1 = reverb; `filterType` 0 none, 1 low-pass, 2 high-pass, 3 band-pass. After that, reverb areas leave this Speaker alone.

#### SetSound(sound, cache=False)

 `method`

Changes the sound (an `aud.Sound`). With `cache=True`, keeps the decoded sound in memory.

#### Stop()

 `method`

Stops the sound.

#### attenuation

 `attribute`

How much the volume drops with distance (3D sound).

#### catkey

 `attribute`

Sound category key in the playback manager, or `None`.

#### cone_angle_inner

 `attribute`

Angle, in degrees, of the cone where the sound plays at full volume.

#### cone_angle_outer

 `attribute`

Angle, in degrees, of the cone outside of which the volume is `cone_volume_outer`.

#### cone_volume_outer

 `attribute`

Volume outside the outer cone.

#### distance_maximum

 `attribute`

Distance after which the volume stops dropping.

#### distance_reference

 `attribute`

Distance at which the sound plays at normal volume.

#### filter_gain

 `attribute`

Overall filter gain.

#### filter_gainhf

 `attribute`

High frequency gain in the filter.

#### filter_gainlf

 `attribute`

Low frequency gain in the filter.

#### is3D

 `attribute · read-only`

`True` if the sound is positional (3D).

#### mode

 `attribute`

Playback mode: 1 plays to the end, 2 loops, 3 ping-pong loop.

#### pitch

 `attribute`

Sound pitch (speed). 1.0 is normal.

#### playbackManager

 `attribute`

Playback manager (`aud.PlaybackManager`) used by the Speaker, or `None`.

#### reverb_air_absorption_gain_hf

 `attribute`

Reverb: high frequency absorption by the air.

#### reverb_decay_hf_ratio

 `attribute`

Reverb: how much faster high frequencies fade than low ones.

#### reverb_decay_limit_hf

 `attribute`

Reverb: limits the high frequency decay.

#### reverb_decay_time

 `attribute`

Reverb: time in seconds the echo takes to fade.

#### reverb_density

 `attribute`

Reverb: echo density.

#### reverb_diffusion

 `attribute`

Reverb: echo diffusion.

#### reverb_gain

 `attribute`

Reverb: overall effect volume.

#### reverb_gain_hf

 `attribute`

Reverb: high frequency volume.

#### reverb_late_reverb_delay

 `attribute`

Reverb: delay of the echo tail.

#### reverb_late_reverb_gain

 `attribute`

Reverb: volume of the echo tail.

#### reverb_reflections_delay

 `attribute`

Reverb: delay of the early reflections.

#### reverb_reflections_gain

 `attribute`

Reverb: volume of the early reflections.

#### reverb_room_rolloff_factor

 `attribute`

Reverb: how much the effect drops with distance.

#### sound

 `attribute`

Current sound (`aud.Sound`), or `None`.

#### time

 `attribute`

Current sound position, in seconds. Can be changed to seek.

#### volume

 `attribute`

Sound volume.

#### volume_maximum

 `attribute`

Maximum volume, even up close.

#### volume_minimum

 `attribute`

Minimum volume, even far away.

---

## KX_StateActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

State actuator changes the state mask of parent object.

```python
# Turn on state 2 of the object.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["State"]

act.operation = Range.logic.KX_STATE_OP_SET
act.mask = Range.logic.KX_STATE2
cont.activate(act)
```

#### operation

Type of bit operation to be applied on object state mask.

You can use one of `these constants`

**Type:** integer

#### mask

Value that defines the bits that will be modified by the operation.

The bits that are 1 in the mask will be updated in the object state.

The bits that are 0 are will be left unmodified expect for the Copy operation which copies the mask to the object state.

**Type:** integer

---

## KX_SteeringActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

> **See also:**
[`KX_NavMeshObject`](#kx_navmeshobject)

Steering Actuator for navigation.

```python
# Follow the player using a navigation mesh.
import Range

cont = Range.logic.getCurrentController()
scene = Range.logic.getCurrentScene()
act = cont.actuators["Steering"]

act.behavior = Range.logic.KX_STEERING_PATHFOLLOWING
act.target = scene.objects["Player"]
act.navmesh = scene.objects["Navmesh"]
act.velocity = 3.0
act.distance = 1.0
cont.activate(act)
```

#### behavior

The steering behavior to use.

**Type:** one of `these constants`

#### velocity

Velocity magnitude

**Type:** float

#### acceleration

Max acceleration

**Type:** float

#### turnspeed

Max turn speed

**Type:** float

#### distance

Relax distance

**Type:** float

#### target

Target object

**Type:** `KX_GameObject`

#### navmesh

Navigation mesh

**Type:** `KX_GameObject`

#### selfterminated

Terminate when target is reached

**Type:** boolean

#### enableVisualization

Enable debug visualization

**Type:** boolean

#### pathUpdatePeriod

Path update period

**Type:** int

#### path

Path point list.

**Type:** list of `mathutils.Vector`

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### facingMode

 `attribute`

Where the object turns while walking: 0 doesn't turn, 1 to 3 = +X, +Y, +Z axis, 4 to 6 = -X, -Y, -Z.

#### lockZVelocity

 `attribute`

Doesn't touch the object vertical (Z) velocity.

#### steeringVec

 `attribute · read-only`

Direction vector computed by the actuator this frame.

---

## KX_TextureRenderer

Base class: [`EXP_Value`](#exp_value)

Python API for object doing a render stored in a texture.

```python
# Update a reflection only every few frames to save time.
import Range

own = Range.logic.getCurrentController().owner
renderer = own.meshes[0].materials[0].textures[0].renderer

renderer.autoUpdate = False
own["frames"] = own.get("frames", 0) + 1

if own["frames"] % 10 == 0:
    renderer.update()
```

```python
# Use another point of view and a shorter distance.
import Range

own = Range.logic.getCurrentController().owner
renderer = own.meshes[0].materials[0].textures[0].renderer

renderer.viewpointObject = Range.logic.getCurrentScene().objects["Probe"]
renderer.clipEnd = 50.0
```

#### autoUpdate

Choose to update automatically each frame the texture renderer or not.

**Type:** boolean

#### viewpointObject

The object where the texture renderer will render the scene.

**Type:** `KX_GameObject`

#### enabled

Enable the texture renderer to render the scene.

**Type:** boolean

#### ignoreLayers

The layers to ignore when rendering.

**Type:** bitfield

#### clipStart

The projection view matrix near plane, used for culling.

**Type:** float

#### clipEnd

The projection view matrix far plane, used for culling.

**Type:** float

#### lodDistanceFactor

The factor to multiply distance to camera to adjust levels of detail.
A float < 1.0f will make the distance to camera used to compute
levels of detail decrease.

**Type:** float

#### update()

Request to update this texture renderer during the rendering stage. This function is effective only when `autoUpdate` is disabled.

---

## KX_TrackToActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Edit Object actuator in Track To mode.

> **Caution:**
Track To Actuators will be ignored if at game start, the object to track to is invalid.

This will generate a warning in the console:

```text

GameObject 'Name' no object in EditObjectActuator 'ActuatorName'
```

#### object

the object this actuator tracks.

**Type:** `KX_GameObject` or None

#### time

the time in frames with which to delay the tracking motion.

**Type:** integer

#### use3D

the tracking motion to use 3D.

**Type:** boolean

#### upAxis

The axis that points upward.

**Type:** integer from 0 to 2

* KX_TRACK_UPAXIS_POS_X
* KX_TRACK_UPAXIS_POS_Y
* KX_TRACK_UPAXIS_POS_Z

#### trackAxis

The axis that points to the target object.

**Type:** integer from 0 to 5

* KX_TRACK_TRAXIS_POS_X
* KX_TRACK_TRAXIS_POS_Y
* KX_TRACK_TRAXIS_POS_Z
* KX_TRACK_TRAXIS_NEG_X
* KX_TRACK_TRAXIS_NEG_Y
* KX_TRACK_TRAXIS_NEG_Z

---

## KX_VehicleWrapper

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`KX_GameObject`](#kx_gameobject), [`Range.constraints`](#rangeconstraints), [`KX_CharacterWrapper`](#kx_characterwrapper)

KX_VehicleWrapper

TODO - description

```python
# Create a vehicle with four wheels. The wheel objects must be set to No Collision.
import Range
from Range import constraints

scene = Range.logic.getCurrentScene()
own = Range.logic.getCurrentController().owner

vehicle = constraints.createVehicle(own.getPhysicsId())
own["vehicle_id"] = vehicle.getConstraintId()

wheels = (
    ("WheelFL", (-1.0, 1.5, 0.0), True),
    ("WheelFR", (1.0, 1.5, 0.0), True),
    ("WheelRL", (-1.0, -1.5, 0.0), False),
    ("WheelRR", (1.0, -1.5, 0.0), False),
)

for name, position, steering in wheels:
    vehicle.addWheel(scene.objects[name], position, (0, 0, -1), (-1, 0, 0), 0.4, 0.5, steering)
```

```python
# Drive it every frame.
import Range
from Range import constraints

own = Range.logic.getCurrentController().owner
vehicle = constraints.getVehicleConstraint(own["vehicle_id"])
keys = Range.logic.keyboard.inputs

force = -800.0 if keys[Range.events.WKEY].active else 0.0
steer = 0.3 if keys[Range.events.AKEY].active else 0.0

for wheel in range(vehicle.getNumWheels()):
    vehicle.applyEngineForce(force, wheel)

vehicle.setSteeringValue(steer, 0)
vehicle.setSteeringValue(steer, 1)
print(vehicle.getCurrentSpeedKmh())
```

```python
# Adjust the suspension of each wheel.
for wheel in range(vehicle.getNumWheels()):
    vehicle.setSuspensionStiffness(20.0, wheel)
    vehicle.setSuspensionDamping(2.0, wheel)
    vehicle.setSuspensionCompression(4.0, wheel)
    vehicle.setTyreFriction(2.0, wheel)
```

#### addWheel(wheel, attachPos, downDir, axleDir, suspensionRestLength, wheelRadius, hasSteering)

Add a wheel to the vehicle

- **`wheel`**: The object to use as a wheel.
  - type: `KX_GameObject` or a `KX_GameObject` name
- **`attachPos`**: The position to attach the wheel, relative to the chassis object center.
  - type: vector of 3 floats
- **`downDir`**: The direction vector pointing down to where the vehicle should collide with the floor.
  - type: vector of 3 floats
- **`axleDir`**: The axis the wheel rotates around, relative to the chassis.
  - type: vector of 3 floats
- **`suspensionRestLength`**: The length of the suspension when no forces are being applied.
  - type: float
- **`wheelRadius`**: The radius of the wheel (half the diameter).
  - type: float
- **`hasSteering`**: True if the wheel should turn with steering, typically used in front wheels.
  - type: boolean

#### applyBraking(force, wheelIndex)

Apply a braking force to the specified wheel

- **`force`**: the brake force
  - type: float
- **`wheelIndex`**: index of the wheel where the force needs to be applied
  - type: integer

#### applyEngineForce(force, wheelIndex)

Apply an engine force to the specified wheel

- **`force`**: the engine force
  - type: float
- **`wheelIndex`**: index of the wheel where the force needs to be applied
  - type: integer

#### getConstraintId()

Get the constraint ID

**Returns:** the constraint id

**Return type:** integer

#### getConstraintType()

Returns the constraint type.

**Returns:** constraint type

**Return type:** integer

#### getNumWheels()

Returns the number of wheels.

**Returns:** the number of wheels for this vehicle

**Return type:** integer

#### getWheelOrientationQuaternion(wheelIndex)

Returns the wheel orientation as a quaternion.

- **`wheelIndex`**: the wheel index
  - type: integer

**Returns:** TODO Description

**Return type:** TODO - type should be quat as per method name but from the code it looks like a matrix

#### getWheelPosition(wheelIndex)

Returns the position of the specified wheel

- **`wheelIndex`**: the wheel index
  - type: integer

**Returns:** position vector

**Return type:** list[x, y, z]

#### getWheelRotation(wheelIndex)

Returns the rotation of the specified wheel

- **`wheelIndex`**: the wheel index
  - type: integer

**Returns:** the wheel rotation

**Return type:** float

#### setRollInfluence(rollInfluece, wheelIndex)

Set the specified wheel's roll influence.
The higher the roll influence the more the vehicle will tend to roll over in corners.

- **`rollInfluece`**: the wheel roll influence
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

#### setSteeringValue(steering, wheelIndex)

Set the specified wheel's steering

- **`steering`**: the wheel steering
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

#### setSuspensionCompression(compression, wheelIndex)

Set the specified wheel's compression

- **`compression`**: the wheel compression
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

#### setSuspensionDamping(damping, wheelIndex)

Set the specified wheel's damping

- **`damping`**: the wheel damping
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

#### setSuspensionStiffness(stiffness, wheelIndex)

Set the specified wheel's stiffness

- **`stiffness`**: the wheel stiffness
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

#### setTyreFriction(friction, wheelIndex)

Set the specified wheel's tyre friction

- **`friction`**: the tyre friction
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

#### rayMask

Set ray cast mask.

**Type:** bitfield

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### getCoordinateSystem()

 `method`

Vehicle axes `(right, up, forward)` (0=X, 1=Y, 2=Z).

**Returns:** `tuple`

#### getCurrentSpeedKmh()

 `method`

Current speed in km/h.

**Returns:** `float`

#### getCurrentSpeedMps()

 `method`

Current speed in meters per second.

**Returns:** `float`

#### getForwardVector()

 `method`

Vehicle forward direction, in world space.

**Returns:** `Vector`

#### getWheelConfig(wheelIndex)

 `method`

Wheel configuration: `connectionPoint`, `downDirection`, `axleDirection`, `suspensionRestLength`, `wheelRadius`, `hasSteering` and `isDriveWheel`.

**Returns:** `dict`

#### getWheelState(wheelIndex)

 `method`

Wheel state this tick: world position and orientation, `rotation`, `isInContact`, contact point and normal, `suspensionForce` and more.

**Returns:** `dict`

#### loadPreset(path)

 `method`

Loads a vehicle preset (file) and applies it to this vehicle.

#### rebuildPreset(path, wheelObjects)

 `method`

Rebuilds the wheels from the preset, using the given objects (one per wheel). Use Empties with **No Collision** physics as wheels.

#### resetSuspension()

 `method`

Puts the suspension back at rest (useful after teleporting the car).

#### savePreset(path)

 `method`

Saves the current vehicle setup to a preset file.

#### setCoordinateSystem(right, up, forward)

 `method`

Sets which axes (0=X, 1=Y, 2=Z) are right, up and forward. All three axes must be used without repeating.

#### setSuspensionRestLength(value, wheelIndex)

*(new in Anastacio)* `method`

Changes a wheel's suspension rest length (positive value). Applied on the next physics step.

#### setWheelIsDriveWheel(wheelIndex, isDriveWheel)

 `method`

Sets whether the wheel gets engine traction.

#### setWheelRadius(value, wheelIndex)

*(new in Anastacio)* `method`

Changes a wheel's radius (positive value). Applied on the next physics step.

#### constraint_id

 `attribute · read-only`

Id of the vehicle physics constraint.

#### constraint_type

 `attribute · read-only`

Type of the vehicle physics constraint.

---

## KX_VertexProxy

Base class: [`SCA_IObject`](#sca_iobject)

A vertex holds position, UV, color and normal information.

Note:
The physics simulation is NOT currently updated - physics will not respond
to changes in the vertex position.

```python
# Raise every vertex of a mesh a little.
import Range

mesh = Range.logic.getCurrentController().owner.meshes[0]

for i in range(mesh.getVertexArrayLength(0)):
    vertex = mesh.getVertex(0, i)
    vertex.z += 0.01
```

```python
# Paint the vertices red.
import Range

mesh = Range.logic.getCurrentController().owner.meshes[0]

for i in range(mesh.getVertexArrayLength(0)):
    mesh.getVertex(0, i).color = (1.0, 0.0, 0.0, 1.0)
```

#### XYZ

The position of the vertex.

**Type:** Vector((x, y, z))

#### UV

The texture coordinates of the vertex.

**Type:** Vector((u, v))

#### uvs

The texture coordinates list of the vertex.

**Type:** list of Vector((u, v))

#### normal

The normal of the vertex.

**Type:** Vector((nx, ny, nz))

#### tangent

The tangent of the vertex (read-only), computed from the UV map used by the material's Normal Map or Tangent node (the active UV map by default). The w component holds the bitangent sign.

**Type:** Vector((tx, ty, tz, w))

#### color

The color of the vertex.

**Type:** Vector((r, g, b, a))

Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0]

#### colors

The color list of the vertex.

**Type:** list of Vector((r, g, b, a))

#### x

The x coordinate of the vertex.

**Type:** float

#### y

The y coordinate of the vertex.

**Type:** float

#### z

The z coordinate of the vertex.

**Type:** float

#### u

The u texture coordinate of the vertex.

**Type:** float

#### v

The v texture coordinate of the vertex.

**Type:** float

#### u2

The second u texture coordinate of the vertex.

**Type:** float

#### v2

The second v texture coordinate of the vertex.

**Type:** float

#### r

The red component of the vertex color. 0.0 <= r <= 1.0.

**Type:** float

#### g

The green component of the vertex color. 0.0 <= g <= 1.0.

**Type:** float

#### b

The blue component of the vertex color. 0.0 <= b <= 1.0.

**Type:** float

#### a

The alpha component of the vertex color. 0.0 <= a <= 1.0.

**Type:** float

#### getXYZ()

Gets the position of this vertex.

**Returns:** this vertexes position in local coordinates.

**Return type:** Vector((x, y, z))

#### setXYZ(pos)

Sets the position of this vertex.

**Type:** Vector((x, y, z))

- **`pos`**: the new position for this vertex in local coordinates.

#### getUV()

Gets the UV (texture) coordinates of this vertex.

**Returns:** this vertexes UV (texture) coordinates.

**Return type:** Vector((u, v))

#### setUV(uv)

Sets the UV (texture) coordinates of this vertex.

**Type:** Vector((u, v))

#### getUV2()

Gets the 2nd UV (texture) coordinates of this vertex.

**Returns:** this vertexes UV (texture) coordinates.

**Return type:** Vector((u, v))

#### setUV2(uv, unit)

Sets the 2nd UV (texture) coordinates of this vertex.

**Type:** Vector((u, v))

- **`unit`**: optional argument, FLAT==1, SECOND_UV==2, defaults to SECOND_UV
- **`unit`**: integer

#### getRGBA()

Gets the color of this vertex.

The color is represented as four bytes packed into an integer value.  The color is
packed as RGBA.

Since Python offers no way to get each byte without shifting, you must use the struct module to
access color in an machine independent way.

Because of this, it is suggested you use the r, g, b and a attributes or the color attribute instead.

```python

import struct;
col = struct.unpack('4B', struct.pack('I', v.getRGBA()))
# col = (r, g, b, a)
# black = (  0, 0, 0, 255)
# white = (255, 255, 255, 255)
```

**Returns:** packed color. 4 byte integer with one byte per color channel in RGBA format.

**Return type:** integer

#### setRGBA(col)

Sets the color of this vertex.

See getRGBA() for the format of col, and its relevant problems.  Use the r, g, b and a attributes
or the color attribute instead.

setRGBA() also accepts a four component list as argument col.  The list represents the color as [r, g, b, a]
with black = [0.0, 0.0, 0.0, 1.0] and white = [1.0, 1.0, 1.0, 1.0]

```python

v.setRGBA(0xff0000ff) # Red
v.setRGBA(0xff00ff00) # Green on little endian, transparent purple on big endian
v.setRGBA([1.0, 0.0, 0.0, 1.0]) # Red
v.setRGBA([0.0, 1.0, 0.0, 1.0]) # Green on all platforms.
```

- **`col`**: the new color of this vertex in packed RGBA format.
  - type: integer or list [r, g, b, a]

#### getNormal()

Gets the normal vector of this vertex.

**Returns:** normalized normal vector.

**Return type:** Vector((nx, ny, nz))

#### setNormal(normal)

Sets the normal vector of this vertex.

**Type:** sequence of floats [r, g, b]

- **`normal`**: the new normal of this vertex.

---

## KX_VideoActuator

Class `Range.types.KX_VideoActuator`.

```python
# Pause the video of another object.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Video"]

act.object = "Screen"
act.mode = 1
cont.activate(act)
```

```python
# Skip ten seconds ahead.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Video"]

act.mode = 5
act.seconds = 10.0
act.useRelative = True
cont.activate(act)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### mode

*(new in Anastacio)* `attribute`

Action on the Video Player: `0` Play, `1` Pause, `2` Toggle, `3` Stop, `4` Restart, `5` Seek.

#### object

*(new in Anastacio)* `attribute`

Object with the Video Player controlled by the actuator (`KX_GameObject`, name or `None`).

#### seconds

*(new in Anastacio)* `attribute`

Position in seconds used by Seek mode.

#### useRelative

*(new in Anastacio)* `attribute`

In Seek mode, if `True`, `seconds` is added to the current position instead of being absolute.

---

## KX_VisibilityActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Visibility Actuator.

```python
# Hide the object and its children.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Visibility"]

act.visibility = False
act.useRecursion = True
cont.activate(act)
```

#### visibility

whether the actuator makes its parent object visible or invisible.

**Type:** boolean

#### useOcclusion

whether the actuator makes its parent object an occluder or not.

**Type:** boolean

#### useRecursion

whether the visibility/occlusion should be propagated to all children of the object.

**Type:** boolean

---

## KX_VoiceActuator

Class `Range.types.KX_VoiceActuator`.

```python
# Change the voice effect before playing.
import Range

cont = Range.logic.getCurrentController()
voice = cont.actuators["Voice"]
voice.effect = "RADIO"
cont.activate(voice)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### amount

*(new in Anastacio)* `attribute`

Effect strength, 0 to 1.

#### effect

*(new in Anastacio)* `attribute`

Voice effect, such as `NONE`, `CHIPMUNK`, `GIANT`, `ROBOT`, `RADIO`, `ECHO` or `CAVE`.

#### maxSeconds

*(new in Anastacio)* `attribute`

Maximum recording time in seconds, 0 to 600.

#### mode

*(new in Anastacio)* `attribute`

Action: `0` record, `1` play, `2` live, `3` stop, `4` save.

#### slot

*(new in Anastacio)* `attribute`

Name of the recording used by the actuator.

#### useReverb

*(new in Anastacio)* `attribute`

Uses the area or World reverb.

#### volume

*(new in Anastacio)* `attribute`

Volume, 0 to 4.

---

## KX_VRHeadSensor

Class `Range.types.KX_VRHeadSensor`.

```python
# Confirm with a nod of the head.
import Range

sensor = Range.logic.getCurrentController().sensors["VRHead"]

sensor.mode = 4
sensor.time = 1.0

if sensor.positive:
    print("Yes")
```

```python
# Read the current rotation of the head.
import Range

sensor = Range.logic.getCurrentController().sensors["VRHead"]

print(sensor.yaw, sensor.pitch, sensor.roll)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### angle

*(new in Anastacio)* `attribute`

Angle, in radians, the head must turn for the gesture to count (0 to 1.6).

#### mode

*(new in Anastacio)* `attribute`

Detected gesture: 0 look up, 1 down, 2 tilt left, 3 right, 4 nod "yes", 5 shake "no".

#### pitch

*(new in Anastacio)* `attribute · read-only`

Current head up/down tilt.

#### roll

*(new in Anastacio)* `attribute · read-only`

Current head sideways tilt.

#### time

*(new in Anastacio)* `attribute`

Time in seconds to complete the gesture (0.05 to 10).

#### yaw

*(new in Anastacio)* `attribute · read-only`

Current head left/right turn.

---

## KX_WorldInfo

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

> **See also:**
[`KX_Scene`](#kx_scene), [`KX_LightObject`](#kx_lightobject), [`KX_Camera`](#kx_camera)

A world object.

```python

# Set the mist color to red.
import Range

sce = Range.logic.getCurrentScene()

sce.world.mistColor = [1.0, 0.0, 0.0]
```

```python

# Turn the mist on and bring it closer to the camera.
import Range

world = Range.logic.getCurrentScene().world
world.mistEnable = True
world.mistStart = 5.0
world.mistDistance = 40.0
```

```python

# Start the rain, and read the current value back.
import Range

world = Range.logic.getCurrentScene().world
world.setWeather("rain", True)
print(world.getWeather("rain"))
```

```python

# Evening light: warm horizon and a weaker ambient light.
import Range

world = Range.logic.getCurrentScene().world
world.horizonColor = [1.0, 0.5, 0.2]
world.ambientColor = [0.2, 0.15, 0.1]
```

#### KX_MIST_QUADRATIC

Type of quadratic attenuation used to fade mist.

#### KX_MIST_LINEAR

Type of linear attenuation used to fade mist.

#### KX_MIST_INV_QUADRATIC

Type of inverse quadratic attenuation used to fade mist.

#### mistEnable

Return the state of the mist.

**Type:** bool

#### mistStart

The mist start point.

**Type:** float

#### mistDistance

The mist distance fom the start point to reach 100% mist.

**Type:** float

#### mistIntensity

The mist intensity.

**Type:** float

#### mistType

The type of mist - must be KX_MIST_QUADRATIC, KX_MIST_LINEAR or KX_MIST_INV_QUADRATIC

#### mistColor

The color of the mist. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
Mist and background color sould always set to the same color.

**Type:** `mathutils.Color`

#### horizonColor

The horizon color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0].
Mist and horizon color should always be set to the same color.

**Type:** `mathutils.Vector`

#### zenithColor

The zenith color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0].

**Type:** `mathutils.Vector`

#### ambientColor

The color of the ambient light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].

**Type:** `mathutils.Color`

#### exposure

Amount of exponential color correction for light.

**Type:** float between 0.0 and 1.0 inclusive

#### range

The color range that will be mapped to 0 - 1.

**Type:** float between 0.2 and 5.0 inclusive

#### envLightEnergy

The environment light energy.

**Type:** float from 0.0 to infinite

#### envLightEnabled

Returns True if Environment Lighting is enabled. Else returns False

**Type:** bool (read only)

#### envLightColor

White:       returns 0
SkyColor:    returns 1
SkyTexture:  returns 2

**Type:** int (read only)

#### setWeather(name, value)

Changes a World weather setting at runtime (the "weather." prefix is optional).
Booleans: `rain`, `ripples`, `splash`, `puddles`, `puddle_ssr`, `ripple_puddle_only`, `splash_puddle_only` (both also turn `puddles` on), `aura`, `lightning`, `lightning_side`, `clouds`, `lens_flare`, `mist`.
Floats: `rain_intensity`, `rain_density`, `rain_speed`, `rain_wind`, `rain_darken`,
`rain_streak_width`, `ripple_intensity`, `ripple_normal`, `ripple_size`, `ripple_rate`, `splash_normal`, `splash_min_up`, `splash_size`, `splash_rate`, `splash_intensity`,
`splash_distance`, `puddle_amount`, `puddle_size`, `puddle_darkness`, `puddle_reflection`,
`puddle_distance`, `puddle_min_up`, `aura_size`, `aura_rate`, `aura_intensity`, `aura_distance`,
`lightning_rate`, `lightning_intensity`, `lightning_distance`, `lightning_width`,
`cloud_coverage`, `cloud_scale`, `cloud_speed`, `flare_scale`, `flare_intensity`, `mist_*`.

Wet Surfaces (rain): boolean `wet`; integer `wet_smooth_quality` (0 Off, 1 Low, 2 Medium, 3 High);
floats `wet_darkness` (0-1), `wet_gloss` (0-1), `wet_distance` (meters), `wet_dry_time` (seconds),
`wet_smooth_strength` (0-1), `wet_smooth_radius` (0.25-4), `wet_smooth_angle` (Keep Edges, radians)
and `wet_smooth_distance` (meters).

Clouds, Sky Layers and Volumetric Clouds (the toggles need the clouds pass, built at load when any of
the three is enabled in the World): booleans `use_sky_layers`, `use_volumetric_clouds`,
`vcloud_shadow_enable`; integers `cloud_detail` (1-8), `vcloud_quality` (0 Low, 1 Medium, 2 High);
floats `cloud_color_r/_g/_b`, `vcloud_coverage`, `vcloud_scale`, `vcloud_speed`,
`vcloud_altitude`, `vcloud_thickness`, `vcloud_density`, `vcloud_detail_scale`,
`vcloud_silver_intensity`, `vcloud_shadow_strength`, `vcloud_color_r/_g/_b`.

Fog - Volumetric: booleans `vfog`, `vfog_use_lamps`, `vfog_use_shafts`, `vfog_use_sun_shafts`,
`vfog_volumes_only`, `vfog_use_wind`, `vfog_use_time_of_day`, `vfog_use_layer`,
`vfog_use_reach_clouds`; integers `vfog_quality` (0 Low, 1 Medium, 2 High), `vfog_max_lights` (1-8);
floats `vfog_density`, `vfog_base`, `vfog_falloff`, `vfog_distance`, `vfog_noise_scale`,
`vfog_noise_amount`, `vfog_speed`, `vfog_anisotropy`, `vfog_edge`, `vfog_light_intensity`,
`vfog_sun_intensity`, `vfog_shaft_intensity`, `vfog_ambient`, `vfog_morning_boost`,
`vfog_wind_direction` (degrees), `vfog_dust` (0-1, motes in the light beams), `vfog_color_r/_g/_b`. The fog resolution is fixed at load.

```python

scene.world.setWeather("aura", True)
scene.world.setWeather("splash_size", 1.5)
```

- **`name`**: setting name
  - type: string
- **`value`**: new value
  - type: bool or float

**Raises:** unknown setting name

#### strikeLightning(bolt=True)

Strikes a lightning now (World > Rain must be on; automatic lightning can stay off).

- **`bolt`**: show a bolt; False gives only a far flash behind the clouds
  - type: bool

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### getWeather(name)

*(new in Anastacio)* `method`

current value of a World weather setting (bool or float)

#### atmosphereAltitude

*(new in Anastacio)* `attribute`

Observer altitude in the atmosphere.

#### atmosphereIntensity

*(new in Anastacio)* `attribute`

Intensity of the atmospheric sky.

#### atmosphereMieDensity

*(new in Anastacio)* `attribute`

Mie scattering density (haze and halo around the sun).

#### atmosphereMieDirection

*(new in Anastacio)* `attribute`

Mie scattering direction: how much the glow concentrates near the sun.

#### atmosphereRayleighColor

*(new in Anastacio)* `attribute`

Rayleigh scattering color (the blue of the sky), as `[r, g, b]`. Negative values become 0.

#### atmosphereRayleighDensity

*(new in Anastacio)* `attribute`

Rayleigh scattering density.

#### auroraColors

*(new in Anastacio)* `attribute`

Aurora color palette: `'GREEN'`, `'CLASSIC'` or `'SHIFTING'`.

#### backgroundColor

 `attribute`

World background color `[r, g, b]`.

#### moonBrightness

*(new in Anastacio)* `attribute`

Moon brightness.

#### moonSize

*(new in Anastacio)* `attribute`

Size of the moon in the sky.

#### skyType

*(new in Anastacio)* `attribute`

World sky type: `'FLAT'`, `'GRADIENT'`, `'PROCEDURAL'` or `'ATMOSPHERIC'`. Changing it recompiles the world shader on the next frame; object materials keep the sky type they were compiled with.

#### starStyle

*(new in Anastacio)* `attribute`

Star style: `'SIMPLE'`, `'REALISTIC'` or `'CONSTELLATIONS'`.

#### sunSize

 `attribute`

Size of the sun in the sky (0 to 1).

#### useSkyAurora

*(new in Anastacio)* `attribute`

Turns the aurora in the sky on or off.

#### useSkyMoon

*(new in Anastacio)* `attribute`

Turns the moon in the sky on or off. Changes immediately, without recompiling the shader.

#### useSkyStars

*(new in Anastacio)* `attribute`

Turns the stars in the sky on or off.

---

## SCA_2DFilterActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Create, enable and disable 2D filters.

The following properties don't have an immediate effect.
You must active the actuator to get the result.
The actuator is not persistent: it automatically stops itself after setting up the filter
but the filter remains active. To stop a filter you must activate the actuator with 'type'
set to `RAS_2DFILTER_DISABLED` or `RAS_2DFILTER_NOFILTER`.

```python
# Turn on the filter of this actuator.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Filter"]

act.mode = Range.logic.RAS_2DFILTER_SEPIA
act.passNumber = 0
cont.activate(act)
```

#### shaderText

shader source code for custom shader.

**Type:** string

#### disableMotionBlur

action on motion blur: 0=enable, 1=disable.

**Type:** integer

#### mode

Type of 2D filter, use one of `these constants`.

**Type:** integer

#### passNumber

order number of filter in the stack of 2D filters. Filters are executed in increasing order of passNb.

Only be one filter can be defined per passNb.

**Type:** integer (0-100)

#### value

argument for motion blur filter.

**Type:** float (0.0-100.0)

---

## SCA_ActuatorSensor

Base class: [`SCA_ISensor`](#sca_isensor)

Actuator sensor detect change in actuator state of the parent object.
It generates a positive pulse if the corresponding actuator is activated
and a negative pulse if the actuator is deactivated.

```python
# Wait for an action to end before going on.
import Range

sensor = Range.logic.getCurrentController().sensors["ActuatorDone"]

sensor.actuator = "Wait"
sensor.mode = 1

if sensor.positive:
    print("Finished")
```

#### actuator

the name of the actuator that the sensor is monitoring.

**Type:** string

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### mode

*(new in Anastacio)* `attribute`

`0` Active: true while the watched actuator is active. `1` Finished: pulses when the actuator finishes (e.g. Wait, Action, Video).

---

## SCA_AlwaysSensor

Base class: [`SCA_ISensor`](#sca_isensor)

This sensor is always activated.

```python
# Run a script only once, when the object starts.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Always"]

sensor.usePosPulseMode = False

if sensor.positive:
    cont.owner["life"] = 100
```

```python
# Repeat every 30 logic frames.
import Range

sensor = Range.logic.getCurrentController().sensors["Always"]

sensor.usePosPulseMode = True
sensor.skippedTicks = 30
```

---

## SCA_ANDController

Base class: [`SCA_IController`](#sca_icontroller)

An AND controller activates only when all linked sensors are activated.

There are no special python methods for this controller.

```python
# With an AND controller, the actuators run when all sensors are positive. This script shows the same rule.
import Range

cont = Range.logic.getCurrentController()

if all(sensor.positive for sensor in cont.sensors):
    print("All sensors are on")
```

---

## SCA_AnimationEventSensor

Class `Range.types.SCA_AnimationEventSensor`.

```python
# Fires on the frames marked in the animation.
import Range

cont = Range.logic.getCurrentController()

if cont.sensors["AnimationEvent"].positive:
    print("Step")
```

---

## SCA_DelaySensor

Base class: [`SCA_ISensor`](#sca_isensor)

The Delay sensor generates positive and negative triggers at precise time,
expressed in number of frames. The delay parameter defines the length of the initial OFF period. A positive trigger is generated at the end of this period.

The duration parameter defines the length of the ON period following the OFF period.
There is a negative trigger at the end of the ON period. If duration is 0, the sensor stays ON and there is no negative trigger.

The sensor runs the OFF-ON cycle once unless the repeat option is set: the OFF-ON cycle repeats indefinately (or the OFF cycle if duration is 0).

Use `SCA_ISensor.reset` at any time to restart sensor.

```python
# Fire 60 logic frames after the object starts.
import Range

sensor = Range.logic.getCurrentController().sensors["Delay"]

sensor.delay = 60
sensor.duration = 10
sensor.repeat = False
```

#### delay

length of the initial OFF period as number of frame, 0 for immediate trigger.

**Type:** integer.

#### duration

length of the ON period in number of frame after the initial OFF period.

If duration is greater than 0, a negative trigger is sent at the end of the ON pulse.

**Type:** integer

#### repeat

1 if the OFF-ON cycle should be repeated indefinately, 0 if it should run once.

**Type:** integer

#### repeatTimes

Number of times the actuator will repeat.

**Type:** integer.

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### useDelta

 `attribute`

Counts the delay in seconds (real time) instead of logic frames.

---

## SCA_IActuator

Base class: [`SCA_ILogicBrick`](#sca_ilogicbrick)

Base class for all actuator logic bricks.

```python
# All actuators are turned on and off by the controller.
import Range

cont = Range.logic.getCurrentController()

for act in cont.actuators:
    if cont.sensors[0].positive:
        cont.activate(act)
    else:
        cont.deactivate(act)
```

---

## SCA_IController

Base class: [`SCA_ILogicBrick`](#sca_ilogicbrick)

Base class for all controller logic bricks.

```python
# List what is connected to this controller.
import Range

cont = Range.logic.getCurrentController()

print([sensor.name for sensor in cont.sensors])
print([act.name for act in cont.actuators])
```

```python
# Run this controller before the others.
import Range

Range.logic.getCurrentController().useHighPriority = True
```

#### state

The controllers state bitmask. This can be used with the GameObject's state to test if the controller is active.

**Type:** int bitmask

#### sensors

A list of sensors linked to this controller.

**Type:** sequence supporting index/string lookups and iteration.

> **Note:**
The sensors are not necessarily owned by the same object.

> **Note:**
When objects are instanced in dupligroups links may be lost from objects outside the dupligroup.

#### actuators

A list of actuators linked to this controller.

**Type:** sequence supporting index/string lookups and iteration.

> **Note:**
The sensors are not necessarily owned by the same object.

> **Note:**
When objects are instanced in dupligroups links may be lost from objects outside the dupligroup.

#### useHighPriority

When set the controller executes always before all other controllers that dont have this set.

**Type:** boolen

> **Note:**
Order of execution between high priority controllers is not guaranteed.

---

## SCA_ILogicBrick

Base class: [`EXP_Value`](#exp_value)

Base class for all logic bricks.

```python
# Sensors, controllers and actuators know their object.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors[0]

print(sensor.owner.name, sensor.name, sensor.executePriority)
```

#### executePriority

This determines the order controllers are evaluated, and actuators are activated (lower priority is executed first).

**Type:** executePriority: int

#### owner

The game object this logic brick is attached to (read-only).

**Type:** `KX_GameObject` or None in exceptional cases.

#### name

The name of this logic brick (read-only).

**Type:** string

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### fireCount

*(new in Anastacio)* `attribute · read-only`

---

## SCA_InputEvent

Base class: [`EXP_PyObjectPlus`](#exp_pyobjectplus)

Events for a keyboard or mouse input.

```python
# The three moments of a key.
import Range

space = Range.logic.keyboard.inputs[Range.events.SPACEKEY]

if space.activated:
    print("Pressed")
if space.active:
    print("Held")
if space.released:
    print("Released")
```

```python
# Mouse wheel value on this frame.
import Range

wheel = Range.logic.mouse.inputs[Range.events.WHEELUPMOUSE]

if wheel.active:
    print(wheel.values[-1])
```

#### status

A list of existing status of the input from the last frame.
Can contain `Range.logic.KX_INPUT_NONE` and `Range.logic.KX_INPUT_ACTIVE`.
The list always contains one value.
The first value of the list is the last value of the list in the last frame. (read-only)

**Type:** list of integer.

#### queue

A list of existing events of the input from the last frame.
Can contain `Range.logic.KX_INPUT_JUST_ACTIVATED` and `Range.logic.KX_INPUT_JUST_RELEASED`.
The list can be empty. (read-only)

**Type:** list of integer.

#### values

A list of existing value of the input from the last frame.
For keyboard it contains 1 or 0 and for mouse the coordinate of the mouse or the movement of the wheel mouse.
The list contains always one value, the size of the list is the same than `queue` + 1 only for keyboard inputs.
The first value of the list is the last value of the list in the last frame. (read-only)

Example to get the non-normalized mouse coordinates:

```python

import Range

x = Range.logic.mouse.inputs[Range.events.MOUSEX].values[-1]
y = Range.logic.mouse.inputs[Range.events.MOUSEY].values[-1]

print("Mouse non-normalized position: x: {0}, y: {1}".format(x, y))
```

**Type:** list of integer.

#### inactive

True if the input was inactive from the last frame.

**Type:** boolean

#### active

True if the input was active from the last frame.

**Type:** boolean

#### activated

True if the input was activated from the last frame.

**Type:** boolean

#### released

True if the input was released from the last frame.

**Type:** boolean

#### type

The type of the input.
One of `these constants`

**Type:** integer

---

## SCA_IObject

Base class: [`EXP_Value`](#exp_value)

This class has no python functions

```python

# Every game object is also a SCA_IObject.
import Range

obj = Range.logic.getCurrentController().owner
print(isinstance(obj, Range.types.SCA_IObject))
```

---

## SCA_ISensor

Base class: [`SCA_ILogicBrick`](#sca_ilogicbrick)

Base class for all sensor logic bricks.

```python
# Separate the frame of the press from the frame of the release.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

if sensor.triggered and sensor.positive:
    print("Pressed")
elif sensor.triggered:
    print("Released")
```

```python
# Use the state of the sensor.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

if sensor.status == Range.logic.KX_SENSOR_JUST_ACTIVATED:
    print("Just pressed")
```

```python
# Turn the result of the sensor upside down.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

sensor.invert = True
sensor.reset()
```

#### usePosPulseMode

Flag to turn positive pulse mode on and off.

**Type:** boolean

#### useNegPulseMode

Flag to turn negative pulse mode on and off.

**Type:** boolean

#### frequency

The frequency for pulse mode sensors. (Deprecated: use SCA_ISensor.skippedTicks)

**Type:** integer

#### skippedTicks

Number of logic ticks skipped between 2 active pulses

**Type:** integer

#### level

level Option whether to detect level or edge transition when entering a state.
It makes a difference only in case of logic state transition (state actuator).
A level detector will immediately generate a pulse, negative or positive
depending on the sensor condition, as soon as the state is activated.
A edge detector will wait for a state change before generating a pulse.
note: mutually exclusive with `tap`, enabling will disable `tap`.

**Type:** boolean

#### tap

When enabled only sensors that are just activated will send a positive event,
after this they will be detected as negative by the controllers.
This will make a key thats held act as if its only tapped for an instant.
note: mutually exclusive with `level`, enabling will disable `level`.

**Type:** boolean

#### invert

Flag to set if this sensor activates on positive or negative events.

**Type:** boolean

#### triggered

True if this sensor brick is in a positive state. (read-only).

**Type:** boolean

#### positive

True if this sensor brick is in a positive state. (read-only).

**Type:** boolean

#### pos_ticks

The number of ticks since the last positive pulse (read-only).

**Type:** int

#### neg_ticks

The number of ticks since the last negative pulse (read-only).

**Type:** int

#### status

The status of the sensor (read-only): can be one of `these constants`.

**Type:** int

> **Note:**
This convenient attribute combines the values of triggered and positive attributes.

#### reset()

Reset sensor internal state, effect depends on the type of sensor and settings.

The sensor is put in its initial state as if it was just activated.

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### useDeltaTime

 `attribute`

Uses real time (delta time) for the sensor intervals instead of counting frames.

---

## SCA_JoystickSensor

Base class: [`SCA_ISensor`](#sca_isensor)

This sensor detects player joystick events.

```python
# Read the axes of the sensor.
import Range

sensor = Range.logic.getCurrentController().sensors["Joystick"]

if sensor.connected:
    print(sensor.axisValues)
```

```python
# See which buttons are pressed.
import Range

sensor = Range.logic.getCurrentController().sensors["Joystick"]

print(sensor.getButtonActiveList())

if sensor.getButtonStatus(0):
    print("First button")
```

#### axisValues

The state of the joysticks axis as a list of values `numAxis` long. (read-only).

**Type:** list of ints.

Each specifying the value of an axis between -32767 and 32767 depending on how far the axis is pushed, 0 for nothing.
The first 2 values are used by most joysticks and gamepads for directional control. 3rd and 4th values are only on some joysticks and can be used for arbitary controls.

* left:[-32767, 0, ...]
* right:[32767, 0, ...]
* up:[0, -32767, ...]
* down:[0, 32767, ...]

#### axisSingle

like `axisValues` but returns a single axis value that is set by the sensor. (read-only).

**Type:** integer

> **Note:**
Only use this for "Single Axis" type sensors otherwise it will raise an error.

#### hatValues (Deprecated. Use :data:button instead)

The state of the joysticks hats as a list of values `numHats` long. (read-only).

**Type:** list of ints

Each specifying the direction of the hat from 1 to 12, 0 when inactive.

Hat directions are as follows...

* 0:None
* 1:Up
* 2:Right
* 4:Down
* 8:Left
* 3:Up - Right
* 6:Down - Right
* 12:Down - Left
* 9:Up - Left

#### hatSingle (Deprecated. Use :data:button instead)

Like `hatValues` but returns a single hat direction value that is set by the sensor. (read-only).

**Type:** integer

#### numAxis

The number of axes for the joystick at this index. (read-only).

**Type:** integer

#### numButtons

The number of buttons for the joystick at this index. (read-only).

**Type:** integer

#### numHats (Deprecated. Use :data:numButtons instead)

The number of hats for the joystick at this index. (read-only).

**Type:** integer

#### connected

True if a joystick is connected at this joysticks index. (read-only).

**Type:** boolean

#### index

The joystick index to use (from 0 to 7). The first joystick is always 0.

**Type:** integer

#### threshold

Axis threshold. Joystick axis motion below this threshold wont trigger an event. Use values between (0 and 32767), lower values are more sensitive.

**Type:** integer

#### button

The button index the sensor reacts to (first button = 0). When the "All Events" toggle is set, this option has no effect.

**Type:** integer

#### axis

The axis this sensor reacts to, as a list of two values [axisIndex, axisDirection]

* axisIndex: the axis index to use when detecting axis movement, 1=primary directional control, 2=secondary directional control.
* axisDirection: 0=right, 1=up, 2=left, 3=down.

**Type:** [integer, integer]

#### hat (Deprecated. Use :data:button instead)

The hat the sensor reacts to, as a list of two values: [hatIndex, hatDirection]

* hatIndex: the hat index to use when detecting hat movement, 1=primary hat, 2=secondary hat (4 max).
* hatDirection: 1-12.

**Type:** [integer, integer]

#### getButtonActiveList()

**Returns:** A list containing the indicies of the currently pressed buttons.

**Return type:** list

#### getButtonStatus(buttonIndex)

- **`buttonIndex`**: the button index, 0=first button
  - type: integer

**Returns:** The current pressed state of the specified button.

**Return type:** boolean

---

## SCA_KeyboardSensor

Base class: [`SCA_ISensor`](#sca_isensor)

A keyboard sensor detects player key presses.

See module `Range.events` for keycode values.

```python
# Watch all keys and show the ones held down.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

sensor.useAllKeys = True

for code, event in sensor.inputs.items():
    if event.active:
        print(Range.events.EventToString(code))
```

```python
# Change the key by script.
import Range

sensor = Range.logic.getCurrentController().sensors["Keyboard"]

sensor.key = Range.events.EKEY
```

#### key

The key code this sensor is looking for.

**Type:** keycode from `Range.events` module

#### hold1

The key code for the first modifier this sensor is looking for.

**Type:** keycode from `Range.events` module

#### hold2

The key code for the second modifier this sensor is looking for.

**Type:** keycode from `Range.events` module

#### toggleProperty

The name of the property that indicates whether or not to log keystrokes as a string.

**Type:** string

#### targetProperty

The name of the property that receives keystrokes in case in case a string is logged.

**Type:** string

#### useAllKeys

Flag to determine whether or not to accept all keys.

**Type:** boolean

#### inputs

A list of pressed input keys that have either been pressed, or just released, or are active this frame. (read-only).

**Type:** dictionary {`keycode`:`SCA_InputEvent`, ...}

#### ~~events~~

a list of pressed keys that have either been pressed, or just released, or are active this frame. (read-only).

> **Deprecated use :data:`inputs`:**

**Type:** list [[`keycode`, `status`], ...]

#### getKeyStatus(keycode)

Get the status of a key.

- **`keycode`**: The code that represents the key you want to get the state of, use one of `these constants`
  - type: integer

**Returns:** The state of the given key, can be one of `these constants`

**Return type:** int

---

## SCA_MouseSensor

Base class: [`SCA_ISensor`](#sca_isensor)

Mouse Sensor logic brick.

```python
# Read the position of the mouse and the left button.
import Range

sensor = Range.logic.getCurrentController().sensors["Mouse"]

print(sensor.position)

if sensor.getButtonStatus(Range.logic.KX_MOUSE_BUT_LEFT) == Range.logic.KX_INPUT_ACTIVE:
    print("Left button held")
```

#### position

current [x, y] coordinates of the mouse, in frame coordinates (pixels).

**Type:** [integer, interger]

#### mode

sensor mode.

**Type:** integer * KX_MOUSESENSORMODE_LEFTBUTTON(1) * KX_MOUSESENSORMODE_MIDDLEBUTTON(2) * KX_MOUSESENSORMODE_RIGHTBUTTON(3) * KX_MOUSESENSORMODE_WHEELUP(4) * KX_MOUSESENSORMODE_WHEELDOWN(5) * KX_MOUSESENSORMODE_MOVEMENT(6)

#### getButtonStatus(button)

Get the mouse button status.

- **`button`**: The code that represents the key you want to get the state of, use one of `these constants`
  - type: int

**Returns:** The state of the given key, can be one of `these constants`

**Return type:** int

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### holdTime

*(new in Anastacio)* `attribute`

Time in seconds holding the button for the sensor to fire (0 to 30).

---

## SCA_NANDController

Base class: [`SCA_IController`](#sca_icontroller)

An NAND controller activates when all linked sensors are not active.

There are no special python methods for this controller.

```python
# NAND turns the actuators on unless all sensors are positive.
import Range

cont = Range.logic.getCurrentController()

print(not all(sensor.positive for sensor in cont.sensors))
```

---

## SCA_NORController

Base class: [`SCA_IController`](#sca_icontroller)

An NOR controller activates only when all linked sensors are de-activated.

There are no special python methods for this controller.

```python
# NOR turns the actuators on only when no sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(not any(sensor.positive for sensor in cont.sensors))
```

---

## SCA_ORController

Base class: [`SCA_IController`](#sca_icontroller)

An OR controller activates when any connected sensor activates.

There are no special python methods for this controller.

```python
# OR turns the actuators on when at least one sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(any(sensor.positive for sensor in cont.sensors))
```

---

## SCA_PropertyActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Property Actuator

```python
# Change the property that this actuator writes.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Property"]

cont.owner["score"] = 0
act.propName = "score"
act.value = "score + 10"
cont.activate(act)
```

#### propName

the property on which to operate.

**Type:** string

#### value

the value with which the actuator operates.

**Type:** string

#### mode

TODO - add constants to game logic dict!.

**Type:** integer

---

## SCA_PropertySensor

Base class: [`SCA_ISensor`](#sca_isensor)

Activates when the game object property matches.

```python
# Fire when the life property reaches zero.
import Range

sensor = Range.logic.getCurrentController().sensors["Property"]

sensor.mode = Range.logic.KX_PROPSENSOR_EQUAL
sensor.propName = "life"
sensor.value = "0"
```

```python
# Fire when the value is inside an interval.
import Range

sensor = Range.logic.getCurrentController().sensors["Property"]

sensor.mode = Range.logic.KX_PROPSENSOR_INTERVAL
sensor.propName = "life"
sensor.min = "1"
sensor.max = "20"
```

#### mode

Type of check on the property. Can be one of `these constants`

**Type:** integer.

#### propName

the property the sensor operates.

**Type:** string

#### value

the value with which the sensor compares to the value of the property.

**Type:** string

#### min

the minimum value of the range used to evaluate the property when in interval mode.

**Type:** string

#### max

the maximum value of the range used to evaluate the property when in interval mode.

**Type:** string

---

## SCA_PythonController

Base class: [`SCA_IController`](#sca_icontroller)

> **See also:**
[`KX_PythonComponent`](#kx_pythoncomponent), [`SCA_ISensor`](#sca_isensor), [`SCA_IActuator`](#sca_iactuator), [`Range.logic`](#rangelogic)

A Python controller uses a Python script to activate it's actuators,
based on it's sensors.

```python
# The usual start of a script.
import Range

cont = Range.logic.getCurrentController()
own = cont.owner

if cont.sensors["Keyboard"].positive:
    cont.activate("Motion")
else:
    cont.deactivate("Motion")
```

```python
# Module mode: the engine calls one function and passes the controller.
def main(cont):
    print(cont.owner.name, cont.script)
```

#### owner

The object the controller is attached to.

**Type:** `KX_GameObject`

#### script

The value of this variable depends on the execution methid.

* When 'Script' execution mode is set this value contains the entire python script as a single string (not the script name as you might expect) which can be modified to run different scripts.
* When 'Module' execution mode is set this value will contain a single line string - module name and function "module.func" or "package.modile.func" where the module names are python textblocks or external scripts.

**Type:** string

> **Note:**
Once this is set the script name given for warnings will remain unchanged.

#### mode

the execution mode for this controller (read-only).

* Script: 0, Execite the `script` as a python code.
* Module: 1, Execite the `script` as a module and function.

**Type:** integer

#### activate(actuator)

Activates an actuator attached to this controller.

- **`actuator`**: The actuator to operate on.
  - type: actuator or the actuator name as a string

#### deactivate(actuator)

Deactivates an actuator attached to this controller.

- **`actuator`**: The actuator to operate on.
  - type: actuator or the actuator name as a string

---

## SCA_RandomActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Random Actuator

```python
# Choose a number from 1 to 6 and save it in a property.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Random"]

cont.owner["dice"] = 0
act.propName = "dice"
act.setIntUniform(1, 6)
cont.activate(act)
```

```python
# Use a float value around a mean.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Random"]

cont.owner["damage"] = 0.0
act.propName = "damage"
act.setFloatNormal(10.0, 2.0)
cont.activate(act)
```

#### seed

Seed of the random number generator.

**Type:** integer.

Equal seeds produce equal series. If the seed is 0, the generator will produce the same value on every call.

#### para1

the first parameter of the active distribution.

**Type:** float, read-only.

Refer to the documentation of the generator types for the meaning of this value.

#### para2

the second parameter of the active distribution.

**Type:** float, read-only

Refer to the documentation of the generator types for the meaning of this value.

#### distribution

Distribution type. (read-only). Can be one of `these constants`

**Type:** integer

#### propName

the name of the property to set with the random value.

**Type:** string

If the generator and property types do not match, the assignment is ignored.

#### setBoolConst(value)

Sets this generator to produce a constant boolean value.

- **`value`**: The value to return.
  - type: boolean

#### setBoolUniform()

Sets this generator to produce a uniform boolean distribution.

The generator will generate True or False with 50% chance.

#### setBoolBernouilli(value)

Sets this generator to produce a Bernouilli distribution.

- **`value`**: Specifies the proportion of False values to produce. * 0.0: Always generate True * 1.0: Always generate False
  - type: float

#### setIntConst(value)

Sets this generator to always produce the given value.

- **`value`**: the value this generator produces.
  - type: integer

#### setIntUniform(lower_bound, upper_bound)

Sets this generator to produce a random value between the given lower and
upper bounds (inclusive).

  - type: integer
  - type: integer

#### setIntPoisson(value)

Generate a Poisson-distributed number.

This performs a series of Bernouilli tests with parameter value.
It returns the number of tries needed to achieve succes.

  - type: float

#### setFloatConst(value)

Always generate the given value.

  - type: float

#### setFloatUniform(lower_bound, upper_bound)

Generates a random float between lower_bound and upper_bound with a
uniform distribution.

  - type: float
  - type: float

#### setFloatNormal(mean, standard_deviation)

Generates a random float from the given normal distribution.

- **`mean`**: The mean (average) value of the generated numbers
  - type: float
- **`standard_deviation`**: The standard deviation of the generated numbers.
  - type: float

#### setFloatNegativeExponential(half_life)

Generate negative-exponentially distributed numbers.

The half-life 'time' is characterized by half_life.

  - type: float

---

## SCA_RandomSensor

Base class: [`SCA_ISensor`](#sca_isensor)

This sensor activates randomly.

```python
# Use a fixed seed to repeat the same sequence.
import Range

sensor = Range.logic.getCurrentController().sensors["Random"]

sensor.seed = 1234
print(sensor.lastDraw)
```

#### lastDraw

The seed of the random number generator.

**Type:** integer

#### seed

The seed of the random number generator.

**Type:** integer

---

## SCA_VibrationActuator

Base class: [`SCA_IActuator`](#sca_iactuator)

Vibration Actuator.

```python
# Vibrate the first controller when hit.
import Range

act = Range.logic.getCurrentController().actuators["Vibration"]

if act.hasVibration and not act.isVibrating:
    act.joyindex = 0
    act.strengthLeft = 1.0
    act.strengthRight = 0.5
    act.duration = 300
    act.startVibration()
```

#### joyindex

Joystick index.

**Type:** integer (0 to 7)

#### strengthLeft

Strength of the Low frequency joystick's motor (placed at left position usually).

**Type:** float (0.0 to 1.0)

#### strengthRight

Strength of the High frequency joystick's motor (placed at right position usually).

**Type:** float (0.0 to 1.0)

#### duration

Duration of the vibration in milliseconds.

**Type:** integer (0 to infinite)

#### isVibrating

Check status of joystick vibration

**Type:** bool (true vibrating and false stopped)

#### hasVibration

Check if the joystick supports vibration

**Type:** bool (true supported and false not supported)

#### startVibration()

Starts the vibration.

**Returns:** None

#### stopVibration()

Stops the vibration.

**Returns:** None

---

## SCA_WaitActuator

Class `Range.types.SCA_WaitActuator`.

```python
# Wait three seconds.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Wait"]

act.duration = 3.0
act.useRestart = False
cont.activate(act)
```

```python
# Show the remaining time.
import Range

act = Range.logic.getCurrentController().actuators["Wait"]

if act.waiting:
    print(act.duration - act.elapsed)
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### duration

*(new in Anastacio)* `attribute`

Wait time in seconds (0 to 100000). A positive pulse starts the count; when it elapses the actuator finishes and an **Actuator** sensor in Finished mode fires.

#### elapsed

*(new in Anastacio)* `attribute · read-only`

Seconds elapsed since the current wait started.

#### useRestart

*(new in Anastacio)* `attribute`

If `True`, a new positive pulse while waiting restarts the count from zero.

#### waiting

*(new in Anastacio)* `attribute · read-only`

`True` while the actuator is counting.

---

## SCA_XNORController

Base class: [`SCA_IController`](#sca_icontroller)

An XNOR controller activates when all linked sensors are the same (activated or inative).

There are no special python methods for this controller.

```python
# XNOR turns the actuators on unless exactly one sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(sum(sensor.positive for sensor in cont.sensors) != 1)
```

---

## SCA_XORController

Base class: [`SCA_IController`](#sca_icontroller)

An XOR controller activates when there is the input is mixed, but not when all are on or off.

There are no special python methods for this controller.

```python
# XOR turns the actuators on when exactly one sensor is positive.
import Range

cont = Range.logic.getCurrentController()

print(sum(sensor.positive for sensor in cont.sensors) == 1)
```

---

## Texture

Class `Range.types.Texture`.

```python
# Put an image on a material. Keep the object in a property or it will be released.
import Range
from Range import texture

own = Range.logic.getCurrentController().owner

tex = texture.Texture(own, 0)
tex.source = texture.ImageFFmpeg(Range.logic.expandPath("//poster.png"))
tex.mipmap = True
tex.refresh(False)
own["poster"] = tex
```

```python
# Give the original texture back.
import Range

own = Range.logic.getCurrentController().owner

own["poster"].close()
del own["poster"]
```

### Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

#### close()

 `method`

Close dynamic decklink and restore original

#### refresh()

 `method`

Refresh decklink from source

#### bindId

 `attribute · read-only`

OpenGL id of the texture.

#### mipmap

 `attribute`

Uses mipmaps on the texture (`True`/`False`).

#### source

 `attribute`

Image source (video, camera, image...) drawn on the texture.

---

## TrackLine

Closed polyline for racing AI, computed in C++. Tells how far along the track a car is,
gives the point and the side of the track at a distance, and stores per-point profiles
(curvature, safe speed). Build it once per track and share it between the cars.

The line is closed: the last point connects to the first. `s` is the distance in meters
from the first point and wraps around, so `s` greater than `length` or negative works.

```python

import Range
from mathutils import Vector

points = curve.getCurvePoints()        # or the center of the road mesh
line = Range.types.TrackLine(points)

d2, s, seg = line.locate(car.worldPosition)               # global search
d2, s, seg = line.locate(car.worldPosition, seg, 15, 40, 20.0)  # near the last segment
target = line.point(s + 12.0)          # 12 m ahead
right = line.side(s)                   # unit vector to the right, or None
```

- **`points`**: at least 3 points (`mathutils.Vector` or 3-item sequences).
  - type: sequence

#### length

Total length of the closed line, in meters (read-only).

**Type:** float

#### locate(pos, seg=-1, back=0, ahead=0, lost=0.0)

Closest segment of the line to `pos`.

With `seg` >= 0 only the segments from `seg - back` to `seg + ahead` are tested,
which avoids jumping to a neighbouring part of the track. When that result is farther
than `lost` meters (respawn, shortcut), or with `seg` = -1, the whole line is searched.

- **`pos`**: position in world coordinates.
  - type: `mathutils.Vector`
- **`seg`**: segment from the previous call, -1 if unknown.
  - type: integer
- **`back`**: segments to test behind `seg`.
  - type: integer
- **`ahead`**: segments to test ahead of `seg`.
  - type: integer
- **`lost`**: distance in meters that triggers the global search.
  - type: float

**Returns:** (squared distance to the line, `s` in meters, segment index).

**Return type:** tuple (float, float, integer)

#### point(s)

Point of the line `s` meters from the start.

**Return type:** `mathutils.Vector`

#### side(s)

Horizontal unit vector pointing to the right of the line at `s`, or None where the
line is vertical or degenerate.

**Return type:** `mathutils.Vector` or None

#### setProfile(name, values)

Stores one value per point under `name` (curvature, safe speed, any number).

- **`name`**: profile name.
  - type: string
- **`values`**: one number per point of the line.
  - type: sequence of float

#### profile(name, s)

Value of the profile `name` interpolated at `s` meters.

**Return type:** float
