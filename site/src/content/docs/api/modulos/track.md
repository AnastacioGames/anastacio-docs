---
title: "Range.track"
description: "Referência do módulo Range.track"
---

Dados de pista gravados pelo Track Tool (`Range.track`; `bge.track` também funciona).

A ferramenta do editor grava uma tabela por amostra do traçado da pista no Text `TRACK_<name>.json` (formato versão 1, veja `docs/plano-track-tool.md`). No jogo, a engine lê esse Text do arquivo carregado (e dos arquivos carregados com `Range.logic.LibLoad`) na primeira vez que `get` pede por ele, guarda pelo nome e responde as consultas em C++. Os resultados batem com a referência em Python puro `range_track.runtime` (scripts/modules) com diferença de até 1 mm.

As unidades são metros e radianos. "Esquerda" é o lado lateral positivo.

```python

import Range

track = Range.track.get("Pista_4")
s, side, dist = track.project(own.worldPosition, near=own.get("track_s"))
own["track_s"] = s
lap_progress = s / track.length
target = track.racingLine(s + 15.0)
```

### get(name)

Pista gravada no Text `TRACK_<name>.json` do arquivo do jogo ou de um arquivo carregado com LibLoad. O nome do próprio Text (`"TRACK_Pista_4.json"`) também é aceito. Lida uma vez e guardada em cache; o cache acompanha LibLoad/LibFree e é limpo quando o jogo termina.

- **`name`**: nome da pista (o nome do objeto do traçado).
  - tipo: str

**Retorna:** a pista, ou None quando esse Text não existe.

**Tipo do retorno:** `Track` or None

**Erro:** o Text não é uma pista válida (a mensagem diz o que está errado).

### names()

Nomes das pistas disponíveis nos arquivos carregados (Texts `TRACK_*.json`).

**Tipo do retorno:** list of str

### fromJson(text, name="")

Pista montada a partir de um texto JSON no formato gravado (versão 1), para dados guardados em outro lugar.

- **`text`**: texto JSON.
  - tipo: str
- **`name`**: nome usado quando o JSON não tem `name`.
  - tipo: str

**Tipo do retorno:** `Track`

### reload()

Esquece as pistas em cache: o próximo `get` lê o Text de novo.

## Classe `Track`

Pista gravada. Pegue uma com `get`; ela continua válida depois que o arquivo que a continha é liberado.

Posições podem ser um `mathutils.Vector` ou uma sequência de números. Só com `(x, y)` a altura é ignorada; com `z` a altura escolhe o nível certo em pontes e cruzamentos. `s` dá a volta num circuito fechado e fica preso em `[0, length]` numa pista aberta.

### project(pos, near=None)

Projeção de uma posição na pista.

Para carros, passe o `s` do frame anterior como `near`: a busca fica a até 50 m dele, então o carro nunca pula para outro trecho da pista que passa perto (grampos, retas paralelas). Quando a posição está a mais de 15 m desse trecho (respawn, teleporte), a pista inteira é buscada, como sem `near`.

```python

s, side, dist = track.project(own.worldPosition, near=own.get("track_s"))
own["track_s"] = s
```

**Retorna:** `(s, side, dist)`: metros ao longo da pista, `1` à esquerda / `-1` à direita da linha central e a distância lateral até ela (>= 0).

**Tipo do retorno:** tuple (float, int, float)

### pointAt(s)

Ponto da linha central em `s`.

**Tipo do retorno:** `mathutils.Vector`

### tangentAt(s)

Direção 3D unitária do sentido da pista em `s`.

**Tipo do retorno:** `mathutils.Vector`

### lateralAt(s)

Vetor horizontal unitário apontando para a esquerda em `s`.

**Tipo do retorno:** `mathutils.Vector`

### bankAt(s)

Inclinação lateral (banking) em `s`, em radianos (positivo: a borda esquerda fica mais baixa).

**Tipo do retorno:** float

### widthAt(s)

Meias larguras do asfalto em `s`.

**Retorna:** `(left, right)`

**Tipo do retorno:** tuple of 2 floats

### edgeAt(s)

Distância lateral da faixa de borda externa (muro, guard rail) em `s`.

**Retorna:** `(left, right)`

**Tipo do retorno:** tuple of 2 floats

### racingLine(s)

Ponto da linha de corrida em `s`, sobre a superfície inclinada.

**Tipo do retorno:** `mathutils.Vector`

### isOnRoad(pos)

True quando `pos` está sobre o asfalto (dentro das meias larguras) e a até 3 m da superfície (altura ignorada sem `z`). Antes do início ou depois do fim de uma pista aberta: False.

**Tipo do retorno:** bool

### surfaceAt(s)

Nome da superfície da amostra que começa o trecho em `s` (`""` quando a pista não tem nomes de superfície).

**Tipo do retorno:** str

### name

Nome da pista.

**Tipo:** str

### length

Comprimento da pista em metros.

**Tipo:** float

### cyclic

True para um circuito fechado.

**Tipo:** bool

### count

Número de amostras gravadas.

**Tipo:** int

### surfaces

Nomes das superfícies.

**Tipo:** list of str

