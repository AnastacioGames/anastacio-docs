# KX_MicrophoneSensor

Sensor Microphone: reage à voz do jogador.

```python
# Abre a boca do personagem enquanto o jogador fala.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors["Microphone"]
cont.owner["mouth"] = sensor.level
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### hold

*(novo na Anastacio)* `atributo`

Segundos, de 0 a 60: quanto a fala se mantém positiva, ou quanto silêncio é preciso.

### level

*(novo na Anastacio)* `atributo · só leitura`

Nível da voz agora (só leitura).

### mode

*(novo na Anastacio)* `atributo`

Modo: `0` falando (nível acima de `threshold`), `1` pico (um pulso, como palma ou sopro), `2` silêncio (depois de `hold` segundos abaixo de `threshold`).

### peak

*(novo na Anastacio)* `atributo · só leitura`

Pico da voz (só leitura).

### propName

*(novo na Anastacio)* `atributo`

Nome da propriedade do objeto ligada ao sensor.

### threshold

*(novo na Anastacio)* `atributo`

Nível de voz que dispara o sensor, de 0 a 1.
