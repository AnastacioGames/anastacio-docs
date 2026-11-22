# KX_VisibilityActuator

Classe base: [`SCA_IActuator`](SCA_IActuator.md)

Atuador Visibility.

```python
# Esconde o objeto e os filhos.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Visibility"]

act.visibility = False
act.useRecursion = True
cont.activate(act)
```

## visibility

se o atuador deixa o objeto pai visível ou invisível.

**Tipo:** boolean

### useOcclusion

se o atuador torna o objeto pai um occluder ou não.

**Tipo:** boolean

### useRecursion

se a visibilidade/oclusão deve ser propagada a todos os filhos do objeto.

**Tipo:** boolean
