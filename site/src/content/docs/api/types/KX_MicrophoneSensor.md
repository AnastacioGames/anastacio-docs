---
title: "KX_MicrophoneSensor"
description: "Referência da classe Range.types.KX_MicrophoneSensor"
---

Sensor Microphone: reage à voz do jogador.

```python
# Abre a boca do personagem enquanto o jogador fala.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Microphone"]
cont.owner["mouth"] = sensor.level
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### hold

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Segundos, de 0 a 60: quanto a fala se mantém positiva, ou quanto silêncio é preciso.

### level

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Nível da voz agora (só leitura).

### mode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Modo: `0` falando (nível acima de `threshold`), `1` pico (um pulso, como palma ou sopro), `2` silêncio (depois de `hold` segundos abaixo de `threshold`).

### peak

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo · só leitura</small>

Pico da voz (só leitura).

### propName

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Nome da propriedade do objeto ligada ao sensor.

### threshold

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Nível de voz que dispara o sensor, de 0 a 1.

