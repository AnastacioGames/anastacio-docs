---
title: Clima (chuva, raios, nuvens e neblina)
description: Ligar e mudar o clima do World durante o jogo com setWeather e strikeLightning.
draft: true
---

O clima da Anastacio fica no **World**: chuva, respingos, poças, raios, nuvens, Sky Layers, nuvens volumétricas e neblina volumétrica. Você deixa tudo pronto no editor e muda os valores durante o jogo pelo Python, com [`setWeather`](../../api/types/kx_worldinfo/).

## 1. Prepare no editor

1. Abra a aba **World** nas propriedades.
2. No painel de clima, ligue **Rain** e ajuste a intensidade até gostar do resultado na viewport.
3. Se for usar nuvens, ligue **Clouds** (ou Sky Layers / Volumetric Clouds) já no editor.

:::caution
As nuvens precisam de um passe criado no carregamento. Se nenhuma delas estiver ligada no World quando o jogo abre, `setWeather("clouds", True)` não tem onde desenhar. Ligue no editor e, se quiser começar sem nuvens, zere a cobertura pelo script.
:::

<!-- PRINT: aba World com o painel de clima aberto e Rain ligado -->

## 2. Mude o clima pelo script

Crie `clima.py` no Text Editor, anexe como componente em qualquer objeto da cena (por exemplo o Cubo) e registre como no guia [Primeiro script](../primeiro-script/).

```python
import Range
from collections import OrderedDict


class Clima(Range.types.KX_PythonComponent):
    args = OrderedDict([
        ("Segundos ate a tempestade", 5.0),
    ])

    def start(self, args):
        self.espera = args["Segundos ate a tempestade"]
        self.tempo = 0.0
        self.tempestade = False
        mundo = self.object.scene.world
        mundo.setWeather("rain", True)
        mundo.setWeather("rain_intensity", 0.2)

    def update(self):
        self.tempo += 1.0 / Range.logic.getAverageFrameRate()
        if not self.tempestade and self.tempo >= self.espera:
            self.tempestade = True
            mundo = self.object.scene.world
            mundo.setWeather("rain_intensity", 1.0)
            mundo.setWeather("puddles", True)
            mundo.setWeather("lightning", True)
            mundo.strikeLightning()
```

O que acontece:

- no começo cai uma chuva fraca;
- depois de 5 segundos a chuva engrossa, aparecem poças e cai um raio na hora; os raios automáticos continuam a cada intervalo.

## Nomes que você pode mudar

Os nomes aceitam o prefixo `weather.` (opcional). Alguns dos mais usados:

| Nome | Tipo | O que faz |
|---|---|---|
| `rain` | bool | Liga a chuva |
| `rain_intensity` | float | Quanto chove |
| `rain_wind` | float | Inclinação da chuva pelo vento |
| `puddles` | bool | Poças no chão |
| `lightning` | bool | Raios automáticos |
| `clouds` | bool | Nuvens (precisa do passe, veja o aviso acima) |
| `cloud_coverage` | float | Quanto do céu fica coberto |
| `vfog` | bool | Neblina volumétrica |
| `vfog_density` | float | Densidade da neblina |

A lista completa está em [`KX_WorldInfo.setWeather`](../../api/types/kx_worldinfo/). Um nome errado gera erro, o que ajuda a achar erros de digitação.

## Sem script: Logic Bricks

O atuador **Weather Effects** faz as mesmas mudanças sem Python. Ligue um sensor (Keyboard, Delay, Property) a ele e escolha o que mudar.

<!-- PRINT: atuador Weather Effects ligado a um sensor Keyboard -->
