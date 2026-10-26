---
title: "TrackLine"
description: "Referência da classe Range.types.TrackLine"
---

Polilinha fechada para IA de corrida, calculada em C++. Diz quanto da pista o carro já percorreu, dá o ponto e o lado da pista a uma distância e guarda perfis por ponto (curvatura, velocidade segura). Monte uma vez por pista e compartilhe entre os carros.

A linha é fechada: o último ponto liga no primeiro. `s` é a distância em metros desde o primeiro ponto e dá a volta, então `s` maior que `length` ou negativo funciona.

```python

import Range
from mathutils import Vector

points = curve.getCurvePoints()        # ou o centro da malha da estrada
line = Range.types.TrackLine(points)

d2, s, seg = line.locate(car.worldPosition)               # busca global
d2, s, seg = line.locate(car.worldPosition, seg, 15, 40, 20.0)  # perto do último segmento
target = line.point(s + 12.0)          # 12 m à frente
right = line.side(s)                   # vetor unitário para a direita, ou None
```

- **`points`**: pelo menos 3 pontos (`mathutils.Vector` ou sequências de 3 números).
  - tipo: sequence

### length

Comprimento total da linha fechada, em metros (só leitura).

**Tipo:** float

### locate(pos, seg=-1, back=0, ahead=0, lost=0.0)

Segmento da linha mais perto de `pos`.

Com `seg` >= 0 só os segmentos de `seg - back` a `seg + ahead` são testados, o que evita pular para um trecho vizinho da pista. Quando esse resultado fica a mais de `lost` metros (respawn, atalho), ou com `seg` = -1, a linha inteira é procurada.

- **`pos`**: posição em coordenadas do mundo.
  - tipo: `mathutils.Vector`
- **`seg`**: segmento da chamada anterior, -1 se desconhecido.
  - tipo: integer
- **`back`**: segmentos testados atrás de `seg`.
  - tipo: integer
- **`ahead`**: segmentos testados à frente de `seg`.
  - tipo: integer
- **`lost`**: distância em metros que dispara a busca global.
  - tipo: float

**Retorna:** (distância ao quadrado até a linha, `s` em metros, índice do segmento).

**Tipo do retorno:** tuple (float, float, integer)

### point(s)

Ponto da linha a `s` metros do início.

**Tipo do retorno:** `mathutils.Vector`

### side(s)

Vetor horizontal unitário apontando para a direita da linha em `s`, ou None onde a linha é vertical ou degenerada.

**Tipo do retorno:** `mathutils.Vector` or None

### setProfile(name, values)

Guarda um valor por ponto com o nome `name` (curvatura, velocidade segura, qualquer número).

- **`name`**: nome do perfil.
  - tipo: string
- **`values`**: um número por ponto da linha.
  - tipo: sequence of float

### profile(name, s)

Valor do perfil `name` interpolado em `s` metros.

**Tipo do retorno:** float

