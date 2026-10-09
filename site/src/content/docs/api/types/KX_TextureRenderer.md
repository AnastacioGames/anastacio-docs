---
title: "KX_TextureRenderer"
description: "Referência da classe Range.types.KX_TextureRenderer"
---

Classe base: [`EXP_Value`](../exp_value/)



Python API for object doing a render stored in a texture.

### autoUpdate

Choose to update automatically each frame the texture renderer or not.

**Tipo:** boolean

### viewpointObject

The object where the texture renderer will render the scene.

**Tipo:** `KX_GameObject`

### enabled

Enable the texture renderer to render the scene.

**Tipo:** boolean

### ignoreLayers

The layers to ignore when rendering.

**Tipo:** bitfield

### clipStart

The projection view matrix near plane, used for culling.

**Tipo:** float

### clipEnd

The projection view matrix far plane, used for culling.

**Tipo:** float

### lodDistanceFactor

The factor to multiply distance to camera to adjust levels of detail. A float < 1.0f will make the distance to camera used to compute levels of detail decrease.

**Tipo:** float

### update()

Request to update this texture renderer during the rendering stage. This function is effective only when `autoUpdate` is disabled.

