---
title: "KX_PlanarMap"
description: "Referência da classe Range.types.KX_PlanarMap"
---

Classe base: [`KX_TextureRenderer`](../kx_texturerenderer/)

:::tip[Veja também]
[`KX_CubeMap`](../../types/kx_cubemap/), [`KX_TextureRenderer`](../../types/kx_texturerenderer/)
:::



API Python para texturas de planar map em tempo real.

```python
# Atualiza um espelho só quando precisa.
import Range

own = Range.logic.getCurrentController().owner
mirror = own.meshes[0].materials[0].textures[0].renderer

mirror.autoUpdate = False
mirror.update()
print(mirror.normal)
```

### normal

Normal do plano usada para calcular a orientação de reflexão ou refração da câmera de render.

**Tipo:** `mathutils.Vector`

