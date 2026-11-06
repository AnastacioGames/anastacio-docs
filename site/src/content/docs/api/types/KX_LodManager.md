---
title: "KX_LodManager"
description: "Referência da classe Range.types.KX_LodManager"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Esta classe tem a lista de todos os níveis de detalhe usados por um game object.

```python

# Opção gráfica: valores acima de 1.0 trocam mais cedo para os níveis simples.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    obj.lodManager.distanceFactor = 2.0
```

```python

# Usa os mesmos níveis de detalhe em outro objeto.
import Range

scene = Range.logic.getCurrentScene()
scene.objects["TreeB"].lodManager = scene.objects["TreeA"].lodManager
```

```python

# Troca também a malha de física quando o nível muda.
import Range

obj = Range.logic.getCurrentController().owner

if obj.lodManager is not None:
    obj.lodManager.updatePhysics = True
```

### levels

Devolve a lista de todos os níveis de detalhe do lod manager.

**Tipo:** list of `KX_LodLevel`

### distanceFactor

Multiplicador da distância até a câmera.

**Tipo:** float

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### updatePhysics

 <small>atributo</small>

Também troca a malha de física quando o nível de detalhe (LOD) muda.

