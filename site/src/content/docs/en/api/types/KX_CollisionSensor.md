---
title: "KX_CollisionSensor"
description: "Range.types.KX_CollisionSensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



Collision sensor detects collisions between objects.

### propName

The property or material to collide with.

**Type:** string

### useMaterial

Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property.

**Type:** boolean

### usePulseCollision

When enabled, changes to the set of colliding objects generate a pulse.

**Type:** boolean

### hitObject

The last collided object. (read-only).

**Type:** `KX_GameObject` or None

### hitObjectList

A list of colliding objects. (read-only).

**Type:** `EXP_ListValue` of `KX_GameObject`

### hitMaterial

The material of the object in the face hit by the ray. (read-only).

**Type:** string

