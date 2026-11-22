# SCA_WaitActuator

Classe `Range.types.SCA_WaitActuator`.

```python
# Espera três segundos.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Wait"]

act.duration = 3.0
act.useRestart = False
cont.activate(act)
```

```python
# Mostra o tempo que falta.
import Range

act = Range.logic.getCurrentController().actuators["Wait"]

if act.waiting:
    print(act.duration - act.elapsed)
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### duration

*(novo na Anastacio)* `atributo`

Tempo de espera em segundos (0 a 100000). Ao receber pulso positivo o actuator começa a contar; quando o tempo passa, ele termina e um sensor **Actuator** em modo Finished dispara.

### elapsed

*(novo na Anastacio)* `atributo · só leitura`

Segundos já passados desde o início da espera atual.

### useRestart

*(novo na Anastacio)* `atributo`

Se `True`, um novo pulso positivo durante a espera reinicia a contagem do zero.

### waiting

*(novo na Anastacio)* `atributo · só leitura`

`True` enquanto o actuator está contando.
