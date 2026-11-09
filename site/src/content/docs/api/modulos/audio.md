---
title: "Range.audio"
description: "Referência do módulo Range.audio"
---

Módulo `Range.audio` da Anastacio Engine. Também acessível como `bge.audio`.

```python
# Liga o microfone e lê o nível da voz.
import Range

if Range.audio.microphoneState() == "closed":
    Range.audio.microphoneStart()

print("Voice:", Range.audio.microphoneLevel())
```

```python
# Grava a voz e toca de volta com efeito de robô.
import Range

Range.audio.microphoneRecordStart()

# Depois, quando o jogador parar de falar.
Range.audio.microphoneRecordStop("taunt")
Range.audio.playVoice("taunt", effect="ROBOT", reverb=True)
```

```python
# Controla um módulo do World Sound pelo nome.
import Range

Range.audio.play("Music", fade=2.0)
Range.audio.setVolume("Music", 0.5)
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### edit(sound, start=0, end=-1, fade_in=0, fade_out=0, normalize=False)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Corta, aplica fades e normaliza um som; igual a `aud.edit`.

**Retorna:** `aud.Sound`

### getVolume(module)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Volume do módulo; `None` se ele não existe.

**Retorna:** `float`

### isLive()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

`True` enquanto o microfone está sendo ouvido.

**Retorna:** `bool`

### isPlaying(module)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

`True` enquanto um som do módulo toca.

**Retorna:** `bool`

### microphone()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

O `aud.Microphone` em uso, para uso avançado; `None` antes de ligar.

**Retorna:** `aud.Microphone`

### microphoneDropped()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Quantas vezes o áudio se perdeu porque o jogo travou.

**Retorna:** `int`

### microphoneError()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Motivo de o microfone não ter aberto.

**Retorna:** `str`

### microphoneIsRecording()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

`True` enquanto grava.

**Retorna:** `bool`

### microphoneLevel()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Nível da voz agora, de 0 a 1.

**Retorna:** `float`

### microphonePeak()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Pico com queda lenta, de 0 a 1.

**Retorna:** `float`

### microphoneRecordingSeconds()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Duração da gravação em andamento, em segundos.

**Retorna:** `float`

### microphoneRecordStart()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Começa a gravar.

### microphoneRecordStop(slot="last")

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Para e guarda a gravação com o nome `slot`. Retorna o `aud.Sound` ou `None`.

**Retorna:** `aud.Sound`

### microphoneSave(slot, path)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Salva uma gravação em WAV. Caminho relativo vai para a pasta do jogo (Web: `/saves`).

### microphoneStart(device="")

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Liga o microfone. Na Web, chame depois de um clique ou toque. `False` se não abrir.

**Retorna:** `bool`

### microphoneState()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Estado do microfone: `'closed'`, `'pending'`, `'granted'`, `'denied'` ou `'error'`.

**Retorna:** `str`

### microphoneStop()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Desliga o microfone.

### modules()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Nomes dos módulos do World Sound carregados até agora.

**Retorna:** `list`

### next(module)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Music: passa para a próxima faixa.

### pause(module)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Pausa todos os sons do módulo onde estão.

### play(module, sound="", fade=-1.0)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Toca um som de um módulo do World Sound, ou retoma o módulo pausado. Sem `sound`, Music toca a faixa atual e Ambient toca todas as camadas. `fade` em segundos; negativo usa o Fade do módulo. `False` se o módulo ou o som não existe.

**Retorna:** `bool`

### playing(module)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Nomes dos sons tocando agora (Music: a faixa atual).

**Retorna:** `list`

### playLive(effect="NONE", amount=1.0, volume=1.0, reverb=False)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Faz ouvir o microfone agora, com efeito de voz. Só um por vez; chamar de novo troca o efeito. Use fones: caixas de som realimentam o microfone.

### playVoice(sound, effect="NONE", amount=1.0, volume=1.0, reverb=False)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Toca uma gravação (nome ou `aud.Sound`) com efeito de voz; veja `voicePresets()`. `reverb=True` usa o reverb da área ou do World. `False` se a gravação ou o efeito não existe.

**Retorna:** `bool`

### previous(module)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Music: volta para a faixa anterior.

### recording(slot)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

O `aud.Sound` de uma gravação, ou `None`.

**Retorna:** `aud.Sound`

### recordings()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Nomes das gravações guardadas até agora.

**Retorna:** `list`

### resume(module)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Continua de onde `pause(module)` parou.

### setRecording(slot, sound)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Guarda um `aud.Sound` com um nome. `None` remove.

### setVolume(module, volume)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Define o volume do módulo, de 0.0 a 1.0.

### sounds(module)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Nomes dos sons do módulo.

**Retorna:** `list`

### stop(module, sound="", fade=-1.0)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Para um módulo do World Sound, ou só um dos sons dele. `fade` em segundos; negativo usa o Fade do módulo.

### stopLive()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Para de ouvir o microfone.

### voiceFx(sound, preset, amount=1.0)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Aplica um efeito de voz; igual a `aud.voice_fx`.

**Retorna:** `aud.Sound`

### voicePresets(live=False)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Nomes dos efeitos de voz.

**Retorna:** `list`

