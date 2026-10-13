---
title: Primeiro script
description: Um script Python que move um objeto quando você aperta uma tecla.
---

1. Selecione um objeto na cena e adicione um sensor **Always** (com *True Level Triggering* ligado) ligado a um controlador **Python**.
2. Crie um texto chamado `mover.py` no editor de texto e escolha-o no controlador.
3. Cole o código e aperte **P** para jogar.

![Sensor Always ligado ao controlador Python com o script mover.py, e o código no editor de texto](../../../assets/guias/logic-bricks-mover.png)

```python
import Range
from Range import logic, events

cont = logic.getCurrentController()
own = cont.owner
teclado = logic.keyboard

if teclado.inputs[events.WKEY].active:
    own.applyMovement((0, 0.1, 0), True)   # anda para a frente
if teclado.inputs[events.SKEY].active:
    own.applyMovement((0, -0.1, 0), True)
```

- `logic.getCurrentController()` devolve o controlador que está rodando o script.
- `own` é o objeto dono do controlador, um [`KX_GameObject`](../../api/types/kx_gameobject/).
- `applyMovement(vetor, local)` move o objeto; `True` usa os eixos do próprio objeto.

## O mesmo com um componente

Um componente faz o mesmo trabalho sem precisar de logic bricks. Ele é uma classe Python ligada ao objeto, e você pode mudar os parâmetros dela no painel, sem mexer no código.

1. Crie um texto chamado `mover_componente.py` no editor de texto (o nome precisa terminar em `.py`) e cole o código abaixo.
2. Selecione o objeto e abra a aba de componentes (ícone do Python) nas propriedades. Em **Existing Components**, escolha **In .Range File** em *Modules*, depois a classe **Mover** em *Classes*, e clique em **Register**. Se a classe não aparecer, clique no botão de atualizar no canto do painel.
3. O componente aparece em **Object's Components**, com o campo **Velocidade**. Ajuste se quiser e aperte **P** para jogar.

![Componente Mover registrado no objeto, com o campo Velocidade, e o código no editor de texto](../../../assets/guias/componente-mover.png)

```python
import Range
from Range import logic, events
from collections import OrderedDict


class Mover(Range.types.KX_PythonComponent):
    # parâmetros que aparecem no painel Components
    args = OrderedDict([
        ("Velocidade", 0.1),
    ])

    def start(self, args):
        # roda uma vez, quando o jogo começa
        self.velocidade = args["Velocidade"]

    def update(self):
        # roda a cada frame
        teclado = logic.keyboard
        if teclado.inputs[events.WKEY].active:
            self.object.applyMovement((0, self.velocidade, 0), True)   # anda para a frente
        if teclado.inputs[events.SKEY].active:
            self.object.applyMovement((0, -self.velocidade, 0), True)
```

- A classe herda de [`KX_PythonComponent`](../../api/types/kx_pythoncomponent/).
- `args` define os parâmetros do painel. A ordem do `OrderedDict` é a ordem em que eles aparecem.
- `start(args)` recebe os valores do painel; `update()` roda a cada frame, antes dos logic bricks.
- `self.object` é o objeto dono do componente, no lugar do `cont.owner` do script.

**Script ou componente?** Use script com logic bricks para ligar sensores e atuadores visualmente. Use componente quando a lógica é toda em Python e você quer reaproveitar a mesma classe em vários objetos, cada um com seus próprios valores.
