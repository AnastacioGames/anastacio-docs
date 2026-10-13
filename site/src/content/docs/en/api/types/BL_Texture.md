---
title: "BL_Texture"
description: "Range.types.BL_Texture class reference"
---

Base class: [`EXP_Value`](../exp_value/)



A texture object that contains attributes of a material texture.

### diffuseIntensity

Amount texture affects diffuse reflectivity.

**Type:** float

### diffuseFactor

Amount texture affects diffuse color.

**Type:** float

### alpha

Amount texture affects alpha.

**Type:** float

### specularIntensity

Amount texture affects specular reflectivity.

**Type:** float

### specularFactor

Amount texture affects specular color.

**Type:** float

### hardness

Amount texture affects hardness.

**Type:** float

### emit

Amount texture affects emission.

**Type:** float

### mirror

Amount texture affects mirror color.

**Type:** float

### normal

Amount texture affects normal values.

**Type:** float

### parallaxBump

Height of parallax occlusion mapping.

**Type:** float

### parallaxStep

Number of steps to achieve parallax effect.

**Type:** float

### lodBias

Amount bias on mipmapping.

**Type:** float

### bindCode

Texture bind code/Id/number.

**Type:** integer

### renderer

Texture renderer of this texture.

**Type:** `KX_CubeMap`, `KX_PlanarMap` or None

### ior

Index Of Refraction used to compute refraction.

**Type:** float (1.0 to 50.0)

### refractionRatio

Amount refraction mixed with reflection.

**Type:** float (0.0 to 1.0)

### uvOffset

Offset applied to texture UV coordinates (mainly translation on U and V axis).

**Type:** `mathutils.Vector`

### uvSize

Scale applied to texture UV coordinates.

**Type:** `mathutils.Vector`

### uvRotation

Rotation applied to texture UV coordinates.

**Type:** float (radians)

