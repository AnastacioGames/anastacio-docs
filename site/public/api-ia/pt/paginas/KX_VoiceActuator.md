# KX_VoiceActuator

Atuador Voice: grava, toca e salva a voz do jogador.

```python
# Troca o efeito de voz antes de tocar.
import Range

cont = Range.logic.getCurrentController()
voice = cont.actuators["Voice"]
voice.effect = "RADIO"
cont.activate(voice)
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### amount

*(novo na Anastacio)* `atributo`

Intensidade do efeito, de 0 a 1.

### effect

*(novo na Anastacio)* `atributo`

Efeito de voz, como `NONE`, `CHIPMUNK`, `GIANT`, `ROBOT`, `RADIO`, `ECHO` ou `CAVE`.

### maxSeconds

*(novo na Anastacio)* `atributo`

Tempo máximo de gravação em segundos, de 0 a 600.

### mode

*(novo na Anastacio)* `atributo`

Ação: `0` gravar, `1` tocar, `2` ao vivo, `3` parar, `4` salvar.

### slot

*(novo na Anastacio)* `atributo`

Nome da gravação usada pelo atuador.

### useReverb

*(novo na Anastacio)* `atributo`

Usa o reverb da área ou do World.

### volume

*(novo na Anastacio)* `atributo`

Volume, de 0 a 4.
