---
title: "KX_ChangeColorActuator"
description: "Referência da classe Range.types.KX_ChangeColorActuator"
---

Classe `Range.types.KX_ChangeColorActuator`.

```python
# Muda aos poucos a cor do objeto para vermelho.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["ChangeColor"]

act.color = [1.0, 0.0, 0.0, 1.0]
act.useLerp = True
act.lerp = 0.2
cont.activate(act)
```



## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### color

 <small>atributo</small>

Cor `[r, g, b, a]` aplicada pelo atuador.

### lerp

 <small>atributo</small>

Velocidade da transição de cor quando `useLerp` está ligado (0.1 a 1.0).

### useLerp

 <small>atributo</small>

Faz a cor mudar aos poucos em vez de trocar de uma vez.

