---
title: "KX_MouseFocusSensor"
description: "Referência da classe Range.types.KX_MouseFocusSensor"
---

Classe base: [`SCA_MouseSensor`](../sca_mousesensor/)



The mouse focus sensor detects when the mouse is over the current game object.

The mouse focus sensor works by transforming the mouse coordinates from 2d device space to 3d space then raycasting away from the camera.

### raySource

The worldspace source of the ray (the view position).

**Tipo:** list (vector of 3 floats)

### rayTarget

The worldspace target of the ray.

**Tipo:** list (vector of 3 floats)

### rayDirection

The `rayTarget` - `raySource` normalized.

**Tipo:** list (normalized vector of 3 floats)

### hitObject

the last object the mouse was over.

**Tipo:** `KX_GameObject` or None

### hitPosition

The worldspace position of the ray intersecton.

**Tipo:** list (vector of 3 floats)

### hitNormal

the worldspace normal from the face at point of intersection.

**Tipo:** list (normalized vector of 3 floats)

### hitUV

the UV coordinates at the point of intersection.

**Tipo:** list (vector of 2 floats)

If the object has no UV mapping, it returns [0, 0].

The UV coordinates are not normalized, they can be < 0 or > 1 depending on the UV mapping.

### usePulseFocus

When enabled, moving the mouse over a different object generates a pulse. (only used when the 'Mouse Over Any' sensor option is set).

**Tipo:** boolean

### useXRay

If enabled it allows the sensor to see through game objects that don't have the selected property or material.

**Tipo:** boolean

### mask

The collision mask (16 layers mapped to a 16-bit integer) combined with each object's collision group, to hit only a subset of the objects in the scene. Only those objects for which `collisionGroup & mask` is true can be hit.

**Tipo:** bitfield

### propName

The property or material the sensor is looking for.

**Tipo:** string

### useMaterial

Determines if the sensor is looking for a property or material. KX_True = Find material; KX_False = Find property.

**Tipo:** boolean

