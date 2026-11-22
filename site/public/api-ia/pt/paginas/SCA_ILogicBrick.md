# SCA_ILogicBrick

Classe base: [`EXP_Value`](EXP_Value.md)

Classe base de todos os logic bricks.

```python
# Sensores, controladores e atuadores conhecem o objeto deles.
import Range

cont = Range.logic.getCurrentController()
sensor = cont.sensors[0]

print(sensor.owner.name, sensor.name, sensor.executePriority)
```

## executePriority

Define a ordem em que os controladores são avaliados e os atuadores são ativados (prioridade menor roda primeiro).

**Tipo:** executePriority: int

### owner

O game object ao qual este logic brick está ligado (somente leitura).

**Tipo:** `KX_GameObject` or None in exceptional cases.

### name

O nome deste logic brick (somente leitura).

**Tipo:** string

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### fireCount

*(novo na Anastacio)* `atributo · só leitura`

Quantas vezes este brick disparou: o sensor conta as ativações (subidas) e o actuator conta as partidas; outros bricks devolvem 0. Somente leitura.
