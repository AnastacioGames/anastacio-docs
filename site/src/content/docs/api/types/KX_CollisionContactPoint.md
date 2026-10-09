---
title: "KX_CollisionContactPoint"
description: "Referência da classe Range.types.KX_CollisionContactPoint"
---

Classe base: [`EXP_Value`](../exp_value/)



A collision contact point passed to the collision callbacks.

```python

import Range

def oncollision(object, point, normal, points):
    print("Hit by", object)
    for point in points:
        print(point.localPointA)
        print(point.localPointB)
        print(point.worldPoint)
        print(point.normal)
        print(point.combinedFriction)
        print(point.combinedRestitution)
        print(point.appliedImpulse)

cont = Range.logic.getCurrentController()
own = cont.owner
own.collisionCallbacks = [oncollision]
```

### localPointA

The contact point in the owner object space.

**Tipo:** `mathutils.Vector`

### localPointB

The contact point in the collider object space.

**Tipo:** `mathutils.Vector`

### worldPoint

The contact point in world space.

**Tipo:** `mathutils.Vector`

### normal

The contact normal in owner object space.

**Tipo:** `mathutils.Vector`

### combinedFriction

The combined friction of the owner and collider object.

**Tipo:** float

### combinedRollingFriction

The combined rolling friction of the owner and collider object.

**Tipo:** float

### combinedRestitution

The combined restitution of the owner and collider object.

**Tipo:** float

### appliedImpulse

The applied impulse to the owner object.

**Tipo:** float

