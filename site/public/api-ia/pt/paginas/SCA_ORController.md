# SCA_ORController

Classe base: [`SCA_IController`](SCA_IController.md)

Um controlador OR ativa quando qualquer sensor ligado ativa.

Não há métodos Python especiais para este controlador.

```python
# OR liga os atuadores quando pelo menos um sensor está positivo.
import Range

cont = Range.logic.getCurrentController()

print(any(sensor.positive for sensor in cont.sensors))
```
