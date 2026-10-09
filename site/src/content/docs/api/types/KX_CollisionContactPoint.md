---
title: "KX_CollisionContactPoint"
description: "Referência da classe Range.types.KX_CollisionContactPoint"
---

Classe base: [`EXP_Value`](../exp_value/)



Um ponto de contato de colisão passado aos callbacks de colisão.

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

O ponto de contato no espaço do objeto dono.

**Tipo:** `mathutils.Vector`

### localPointB

O ponto de contato no espaço do objeto colisor.

**Tipo:** `mathutils.Vector`

### worldPoint

O ponto de contato no espaço do mundo.

**Tipo:** `mathutils.Vector`

### normal

A normal do contato no espaço do objeto dono.

**Tipo:** `mathutils.Vector`

### combinedFriction

O atrito combinado do objeto dono e do colisor.

**Tipo:** float

### combinedRollingFriction

O atrito de rolagem combinado do objeto dono e do colisor.

**Tipo:** float

### combinedRestitution

A restituição combinada do objeto dono e do colisor.

**Tipo:** float

### appliedImpulse

O impulso aplicado ao objeto dono.

**Tipo:** float

