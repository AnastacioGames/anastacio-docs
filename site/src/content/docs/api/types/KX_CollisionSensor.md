---
title: "KX_CollisionSensor"
description: "Referência da classe Range.types.KX_CollisionSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



O sensor de colisão detecta colisões entre objetos.

```python
# Mostra o que bateu no objeto.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Collision"]

if sensor.positive:
    for obj in sensor.hitObjectList:
        print(obj.name)
```

```python
# Só detecta objetos com a propriedade coin.
import Range

sensor = Range.logic.getCurrentController().sensors["Collision"]

sensor.propName = "coin"
sensor.useMaterial = False
```

### propName

A propriedade ou o material com que colidir.

**Tipo:** string

### useMaterial

Define se o sensor procura uma propriedade ou um material. KX_True = procura material; KX_False = procura propriedade.

**Tipo:** boolean

### usePulseCollision

Quando ligado, mudanças no conjunto de objetos em colisão geram um pulso.

**Tipo:** boolean

### hitObject

O último objeto que colidiu (somente leitura).

**Tipo:** `KX_GameObject` or None

### hitObjectList

Uma lista dos objetos em colisão (somente leitura).

**Tipo:** `EXP_ListValue` of `KX_GameObject`

### hitMaterial

O material do objeto na face atingida pelo raio (somente leitura).

**Tipo:** string

