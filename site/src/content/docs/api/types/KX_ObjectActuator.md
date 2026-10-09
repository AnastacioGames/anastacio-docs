---
title: "KX_ObjectActuator"
description: "Referência da classe Range.types.KX_ObjectActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



The object actuator ("Motion Actuator") applies force, torque, displacement, angular displacement, velocity, or angular velocity to an object. Servo control allows to regulate force to achieve a certain speed target.

### force

The force applied by the actuator.

**Tipo:** Vector((x, y, z))

### useLocalForce

A flag specifying if the force is local.

**Tipo:** boolean

### torque

The torque applied by the actuator.

**Tipo:** Vector((x, y, z))

### useLocalTorque

A flag specifying if the torque is local.

**Tipo:** boolean

### dLoc

The displacement vector applied by the actuator.

**Tipo:** Vector((x, y, z))

### useLocalDLoc

A flag specifying if the dLoc is local.

**Tipo:** boolean

### dRot

The angular displacement vector applied by the actuator

**Tipo:** Vector((x, y, z))

:::note
Since the displacement is applied every frame, you must adjust the displacement based on the frame rate, or you game experience will depend on the player's computer speed.
:::

### useLocalDRot

A flag specifying if the dRot is local.

**Tipo:** boolean

### linV

The linear velocity applied by the actuator.

**Tipo:** Vector((x, y, z))

### useLocalLinV

A flag specifying if the linear velocity is local.

**Tipo:** boolean

:::note
This is the target speed for servo controllers.
:::

### angV

The angular velocity applied by the actuator.

**Tipo:** Vector((x, y, z))

### useLocalAngV

A flag specifying if the angular velocity is local.

**Tipo:** boolean

### damping

The damping parameter of the servo controller.

**Tipo:** short

### forceLimitX

The min/max force limit along the X axis and activates or deactivates the limits in the servo controller.

**Tipo:** list [min(float), max(float), bool]

### forceLimitY

The min/max force limit along the Y axis and activates or deactivates the limits in the servo controller.

**Tipo:** list [min(float), max(float), bool]

### forceLimitZ

The min/max force limit along the Z axis and activates or deactivates the limits in the servo controller.

**Tipo:** list [min(float), max(float), bool]

### pid

The PID coefficients of the servo controller.

**Tipo:** list of floats [proportional, integral, derivate]

### reference

The object that is used as reference to compute the velocity for the servo controller.

**Tipo:** `KX_GameObject` or None

