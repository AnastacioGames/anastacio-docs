# KX_EndObjectActuator

Classe base: [`SCA_IActuator`](SCA_IActuator.md)

Atuador Edit Object (no modo End Object)

Este atuador não tem métodos Python.

```python
# Remove o objeto quando a vida acaba.
import Range

cont = Range.logic.getCurrentController()

if cont.owner["life"] <= 0:
    cont.activate(cont.actuators["EndObject"])
```
