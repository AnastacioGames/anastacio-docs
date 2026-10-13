---
title: "Range.constraints"
description: "Range.constraints module reference"
---

:::tip[See also]
[`KX_VehicleWrapper`](../../types/kx_vehiclewrapper/), [`KX_CharacterWrapper`](../../types/kx_characterwrapper/), [`KX_ConstraintWrapper`](../../types/kx_constraintwrapper/)
:::

Bullet Physics provides collision detection
and rigid body dynamics for the Blender Game Engine.

Features:

- Vehicle simulation.
- Rigid body constraints: hinge and point to point (ball socket).
- Access to internal physics settings,
like deactivation time, and debugging features

:::note
Since this API is not well documented, it can be unclear what kind of values to use for setting parameters.
In general, damping settings should be in the range of 0 to 1 and
stiffness settings should not be much higher than about 10.
:::

## Examples

:::tip
For more examples of Bullet physics and how to use them
see the [pybullet forum](https://pybullet.org/Bullet/phpBB3/viewforum.php?f=17)_.
:::

## Functions

### createConstraint( \

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

### createVehicle(physicsid)

Creates a vehicle constraint.

- **`physicsid`**: The physics id of the chassis object in constraint.
  - type: int

**Returns:** A vehicle constraint wrapper.

**Return type:** `KX_VehicleWrapper`

### exportBulletFile(filename)

Exports a file representing the dynamics world (usually using `.bullet` extension).

See [Bullet binary serialization](http://bulletphysics.org/mediawiki-1.5.8/index.php/Bullet_binary_serialization)_.

- **`filename`**: File path.
  - type: str

### getAppliedImpulse(constraintId)

- **`constraintId`**: The id of the constraint.
  - type: int

**Returns:** The most recent applied impulse.

**Return type:** float

### getVehicleConstraint(constraintId)

- **`constraintId`**: The id of the vehicle constraint.
  - type: int

**Returns:** A vehicle constraint object.

**Return type:** `KX_VehicleWrapper`

### getCharacter(gameobj)

- **`gameobj`**: The game object with the character physics.
  - type: `KX_GameObject`

**Returns:** Character wrapper.

**Return type:** `KX_CharacterWrapper`

### removeConstraint(constraintId)

Removes a constraint.

- **`constraintId`**: The id of the constraint to be removed.
  - type: int

### setCcdMode(ccdMode)

:::note
Very experimental, not recommended
:::

Sets the CCD (Continous Colision Detection) mode in the Physics Environment.

- **`ccdMode`**: The new CCD mode.
  - type: int

### setContactBreakingTreshold(breakingTreshold)

:::note
Reasonable default is 0.02 (if units are meters)
:::

Sets tresholds to do with contact point management.

- **`breakingTreshold`**: The new contact breaking treshold.
  - type: float

### setDeactivationAngularTreshold(angularTreshold)

Sets the angular velocity treshold.

- **`angularTreshold`**: New deactivation angular treshold.
  - type: float

### setDeactivationLinearTreshold(linearTreshold)

Sets the linear velocity treshold.

- **`linearTreshold`**: New deactivation linear treshold.
  - type: float

### setDeactivationTime(time)

Sets the time after which a resting rigidbody gets deactived.

- **`time`**: The deactivation time.
  - type: float

### setDebugMode(mode)

Sets the debug mode.

- **`mode`**: The new debug mode, see `Debug Mode Constants`_.
  - type: int

### setGravity(x, y, z)

Sets the gravity force.

- **`x`**: Gravity X force.
  - type: float
- **`y`**: Gravity Y force.
  - type: float
- **`z`**: Gravity Z force.
  - type: float

### setLinearAirDamping(damping)

:::note
Not implemented
:::

Sets the linear air damping for rigidbodies.

### setNumIterations(numiter)

Sets the number of iterations for an iterative constraint solver.

- **`numiter`**: New number of iterations.
  - type: int

### setLinearSlop(slop)

Sets the contact penetration tolerance for the active physics scene.
A positive value allows objects to overlap by up to `slop` Blender units
before the Bullet solver applies positional correction. The default is `0.0`.

This is a scene-wide solver setting: it affects every physical contact in
the active scene. It does not change an object's collision margin or the
point at which collisions are detected. Use small values appropriate to the
scene scale.

- **`slop`**: Penetration tolerance in Blender units. Use a finite, non-negative value.
  - type: float

### setNumTimeSubSteps(numsubstep)

Sets the number of substeps for each physics proceed. Tradeoff quality for performance.

- **`numsubstep`**: New number of substeps.
  - type: int

### setSolverDamping(damping)

:::note
Very experimental, not recommended
:::

Sets the damper constant of a penalty based solver.

- **`damping`**: New damping for the solver.
  - type: float

### setSolverTau(tau)

:::note
Very experimental, not recommended
:::

Sets the spring constant of a penalty based solver.

- **`tau`**: New tau for the solver.
  - type: float

### setSolverType(solverType)

:::note
Very experimental, not recommended
:::

Sets the solver type.

- **`solverType`**: The new type of the solver.
  - type: int

### setSorConstant(sor)

:::note
Very experimental, not recommended
:::

Sets the successive overrelaxation constant.

- **`sor`**: New sor value.
  - type: float

### setUseEpa(epa)

:::note
Not implemented
:::

## Constants

### error

Symbolic constant string that indicates error.

**Type:** str

## Debug Mode Constants

Debug mode to be used with `setDebugMode`.

### DBG_NODEBUG

No debug.

### DBG_DRAWWIREFRAME

Draw wireframe in debug.

### DBG_DRAWAABB

Draw Axis Aligned Bounding Box in debug.

### DBG_DRAWFREATURESTEXT

Draw features text in debug.

### DBG_DRAWCONTACTPOINTS

Draw contact points in debug.

### DBG_NOHELPTEXT

Debug without help text.

### DBG_DRAWTEXT

Draw text in debug.

### DBG_PROFILETIMINGS

Draw profile timings in debug.

### DBG_ENABLESATCOMPARISION

Enable sat comparision in debug.

### DBG_DISABLEBULLETLCP

Disable Bullet LCP.

### DBG_ENABLECCD

Enable Continous Collision Detection in debug.

### DBG_DRAWCONSTRAINTS

Draw constraints in debug.

### DBG_DRAWCONSTRAINTLIMITS

Draw constraint limits in debug.

### DBG_FASTWIREFRAME

Draw a fast wireframe in debug.

## Create Constraint Constants

Constraint type to be used with `createConstraint`.

### POINTTOPOINT_CONSTRAINT

.. to do

### LINEHINGE_CONSTRAINT

.. to do

### ANGULAR_CONSTRAINT

.. to do

### CONETWIST_CONSTRAINT

.. to do

### VEHICLE_CONSTRAINT

.. to do

### GENERIC_6DOF_CONSTRAINT

.. to do

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### setErp(value)

 <small>function</small>

Physics solver ERP: how much of the penetration between objects is corrected per step (default 0.2).

### setErp2(value)

 <small>function</small>

ERP used with split impulse (default 0.8).

### setGlobalCfm(value)

 <small>function</small>

Global CFM: makes contacts and joints "softer" (default 0.0).

### setMaxGyroscopicForce(value)

 <small>function</small>

Gyroscopic force limit (explicit mode only).

### setSplitImpulse(enabled)

 <small>function</small>

Solves contact position and velocity separately. Avoids objects "popping" when separating.

### setSplitImpulsePenetrationThreshold(value)

 <small>function</small>

Penetration from which split impulse is used (default -0.04).

### setSplitImpulseTurnErp(value)

 <small>function</small>

Split impulse rotation correction (default 0.1).

### setWarmstartingFactor(value)

 <small>function</small>

How much the solver reuses the previous frame result (0.0 to 1.0).

