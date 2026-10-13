---
title: "KX_Speaker"
description: "Referência da classe Range.types.KX_Speaker"
---

:::tip[Veja também]
[`KX_SoundActuator`](../../types/kx_soundactuator/), [`KX_Scene`](../../types/kx_scene/)
:::

Classe `Range.types.KX_Speaker`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### GetActiveEffect()

 <small>método</small>

Efeito de som ativo: 0 nenhum, 1 reverb.

**Retorna:** `int`

### GetActiveEffectFilter()

 <small>método</small>

Filtro ativo: 0 nenhum, 1 passa-baixa, 2 passa-alta, 3 passa-banda.

**Retorna:** `int`

### Pause()

 <small>método</small>

Pausa o som.

### Play()

 <small>método</small>

Toca o som.

### RemoveEffect()

 <small>método</small>

Remove o efeito de som.

### Restart()

 <small>método</small>

Toca o som desde o começo.

### SetEffect(effectType, filterType=0)

 <small>método</small>

Aplica um efeito: `effectType` 1 = reverb; `filterType` 0 nenhum, 1 passa-baixa, 2 passa-alta, 3 passa-banda. Depois disso as áreas de reverb deixam este Speaker em paz.

### SetSound(sound, cache=False)

 <small>método</small>

Troca o som (um `aud.Sound`). Com `cache=True`, guarda o som decodificado na memória.

### Stop()

 <small>método</small>

Para o som.

### attenuation

 <small>atributo</small>

Quanto o volume cai com a distância (som 3D).

### catkey

 <small>atributo</small>

Chave da categoria de som no gerenciador de reprodução, ou `None`.

### cone_angle_inner

 <small>atributo</small>

Ângulo, em graus, do cone em que o som toca no volume cheio.

### cone_angle_outer

 <small>atributo</small>

Ângulo, em graus, do cone fora do qual o volume é `cone_volume_outer`.

### cone_volume_outer

 <small>atributo</small>

Volume fora do cone externo.

### distance_maximum

 <small>atributo</small>

Distância a partir da qual o volume para de cair.

### distance_reference

 <small>atributo</small>

Distância em que o som toca no volume normal.

### filter_gain

 <small>atributo</small>

Ganho geral do filtro.

### filter_gainhf

 <small>atributo</small>

Ganho das frequências altas no filtro.

### filter_gainlf

 <small>atributo</small>

Ganho das frequências baixas no filtro.

### is3D

 <small>atributo · só leitura</small>

`True` se o som é posicional (3D).

### mode

 <small>atributo</small>

Modo de reprodução: 1 toca até o fim, 2 repete, 3 repete indo e voltando.

### pitch

 <small>atributo</small>

Tom (velocidade) do som. 1.0 é normal.

### playbackManager

 <small>atributo</small>

Gerenciador de reprodução (`aud.PlaybackManager`) usado pelo Speaker, ou `None`.

### reverb_air_absorption_gain_hf

 <small>atributo</small>

Reverb: absorção das altas frequências pelo ar.

### reverb_decay_hf_ratio

 <small>atributo</small>

Reverb: quanto as altas frequências somem mais rápido que as baixas.

### reverb_decay_limit_hf

 <small>atributo</small>

Reverb: limita o decaimento das altas frequências.

### reverb_decay_time

 <small>atributo</small>

Reverb: tempo, em segundos, que o eco leva para sumir.

### reverb_density

 <small>atributo</small>

Reverb: densidade dos ecos.

### reverb_diffusion

 <small>atributo</small>

Reverb: espalhamento dos ecos.

### reverb_gain

 <small>atributo</small>

Reverb: volume geral do efeito.

### reverb_gain_hf

 <small>atributo</small>

Reverb: volume das altas frequências.

### reverb_late_reverb_delay

 <small>atributo</small>

Reverb: atraso da cauda do eco.

### reverb_late_reverb_gain

 <small>atributo</small>

Reverb: volume da cauda do eco.

### reverb_reflections_delay

 <small>atributo</small>

Reverb: atraso das primeiras reflexões.

### reverb_reflections_gain

 <small>atributo</small>

Reverb: volume das primeiras reflexões.

### reverb_room_rolloff_factor

 <small>atributo</small>

Reverb: quanto o efeito cai com a distância.

### sound

 <small>atributo</small>

Som atual (`aud.Sound`), ou `None`.

### time

 <small>atributo</small>

Posição atual do som, em segundos. Pode ser mudada para pular.

### volume

 <small>atributo</small>

Volume do som.

### volume_maximum

 <small>atributo</small>

Volume máximo, mesmo de perto.

### volume_minimum

 <small>atributo</small>

Volume mínimo, mesmo de longe.

