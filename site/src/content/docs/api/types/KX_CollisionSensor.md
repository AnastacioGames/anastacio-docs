---
title: "KX_CollisionSensor"
description: "Referência da classe Range.types.KX_CollisionSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Collision sensor detects collisions between objects.

### propName

The property or material to collide with.

**Tipo:** string

### useMaterial

Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property.

**Tipo:** boolean

### usePulseCollision

When enabled, changes to the set of colliding objects generate a pulse.

**Tipo:** boolean

### hitObject

The last collided object. (read-only).

**Tipo:** `KX_GameObject` or None

### hitObjectList

A list of colliding objects. (read-only).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

### hitMaterial

The material of the object in the face hit by the ray. (read-only).

**Tipo:** string

