---
title: Smart Components (Range.args e classe Editor)
description: Campos com slider, dica e seletor de objeto, avisos e botões no editor, sem mudar nada no jogo.
---

Um componente Python comum tem `args` e o código do jogo. O **Smart Component** é o mesmo componente com dois recursos a mais, os dois opcionais:

1. **Campos melhores** com `Range.args`: slider com limite, dica ao passar o mouse, seções, lista em ordem e escolha de objeto ou cena com o mouse.
2. **Uma classe `Editor`** que roda só no editor: arruma o objeto ao adicionar, mostra avisos nos campos, cria botões e desenha guias na viewport.

O jogo não muda: `args["Velocidade"]` continua sendo um `float`, e o jogo exportado roda sem `bpy`. Componentes antigos funcionam igual.

:::tip[Exemplo pronto]
No Text Editor, **Templates > Components > 04 Smart Component** abre um perseguidor completo com tudo deste guia.
:::

## 1. Campos com Range.args

```python
from collections import OrderedDict
from Range import types
from Range.args import Float, Int, Bool, Text, Choice, Object, Scene, Header

class Perseguidor(types.KX_PythonComponent):
    args = OrderedDict([
        Header("Alvo", icon="OBJECT_DATA"),
        ("Alvo", Object(tip="Objeto que ele persegue")),
        ("Distancia de parada", Float(1.5, min=0, max=10, tip="Para a essa distância")),

        Header("Movimento", icon="AUTO"),
        ("Velocidade", Float(3.0, min=0, max=20, tip="Metros por segundo")),
        ("Modo", Choice("Andar", "Andar", "Correr", "Pular")),
        ("Olhar para o alvo", Bool(True, tip="Gira o corpo na direção do alvo")),
        ("Cena ao pegar", Scene(tip="Cena que entra por cima ao pegar o jogador")),
    ])

    def start(self, args):
        self.alvo = args["Alvo"]            # KX_GameObject ou None
        self.velocidade = args["Velocidade"]
```

| Campo | No editor | No jogo chega como |
|---|---|---|
| `Float(valor, min, max, tip)` | número; slider quando tem `min` e `max` | `float` |
| `Int(valor, min, max, tip)` | inteiro; slider quando tem `min` e `max` | `int` |
| `Bool(valor, tip)` | caixa de marcar | `bool` |
| `Text(valor, tip)` | campo de texto | `str` |
| `Choice(padrao, item1, item2, ..., tip)` | lista na ordem escrita | `str` |
| `Object(tip)` | escolher um objeto da cena | `KX_GameObject`, ou `None` |
| `Scene(tip)` | escolher uma cena do arquivo | `str` com o nome (`""` se vazio), pronto para `logic.addScene` |
| `Header(nome, icon, open)` | título de seção que abre e fecha | (não é campo) |

O valor fora do limite é cortado: digitar 50 num `Float(max=20)` vira 20. O formato antigo (`("Nome", 1.0)`) continua valendo na mesma lista, só sem dica.

## 2. Pedir coisas ao adicionar: `requires`

```python
class Perseguidor(types.KX_PythonComponent):
    requires = {"physics": "NO_COLLISION", "components": ["vida.Vida"]}
```

Ao adicionar o componente, o editor ajusta o tipo de física do objeto e adiciona os outros componentes da lista.

## 3. A classe Editor

Fica dentro do componente. O jogo nunca roda essa classe. Ela pode usar `bpy`, mas importe só dentro dos métodos. Lá dentro, `self.object` é o objeto e `self.args["Campo"]` lê e grava os campos.

```python
class Perseguidor(types.KX_PythonComponent):
    # ... args, start, update ...

    class Editor:
        buttons = [
            ("Colocar no chão", "colocar_no_chao", "TRIA_DOWN_BAR"),
        ]

        def on_attach(self, obj):
            # uma vez, logo que o componente entra no objeto
            self.args["Nome"] = obj.name

        def on_change(self, obj, nome, valor):
            # roda para cada campo quando algo muda e ao abrir o arquivo;
            # devolver um texto mostra um aviso embaixo do campo
            if nome == "Velocidade" and valor > 15:
                return "Muito rápido: pode atravessar paredes"
            if nome == "Alvo" and valor is None:
                return "Sem alvo: ele vai ficar parado"

        def colocar_no_chao(self, obj, context):
            context.scene.update()
            menor_z = min((obj.matrix_world * v.co).z for v in obj.data.vertices)
            obj.location.z -= menor_z

        def draw_gizmo(self, obj, args, g, selected):
            # desenho na viewport, não aparece no jogo
            pos = obj.matrix_world.translation
            g.circle(pos, args["Distancia de parada"], "GREEN")
            if args["Alvo"] is not None:
                g.arrow(pos, args["Alvo"].matrix_world.translation, "YELLOW", width=2)
```

| Item | Quando roda |
|---|---|
| `on_attach(self, obj)` | Uma vez, quando o componente é adicionado. |
| `on_change(self, obj, nome, valor)` | Quando um campo muda e ao abrir o arquivo. O texto devolvido vira aviso. |
| `buttons = [(texto, metodo, icone)]` | Botões no fim da caixa do componente; o método recebe `(obj, context)` e tem undo. |
| `draw_gizmo(self, obj, args, g, selected)` | A cada redesenho da viewport. `g` tem `line`, `path`, `circle`, `sphere`, `box`, `arrow` e `text`; cores por nome (`"RED"`) ou `(r, g, b)`, posições no mundo. |

Por padrão os gizmos só aparecem com o objeto selecionado. A opção **Overlay > Component Gizmos** muda isso.

Erro no código do `Editor` aparece em vermelho na caixa do componente e não afeta o jogo.

## 4. Interface própria: `draw_ui`

Para desenhar a caixa do componente do seu jeito, crie `draw_ui(self, layout, obj, comp)` na classe `Editor`. `layout` é o mesmo do Blender (`row()`, `column()`, `prop()`, `operator()`, `label()`). O desenho entra depois dos campos e antes dos botões.

```python
class VideoPlayer(types.KX_PythonComponent):
    # ... args, start, update ...

    class Editor:
        fields = False          # esconde a lista padrão de campos

        def draw_ui(self, layout, obj, comp):
            # layout é o layout do Blender
            layout.prop(obj, "name")
            layout.label("Arquivo: %s" % comp.args["File"])
```

Com `fields = False`, só o seu `draw_ui` aparece. O **Video Player** e o **Rigid Body Joint** da engine já são feitos assim. Se o `draw_ui` der erro, aparece um aviso vermelho e o resto da caixa continua.
