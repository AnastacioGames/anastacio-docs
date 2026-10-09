---
title: "KX_CollisionSensor"
description: "Referência da classe Range.types.KX_CollisionSensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



O sensor de colisão detecta colisões entre objetos.

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

