---
title: "Range.constraints"
description: "Referência do módulo Range.constraints"
---

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
  - tipo: int
- **`physicsid_2`**: The physics id of the second object in constraint.
  - tipo: int
- **`constraint_type`**: The type of the constraint, see `Create Constraint Constants`_.
  - tipo: int
- **`pivot_x`**: Pivot X position. (optional)
  - tipo: float
- **`pivot_y`**: Pivot Y position. (optional)
  - tipo: float
- **`pivot_z`**: Pivot Z position. (optional)
  - tipo: float
- **`axis_x`**: X axis angle in degrees. (optional)
  - tipo: float
- **`axis_y`**: Y axis angle in degrees. (optional)
  - tipo: float
- **`axis_z`**: Z axis angle in degrees. (optional)
  - tipo: float
- **`flag`**: 128 to disable collision between linked bodies. (optional)
  - tipo: int

**Retorna:** A constraint wrapper.

**Tipo do retorno:** `KX_ConstraintWrapper`

### createVehicle(physicsid)

Creates a vehicle constraint.

- **`physicsid`**: The physics id of the chassis object in constraint.
  - tipo: int

**Retorna:** A vehicle constraint wrapper.

**Tipo do retorno:** `KX_VehicleWrapper`

### exportBulletFile(filename)

Exports a file representing the dynamics world (usually using `.bullet` extension).

See [Bullet binary serialization](http://bulletphysics.org/mediawiki-1.5.8/index.php/Bullet_binary_serialization)_.

- **`filename`**: File path.
  - tipo: str

### getAppliedImpulse(constraintId)

- **`constraintId`**: The id of the constraint.
  - tipo: int

**Retorna:** The most recent applied impulse.

**Tipo do retorno:** float

### getVehicleConstraint(constraintId)

- **`constraintId`**: The id of the vehicle constraint.
  - tipo: int

**Retorna:** A vehicle constraint object.

**Tipo do retorno:** `KX_VehicleWrapper`

### getCharacter(gameobj)

- **`gameobj`**: The game object with the character physics.
  - tipo: `KX_GameObject`

**Retorna:** Character wrapper.

**Tipo do retorno:** `KX_CharacterWrapper`

### removeConstraint(constraintId)

Removes a constraint.

- **`constraintId`**: The id of the constraint to be removed.
  - tipo: int

### setCcdMode(ccdMode)

:::note
Very experimental, not recommended
:::

Sets the CCD (Continous Colision Detection) mode in the Physics Environment.

- **`ccdMode`**: The new CCD mode.
  - tipo: int

### setContactBreakingTreshold(breakingTreshold)

:::note
Reasonable default is 0.02 (if units are meters)
:::

Sets tresholds to do with contact point management.

- **`breakingTreshold`**: The new contact breaking treshold.
  - tipo: float

### setDeactivationAngularTreshold(angularTreshold)

Sets the angular velocity treshold.

- **`angularTreshold`**: New deactivation angular treshold.
  - tipo: float

### setDeactivationLinearTreshold(linearTreshold)

Sets the linear velocity treshold.

- **`linearTreshold`**: New deactivation linear treshold.
  - tipo: float

### setDeactivationTime(time)

Sets the time after which a resting rigidbody gets deactived.

- **`time`**: The deactivation time.
  - tipo: float

### setDebugMode(mode)

Sets the debug mode.

- **`mode`**: The new debug mode, see `Debug Mode Constants`_.
  - tipo: int

### setGravity(x, y, z)

Sets the gravity force.

- **`x`**: Gravity X force.
  - tipo: float
- **`y`**: Gravity Y force.
  - tipo: float
- **`z`**: Gravity Z force.
  - tipo: float

### setLinearAirDamping(damping)

:::note
Not implemented
:::

Sets the linear air damping for rigidbodies.

### setNumIterations(numiter)

Sets the number of iterations for an iterative constraint solver.

- **`numiter`**: New number of iterations.
  - tipo: int

### setLinearSlop(slop)

Sets the contact penetration tolerance for the active physics scene.
A positive value allows objects to overlap by up to `slop` Blender units
before the Bullet solver applies positional correction. The default is `0.0`.

This is a scene-wide solver setting: it affects every physical contact in
the active scene. It does not change an object's collision margin or the
point at which collisions are detected. Use small values appropriate to the
scene scale.

- **`slop`**: Penetration tolerance in Blender units. Use a finite, non-negative value.
  - tipo: float

### setNumTimeSubSteps(numsubstep)

Sets the number of substeps for each physics proceed. Tradeoff quality for performance.

- **`numsubstep`**: New number of substeps.
  - tipo: int

### setSolverDamping(damping)

:::note
Very experimental, not recommended
:::

Sets the damper constant of a penalty based solver.

- **`damping`**: New damping for the solver.
  - tipo: float

### setSolverTau(tau)

:::note
Very experimental, not recommended
:::

Sets the spring constant of a penalty based solver.

- **`tau`**: New tau for the solver.
  - tipo: float

### setSolverType(solverType)

:::note
Very experimental, not recommended
:::

Sets the solver type.

- **`solverType`**: The new type of the solver.
  - tipo: int

### setSorConstant(sor)

:::note
Very experimental, not recommended
:::

Sets the successive overrelaxation constant.

- **`sor`**: New sor value.
  - tipo: float

### setUseEpa(epa)

:::note
Not implemented
:::

## Constants

### error

Symbolic constant string that indicates error.

**Tipo:** str

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

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### setErp()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setErp2()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setGlobalCfm()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setMaxGyroscopicForce()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setSplitImpulse()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setSplitImpulsePenetrationThreshold()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setSplitImpulseTurnErp()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

### setWarmstartingFactor()

<span class="ae-badge pendente">sem documentação</span> <small>função</small>

