---
title: "KX_PythonComponent"
description: "Referência da classe Range.types.KX_PythonComponent"
---

Classe base: [`EXP_Value`](../exp_value/)



Um componente Python pode ser comparado a logic bricks Python com parâmetros. O componente Python é um script carregado pela UI; esse script define uma classe de componente herdando de `KX_PythonComponent`. Essa classe precisa ter um dicionário de propriedades, `args`, e duas funções padrão: `start` e `update`.

O script precisa ter extensão .py.

As propriedades do componente são carregadas do atributo `args` pela UI no carregamento. Quando o jogo começa, a função `start` é chamada recebendo um dicionário com o nome e o valor das propriedades. A função `update` é chamada a cada frame na etapa de lógica, antes dos logic bricks; o papel dela é tratar e processar tudo.

O exemplo de componente a seguir move e gira o objeto ao apertar as teclas W, A, S e D.

```python

import Range
from collections import OrderedDict

class ThirdPerson(Range.types.KX_PythonComponent):
    """Basic third person controls

    W: move forward
    A: turn left
    S: move backward
    D: turn right

    """

    #

    args = OrderedDict([
        ("Move Speed", 0.1),
        ("Turn Speed", 0.04)
    ])

    def start(self, args):
        self.move_speed = args['Move Speed']
        self.turn_speed = args['Turn Speed']

    def update(self):
        keyboard = Range.logic.keyboard.events

        move = 0
        rotate = 0

        if keyboard[Range.events.WKEY]:
            move += self.move_speed
        if keyboard[Range.events.SKEY]:
            move -= self.move_speed

        if keyboard[Range.events.AKEY]:
            rotate += self.turn_speed
        if keyboard[Range.events.DKEY]:
            rotate -= self.turn_speed

        self.object.applyMovement((0, move, 0), True)
        self.object.applyRotation((0, 0, rotate), True)
```

Como os componentes são carregados pela primeira vez fora do bge, `bge` é um módulo falso que só contém a classe `KX_PythonComponent`, para não importar todos os módulos do bge. Isso é mais seguro, mas dá problema no carregamento quando o usuário quer usar funções ou atributos dos módulos do bge além da classe `KX_PythonComponent`. A saída é não chamar essas funções no carregamento fora da Range. Para detectar isso, o módulo bge tem o atributo `__component__` quando é importado fora da Range.

O exemplo de componente a seguir adiciona um objeto "Cube" na inicialização e o move no eixo x a cada update. Ele mostra que dá para usar funções da cena e carregar o componente fora do bge definindo atributos globais numa condição no começo do script.

```python

import Range

if not hasattr(bge, "__component__"):
    global scene
    scene = Range.logic.getCurrentScene()

class Component(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        scene.addObject("Cube")

    def update(self):
        scene.objects["Cube"].worldPosition.x += 0.1
```

Os tipos de propriedade suportados são float, integer, boolean, string, set (para enumeração) e Vector 2D, 3D e 4D. O exemplo a seguir mostra todos esses tipos.

```python

from Range import *
from mathutils import *
from collections import OrderedDict

class Component(types.KX_PythonComponent):
     args = OrderedDict([
         ("Float", 58.6),
         ("Integer", 150),
         ("Boolean", True),
         ("String", "Cube"),
         ("Enum", {"Enum 1", "Enum 2", "Enum 3"}),
         ("Vector 2D", Vector((0.8, 0.7))),
         ("Vector 3D", Vector((0.4, 0.3, 0.1))),
         ("Vector 4D", Vector((0.5, 0.2, 0.9, 0.6)))
     ])

     def start(self, args):
         print(args)

     def update(self):
         pass
```

### object

O objeto dono do componente.

**Tipo:** `KX_GameObject`

### args

Dicionário das propriedades do componente; as chaves são strings e o valor pode ser: float, integer, Vector(2D/3D/4D), set, string.

**Tipo:** dict

### start(args)

Inicializa o componente.

- **`args`**: O dicionário com o nome e o valor das propriedades.
  - tipo: dict

:::caution
Esta função precisa ser herdada na classe do componente Python.
:::

### update()

Processa a lógica do componente.

:::caution
Esta função precisa ser herdada na classe do componente Python.
:::

### dispose()

Função chamada quando o componente é destruído.

:::caution
Esta função precisa ser herdada na classe do componente Python.
:::

