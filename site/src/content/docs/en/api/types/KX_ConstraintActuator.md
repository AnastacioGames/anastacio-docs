---
title: "KX_ConstraintActuator"
description: "Range.types.KX_ConstraintActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)



A constraint actuator limits the position, rotation, distance or orientation of an object.

### damp

Time constant of the constraint expressed in frame (not use by Force field constraint).

**Type:** integer

### rotDamp

Time constant for the rotation expressed in frame (only for the distance constraint), 0 = use damp for rotation as well.

**Type:** integer

### direction

The reference direction in world coordinate for the orientation constraint.

**Type:** `mathutils.Vector`

### option

Binary combination of `these constants`

**Type:** integer

### time

activation time of the actuator. The actuator disables itself after this many frame. If set to 0, the actuator is not limited in time.

**Type:** integer

### propName

the name of the property or material for the ray detection of the distance constraint.

**Type:** string

### min

The lower bound of the constraint. For the rotation and orientation constraint, it represents radiant.

**Type:** float

### distance

the target distance of the distance constraint.

**Type:** float

### max

the upper bound of the constraint. For rotation and orientation constraints, it represents radiant.

**Type:** float

### rayLength

the length of the ray of the distance constraint.

**Type:** float

### limit

type of constraint. Use one of the `these constants`

**Type:** integer.

