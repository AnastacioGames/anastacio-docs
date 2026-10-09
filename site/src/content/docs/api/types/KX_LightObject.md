---
title: "KX_LightObject"
description: "Referência da classe Range.types.KX_LightObject"
---

Classe base: [`KX_GameObject`](../kx_gameobject/)



A Light object.

```python

# Turn on a red alert light.
import Range

co = Range.logic.getCurrentController()
light = co.owner

light.energy = 1.0
light.color = [1.0, 0.0, 0.0]
```

### SPOT

A spot light source. See attribute `type`

### SUN

A point light source with no attenuation. See attribute `type`

### NORMAL

A point light source. See attribute `type`

### HEMI

A hemi light source. See attribute `type`

### type

The type of light - must be SPOT, SUN or NORMAL

### energy

The brightness of this light.

**Tipo:** float

### shadowClipStart

The shadowmap clip start, below which objects will not generate shadows.

**Tipo:** float (read only)

### shadowClipEnd

The shadowmap clip end, beyond which objects will not generate shadows.

**Tipo:** float (read only)

### shadowFrustumSize

Size of the frustum used for creating the shadowmap.

**Tipo:** float (read only)

### shadowBindId

The OpenGL shadow texture bind number/id.

**Tipo:** int (read only)

### shadowMapType

The shadow shadow map type (0 -> Simple; 1 -> Variance)

**Tipo:** int (read only)

### shadowBias

The shadow buffer sampling bias.

**Tipo:** float (read only)

### shadowBleedBias

The bias for reducing light-bleed on variance shadow maps.

**Tipo:** float (read only)

### useShadow

Returns True if the light has Shadow option activated, else returns False.

**Tipo:** boolean (read only)

### shadowColor

The color of this light shadows. Black = (0.0, 0.0, 0.0), White = (1.0, 1.0, 1.0).

**Tipo:** `mathutils.Color` (read only)

### shadowMatrix

Matrix that converts a vector in camera space to shadow buffer depth space.

Computed as: mat4_perspective_to_depth * mat4_lamp_to_perspective * mat4_world_to_lamp * mat4_cam_to_world.

mat4_perspective_to_depth is a fixed matrix defined as follow:

0.5 0.0 0.0 0.5 0.0 0.5 0.0 0.5 0.0 0.0 0.5 0.5 0.0 0.0 0.0 1.0

.. note:

There is one matrix of that type per lamp casting shadow in the scene.

**Tipo:** Matrix4x4 (read only)

### distance

The maximum distance this light can illuminate. (SPOT and NORMAL lights only).

**Tipo:** float

### color

The color of this light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].

**Tipo:** list [r, g, b]

### lin_attenuation

The linear component of this light's attenuation. (SPOT and NORMAL lights only).

**Tipo:** float

### quad_attenuation

The quadratic component of this light's attenuation (SPOT and NORMAL lights only).

**Tipo:** float

### spotsize

The cone angle of the spot light, in degrees (SPOT lights only).

**Tipo:** float in [0 - 180].

### spotblend

Specifies the intensity distribution of the spot light (SPOT lights only).

**Tipo:** float in [0 - 1]

:::note
Higher values result in a more focused light source.
:::

### staticShadow

Enables static shadows. By default (staticShadow=False) the shadow cast by the lamp is recalculated every frame. When this is not needed, set staticShadow=True. In that case, call :py`updateShadow` to request a shadow update.

**Tipo:** boolean.

### updateShadow()

Set the shadow to be updated next frame if the lamp uses a static shadow, see `staticShadow`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### autoShadowUpdate

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

