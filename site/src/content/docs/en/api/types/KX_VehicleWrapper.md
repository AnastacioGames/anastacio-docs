---
title: "KX_VehicleWrapper"
description: "Range.types.KX_VehicleWrapper class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`KX_GameObject`](../../types/kx_gameobject/), [`Range.constraints`](../../modulos/constraints/), [`KX_CharacterWrapper`](../../types/kx_characterwrapper/)
:::



KX_VehicleWrapper

TODO - description

### addWheel(wheel, attachPos, downDir, axleDir, suspensionRestLength, wheelRadius, hasSteering)

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

### applyBraking(force, wheelIndex)

Apply a braking force to the specified wheel

- **`force`**: the brake force
  - type: float
- **`wheelIndex`**: index of the wheel where the force needs to be applied
  - type: integer

### applyEngineForce(force, wheelIndex)

Apply an engine force to the specified wheel

- **`force`**: the engine force
  - type: float
- **`wheelIndex`**: index of the wheel where the force needs to be applied
  - type: integer

### getConstraintId()

Get the constraint ID

**Returns:** the constraint id

**Return type:** integer

### getConstraintType()

Returns the constraint type.

**Returns:** constraint type

**Return type:** integer

### getNumWheels()

Returns the number of wheels.

**Returns:** the number of wheels for this vehicle

**Return type:** integer

### getWheelOrientationQuaternion(wheelIndex)

Returns the wheel orientation as a quaternion.

- **`wheelIndex`**: the wheel index
  - type: integer

**Returns:** TODO Description

**Return type:** TODO - type should be quat as per method name but from the code it looks like a matrix

### getWheelPosition(wheelIndex)

Returns the position of the specified wheel

- **`wheelIndex`**: the wheel index
  - type: integer

**Returns:** position vector

**Return type:** list[x, y, z]

### getWheelRotation(wheelIndex)

Returns the rotation of the specified wheel

- **`wheelIndex`**: the wheel index
  - type: integer

**Returns:** the wheel rotation

**Return type:** float

### setRollInfluence(rollInfluece, wheelIndex)

Set the specified wheel's roll influence.
The higher the roll influence the more the vehicle will tend to roll over in corners.

- **`rollInfluece`**: the wheel roll influence
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

### setSteeringValue(steering, wheelIndex)

Set the specified wheel's steering

- **`steering`**: the wheel steering
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

### setSuspensionCompression(compression, wheelIndex)

Set the specified wheel's compression

- **`compression`**: the wheel compression
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

### setSuspensionDamping(damping, wheelIndex)

Set the specified wheel's damping

- **`damping`**: the wheel damping
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

### setSuspensionStiffness(stiffness, wheelIndex)

Set the specified wheel's stiffness

- **`stiffness`**: the wheel stiffness
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

### setTyreFriction(friction, wheelIndex)

Set the specified wheel's tyre friction

- **`friction`**: the tyre friction
  - type: float
- **`wheelIndex`**: the wheel index
  - type: integer

### rayMask

Set ray cast mask.

**Type:** bitfield

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### getCoordinateSystem()

 <small>method</small>

Vehicle axes `(right, up, forward)` (0=X, 1=Y, 2=Z).

**Returns:** `tuple`

### getCurrentSpeedKmh()

 <small>method</small>

Current speed in km/h.

**Returns:** `float`

### getCurrentSpeedMps()

 <small>method</small>

Current speed in meters per second.

**Returns:** `float`

### getForwardVector()

 <small>method</small>

Vehicle forward direction, in world space.

**Returns:** `Vector`

### getWheelConfig(wheelIndex)

 <small>method</small>

Wheel configuration: `connectionPoint`, `downDirection`, `axleDirection`, `suspensionRestLength`, `wheelRadius`, `hasSteering` and `isDriveWheel`.

**Returns:** `dict`

### getWheelState(wheelIndex)

 <small>method</small>

Wheel state this tick: world position and orientation, `rotation`, `isInContact`, contact point and normal, `suspensionForce` and more.

**Returns:** `dict`

### loadPreset(path)

 <small>method</small>

Loads a vehicle preset (file) and applies it to this vehicle.

### rebuildPreset(path, wheelObjects)

 <small>method</small>

Rebuilds the wheels from the preset, using the given objects (one per wheel). Use Empties with **No Collision** physics as wheels.

### resetSuspension()

 <small>method</small>

Puts the suspension back at rest (useful after teleporting the car).

### savePreset(path)

 <small>method</small>

Saves the current vehicle setup to a preset file.

### setCoordinateSystem(right, up, forward)

 <small>method</small>

Sets which axes (0=X, 1=Y, 2=Z) are right, up and forward. All three axes must be used without repeating.

### setSuspensionRestLength(value, wheelIndex)

<span class="ae-badge novo">new in Anastacio</span> <small>method</small>

Changes a wheel's suspension rest length (positive value). Applied on the next physics step.

### setWheelIsDriveWheel(wheelIndex, isDriveWheel)

 <small>method</small>

Sets whether the wheel gets engine traction.

### setWheelRadius(value, wheelIndex)

<span class="ae-badge novo">new in Anastacio</span> <small>method</small>

Changes a wheel's radius (positive value). Applied on the next physics step.

### constraint_id

 <small>attribute · read-only</small>

Id of the vehicle physics constraint.

### constraint_type

 <small>attribute · read-only</small>

Type of the vehicle physics constraint.

