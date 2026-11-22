# Range.audio

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

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### edit(sound, start=0, end=-1, fade_in=0, fade_out=0, normalize=False)

*(novo na Anastacio)* `função`

Corta, aplica fades e normaliza um som; igual a `aud.edit`.

**Retorna:** `aud.Sound`

### getVolume(module)

*(novo na Anastacio)* `função`

Volume do módulo; `None` se ele não existe.

**Retorna:** `float`

### isLive()

*(novo na Anastacio)* `função`

`True` enquanto o microfone está sendo ouvido.

**Retorna:** `bool`

### isPlaying(module)

*(novo na Anastacio)* `função`

`True` enquanto um som do módulo toca.

**Retorna:** `bool`

### microphone()

*(novo na Anastacio)* `função`

O `aud.Microphone` em uso, para uso avançado; `None` antes de ligar.

**Retorna:** `aud.Microphone`

### microphoneDropped()

*(novo na Anastacio)* `função`

Quantas vezes o áudio se perdeu porque o jogo travou.

**Retorna:** `int`

### microphoneError()

*(novo na Anastacio)* `função`

Motivo de o microfone não ter aberto.

**Retorna:** `str`

### microphoneIsRecording()

*(novo na Anastacio)* `função`

`True` enquanto grava.

**Retorna:** `bool`

### microphoneLevel()

*(novo na Anastacio)* `função`

Nível da voz agora, de 0 a 1.

**Retorna:** `float`

### microphoneNote(a4=440.0)

*(novo na Anastacio)* `função`

(name, cents, midi) da nota atual, por exemplo ('A4', -12.5, 69); ('', 0.0, 0) sem nota clara.

### microphonePeak()

*(novo na Anastacio)* `função`

Pico com queda lenta, de 0 a 1.

**Retorna:** `float`

### microphonePitch()

*(novo na Anastacio)* `função`

Frequência da nota que está sendo cantada ou tocada no microfone, em Hz; 0 quando não há nota clara.

**Retorna:** `float`

### microphoneRecordingSeconds()

*(novo na Anastacio)* `função`

Duração da gravação em andamento, em segundos.

**Retorna:** `float`

### microphoneRecordStart()

*(novo na Anastacio)* `função`

Começa a gravar.

### microphoneRecordStop(slot="last")

*(novo na Anastacio)* `função`

Para e guarda a gravação com o nome `slot`. Retorna o `aud.Sound` ou `None`.

**Retorna:** `aud.Sound`

### microphoneSave(slot, path)

*(novo na Anastacio)* `função`

Salva uma gravação em WAV. Caminho relativo vai para a pasta do jogo (Web: `/saves`).

### microphoneStart(device="")

*(novo na Anastacio)* `função`

Liga o microfone. Na Web, chame depois de um clique ou toque. `False` se não abrir.

**Retorna:** `bool`

### microphoneState()

*(novo na Anastacio)* `função`

Estado do microfone: `'closed'`, `'pending'`, `'granted'`, `'denied'` ou `'error'`.

**Retorna:** `str`

### microphoneStop()

*(novo na Anastacio)* `função`

Desliga o microfone.

### modules()

*(novo na Anastacio)* `função`

Nomes dos módulos do World Sound carregados até agora.

**Retorna:** `list`

### next(module)

*(novo na Anastacio)* `função`

Music: passa para a próxima faixa.

### pause(module)

*(novo na Anastacio)* `função`

Pausa todos os sons do módulo onde estão.

### play(module, sound="", fade=-1.0)

*(novo na Anastacio)* `função`

Toca um som de um módulo do World Sound, ou retoma o módulo pausado. Sem `sound`, Music toca a faixa atual e Ambient toca todas as camadas. `fade` em segundos; negativo usa o Fade do módulo. `False` se o módulo ou o som não existe.

**Retorna:** `bool`

### playing(module)

*(novo na Anastacio)* `função`

Nomes dos sons tocando agora (Music: a faixa atual).

**Retorna:** `list`

### playLive(effect="NONE", amount=1.0, volume=1.0, reverb=False)

*(novo na Anastacio)* `função`

Faz ouvir o microfone agora, com efeito de voz. Só um por vez; chamar de novo troca o efeito. Use fones: caixas de som realimentam o microfone.

### playVoice(sound, effect="NONE", amount=1.0, volume=1.0, reverb=False)

*(novo na Anastacio)* `função`

Toca uma gravação (nome ou `aud.Sound`) com efeito de voz; veja `voicePresets()`. `reverb=True` usa o reverb da área ou do World. `False` se a gravação ou o efeito não existe.

**Retorna:** `bool`

### previous(module)

*(novo na Anastacio)* `função`

Music: volta para a faixa anterior.

### recording(slot)

*(novo na Anastacio)* `função`

O `aud.Sound` de uma gravação, ou `None`.

**Retorna:** `aud.Sound`

### recordings()

*(novo na Anastacio)* `função`

Nomes das gravações guardadas até agora.

**Retorna:** `list`

### resume(module)

*(novo na Anastacio)* `função`

Continua de onde `pause(module)` parou.

### setRecording(slot, sound)

*(novo na Anastacio)* `função`

Guarda um `aud.Sound` com um nome. `None` remove.

### setVolume(module, volume)

*(novo na Anastacio)* `função`

Define o volume do módulo, de 0.0 a 1.0.

### sounds(module)

*(novo na Anastacio)* `função`

Nomes dos sons do módulo.

**Retorna:** `list`

### stop(module, sound="", fade=-1.0)

*(novo na Anastacio)* `função`

Para um módulo do World Sound, ou só um dos sons dele. `fade` em segundos; negativo usa o Fade do módulo.

### stopLive()

*(novo na Anastacio)* `função`

Para de ouvir o microfone.

### voiceFx(sound, preset, amount=1.0)

*(novo na Anastacio)* `função`

Aplica um efeito de voz; igual a `aud.voice_fx`.

**Retorna:** `aud.Sound`

### voicePresets(live=False)

*(novo na Anastacio)* `função`

Nomes dos efeitos de voz.

**Retorna:** `list`
