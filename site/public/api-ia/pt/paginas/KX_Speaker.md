# KX_Speaker

> **Veja também:**
[`KX_SoundActuator`](KX_SoundActuator.md), [`KX_Scene`](KX_Scene.md)

Classe `Range.types.KX_Speaker`.

```python
# Controla um speaker da cena.
import Range

scene = Range.logic.getCurrentScene()

for speaker in scene.speakers:
    speaker.volume = 0.5
    speaker.pitch = 1.0
    speaker.Play()
```

```python
# Pausa, recomeça ou para.
import Range

speaker = Range.logic.getCurrentScene().speakers[0]

speaker.Pause()
speaker.Restart()
speaker.Stop()
```

```python
# Som que abaixa com a distância.
import Range

speaker = Range.logic.getCurrentScene().speakers[0]

speaker.distance_reference = 2.0
speaker.distance_maximum = 40.0
speaker.attenuation = 1.0
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### GetActiveEffect()

 `método`

Efeito de som ativo: 0 nenhum, 1 reverb.

**Retorna:** `int`

### GetActiveEffectFilter()

 `método`

Filtro ativo: 0 nenhum, 1 passa-baixa, 2 passa-alta, 3 passa-banda.

**Retorna:** `int`

### Pause()

 `método`

Pausa o som.

### Play()

 `método`

Toca o som.

### RemoveEffect()

 `método`

Remove o efeito de som.

### Restart()

 `método`

Toca o som desde o começo.

### SetEffect(effectType, filterType=0)

 `método`

Aplica um efeito: `effectType` 1 = reverb; `filterType` 0 nenhum, 1 passa-baixa, 2 passa-alta, 3 passa-banda. Depois disso as áreas de reverb deixam este Speaker em paz.

### SetSound(sound, cache=False)

 `método`

Troca o som (um `aud.Sound`). Com `cache=True`, guarda o som decodificado na memória.

### Stop()

 `método`

Para o som.

### attenuation

 `atributo`

Quanto o volume cai com a distância (som 3D).

### catkey

 `atributo`

Chave da categoria de som no gerenciador de reprodução, ou `None`.

### cone_angle_inner

 `atributo`

Ângulo, em graus, do cone em que o som toca no volume cheio.

### cone_angle_outer

 `atributo`

Ângulo, em graus, do cone fora do qual o volume é `cone_volume_outer`.

### cone_volume_outer

 `atributo`

Volume fora do cone externo.

### distance_maximum

 `atributo`

Distância a partir da qual o volume para de cair.

### distance_reference

 `atributo`

Distância em que o som toca no volume normal.

### filter_gain

 `atributo`

Ganho geral do filtro.

### filter_gainhf

 `atributo`

Ganho das frequências altas no filtro.

### filter_gainlf

 `atributo`

Ganho das frequências baixas no filtro.

### is3D

 `atributo · só leitura`

`True` se o som é posicional (3D).

### mode

 `atributo`

Modo de reprodução: 1 toca até o fim, 2 repete, 3 repete indo e voltando.

### pitch

 `atributo`

Tom (velocidade) do som. 1.0 é normal.

### playbackManager

 `atributo`

Gerenciador de reprodução (`aud.PlaybackManager`) usado pelo Speaker, ou `None`.

### reverb_air_absorption_gain_hf

 `atributo`

Reverb: absorção das altas frequências pelo ar.

### reverb_decay_hf_ratio

 `atributo`

Reverb: quanto as altas frequências somem mais rápido que as baixas.

### reverb_decay_limit_hf

 `atributo`

Reverb: limita o decaimento das altas frequências.

### reverb_decay_time

 `atributo`

Reverb: tempo, em segundos, que o eco leva para sumir.

### reverb_density

 `atributo`

Reverb: densidade dos ecos.

### reverb_diffusion

 `atributo`

Reverb: espalhamento dos ecos.

### reverb_gain

 `atributo`

Reverb: volume geral do efeito.

### reverb_gain_hf

 `atributo`

Reverb: volume das altas frequências.

### reverb_late_reverb_delay

 `atributo`

Reverb: atraso da cauda do eco.

### reverb_late_reverb_gain

 `atributo`

Reverb: volume da cauda do eco.

### reverb_reflections_delay

 `atributo`

Reverb: atraso das primeiras reflexões.

### reverb_reflections_gain

 `atributo`

Reverb: volume das primeiras reflexões.

### reverb_room_rolloff_factor

 `atributo`

Reverb: quanto o efeito cai com a distância.

### sound

 `atributo`

Som atual (`aud.Sound`), ou `None`.

### time

 `atributo`

Posição atual do som, em segundos. Pode ser mudada para pular.

### volume

 `atributo`

Volume do som.

### volume_maximum

 `atributo`

Volume máximo, mesmo de perto.

### volume_minimum

 `atributo`

Volume mínimo, mesmo de longe.
