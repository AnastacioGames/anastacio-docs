# KX_LightningActuator

Classe `Range.types.KX_LightningActuator`.

```python
# Dispara um clarão com o raio visível.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Lightning"]

act.bolt = True
cont.activate(act)
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### bolt

*(novo na Anastacio)* `atributo`

Liga o raio visível do relâmpago, além do clarão.
