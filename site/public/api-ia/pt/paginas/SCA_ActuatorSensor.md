# SCA_ActuatorSensor

Classe base: [`SCA_ISensor`](SCA_ISensor.md)

O sensor Actuator detecta mudanças no estado de um atuador do objeto pai. Ele gera um pulso positivo quando o atuador é ativado e um pulso negativo quando é desativado.

```python
# Espera uma ação terminar antes de continuar.
import Range

sensor = Range.logic.getCurrentController().sensors["ActuatorDone"]

sensor.actuator = "Wait"
sensor.mode = 1

if sensor.positive:
    print("Finished")
```

## actuator

o nome do atuador que o sensor está monitorando.

**Tipo:** string

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### mode

*(novo na Anastacio)* `atributo`

`0` Active: verdadeiro enquanto o actuator monitorado está ativo. `1` Finished: dá um pulso quando o actuator termina (ex.: Wait, Action, Video).
