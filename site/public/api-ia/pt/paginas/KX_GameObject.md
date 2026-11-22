# KX_GameObject

Classe base: [`SCA_IObject`](SCA_IObject.md)

> **Veja também:**
[`KX_Scene`](KX_Scene.md), [`KX_Mesh`](KX_Mesh.md), [`KX_PythonComponent`](KX_PythonComponent.md), [`KX_VehicleWrapper`](KX_VehicleWrapper.md), [`KX_ParticleSystem`](KX_ParticleSystem.md)

Todos os objetos do jogo derivam desta classe.

As propriedades de jogo do objeto podem ser acessadas como atributos desta classe.

> **Note:**
Chamar QUALQUER método ou atributo de um objeto que já foi removido da cena gera SystemError. Se o objeto pode ter sido removido desde o último acesso, confira antes com o atributo `invalid`.

KX_GameObject pode ser herdado para estender o que ele faz. Por exemplo:

```python

import Range

class CustomGameObject(Range.types.KX_GameObject):
    RATE = 0.05

    def __init__(self, old_owner):
        # "old_owner" pode ser ignorado. Neste ponto, "self" já é
        # o objeto na cena, e "old_owner" já foi
        # destruído.

        # Dá para criar atributos novos, mas também poderíamos usar uma
        # propriedade de jogo, como "self['rate']".
        self.rate = CustomGameObject.RATE

    def update(self):
        self.worldPosition.z += self.rate

        # inverte a direção
        if self.worldPosition.z > 1.0:
            self.rate = -CustomGameObject.RATE
        elif self.worldPosition.z < 0.0:
            self.rate = CustomGameObject.RATE

# Chamado primeiro
def mutate(cont):
    old_object = cont.owner
    mutated_object = CustomGameObject(cont.owner)

    # Depois de chamar o construtor acima, as referências ao objeto antigo
    # não devem mais ser usadas.
    assert(old_object is not mutated_object)
    assert(old_object.invalid)
    assert(mutated_object is cont.owner)

# Chamado depois. Repare que agora estamos usando o objeto transformado.
def update(cont):
    cont.owner.update()
```

Ao herdar de objetos que não são vazios nem malhas, use o tipo específico. Por exemplo, herde de `BL_ArmatureObject` quando o objeto a transformar for uma armature.

```python

# Move e gira o objeto com W e A. Rode a cada frame (sensor Always com True Pulse).
import Range

obj = Range.logic.getCurrentController().owner
keys = Range.logic.keyboard.events

if keys[Range.events.WKEY]:
    obj.applyMovement((0, 0.1, 0), True)
if keys[Range.events.AKEY]:
    obj.applyRotation((0, 0, 0.05), True)
```

```python

# Lê e muda propriedades de jogo.
import Range

obj = Range.logic.getCurrentController().owner

obj["health"] = obj.get("health", 100) - 10

if obj["health"] <= 0:
    obj.endObject()
```

```python

# Procura o chão embaixo do objeto.
import Range

obj = Range.logic.getCurrentController().owner
below = obj.worldPosition - obj.getAxisVect((0, 0, 1))

hit, point, normal = obj.rayCast(below, obj, 10.0)

if hit is not None:
    print(hit.name, point)
```

```python

# Persegue o jogador quando ele chega perto.
import Range

scene = Range.logic.getCurrentScene()
obj = Range.logic.getCurrentController().owner
player = scene.objects["Player"]

if obj.getDistanceTo(player) < 15.0:
    distance, direction, local = obj.getVectTo(player)
    obj.alignAxisToVect(direction, 1, 0.1)
    obj.applyMovement((0, 0.05, 0), True)
```

```python

# Toca os frames 1 a 30 de uma action.
import Range

obj = Range.logic.getCurrentController().owner

if not obj.isPlayingAction():
    obj.playAction("Walk", 1, 30)
```

```python

# Prende o objeto em uma mão e solta depois.
import Range

scene = Range.logic.getCurrentScene()
obj = Range.logic.getCurrentController().owner

obj.setParent(scene.objects["Hand"])

# Depois:
obj.removeParent()
```

Visão geral. Os itens estão nas partes abaixo:

- [atributos](KX_GameObject--props.md) (121 itens)
- [métodos e funções](KX_GameObject--funcs.md) (106 itens)
