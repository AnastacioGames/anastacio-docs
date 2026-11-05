---
title: "Range.track"
description: "Range.track module reference"
---

Baked track data of the Track Tool (`Range.track`, alias `Range.track`).

The editor tool bakes one table per sample of a track layout into the Text datablock
`TRACK_<name>.json` (format version 1, see `docs/plano-track-tool.md`). In the game the engine
reads that Text from the loaded file (and from files loaded with `Range.logic.LibLoad`) the
first time `get` asks for it, keeps it by name and answers the queries in C++.
The results match the pure Python reference `range_track.runtime` (scripts/modules) within 1 mm.

Units are meters and radians. "Left" is the positive lateral side.

```python

import Range

track = Range.track.get("Pista_4")
s, side, dist = track.project(own.worldPosition, near=own.get("track_s"))
own["track_s"] = s
lap_progress = s / track.length
target = track.racingLine(s + 15.0)
```

### get(name)

Track baked in the Text `TRACK_<name>.json` of the game file or of a LibLoaded file.
The Text name itself (`"TRACK_Pista_4.json"`) is accepted too. Read once and cached; the cache
follows LibLoad/LibFree and is cleared when the game ends.

- **`name`**: track name (the name of the track layout object).
  - type: str

**Returns:** the track, or None when there is no such Text.

**Return type:** `Track` or None

**Raises:** the Text is not a valid track (the message says what is wrong).

### names()

Names of the tracks available in the loaded files (Texts `TRACK_*.json`).

**Return type:** list of str

### fromJson(text, name="")

Track built from a JSON string in the baked format (version 1), for data kept elsewhere.

- **`text`**: JSON text.
  - type: str
- **`name`**: name used when the JSON has no `name`.
  - type: str

**Return type:** `Track`

### reload()

Forget the cached tracks: the next `get` reads the Text again.

## Class `Track`

Baked track. Get one with `get`; it stays valid after the file that held it is freed.

Positions may be a `mathutils.Vector` or a sequence of numbers. With only `(x, y)` the
height is ignored; with `z` the height picks the right level on bridges and crossings.
`s` wraps around on a closed circuit and is clamped to `[0, length]` on an open track.

### project(pos, near=None)

Projection of a position on the track.

Pass the `s` of the previous frame as `near` for cars: the search stays within 50 m of it,
so a car never jumps to another stretch of the track that passes close by (hairpins, parallel
straights). When the position is more than 15 m away from that stretch (respawn, teleport)
the whole track is searched, as without `near`.

```python

s, side, dist = track.project(own.worldPosition, near=own.get("track_s"))
own["track_s"] = s
```

**Returns:** `(s, side, dist)`: meters along the track, `1` left / `-1` right of the center line and lateral distance from it (>= 0).

**Return type:** tuple (float, int, float)

### pointAt(s)

Center line point at `s`.

**Return type:** `mathutils.Vector`

### tangentAt(s)

Unit 3D direction of travel at `s`.

**Return type:** `mathutils.Vector`

### lateralAt(s)

Horizontal unit vector to the left at `s`.

**Return type:** `mathutils.Vector`

### bankAt(s)

Banking at `s` in radians (positive: the left edge is lower).

**Return type:** float

### widthAt(s)

Asphalt half widths at `s`.

**Returns:** `(left, right)`

**Return type:** tuple of 2 floats

### edgeAt(s)

Lateral distance of the outer border band (wall, guard rail) at `s`.

**Returns:** `(left, right)`

**Return type:** tuple of 2 floats

### racingLine(s)

Racing line point at `s`, on the banked surface.

**Return type:** `mathutils.Vector`

### isOnRoad(pos)

True when `pos` is over the asphalt (inside the half widths) and up to 3 m from the
surface (height ignored without `z`). Past the start or the end of an open track: False.

**Return type:** bool

### surfaceAt(s)

Surface name of the sample that starts the stretch at `s` (`""` when the track has no
surface names).

**Return type:** str

### name

Track name.

**Type:** str

### length

Track length in meters.

**Type:** float

### cyclic

True for a closed circuit.

**Type:** bool

### count

Number of baked samples.

**Type:** int

### surfaces

Surface names.

**Type:** list of str

