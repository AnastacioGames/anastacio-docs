---
title: "KX_RaySensor"
description: "Range.types.KX_RaySensor class reference"
---

Base class: [`SCA_ISensor`](../sca_isensor/)



A ray sensor detects the first object in a given direction.

### propName

The property the ray is looking for.

**Type:** string

### range

The distance of the ray.

**Type:** float

### useMaterial

Whether or not to look for a material (false = property).

**Type:** boolean

### useXRay

Whether or not to use XRay.

**Type:** boolean

### mask

The collision mask (16 layers mapped to a 16-bit integer) combined with each object's collision group, to hit only a subset of the
objects in the scene. Only those objects for which `collisionGroup & mask` is true can be hit.

**Type:** bitfield

### hitObject

The game object that was hit by the ray. (read-only).

**Type:** `KX_GameObject`

### hitPosition

The position (in worldcoordinates) where the object was hit by the ray. (read-only).

**Type:** `mathutils.Vector`

### hitNormal

The normal (in worldcoordinates) of the object at the location where the object was hit by the ray. (read-only).

**Type:** `mathutils.Vector`

### hitMaterial

The material of the object in the face hit by the ray. (read-only).

**Type:** string

### rayDirection

The direction from the ray (in worldcoordinates). (read-only).

**Type:** `mathutils.Vector`

### axis

The axis the ray is pointing on.

**Type:** integer from 0 to 5

* KX_RAY_AXIS_POS_X
* KX_RAY_AXIS_POS_Y
* KX_RAY_AXIS_POS_Z
* KX_RAY_AXIS_NEG_X
* KX_RAY_AXIS_NEG_Y
* KX_RAY_AXIS_NEG_Z

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### gazeAngle

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Gaze tolerance (0 to 1): how far off the ray center the target can be.

### gazeProgress

<span class="ae-badge novo">new in Anastacio</span> <small>attribute · read-only</small>

Fixed gaze progress, from 0 to 1. Reaches 1 after `gazeTime` seconds looking at the target.

### gazeTime

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Time in seconds looking at the target for the sensor to fire (0 to 30).

