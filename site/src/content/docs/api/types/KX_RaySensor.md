---
title: "KX_RaySensor"
description: "Referência da classe Range.types.KX_RaySensor"
---

Classe base: [`SCA_ISensor`](../sca_isensor/)



Um sensor Ray detecta o primeiro objeto numa direção.

### propName

A propriedade que o raio procura.

**Tipo:** string

### range

A distância do raio.

**Tipo:** float

### useMaterial

Se procura um material ou não (false = propriedade).

**Tipo:** boolean

### useXRay

Se usa XRay ou não.

**Tipo:** boolean

### mask

A máscara de colisão (16 layers mapeadas num inteiro de 16 bits) combinada com o grupo de colisão de cada objeto, para atingir só parte dos objetos da cena. Só os objetos em que `collisionGroup & mask` é verdadeiro podem ser atingidos.

**Tipo:** bitfield

### hitObject

O game object atingido pelo raio (somente leitura).

**Tipo:** `KX_GameObject`

### hitPosition

A posição (em coordenadas do mundo) em que o objeto foi atingido pelo raio (somente leitura).

**Tipo:** `mathutils.Vector`

### hitNormal

A normal (em coordenadas do mundo) do objeto no ponto em que foi atingido pelo raio (somente leitura).

**Tipo:** `mathutils.Vector`

### hitMaterial

O material do objeto na face atingida pelo raio (somente leitura).

**Tipo:** string

### rayDirection

A direção do raio (em coordenadas do mundo) (somente leitura).

**Tipo:** `mathutils.Vector`

### axis

O eixo para onde o raio aponta.

**Tipo:** integer from 0 to 5

* KX_RAY_AXIS_POS_X
* KX_RAY_AXIS_POS_Y
* KX_RAY_AXIS_POS_Z
* KX_RAY_AXIS_NEG_X
* KX_RAY_AXIS_NEG_Y
* KX_RAY_AXIS_NEG_Z

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### gazeAngle

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

### gazeProgress

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

### gazeTime

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

