---
title: "KX_ConstraintActuator"
description: "Referência da classe Range.types.KX_ConstraintActuator"
---

Classe base: [`SCA_IActuator`](../sca_iactuator/)



A constraint actuator limits the position, rotation, distance or orientation of an object.

### damp

Time constant of the constraint expressed in frame (not use by Force field constraint).

**Tipo:** integer

### rotDamp

Time constant for the rotation expressed in frame (only for the distance constraint), 0 = use damp for rotation as well.

**Tipo:** integer

### direction

The reference direction in world coordinate for the orientation constraint.

**Tipo:** `mathutils.Vector`

### option

Binary combination of `these constants`

**Tipo:** integer

### time

activation time of the actuator. The actuator disables itself after this many frame. If set to 0, the actuator is not limited in time.

**Tipo:** integer

### propName

the name of the property or material for the ray detection of the distance constraint.

**Tipo:** string

### min

The lower bound of the constraint. For the rotation and orientation constraint, it represents radiant.

**Tipo:** float

### distance

the target distance of the distance constraint.

**Tipo:** float

### max

the upper bound of the constraint. For rotation and orientation constraints, it represents radiant.

**Tipo:** float

### rayLength

the length of the ray of the distance constraint.

**Tipo:** float

### limit

type of constraint. Use one of the `these constants`

**Tipo:** integer.

