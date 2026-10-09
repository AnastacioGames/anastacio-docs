---
title: "KX_RaySensor"
description: "Referência da classe Range.types.KX_RaySensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



A ray sensor detects the first object in a given direction.

### propName

The property the ray is looking for.

**Tipo:** string

### range

The distance of the ray.

**Tipo:** float

### useMaterial

Whether or not to look for a material (false = property).

**Tipo:** boolean

### useXRay

Whether or not to use XRay.

**Tipo:** boolean

### mask

The collision mask (16 layers mapped to a 16-bit integer) combined with each object's collision group, to hit only a subset of the
objects in the scene. Only those objects for which `collisionGroup & mask` is true can be hit.

**Tipo:** bitfield

### hitObject

The game object that was hit by the ray. (read-only).

**Tipo:** `KX_GameObject`

### hitPosition

The position (in worldcoordinates) where the object was hit by the ray. (read-only).

**Tipo:** `mathutils.Vector`

### hitNormal

The normal (in worldcoordinates) of the object at the location where the object was hit by the ray. (read-only).

**Tipo:** `mathutils.Vector`

### hitMaterial

The material of the object in the face hit by the ray. (read-only).

**Tipo:** string

### rayDirection

The direction from the ray (in worldcoordinates). (read-only).

**Tipo:** `mathutils.Vector`

### axis

The axis the ray is pointing on.

**Tipo:** integer from 0 to 5

* KX_RAY_AXIS_POS_X
* KX_RAY_AXIS_POS_Y
* KX_RAY_AXIS_POS_Z
* KX_RAY_AXIS_NEG_X
* KX_RAY_AXIS_NEG_Y
* KX_RAY_AXIS_NEG_Z

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### gazeAngle

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### gazeProgress

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### gazeTime

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

