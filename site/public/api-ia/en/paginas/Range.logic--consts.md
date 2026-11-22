# Range.logic - constants

Part of [Range.logic](Range.logic.md).

## KX_TRUE

True value used by some modules.

## KX_FALSE

False value used by some modules.

## KX_SENSOR_INACTIVE

Sensor state: off.

## KX_SENSOR_JUST_ACTIVATED

Sensor state: just turned on this frame.

## KX_SENSOR_ACTIVE

Sensor state: still on.

## KX_SENSOR_JUST_DEACTIVATED

Sensor state: just turned off this frame.

## KX_ARMSENSOR_STATE_CHANGED

Detect that the constraint is changing state (active/inactive)

**Value:** `0`

## KX_ARMSENSOR_LIN_ERROR_BELOW

Detect that the constraint linear error is above a threshold

**Value:** `1`

## KX_ARMSENSOR_LIN_ERROR_ABOVE

Detect that the constraint linear error is below a threshold

**Value:** `2`

## KX_ARMSENSOR_ROT_ERROR_BELOW

Detect that the constraint rotation error is above a threshold

**Value:** `3`

## KX_ARMSENSOR_ROT_ERROR_ABOVE

Detect that the constraint rotation error is below a threshold

**Value:** `4`

## KX_PROPSENSOR_EQUAL

Activate when the property is equal to the sensor value.

**Value:** `1`

## KX_PROPSENSOR_NOTEQUAL

Activate when the property is not equal to the sensor value.

**Value:** `2`

## KX_PROPSENSOR_INTERVAL

Activate when the property is between the specified limits.

**Value:** `3`

## KX_PROPSENSOR_CHANGED

Activate when the property changes

**Value:** `4`

## KX_PROPSENSOR_EXPRESSION

Activate when the expression matches

**Value:** `5`

## KX_PROPSENSOR_LESSTHAN

Activate when the property is less than the sensor value

**Value:** `6`

## KX_PROPSENSOR_GREATERTHAN

Activate when the property is greater than the sensor value

**Value:** `7`

## KX_RADAR_AXIS_POS_X

Radar sensor: cone pointing along the object +X axis.

## KX_RADAR_AXIS_POS_Y

Radar sensor: cone pointing along the object +Y axis.

## KX_RADAR_AXIS_POS_Z

Radar sensor: cone pointing along the object +Z axis.

## KX_RADAR_AXIS_NEG_X

Radar sensor: cone pointing along the object -X axis.

## KX_RADAR_AXIS_NEG_Y

Radar sensor: cone pointing along the object -Y axis.

## KX_RADAR_AXIS_NEG_Z

Radar sensor: cone pointing along the object -Z axis.

## KX_RAY_AXIS_POS_X

Ray sensor: ray cast along the object +X axis.

## KX_RAY_AXIS_POS_Y

Ray sensor: ray cast along the object +Y axis.

## KX_RAY_AXIS_POS_Z

Ray sensor: ray cast along the object +Z axis.

## KX_RAY_AXIS_NEG_X

Ray sensor: ray cast along the object -X axis.

## KX_RAY_AXIS_NEG_Y

Ray sensor: ray cast along the object -Y axis.

## KX_RAY_AXIS_NEG_Z

Ray sensor: ray cast along the object -Z axis.

## KX_ACTIONACT_PLAY

Action actuator: plays the animation once.

## KX_ACTIONACT_PINGPONG

Action actuator: plays forward and, on the next activation, backward.

## KX_ACTIONACT_FLIPPER

Action actuator: plays while active and goes back to the start when turned off.

## KX_ACTIONACT_LOOPSTOP

Action actuator: loops while the sensor is active.

## KX_ACTIONACT_LOOPEND

Action actuator: loops and, when turned off, finishes the current loop.

## KX_ACTIONACT_PROPERTY

Action actuator: the animation frame comes from a property.

## KX_ACT_ARMATURE_RUN

Just make sure the armature will be updated on the next graphic frame.
This is the only persistent mode of the actuator:
it executes automatically once per frame until stopped by a controller

**Value:** `0`

## KX_ACT_ARMATURE_ENABLE

Enable the constraint.

**Value:** `1`

## KX_ACT_ARMATURE_DISABLE

Disable the constraint (runtime constraint values are not updated).

**Value:** `2`

## KX_ACT_ARMATURE_SETTARGET

Change target and subtarget of constraint.

**Value:** `3`

## KX_ACT_ARMATURE_SETWEIGHT

Change weight of constraint (IK only).

**Value:** `4`

## KX_ACT_ARMATURE_SETINFLUENCE

Change influence of constraint.

**Value:** `5`

## KX_CONSTRAINTACT_NORMAL

Activate alignment to surface

## KX_CONSTRAINTACT_DISTANCE

Activate distance control

## KX_CONSTRAINTACT_LOCAL

Direction of the ray is along the local axis

* Applicable to Force field constraint:

## KX_CONSTRAINTACT_DOROTFH

Force field act on rotation as well

* Applicable to both:

## KX_CONSTRAINTACT_MATERIAL

Detect material rather than property

## KX_CONSTRAINTACT_PERMANENT

No deactivation if ray does not hit target

See `Range.types.KX_ConstraintActuator.limit`

## KX_CONSTRAINTACT_LOCX

Limit X coord.

## KX_CONSTRAINTACT_LOCY

Limit Y coord

## KX_CONSTRAINTACT_LOCZ

Limit Z coord

## KX_CONSTRAINTACT_ROTX

Limit X rotation

## KX_CONSTRAINTACT_ROTY

Limit Y rotation

## KX_CONSTRAINTACT_ROTZ

Limit Z rotation

## KX_CONSTRAINTACT_DIRNX

Set distance along negative X axis

## KX_CONSTRAINTACT_DIRNY

Set distance along negative Y axis

## KX_CONSTRAINTACT_DIRNZ

Set distance along negative Z axis

## KX_CONSTRAINTACT_DIRPX

Set distance along positive X axis

## KX_CONSTRAINTACT_DIRPY

Set distance along positive Y axis

## KX_CONSTRAINTACT_DIRPZ

Set distance along positive Z axis

## KX_CONSTRAINTACT_ORIX

Set orientation of X axis

## KX_CONSTRAINTACT_ORIY

Set orientation of Y axis

## KX_CONSTRAINTACT_ORIZ

Set orientation of Z axis

## KX_CONSTRAINTACT_FHNX

Set force field along negative X axis

## KX_CONSTRAINTACT_FHNY

Set force field along negative Y axis

## KX_CONSTRAINTACT_FHNZ

Set force field along negative Z axis

## KX_CONSTRAINTACT_FHPX

Set force field along positive X axis

## KX_CONSTRAINTACT_FHPY

Set force field along positive Y axis

## KX_CONSTRAINTACT_FHPZ

Set force field along positive Z axis

## KX_DYN_RESTORE_DYNAMICS

Dynamic actuator: turns physics back on.

## KX_DYN_DISABLE_DYNAMICS

Dynamic actuator: turns off the object physics.

## KX_DYN_ENABLE_RIGID_BODY

Dynamic actuator: turns on rigid body mode (physics rotation).

## KX_DYN_DISABLE_RIGID_BODY

Dynamic actuator: turns off rigid body mode.

## KX_DYN_SET_MASS

Dynamic actuator: changes the object mass.

## KX_GAME_LOAD

Game actuator: loads another game file.

## KX_GAME_START

Game actuator: starts another game file.

## KX_GAME_RESTART

Game actuator: restarts the game.

## KX_GAME_QUIT

Game actuator: quits the game.

## KX_GAME_SAVECFG

Game actuator: saves the global properties to a file.

## KX_GAME_LOADCFG

Game actuator: loads the saved global properties.

## KX_ACT_MOUSE_OBJECT_AXIS_X

Mouse (look) actuator: rotates around the object X axis.

## KX_ACT_MOUSE_OBJECT_AXIS_Y

Mouse (look) actuator: rotates around the object Y axis.

## KX_ACT_MOUSE_OBJECT_AXIS_Z

Mouse (look) actuator: rotates around the object Z axis.

## KX_PARENT_REMOVE

Parent actuator: removes the object from its parent.

## KX_PARENT_SET

Parent actuator: attaches the object to a parent.

## KX_RANDOMACT_BOOL_CONST

Random actuator: fixed true/false.

## KX_RANDOMACT_BOOL_UNIFORM

Random actuator: true or false, 50% chance each.

## KX_RANDOMACT_BOOL_BERNOUILLI

Random actuator: true with the chance you set.

## KX_RANDOMACT_INT_CONST

Random actuator: fixed integer.

## KX_RANDOMACT_INT_UNIFORM

Random actuator: integer picked between a minimum and a maximum.

## KX_RANDOMACT_INT_POISSON

Random actuator: integer with a Poisson distribution (given mean).

## KX_RANDOMACT_FLOAT_CONST

Random actuator: fixed float.

## KX_RANDOMACT_FLOAT_UNIFORM

Random actuator: float picked between a minimum and a maximum.

## KX_RANDOMACT_FLOAT_NORMAL

Random actuator: float with a normal distribution (mean and deviation).

## KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL

Random actuator: float with a negative exponential distribution.

## KX_SCENE_RESTART

Scene actuator: restarts the scene.

## KX_SCENE_SET_SCENE

Scene actuator: switches to another scene.

## KX_SCENE_SET_CAMERA

Scene actuator: changes the active camera.

## KX_SCENE_ADD_FRONT_SCENE

Scene actuator: adds a scene on top (overlay, like a HUD).

## KX_SCENE_ADD_BACK_SCENE

Scene actuator: adds a scene behind (background).

## KX_SCENE_REMOVE_SCENE

Scene actuator: removes a scene.

## KX_SCENE_SUSPEND

Scene actuator: pauses a scene.

## KX_SCENE_RESUME

Scene actuator: resumes a paused scene.

## KX_SOUNDACT_PLAYSTOP

Sound actuator: plays while the sensor is active and stops when it turns off.

**Value:** `1`

## KX_SOUNDACT_PLAYEND

Sound actuator: plays the whole sound once.

**Value:** `2`

## KX_SOUNDACT_LOOPSTOP

Sound actuator: loops while the sensor is active.

**Value:** `3`

## KX_SOUNDACT_LOOPEND

Sound actuator: loops and, when turned off, finishes the current loop.

**Value:** `4`

## KX_SOUNDACT_LOOPBIDIRECTIONAL

Sound actuator: plays forward and backward in a loop.

**Value:** `5`

## KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP

Sound actuator: ping-pong loop while the sensor is active.

**Value:** `6`

## KX_STEERING_SEEK

Steering actuator: goes to the target.

**Value:** `1`

## KX_STEERING_FLEE

Steering actuator: runs away from the target.

**Value:** `2`

## KX_STEERING_PATHFOLLOWING

Steering actuator: follows the Navmesh path to the target.

**Value:** `3`

## KX_TRACK_UPAXIS_POS_X

Track To actuator: the object +X axis points up.

## KX_TRACK_UPAXIS_POS_Y

Track To actuator: the object +Y axis points up.

## KX_TRACK_UPAXIS_POS_Z

Track To actuator: the object +Z axis points up.

## KX_TRACK_TRAXIS_POS_X

Track To actuator: the object +X axis points at the target.

## KX_TRACK_TRAXIS_POS_Y

Track To actuator: the object +Y axis points at the target.

## KX_TRACK_TRAXIS_POS_Z

Track To actuator: the object +Z axis points at the target.

## KX_TRACK_TRAXIS_NEG_X

Track To actuator: the object -X axis points at the target.

## KX_TRACK_TRAXIS_NEG_Y

Track To actuator: the object -Y axis points at the target.

## KX_TRACK_TRAXIS_NEG_Z

Track To actuator: the object -Z axis points at the target.

## RAS_2DFILTER_BLUR

2D Filter actuator: blur.

**Value:** `2`

## RAS_2DFILTER_CUSTOMFILTER

2D Filter actuator: your own GLSL shader.

Customer filter, the code code is set via shaderText property.

**Value:** `12`

## RAS_2DFILTER_DILATION

2D Filter actuator: dilation (brightens edges).

**Value:** `4`

## RAS_2DFILTER_DISABLED

2D Filter actuator: disables the filter.

Disable the filter that is currently active

**Value:** `-1`

## RAS_2DFILTER_ENABLED

2D Filter actuator: enables the filter.

Enable the filter that was previously disabled

**Value:** `-2`

## RAS_2DFILTER_EROSION

2D Filter actuator: erosion (darkens edges).

**Value:** `5`

## RAS_2DFILTER_GRAYSCALE

2D Filter actuator: grayscale.

**Value:** `9`

## RAS_2DFILTER_INVERT

2D Filter actuator: inverted colors.

**Value:** `11`

## RAS_2DFILTER_LAPLACIAN

2D Filter actuator: edge detection (Laplace).

**Value:** `6`

## RAS_2DFILTER_MOTIONBLUR

Create and enable preset filters

**Value:** `1`

## RAS_2DFILTER_NOFILTER

2D Filter actuator: removes the filter.

Disable and destroy the filter that is currently active

**Value:** `0`

## RAS_2DFILTER_PREWITT

2D Filter actuator: edge detection (Prewitt).

**Value:** `8`

## RAS_2DFILTER_SEPIA

2D Filter actuator: sepia.

**Value:** `10`

## RAS_2DFILTER_SHARPEN

2D Filter actuator: sharpen.

**Value:** `3`

## RAS_2DFILTER_SOBEL

2D Filter actuator: edge detection (Sobel).

**Value:** `7`

## RAS_2DFILTER_SOBEL

2D Filter actuator: edge detection (Sobel).

**Value:** `14`

## ROT_MODE_QUAT

Use quaternion in rotation attribute to update bone rotation.

**Value:** `0`

## ROT_MODE_XYZ

Use euler_rotation and apply angles on bone's Z, Y, X axis successively.

**Value:** `1`

## ROT_MODE_XZY

Use euler_rotation and apply angles on bone's Y, Z, X axis successively.

**Value:** `2`

## ROT_MODE_YXZ

Use euler_rotation and apply angles on bone's Z, X, Y axis successively.

**Value:** `3`

## ROT_MODE_YZX

Use euler_rotation and apply angles on bone's X, Z, Y axis successively.

**Value:** `4`

## ROT_MODE_ZXY

Use euler_rotation and apply angles on bone's Y, X, Z axis successively.

**Value:** `5`

## ROT_MODE_ZYX

Use euler_rotation and apply angles on bone's X, Y, Z axis successively.

**Value:** `6`

## CONSTRAINT_TYPE_TRACKTO

Bone constraint type: Track To (points at a target).

## CONSTRAINT_TYPE_KINEMATIC

Bone constraint type: IK (inverse kinematics).

## CONSTRAINT_TYPE_ROTLIKE

Bone constraint type: Copy Rotation.

## CONSTRAINT_TYPE_LOCLIKE

Bone constraint type: Copy Location.

## CONSTRAINT_TYPE_MINMAX

Bone constraint type: Floor (min/max limit).

## CONSTRAINT_TYPE_SIZELIKE

Bone constraint type: Copy Scale.

## CONSTRAINT_TYPE_LOCKTRACK

Bone constraint type: Locked Track.

## CONSTRAINT_TYPE_STRETCHTO

Bone constraint type: Stretch To.

## CONSTRAINT_TYPE_CLAMPTO

Bone constraint type: Clamp To (sticks to a curve).

## CONSTRAINT_TYPE_TRANSFORM

Bone constraint type: Transformation.

## CONSTRAINT_TYPE_DISTLIMIT

Bone constraint type: Limit Distance.

See `Range.types.BL_ArmatureConstraint.ik_type`

## CONSTRAINT_IK_COPYPOSE

constraint is trying to match the position and eventually the rotation of the target.

**Value:** `0`

## CONSTRAINT_IK_DISTANCE

Constraint is maintaining a certain distance to target subject to ik_mode

**Value:** `1`

See `Range.types.BL_ArmatureConstraint.ik_flag`

## CONSTRAINT_IK_FLAG_TIP

Set when the constraint operates on the head of the bone and not the tail

**Value:** `1`

## CONSTRAINT_IK_FLAG_ROT

Set when the constraint tries to match the orientation of the target

**Value:** `2`

## CONSTRAINT_IK_FLAG_STRETCH

Set when the armature is allowed to stretch (only the bones with stretch factor > 0.0)

**Value:** `16`

## CONSTRAINT_IK_FLAG_POS

Set when the constraint tries to match the position of the target.

**Value:** `32`

See `Range.types.BL_ArmatureConstraint.ik_mode`

## CONSTRAINT_IK_MODE_INSIDE

The constraint tries to keep the bone within ik_dist of target

**Value:** `0`

## CONSTRAINT_IK_MODE_OUTSIDE

The constraint tries to keep the bone outside ik_dist of the target

**Value:** `1`

## CONSTRAINT_IK_MODE_ONSURFACE

The constraint tries to keep the bone exactly at ik_dist of the target.

**Value:** `2`

## BL_DST_ALPHA

Material blend factor: destination alpha. Used in setBlending().

## BL_DST_COLOR

Material blend factor: destination color. Used in setBlending().

## BL_ONE

Material blend factor: one (full color). Used in setBlending().

## BL_ONE_MINUS_DST_ALPHA

Material blend factor: one minus destination alpha. Used in setBlending().

## BL_ONE_MINUS_DST_COLOR

Material blend factor: one minus destination color. Used in setBlending().

## BL_ONE_MINUS_SRC_ALPHA

Material blend factor: one minus source alpha. Used in setBlending().

## BL_ONE_MINUS_SRC_COLOR

Material blend factor: one minus source color. Used in setBlending().

## BL_SRC_ALPHA

Material blend factor: source alpha. Used in setBlending().

## BL_SRC_ALPHA_SATURATE

Material blend factor: saturated source alpha. Used in setBlending().

## BL_SRC_COLOR

Material blend factor: source color. Used in setBlending().

## BL_ZERO

Material blend factor: zero (ignores the color). Used in setBlending().

## KX_INPUT_NONE

Key/button state: released.

## KX_INPUT_JUST_ACTIVATED

Key/button state: just pressed.

## KX_INPUT_ACTIVE

Key/button state: held down.

## KX_INPUT_JUST_RELEASED

Key/button state: just released.

## KX_ACTION_MODE_PLAY

Play the action once.

**Value:** `0`

## KX_ACTION_MODE_LOOP

Loop the action (repeat it).

**Value:** `1`

## KX_ACTION_MODE_PING_PONG

Play the action one direct then back the other way when it has completed.

**Value:** `2`

## KX_ACTION_BLEND_BLEND

Blend layers using linear interpolation

**Value:** `0`

## KX_ACTION_BLEND_ADD

Adds the layers together

**Value:** `1`

## KX_MOUSE_BUT_LEFT

Left mouse button (for the mouse sensor).

## KX_MOUSE_BUT_MIDDLE

Middle mouse button (for the mouse sensor).

## KX_MOUSE_BUT_RIGHT

Right mouse button (for the mouse sensor).

## RM_WALLS

Draw only the walls.

## RM_POLYS

Draw only polygons.

## RM_TRIS

Draw triangle mesh.

## VIEWMATRIX

Shader uniform with the view (world → camera) matrix. Used in setUniformDef().

## VIEWMATRIX_INVERSE

Shader uniform with the view (world → camera) matrix, inverse. Used in setUniformDef().

## VIEWMATRIX_INVERSETRANSPOSE

Shader uniform with the view (world → camera) matrix, inverse transposed. Used in setUniformDef().

## VIEWMATRIX_TRANSPOSE

Shader uniform with the view (world → camera) matrix, transposed. Used in setUniformDef().

## MODELMATRIX

Shader uniform with the model (object → world) matrix. Used in setUniformDef().

## MODELMATRIX_INVERSE

Shader uniform with the model (object → world) matrix, inverse. Used in setUniformDef().

## MODELMATRIX_INVERSETRANSPOSE

Shader uniform with the model (object → world) matrix, inverse transposed. Used in setUniformDef().

## MODELMATRIX_TRANSPOSE

Shader uniform with the model (object → world) matrix, transposed. Used in setUniformDef().

## MODELVIEWMATRIX

Shader uniform with the model × view matrix. Used in setUniformDef().

## MODELVIEWMATRIX_INVERSE

Shader uniform with the model × view matrix, inverse. Used in setUniformDef().

## MODELVIEWMATRIX_INVERSETRANSPOSE

Shader uniform with the model × view matrix, inverse transposed. Used in setUniformDef().

## MODELVIEWMATRIX_TRANSPOSE

Shader uniform with the model × view matrix, transposed. Used in setUniformDef().

## CAM_POS

Current camera position

## CONSTANT_TIMER

Shader uniform with the game time, for animated effects.

## EYE

User a timer for the uniform value.

## SHD_TANGENT

`BL_Shader` vertex attribute type: the vertex tangent. Value `1`.

## KX_STATE1

Mask for logic brick state 1.

## KX_STATE2

Mask for logic brick state 2.

## KX_STATE3

Mask for logic brick state 3.

## KX_STATE4

Mask for logic brick state 4.

## KX_STATE5

Mask for logic brick state 5.

## KX_STATE6

Mask for logic brick state 6.

## KX_STATE7

Mask for logic brick state 7.

## KX_STATE8

Mask for logic brick state 8.

## KX_STATE9

Mask for logic brick state 9.

## KX_STATE10

Mask for logic brick state 10.

## KX_STATE11

Mask for logic brick state 11.

## KX_STATE12

Mask for logic brick state 12.

## KX_STATE13

Mask for logic brick state 13.

## KX_STATE14

Mask for logic brick state 14.

## KX_STATE15

Mask for logic brick state 15.

## KX_STATE16

Mask for logic brick state 16.

## KX_STATE17

Mask for logic brick state 17.

## KX_STATE18

Mask for logic brick state 18.

## KX_STATE19

Mask for logic brick state 19.

## KX_STATE20

Mask for logic brick state 20.

## KX_STATE21

Mask for logic brick state 21.

## KX_STATE22

Mask for logic brick state 22.

## KX_STATE23

Mask for logic brick state 23.

## KX_STATE24

Mask for logic brick state 24.

## KX_STATE25

Mask for logic brick state 25.

## KX_STATE26

Mask for logic brick state 26.

## KX_STATE27

Mask for logic brick state 27.

## KX_STATE28

Mask for logic brick state 28.

## KX_STATE29

Mask for logic brick state 29.

## KX_STATE30

Mask for logic brick state 30.

See `Range.types.KX_StateActuator.operation`

## KX_STATE_OP_CLR

Substract bits to state mask

**Value:** `0`

## KX_STATE_OP_CPY

Copy state mask

**Value:** `1`

## KX_STATE_OP_NEG

Invert bits to state mask

**Value:** `2`

## KX_STATE_OP_SET

Add bits to state mask

**Value:** `3`

## KX_GAME_SCREENSHOT

 `constant`

Game actuator mode: takes a screenshot.

## KX_JOYSTICK_BUT_A

 `constant`

Gamepad A button.

## KX_JOYSTICK_BUT_B

 `constant`

Gamepad B button.

## KX_JOYSTICK_BUT_BACK

 `constant`

Gamepad Back/Select button.

## KX_JOYSTICK_BUT_GUIDE

 `constant`

Gamepad Guide (center) button.

## KX_JOYSTICK_BUT_LEFTSHOUDER

 `constant`

Gamepad left shoulder button (LB).

## KX_JOYSTICK_BUT_LEFTSTICK

 `constant`

Gamepad left stick click.

## KX_JOYSTICK_BUT_PADDOWN

 `constant`

Gamepad D-pad down.

## KX_JOYSTICK_BUT_PADLEFT

 `constant`

Gamepad D-pad left.

## KX_JOYSTICK_BUT_PADRIGHT

 `constant`

Gamepad D-pad right.

## KX_JOYSTICK_BUT_PADUP

 `constant`

Gamepad D-pad up.

## KX_JOYSTICK_BUT_RIGHTSHOUDER

 `constant`

Gamepad right shoulder button (RB).

## KX_JOYSTICK_BUT_RIGHTSTICK

 `constant`

Gamepad right stick click.

## KX_JOYSTICK_BUT_X

 `constant`

Gamepad X button.

## KX_JOYSTICK_BUT_Y

 `constant`

Gamepad Y button.

## KX_MOUSE_BUT_BUTTON6

 `constant`

Mouse button 6.

## KX_MOUSE_BUT_BUTTON7

 `constant`

Mouse button 7.

## KX_MOUSE_BUT_LEFTTHUMBMOUSE

 `constant`

Left side mouse button (thumb).

## KX_MOUSE_BUT_RIGHTTHUMBMOUSE

 `constant`

Right side mouse button (thumb).

## KX_MOUSESENSORMODE_BUTTON6

 `constant`

Mouse sensor mode: reacts to mouse button 6.

## KX_MOUSESENSORMODE_BUTTON7

 `constant`

Mouse sensor mode: reacts to mouse button 7.

## KX_MOUSESENSORMODE_LEFTBUTTON

 `constant`

Mouse sensor mode: reacts to left mouse button.

## KX_MOUSESENSORMODE_LEFTTHUMBMOUSE

 `constant`

Mouse sensor mode: reacts to left thumb mouse button.

## KX_MOUSESENSORMODE_MIDDLEBUTTON

 `constant`

Mouse sensor mode: reacts to middle mouse button.

## KX_MOUSESENSORMODE_MOVEMENT

 `constant`

Mouse sensor mode: reacts to mouse movement.

## KX_MOUSESENSORMODE_RIGHTBUTTON

 `constant`

Mouse sensor mode: reacts to right mouse button.

## KX_MOUSESENSORMODE_RIGHTTHUMBMOUSE

 `constant`

Mouse sensor mode: reacts to right thumb mouse button.

## KX_MOUSESENSORMODE_WHEELDOWN

 `constant`

Mouse sensor mode: reacts to mouse wheel down.

## KX_MOUSESENSORMODE_WHEELUP

 `constant`

Mouse sensor mode: reacts to mouse wheel up.

## KX_MOVEMENT_ALL_AXIS

 `constant`

Movement sensor: watches all axes.

## KX_MOVEMENT_AXIS_NEG_X

 `constant`

Movement sensor: -X axis.

## KX_MOVEMENT_AXIS_NEG_Y

 `constant`

Movement sensor: -Y axis.

## KX_MOVEMENT_AXIS_NEG_Z

 `constant`

Movement sensor: -Z axis.

## KX_MOVEMENT_AXIS_POS_X

 `constant`

Movement sensor: +X axis.

## KX_MOVEMENT_AXIS_POS_Y

 `constant`

Movement sensor: +Y axis.

## KX_MOVEMENT_AXIS_POS_Z

 `constant`

Movement sensor: +Z axis.

## RAS_2DFILTER_BLOOM

 `constant`

2D filter: Bloom.

## RAS_2DFILTER_FXAA

 `constant`

2D filter: FXAA.

## RAS_2DFILTER_LIGHTSCATTER

 `constant`

2D filter: light scattering (light rays).

## RAS_2DFILTER_OUTLINE

 `constant`

2D filter: outline.

## RAS_2DFILTER_SSAO

 `constant`

2D filter: ambient occlusion (SSAO).

## RAS_2DFILTER_SSR

 `constant`

2D filter: screen-space reflections (SSR).

## RAS_2DFILTER_TONEMAP

 `constant`

2D filter: tonemap.
