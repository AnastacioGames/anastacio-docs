---
title: "BL_Texture"
description: "Referência da classe Range.types.BL_Texture"
---

Classe base: [`EXP_Value`](../exp_value/)



Um objeto de textura com os atributos de uma textura de material.

### diffuseIntensity

Quanto a textura afeta a refletividade difusa.

**Tipo:** float

### diffuseFactor

Quanto a textura afeta a cor difusa.

**Tipo:** float

### alpha

Quanto a textura afeta o alpha.

**Tipo:** float

### specularIntensity

Quanto a textura afeta a refletividade especular.

**Tipo:** float

### specularFactor

Quanto a textura afeta a cor especular.

**Tipo:** float

### hardness

Quanto a textura afeta a hardness.

**Tipo:** float

### emit

Quanto a textura afeta a emissão.

**Tipo:** float

### mirror

Quanto a textura afeta a cor de espelho.

**Tipo:** float

### normal

Quanto a textura afeta os valores de normal.

**Tipo:** float

### parallaxBump

Altura do parallax occlusion mapping.

**Tipo:** float

### parallaxStep

Número de passos para fazer o efeito de parallax.

**Tipo:** float

### lodBias

Bias aplicado ao mipmapping.

**Tipo:** float

### bindCode

Bind code/Id/número da textura.

**Tipo:** integer

### renderer

Texture renderer desta textura.

**Tipo:** `KX_CubeMap`, `KX_PlanarMap` or None

### ior

Índice de refração usado para calcular a refração.

**Tipo:** float (1.0 to 50.0)

### refractionRatio

Quanto da refração é misturada com a reflexão.

**Tipo:** float (0.0 to 1.0)

### uvOffset

Deslocamento aplicado às coordenadas UV da textura (principalmente translação nos eixos U e V).

**Tipo:** `mathutils.Vector`

### uvSize

Escala aplicada às coordenadas UV da textura.

**Tipo:** `mathutils.Vector`

### uvRotation

Rotação aplicada às coordenadas UV da textura.

**Tipo:** float (radians)

