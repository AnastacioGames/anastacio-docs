# SCA_NORController

Classe base: [`SCA_IController`](SCA_IController.md)

Um controlador NOR só ativa quando todos os sensores ligados estão desativados.

Não há métodos Python especiais para este controlador.

```python
# NOR liga os atuadores só quando nenhum sensor está positivo.
import Range

cont = Range.logic.getCurrentController()

print(not any(sensor.positive for sensor in cont.sensors))
```
