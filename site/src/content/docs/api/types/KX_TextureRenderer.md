---
title: "KX_TextureRenderer"
description: "Referência da classe Range.types.KX_TextureRenderer"
---

Classe base: [`EXP_Value`](../exp_value/)



API Python para objetos que fazem um render guardado numa textura.

```python
# Atualiza um reflexo só a cada alguns quadros para poupar tempo.
import Range

own = Range.logic.getCurrentController().owner
renderer = own.meshes[0].materials[0].textures[0].renderer

renderer.autoUpdate = False
own["frames"] = own.get("frames", 0) + 1

if own["frames"] % 10 == 0:
    renderer.update()
```

```python
# Usa outro ponto de vista e uma distância menor.
import Range

own = Range.logic.getCurrentController().owner
renderer = own.meshes[0].materials[0].textures[0].renderer

renderer.viewpointObject = Range.logic.getCurrentScene().objects["Probe"]
renderer.clipEnd = 50.0
```

### autoUpdate

Define se o texture renderer é atualizado automaticamente a cada frame.

**Tipo:** boolean

### viewpointObject

O objeto de onde o texture renderer vai renderizar a cena.

**Tipo:** `KX_GameObject`

### enabled

Liga o render da cena pelo texture renderer.

**Tipo:** boolean

### ignoreLayers

As layers a ignorar no render.

**Tipo:** bitfield

### clipStart

O plano near da matriz de projeção, usado no culling.

**Tipo:** float

### clipEnd

O plano far da matriz de projeção, usado no culling.

**Tipo:** float

### lodDistanceFactor

Fator que multiplica a distância até a câmera para ajustar os níveis de detalhe. Um valor < 1.0 faz a distância usada para calcular os níveis de detalhe diminuir.

**Tipo:** float

### update()

Pede para atualizar este texture renderer na etapa de render. Só tem efeito quando `autoUpdate` está desligado.

