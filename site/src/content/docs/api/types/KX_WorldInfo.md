---
title: "KX_WorldInfo"
description: "Referência da classe Range.types.KX_WorldInfo"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



A world object.

```python

# Set the mist color to red.
import Range

sce = Range.logic.getCurrentScene()

sce.world.mistColor = [1.0, 0.0, 0.0]
```

### KX_MIST_QUADRATIC

Type of quadratic attenuation used to fade mist.

### KX_MIST_LINEAR

Type of linear attenuation used to fade mist.

### KX_MIST_INV_QUADRATIC

Type of inverse quadratic attenuation used to fade mist.

### mistEnable

Return the state of the mist.

**Tipo:** bool

### mistStart

The mist start point.

**Tipo:** float

### mistDistance

The mist distance fom the start point to reach 100% mist.

**Tipo:** float

### mistIntensity

The mist intensity.

**Tipo:** float

### mistType

The type of mist - must be KX_MIST_QUADRATIC, KX_MIST_LINEAR or KX_MIST_INV_QUADRATIC

### mistColor

The color of the mist. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0]. Mist and background color sould always set to the same color.

**Tipo:** `mathutils.Color`

### horizonColor

The horizon color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0]. Mist and horizon color should always be set to the same color.

**Tipo:** `mathutils.Vector`

### zenithColor

The zenith color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0].

**Tipo:** `mathutils.Vector`

### ambientColor

The color of the ambient light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].

**Tipo:** `mathutils.Color`

### exposure

Amount of exponential color correction for light.

**Tipo:** float between 0.0 and 1.0 inclusive

### range

The color range that will be mapped to 0 - 1.

**Tipo:** float between 0.2 and 5.0 inclusive

### envLightEnergy

The environment light energy.

**Tipo:** float from 0.0 to infinite

### envLightEnabled

Returns True if Environment Lighting is enabled. Else returns False

**Tipo:** bool (read only)

### envLightColor

White:       returns 0 SkyColor:    returns 1 SkyTexture:  returns 2

**Tipo:** int (read only)

### setWeather(name, value)

Changes a World weather setting at runtime (the "weather." prefix is optional). Booleans: `rain`, `ripples`, `splash`, `puddles`, `puddle_ssr`, `ripple_puddle_only`, `splash_puddle_only` (both also turn `puddles` on), `aura`, `lightning`, `lightning_side`, `clouds`, `lens_flare`, `mist`. Floats: `rain_intensity`, `rain_density`, `rain_speed`, `rain_wind`, `rain_darken`, `rain_streak_width`, `ripple_intensity`, `ripple_normal`, `ripple_size`, `ripple_rate`, `splash_normal`, `splash_min_up`, `splash_size`, `splash_rate`, `splash_intensity`, `splash_distance`, `puddle_amount`, `puddle_size`, `puddle_darkness`, `puddle_reflection`, `puddle_distance`, `puddle_min_up`, `aura_size`, `aura_rate`, `aura_intensity`, `aura_distance`, `lightning_rate`, `lightning_intensity`, `lightning_distance`, `lightning_width`, `cloud_coverage`, `cloud_scale`, `cloud_speed`, `flare_scale`, `flare_intensity`, `mist_*`.

```python

scene.world.setWeather("aura", True)
scene.world.setWeather("splash_size", 1.5)
```

- **`name`**: setting name
  - tipo: string
- **`value`**: new value
  - tipo: bool or float

**Erro:** unknown setting name

### strikeLightning(bolt=True)

Strikes a lightning now (World > Rain must be on; automatic lightning can stay off).

- **`bolt`**: show a bolt; False gives only a far flash behind the clouds
  - tipo: bool

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getWeather(name)

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

current value of a World weather setting (bool or float)

### backgroundColor

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

### sunSize

<span class="ae-badge pendente">sem documentação</span> <small>atributo</small>

