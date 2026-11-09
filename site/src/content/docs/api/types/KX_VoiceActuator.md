---
title: "KX_VoiceActuator"
description: "Referência da classe Range.types.KX_VoiceActuator"
---

Atuador Voice: grava, toca e salva a voz do jogador.

```python
# Troca o efeito de voz antes de tocar.
import Range

cont = Range.logic.getCurrentController()
voice = cont.actuators["Voice"]
voice.effect = "RADIO"
cont.activate(voice)
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### amount

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Intensidade do efeito, de 0 a 1.

### effect

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Efeito de voz, como `NONE`, `CHIPMUNK`, `GIANT`, `ROBOT`, `RADIO`, `ECHO` ou `CAVE`.

### maxSeconds

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Tempo máximo de gravação em segundos, de 0 a 600.

### mode

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Ação: `0` gravar, `1` tocar, `2` ao vivo, `3` parar, `4` salvar.

### slot

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Nome da gravação usada pelo atuador.

### useReverb

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Usa o reverb da área ou do World.

### volume

<span class="ae-badge novo">novo na Anastacio</span> <small>atributo</small>

Volume, de 0 a 4.

