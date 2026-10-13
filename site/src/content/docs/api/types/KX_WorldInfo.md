---
title: "KX_WorldInfo"
description: "Referência da classe Range.types.KX_WorldInfo"
---

Classe base: [`EXP_PyObjectPlus`](../exp_pyobjectplus/)



Um objeto de mundo.

```python

# Deixa a cor da névoa vermelha.
import Range

sce = Range.logic.getCurrentScene()

sce.world.mistColor = [1.0, 0.0, 0.0]
```

### KX_MIST_QUADRATIC

Tipo de atenuação quadrática usada para esmaecer a névoa.

### KX_MIST_LINEAR

Tipo de atenuação linear usada para esmaecer a névoa.

### KX_MIST_INV_QUADRATIC

Tipo de atenuação quadrática inversa usada para esmaecer a névoa.

### mistEnable

Devolve o estado da névoa.

**Tipo:** bool

### mistStart

O ponto de início da névoa.

**Tipo:** float

### mistDistance

A distância, a partir do ponto de início, para a névoa chegar a 100%.

**Tipo:** float

### mistIntensity

A intensidade da névoa.

**Tipo:** float

### mistType

O tipo de névoa: deve ser KX_MIST_QUADRATIC, KX_MIST_LINEAR ou KX_MIST_INV_QUADRATIC

### mistColor

A cor da névoa. Preto = [0.0, 0.0, 0.0], branco = [1.0, 1.0, 1.0]. A névoa e a cor de fundo devem ter sempre a mesma cor.

**Tipo:** `mathutils.Color`

### horizonColor

A cor do horizonte. Preto = [0.0, 0.0, 0.0, 1.0], branco = [1.0, 1.0, 1.0, 1.0]. A névoa e a cor do horizonte devem ter sempre a mesma cor.

**Tipo:** `mathutils.Vector`

### zenithColor

A cor do zênite. Preto = [0.0, 0.0, 0.0, 1.0], branco = [1.0, 1.0, 1.0, 1.0].

**Tipo:** `mathutils.Vector`

### ambientColor

A cor da luz ambiente. Preto = [0.0, 0.0, 0.0], branco = [1.0, 1.0, 1.0].

**Tipo:** `mathutils.Color`

### exposure

Quantidade de correção de cor exponencial da luz.

**Tipo:** float between 0.0 and 1.0 inclusive

### range

O intervalo de cor que será mapeado para 0 - 1.

**Tipo:** float between 0.2 and 5.0 inclusive

### envLightEnergy

A energia da luz de ambiente.

**Tipo:** float from 0.0 to infinite

### envLightEnabled

Devolve True se Environment Lighting estiver ligado; senão, False

**Tipo:** bool (read only)

### envLightColor

White: devolve 0 SkyColor: devolve 1 SkyTexture: devolve 2

**Tipo:** int (read only)

### setWeather(name, value)

Muda uma configuração de clima do World em tempo de execução (o prefixo "weather." é opcional). Booleanos: `rain`, `ripples`, `splash`, `puddles`, `puddle_ssr`, `ripple_puddle_only`, `splash_puddle_only` (os dois também ligam `puddles`), `aura`, `lightning`, `lightning_side`, `clouds`, `lens_flare`, `mist`. Floats: `rain_intensity`, `rain_density`, `rain_speed`, `rain_wind`, `rain_darken`, `rain_streak_width`, `ripple_intensity`, `ripple_normal`, `ripple_size`, `ripple_rate`, `splash_normal`, `splash_min_up`, `splash_size`, `splash_rate`, `splash_intensity`, `splash_distance`, `puddle_amount`, `puddle_size`, `puddle_darkness`, `puddle_reflection`, `puddle_distance`, `puddle_min_up`, `aura_size`, `aura_rate`, `aura_intensity`, `aura_distance`, `lightning_rate`, `lightning_intensity`, `lightning_distance`, `lightning_width`, `cloud_coverage`, `cloud_scale`, `cloud_speed`, `flare_scale`, `flare_intensity`, `mist_*`.

Nuvens, Sky Layers e Nuvens Volumétricas (as chaves de ligar precisam do passe de nuvens, criado no carregamento quando qualquer um dos três está ligado no World): booleanos `use_sky_layers`, `use_volumetric_clouds`, `vcloud_shadow_enable`; inteiros `cloud_detail` (1-8), `vcloud_quality` (0 Low, 1 Medium, 2 High); floats `cloud_color_r/_g/_b`, `vcloud_coverage`, `vcloud_scale`, `vcloud_speed`, `vcloud_altitude`, `vcloud_thickness`, `vcloud_density`, `vcloud_detail_scale`, `vcloud_silver_intensity`, `vcloud_shadow_strength`, `vcloud_color_r/_g/_b`.

Fog - Volumetric: booleanos `vfog`, `vfog_use_lamps`, `vfog_use_shafts`, `vfog_use_sun_shafts`, `vfog_volumes_only`, `vfog_use_wind`, `vfog_use_time_of_day`, `vfog_use_layer`, `vfog_use_reach_clouds`; inteiros `vfog_quality` (0 Low, 1 Medium, 2 High), `vfog_max_lights` (1-8); floats `vfog_density`, `vfog_base`, `vfog_falloff`, `vfog_distance`, `vfog_noise_scale`, `vfog_noise_amount`, `vfog_speed`, `vfog_anisotropy`, `vfog_edge`, `vfog_light_intensity`, `vfog_sun_intensity`, `vfog_shaft_intensity`, `vfog_ambient`, `vfog_morning_boost`, `vfog_wind_direction` (graus), `vfog_dust` (0-1, partículas de poeira nos feixes de luz), `vfog_color_r/_g/_b`. A resolução da neblina é fixa no carregamento.

```python

scene.world.setWeather("aura", True)
scene.world.setWeather("splash_size", 1.5)
```

- **`name`**: nome da configuração
  - tipo: string
- **`value`**: novo valor
  - tipo: bool or float

**Erro:** nome de configuração desconhecido

### strikeLightning(bolt=True)

Dispara um raio agora (World > Rain precisa estar ligado; os raios automáticos podem ficar desligados).

- **`bolt`**: mostra o raio; False dá só um clarão distante atrás das nuvens
  - tipo: bool

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getWeather(name)

<span class="ae-badge novo">novo na Anastacio</span> <small>método</small>

valor atual de uma configuração de clima do World (bool ou float)

### atmosphereAltitude

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Altitude do observador na atmosfera.

### atmosphereIntensity

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Intensidade do céu atmosférico.

### atmosphereMieDensity

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Densidade do espalhamento Mie (névoa e halo em volta do sol).

### atmosphereMieDirection

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Direção do espalhamento Mie: quanto o brilho se concentra perto do sol.

### atmosphereRayleighColor

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Cor do espalhamento Rayleigh (o azul do céu), como `[r, g, b]`. Valores negativos viram 0.

### atmosphereRayleighDensity

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Densidade do espalhamento Rayleigh.

### auroraColors

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Paleta de cores da aurora: `'GREEN'`, `'CLASSIC'` ou `'SHIFTING'`.

### backgroundColor

 <small>atributo</small>

Cor de fundo `[r, g, b]` do World.

### moonBrightness

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Brilho da lua.

### moonSize

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tamanho da lua no céu.

### skyType

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tipo de céu do World: `'FLAT'`, `'GRADIENT'`, `'PROCEDURAL'` ou `'ATMOSPHERIC'`. Mudar recompila o shader do world no frame seguinte; materiais de objetos mantêm o tipo de céu com que foram compilados.

### starStyle

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Estilo das estrelas: `'SIMPLE'`, `'REALISTIC'` ou `'CONSTELLATIONS'`.

### sunSize

 <small>atributo</small>

Tamanho do sol no céu (0 a 1).

### useSkyAurora

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga ou desliga a aurora no céu.

### useSkyMoon

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga ou desliga a lua no céu. Muda na hora, sem recompilar o shader.

### useSkyStars

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Liga ou desliga as estrelas no céu.

