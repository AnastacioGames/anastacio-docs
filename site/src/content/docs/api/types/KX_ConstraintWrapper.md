---
title: "KX_ConstraintWrapper"
description: "Referência da classe Range.types.KX_ConstraintWrapper"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



KX_ConstraintWrapper

### getConstraintId(val)

Returns the contraint ID

**Retorna:** the constraint ID

**Tipo do retorno:** integer

### setParam(axis, value0, value1)

Set the contraint limits

- **`axis`**: 
  - tipo: integer

:::note
* Lowerlimit == Upperlimit -> axis is locked
* Lowerlimit > Upperlimit -> axis is free
* Lowerlimit < Upperlimit -> axis it limited in that range
:::

For PHY_LINEHINGE_CONSTRAINT = 2 or PHY_ANGULAR_CONSTRAINT = 3:

axis = 3 is a constraint limit, with low/high limit value
* 3: X axis angle

- **`value0 (min)`**: Set the minimum limit of the axis
  - tipo: float
- **`value1 (max)`**: Set the maximum limit of the axis
  - tipo: float
For PHY_CONE_TWIST_CONSTRAINT = 4:

axis = 3..5 are constraint limits, high limit values
* 3: X axis angle
* 4: Y axis angle
* 5: Z axis angle

- **`value0 (min)`**: Set the minimum limit of the axis
  - tipo: float
- **`value1 (max)`**: Set the maximum limit of the axis
  - tipo: float
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
  - tipo: float
- **`value1 (max)`**: Set the maximum limit of the axis
  - tipo: float
axis = 6..8 are translational motors, with value0=target velocity, value1 = max motor force
* 6: X axis position
* 7: Y axis position
* 8: Z axis position

axis = 9..11 are rotational motors, with value0=target velocity, value1 = max motor force
* 9: X axis angle
* 10: Y axis angle
* 11: Z axis angle

- **`value0 (speed)`**: Set the linear velocity of the axis
  - tipo: float Range: -10,000.00 to 10,000.00
- **`value1 (force)`**: Set the maximum force limit of the axis
  - tipo: float Range: -10,000.00 to 10,000.00
axis = 12..14 are for linear springs on each of the position of freedom
* 12: X axis position
* 13: Y axis position
* 14: Z axis position

axis = 15..17 are for angular springs on each of the angle of freedom in radians
* 15: X axis angle
* 16: Y axis angle
* 17: Z axis angle

- **`value0 (stiffness)`**: Set the stiffness of the spring
  - tipo: float
- **`value1 (damping)`**: Tendency of the spring to return to it's original position
  - tipo: float 1.0 = springs back to original position (no damping) 0.0 = don't springs back

### getParam(axis)

Get the contraint position or euler angle of a generic 6DOF constraint

- **`axis`**: 
  - tipo: integer
axis = 0..2 are linear constraint values
* 0: X axis position
* 1: Y axis position
* 2: Z axis position

**Retorna:** position

**Tipo do retorno:** float

axis = 3..5 are relative constraint (Euler) angles in radians
* 3: X axis angle
* 4: Y axis angle
* 5: Z axis angle

**Retorna:** angle

**Tipo do retorno:** float

### constraint_id

Returns the contraint ID  (read only)

**Tipo:** integer

### constraint_type

Returns the contraint type (read only)

**Tipo:** integer - `POINTTOPOINT_CONSTRAINT` - `LINEHINGE_CONSTRAINT` - `ANGULAR_CONSTRAINT` - `CONETWIST_CONSTRAINT` - `VEHICLE_CONSTRAINT` - `GENERIC_6DOF_CONSTRAINT`

### breakingThreshold

The impulse threshold breaking the constraint, if the constraint is broken `enabled` is set to `False`.

**Tipo:** float greater or equal to 0

### enabled

The status of the constraint. Set to `True` to restore a constraint after breaking.

**Tipo:** boolean

