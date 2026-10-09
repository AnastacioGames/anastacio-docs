---
title: "BL_Texture"
description: "Referência da classe Range.types.BL_Texture"
---

Classe base: [`EXP_Value`](../exp_value/)



A texture object that contains attributes of a material texture.

### diffuseIntensity

Amount texture affects diffuse reflectivity.

**Tipo:** float

### diffuseFactor

Amount texture affects diffuse color.

**Tipo:** float

### alpha

Amount texture affects alpha.

**Tipo:** float

### specularIntensity

Amount texture affects specular reflectivity.

**Tipo:** float

### specularFactor

Amount texture affects specular color.

**Tipo:** float

### hardness

Amount texture affects hardness.

**Tipo:** float

### emit

Amount texture affects emission.

**Tipo:** float

### mirror

Amount texture affects mirror color.

**Tipo:** float

### normal

Amount texture affects normal values.

**Tipo:** float

### parallaxBump

Height of parallax occlusion mapping.

**Tipo:** float

### parallaxStep

Number of steps to achieve parallax effect.

**Tipo:** float

### lodBias

Amount bias on mipmapping.

**Tipo:** float

### bindCode

Texture bind code/Id/number.

**Tipo:** integer

### renderer

Texture renderer of this texture.

**Tipo:** `KX_CubeMap`, `KX_PlanarMap` or None

### ior

Index Of Refraction used to compute refraction.

**Tipo:** float (1.0 to 50.0)

### refractionRatio

Amount refraction mixed with reflection.

**Tipo:** float (0.0 to 1.0)

### uvOffset

Offset applied to texture UV coordinates (mainly translation on U and V axis).

**Tipo:** `mathutils.Vector`

### uvSize

Scale applied to texture UV coordinates.

**Tipo:** `mathutils.Vector`

### uvRotation

Rotation applied to texture UV coordinates.

**Tipo:** float (radians)

