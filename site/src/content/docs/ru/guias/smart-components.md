---
title: Smart Components (Range.args и класс Editor)
description: Поля со слайдерами, подсказками и выбором объекта, предупреждения и кнопки в редакторе — без изменений в игре.
---

Обычный Python-компонент содержит `args` и код игры. **Smart Component** — тот же компонент с двумя дополнительными возможностями, обе необязательны:

1. **Удобные поля** через `Range.args`: слайдеры с пределами, подсказки при наведении, разделы, списки в заданном порядке и выбор объекта или сцены мышью.
2. **Класс `Editor`**, который работает только в редакторе: настраивает объект при добавлении, показывает предупреждения у полей, добавляет кнопки и рисует подсказки во вьюпорте.

Игра не меняется: `args["Speed"]` по-прежнему `float`, а экспортированная игра работает без `bpy`. Старые компоненты работают как раньше.

:::tip[Готовый пример]
В Text Editor меню **Templates > Components > 04 Smart Component** открывает полный пример преследователя со всем, что описано здесь.
:::

## 1. Поля через Range.args

```python
from collections import OrderedDict
from Range import types
from Range.args import Float, Int, Bool, Text, Choice, Object, Scene, Color, Header

class Chaser(types.KX_PythonComponent):
    args = OrderedDict([
        Header("Target", icon="OBJECT_DATA"),
        ("Target", Object(tip="Объект, за которым он гонится")),
        ("Stop distance", Float(1.5, min=0, max=10, tip="Останавливается на этом расстоянии")),

        Header("Movement", icon="AUTO"),
        ("Speed", Float(3.0, min=0, max=20, tip="Метров в секунду")),
        ("Mode", Choice("Walk", "Walk", "Run", "Jump")),
        ("Face target", Bool(True, tip="Поворачивается к цели")),
        ("Scene on catch", Scene(tip="Сцена, добавляемая поверх, когда игрок пойман")),
        ("Alert color", Color(1.0, 0.1, 0.1, 1.0, tip="Цвет мигания")),
    ])

    def start(self, args):
        self.target = args["Target"]        # KX_GameObject или None
        self.speed = args["Speed"]
```

| Поле | В редакторе | В игре приходит как |
|---|---|---|
| `Float(value, min, max, tip)` | число; слайдер, если заданы `min` и `max` | `float` |
| `Int(value, min, max, tip)` | целое; слайдер, если заданы `min` и `max` | `int` |
| `Bool(value, tip)` | флажок | `bool` |
| `Text(value, tip)` | текстовое поле | `str` |
| `Choice(default, item1, item2, ..., tip)` | список в заданном порядке | `str` |
| `Object(tip)` | выбор объекта сцены | `KX_GameObject` или `None` |
| `Scene(tip)` | выбор сцены файла | `str` с именем (`""`, если пусто), готово для `logic.addScene` |
| `Color(r, g, b[, a], tip)` | цвет с палитрой (3 или 4 значения) | `Color` (для `obj.color` используйте 4 значения) |
| `Header(name, icon, open)` | сворачиваемый заголовок раздела | (не поле) |

Значения за пределами ограничиваются: 50 в `Float(max=20)` превращается в 20. Старый формат (`("Name", 1.0)`) работает в том же списке, просто без подсказки. Переименование выбранного объекта или сцены обновляет поле автоматически.

## 2. Требования при добавлении: `requires`

```python
class Chaser(types.KX_PythonComponent):
    requires = {"physics": "NO_COLLISION", "components": ["health.Health"]}
```

При добавлении компонента редактор настраивает тип физики объекта и добавляет перечисленные компоненты.

## 3. Класс Editor

Объявляется внутри компонента. Игра его никогда не запускает. Можно использовать `bpy`, но импортируйте его только внутри методов. Внутри `self.object` — объект, а `self.args["Поле"]` читает и записывает поля.

```python
class Chaser(types.KX_PythonComponent):
    # ... args, start, update ...

    class Editor:
        buttons = [
            ("Drop to ground", "drop_to_ground", "TRIA_DOWN_BAR"),
        ]

        def on_attach(self, obj):
            # один раз, сразу после добавления компонента к объекту
            self.args["Name"] = obj.name

        def on_change(self, obj, name, value):
            # вызывается для каждого поля при изменении и при открытии файла;
            # возвращённый текст показывается предупреждением под полем
            if name == "Speed" and value > 15:
                return "Слишком быстро: может пройти сквозь стены"
            if name == "Target" and value is None:
                return "Нет цели: будет стоять на месте"

        def drop_to_ground(self, obj, context):
            context.scene.update()
            lowest_z = min((obj.matrix_world * v.co).z for v in obj.data.vertices)
            obj.location.z -= lowest_z

        def draw_gizmo(self, obj, args, g, selected):
            # рисование во вьюпорте, в игре не видно
            pos = obj.matrix_world.translation
            g.circle(pos, args["Stop distance"], "GREEN")
            if args["Target"] is not None:
                g.arrow(pos, args["Target"].matrix_world.translation, "YELLOW", width=2)
```

| Элемент | Когда вызывается |
|---|---|
| `on_attach(self, obj)` | Один раз, при добавлении компонента. |
| `on_change(self, obj, name, value)` | При изменении поля и при открытии файла. Возвращённый текст становится предупреждением. |
| `buttons = [(text, method, icon)]` | Кнопки внизу блока компонента; метод получает `(obj, context)` и поддерживает отмену. |
| `draw_gizmo(self, obj, args, g, selected)` | При каждой перерисовке вьюпорта. У `g` есть `line`, `path`, `circle`, `sphere`, `box`, `arrow` и `text`; цвета по имени (`"RED"`) или `(r, g, b)`, координаты мировые. |

По умолчанию гизмо видны только у выделенного объекта. Это меняет опция **Overlay > Component Gizmos**.

Ошибки в коде `Editor` показываются красным в блоке компонента и не влияют на игру.

## 4. Свой интерфейс: `draw_ui`

Чтобы рисовать блок компонента по-своему, добавьте `draw_ui(self, layout, obj, comp)` в класс `Editor`. `layout` — обычный layout Blender (`row()`, `column()`, `prop()`, `operator()`, `label()`). Он рисуется после полей и перед кнопками.

```python
class VideoPlayer(types.KX_PythonComponent):
    # ... args, start, update ...

    class Editor:
        fields = False          # скрывает стандартный список полей

        def draw_ui(self, layout, obj, comp):
            # layout — это layout Blender
            layout.prop(obj, "name")
            layout.label("Файл: %s" % comp.args["File"])
```

С `fields = False` показывается только ваш `draw_ui`. **Video Player** и **Rigid Body Joint** движка сделаны именно так. Если в `draw_ui` ошибка, появится красное предупреждение, а остальной блок продолжит работать.
