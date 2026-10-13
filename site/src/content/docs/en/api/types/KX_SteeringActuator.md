---
title: "KX_SteeringActuator"
description: "Range.types.KX_SteeringActuator class reference"
---

Base class: [`SCA_IActuator`](../sca_iactuator/)

:::tip[See also]
[`KX_NavMeshObject`](../../types/kx_navmeshobject/)
:::



Steering Actuator for navigation.

### behavior

The steering behavior to use.

**Type:** one of `these constants`

### velocity

Velocity magnitude

**Type:** float

### acceleration

Max acceleration

**Type:** float

### turnspeed

Max turn speed

**Type:** float

### distance

Relax distance

**Type:** float

### target

Target object

**Type:** `KX_GameObject`

### navmesh

Navigation mesh

**Type:** `KX_GameObject`

### selfterminated

Terminate when target is reached

**Type:** boolean

### enableVisualization

Enable debug visualization

**Type:** boolean

### pathUpdatePeriod

Path update period

**Type:** int

### path

Path point list.

**Type:** list of `mathutils.Vector`

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### facingMode

 <small>attribute</small>

Where the object turns while walking: 0 doesn't turn, 1 to 3 = +X, +Y, +Z axis, 4 to 6 = -X, -Y, -Z.

### lockZVelocity

 <small>attribute</small>

Doesn't touch the object vertical (Z) velocity.

### steeringVec

 <small>attribute · read-only</small>

Direction vector computed by the actuator this frame.

