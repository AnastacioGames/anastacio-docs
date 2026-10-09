---
title: "KX_VehicleWrapper"
description: "Referência da classe Range.types.KX_VehicleWrapper"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



KX_VehicleWrapper

TODO - description

### addWheel(wheel, attachPos, downDir, axleDir, suspensionRestLength, wheelRadius, hasSteering)

Add a wheel to the vehicle

- **`wheel`**: The object to use as a wheel.
  - tipo: `KX_GameObject` or a `KX_GameObject` name
- **`attachPos`**: The position to attach the wheel, relative to the chassis object center.
  - tipo: vector of 3 floats
- **`downDir`**: The direction vector pointing down to where the vehicle should collide with the floor.
  - tipo: vector of 3 floats
- **`axleDir`**: The axis the wheel rotates around, relative to the chassis.
  - tipo: vector of 3 floats
- **`suspensionRestLength`**: The length of the suspension when no forces are being applied.
  - tipo: float
- **`wheelRadius`**: The radius of the wheel (half the diameter).
  - tipo: float
- **`hasSteering`**: True if the wheel should turn with steering, typically used in front wheels.
  - tipo: boolean

### applyBraking(force, wheelIndex)

Apply a braking force to the specified wheel

- **`force`**: the brake force
  - tipo: float
- **`wheelIndex`**: index of the wheel where the force needs to be applied
  - tipo: integer

### applyEngineForce(force, wheelIndex)

Apply an engine force to the specified wheel

- **`force`**: the engine force
  - tipo: float
- **`wheelIndex`**: index of the wheel where the force needs to be applied
  - tipo: integer

### getConstraintId()

Get the constraint ID

**Retorna:** the constraint id

**Tipo do retorno:** integer

### getConstraintType()

Returns the constraint type.

**Retorna:** constraint type

**Tipo do retorno:** integer

### getNumWheels()

Returns the number of wheels.

**Retorna:** the number of wheels for this vehicle

**Tipo do retorno:** integer

### getWheelOrientationQuaternion(wheelIndex)

Returns the wheel orientation as a quaternion.

- **`wheelIndex`**: the wheel index
  - tipo: integer

**Retorna:** TODO Description

**Tipo do retorno:** TODO - type should be quat as per method name but from the code it looks like a matrix

### getWheelPosition(wheelIndex)

Returns the position of the specified wheel

- **`wheelIndex`**: the wheel index
  - tipo: integer

**Retorna:** position vector

**Tipo do retorno:** list[x, y, z]

### getWheelRotation(wheelIndex)

Returns the rotation of the specified wheel

- **`wheelIndex`**: the wheel index
  - tipo: integer

**Retorna:** the wheel rotation

**Tipo do retorno:** float

### setRollInfluence(rollInfluece, wheelIndex)

Set the specified wheel's roll influence. The higher the roll influence the more the vehicle will tend to roll over in corners.

- **`rollInfluece`**: the wheel roll influence
  - tipo: float
- **`wheelIndex`**: the wheel index
  - tipo: integer

### setSteeringValue(steering, wheelIndex)

Set the specified wheel's steering

- **`steering`**: the wheel steering
  - tipo: float
- **`wheelIndex`**: the wheel index
  - tipo: integer

### setSuspensionCompression(compression, wheelIndex)

Set the specified wheel's compression

- **`compression`**: the wheel compression
  - tipo: float
- **`wheelIndex`**: the wheel index
  - tipo: integer

### setSuspensionDamping(damping, wheelIndex)

Set the specified wheel's damping

- **`damping`**: the wheel damping
  - tipo: float
- **`wheelIndex`**: the wheel index
  - tipo: integer

### setSuspensionStiffness(stiffness, wheelIndex)

Set the specified wheel's stiffness

- **`stiffness`**: the wheel stiffness
  - tipo: float
- **`wheelIndex`**: the wheel index
  - tipo: integer

### setTyreFriction(friction, wheelIndex)

Set the specified wheel's tyre friction

- **`friction`**: the tyre friction
  - tipo: float
- **`wheelIndex`**: the wheel index
  - tipo: integer

### rayMask

Set ray cast mask.

**Tipo:** bitfield

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getCoordinateSystem()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getCurrentSpeedKmh()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getCurrentSpeedMps()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getForwardVector()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getWheelConfig()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### getWheelState()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### loadPreset()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### rebuildPreset()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### resetSuspension()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### savePreset()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setCoordinateSystem()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### setWheelIsDriveWheel()

<span class="ae-badge pendente">sem documentação</span> <small>método</small>

### constraint_id

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

### constraint_type

<span class="ae-badge pendente">sem documentação</span> <small>atributo · só leitura</small>

