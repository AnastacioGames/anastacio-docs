# KX_PlanarMap

Classe base: [`KX_TextureRenderer`](KX_TextureRenderer.md)

> **Veja também:**
[`KX_CubeMap`](KX_CubeMap.md), [`KX_TextureRenderer`](KX_TextureRenderer.md)

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

## normal

Normal do plano usada para calcular a orientação de reflexão ou refração da câmera de render.

**Tipo:** `mathutils.Vector`
