# KX_VRHeadSensor

Classe `Range.types.KX_VRHeadSensor`.

```python
# Confirma com um aceno de cabeça.
import Range

sensor = Range.logic.getCurrentController().sensors["VRHead"]

sensor.mode = 4
sensor.time = 1.0

if sensor.positive:
    print("Yes")
```

```python
# Lê a rotação atual da cabeça.
import Range

sensor = Range.logic.getCurrentController().sensors["VRHead"]

print(sensor.yaw, sensor.pitch, sensor.roll)
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### angle

*(novo na Anastacio)* `atributo`

Ângulo, em radianos, que a cabeça precisa girar para o gesto contar (0 a 1.6).

### mode

*(novo na Anastacio)* `atributo`

Gesto detectado: 0 olhar para cima, 1 para baixo, 2 inclinar à esquerda, 3 à direita, 4 acenar "sim", 5 balançar "não".

### pitch

*(novo na Anastacio)* `atributo · só leitura`

Inclinação atual da cabeça para cima/baixo.

### roll

*(novo na Anastacio)* `atributo · só leitura`

Inclinação atual da cabeça para os lados.

### time

*(novo na Anastacio)* `atributo`

Tempo, em segundos, para completar o gesto (0.05 a 10).

### yaw

*(novo na Anastacio)* `atributo · só leitura`

Giro atual da cabeça para a esquerda/direita.
