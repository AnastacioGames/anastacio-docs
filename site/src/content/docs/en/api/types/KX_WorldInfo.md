---
title: "KX_WorldInfo"
description: "Range.types.KX_WorldInfo class reference"
---

Base class: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)

:::tip[See also]
[`KX_Scene`](../../types/kx_scene/), [`KX_LightObject`](../../types/kx_lightobject/), [`KX_Camera`](../../types/kx_camera/)
:::



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

**Type:** bool

### mistStart

The mist start point.

**Type:** float

### mistDistance

The mist distance fom the start point to reach 100% mist.

**Type:** float

### mistIntensity

The mist intensity.

**Type:** float

### mistType

The type of mist - must be KX_MIST_QUADRATIC, KX_MIST_LINEAR or KX_MIST_INV_QUADRATIC

### mistColor

The color of the mist. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
Mist and background color sould always set to the same color.

**Type:** `mathutils.Color`

### horizonColor

The horizon color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0].
Mist and horizon color should always be set to the same color.

**Type:** `mathutils.Vector`

### zenithColor

The zenith color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0].

**Type:** `mathutils.Vector`

### ambientColor

The color of the ambient light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].

**Type:** `mathutils.Color`

### exposure

Amount of exponential color correction for light.

**Type:** float between 0.0 and 1.0 inclusive

### range

The color range that will be mapped to 0 - 1.

**Type:** float between 0.2 and 5.0 inclusive

### envLightEnergy

The environment light energy.

**Type:** float from 0.0 to infinite

### envLightEnabled

Returns True if Environment Lighting is enabled. Else returns False

**Type:** bool (read only)

### envLightColor

White:       returns 0
SkyColor:    returns 1
SkyTexture:  returns 2

**Type:** int (read only)

### setWeather(name, value)

Changes a World weather setting at runtime (the "weather." prefix is optional).
Booleans: `rain`, `ripples`, `splash`, `puddles`, `puddle_ssr`, `ripple_puddle_only`, `splash_puddle_only` (both also turn `puddles` on), `aura`, `lightning`, `lightning_side`, `clouds`, `lens_flare`, `mist`.
Floats: `rain_intensity`, `rain_density`, `rain_speed`, `rain_wind`, `rain_darken`,
`rain_streak_width`, `ripple_intensity`, `ripple_normal`, `ripple_size`, `ripple_rate`, `splash_normal`, `splash_min_up`, `splash_size`, `splash_rate`, `splash_intensity`,
`splash_distance`, `puddle_amount`, `puddle_size`, `puddle_darkness`, `puddle_reflection`,
`puddle_distance`, `puddle_min_up`, `aura_size`, `aura_rate`, `aura_intensity`, `aura_distance`,
`lightning_rate`, `lightning_intensity`, `lightning_distance`, `lightning_width`,
`cloud_coverage`, `cloud_scale`, `cloud_speed`, `flare_scale`, `flare_intensity`, `mist_*`.

Clouds, Sky Layers and Volumetric Clouds (the toggles need the clouds pass, built at load when any of
the three is enabled in the World): booleans `use_sky_layers`, `use_volumetric_clouds`,
`vcloud_shadow_enable`; integers `cloud_detail` (1-8), `vcloud_quality` (0 Low, 1 Medium, 2 High);
floats `cloud_color_r/_g/_b`, `vcloud_coverage`, `vcloud_scale`, `vcloud_speed`,
`vcloud_altitude`, `vcloud_thickness`, `vcloud_density`, `vcloud_detail_scale`,
`vcloud_silver_intensity`, `vcloud_shadow_strength`, `vcloud_color_r/_g/_b`.

Fog - Volumetric: booleans `vfog`, `vfog_use_lamps`, `vfog_use_shafts`, `vfog_use_sun_shafts`,
`vfog_volumes_only`, `vfog_use_wind`, `vfog_use_time_of_day`, `vfog_use_layer`,
`vfog_use_reach_clouds`; integers `vfog_quality` (0 Low, 1 Medium, 2 High), `vfog_max_lights` (1-8);
floats `vfog_density`, `vfog_base`, `vfog_falloff`, `vfog_distance`, `vfog_noise_scale`,
`vfog_noise_amount`, `vfog_speed`, `vfog_anisotropy`, `vfog_edge`, `vfog_light_intensity`,
`vfog_sun_intensity`, `vfog_shaft_intensity`, `vfog_ambient`, `vfog_morning_boost`,
`vfog_wind_direction` (degrees), `vfog_dust` (0-1, motes in the light beams), `vfog_color_r/_g/_b`. The fog resolution is fixed at load.

```python

scene.world.setWeather("aura", True)
scene.world.setWeather("splash_size", 1.5)
```

- **`name`**: setting name
  - type: string
- **`value`**: new value
  - type: bool or float

**Raises:** unknown setting name

### strikeLightning(bolt=True)

Strikes a lightning now (World > Rain must be on; automatic lightning can stay off).

- **`bolt`**: show a bolt; False gives only a far flash behind the clouds
  - type: bool

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### getWeather(name)

<span class="ae-badge novo">new in Anastacio</span> <small>method</small>

current value of a World weather setting (bool or float)

### atmosphereAltitude

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Observer altitude in the atmosphere.

### atmosphereIntensity

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Intensity of the atmospheric sky.

### atmosphereMieDensity

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Mie scattering density (haze and halo around the sun).

### atmosphereMieDirection

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Mie scattering direction: how much the glow concentrates near the sun.

### atmosphereRayleighColor

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Rayleigh scattering color (the blue of the sky), as `[r, g, b]`. Negative values become 0.

### atmosphereRayleighDensity

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Rayleigh scattering density.

### auroraColors

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Aurora color palette: `'GREEN'`, `'CLASSIC'` or `'SHIFTING'`.

### backgroundColor

 <small>attribute</small>

World background color `[r, g, b]`.

### moonBrightness

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Moon brightness.

### moonSize

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Size of the moon in the sky.

### skyType

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

World sky type: `'FLAT'`, `'GRADIENT'`, `'PROCEDURAL'` or `'ATMOSPHERIC'`. Changing it recompiles the world shader on the next frame; object materials keep the sky type they were compiled with.

### starStyle

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Star style: `'SIMPLE'`, `'REALISTIC'` or `'CONSTELLATIONS'`.

### sunSize

 <small>attribute</small>

Size of the sun in the sky (0 to 1).

### useSkyAurora

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns the aurora in the sky on or off.

### useSkyMoon

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns the moon in the sky on or off. Changes immediately, without recompiling the shader.

### useSkyStars

<span class="ae-badge novo">new in Anastacio</span> <small>attribute</small>

Turns the stars in the sky on or off.

