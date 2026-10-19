---
title: Первый скрипт
description: Скрипт на Python, который двигает объект по нажатию клавиши.
---

1. Выберите объект в сцене и добавьте сенсор **Always** (с включённым *True Level Triggering*), подключённый к контроллеру **Python**.
2. Создайте в текстовом редакторе текст `mover.py` и выберите его в контроллере.
3. Вставьте код и нажмите **P** для запуска.

![Сенсор Always, подключённый к контроллеру Python со скриптом mover.py, и код в текстовом редакторе](../../../../assets/guias/logic-bricks-mover.png)

```python
import Range
from Range import logic, events

cont = logic.getCurrentController()
own = cont.owner
teclado = logic.keyboard

if teclado.inputs[events.WKEY].active:
    own.applyMovement((0, 0.1, 0), True)   # движение вперёд
if teclado.inputs[events.SKEY].active:
    own.applyMovement((0, -0.1, 0), True)
```

В коде португальские имена, те же, что на скриншотах: `mover` = двигать, `teclado` = клавиатура, `Velocidade` = скорость.

- `logic.getCurrentController()` возвращает контроллер, выполняющий скрипт.
- `own` — объект-владелец контроллера, [`KX_GameObject`](../../api/types/kx_gameobject/).
- `applyMovement(vector, local)` перемещает объект; `True` использует собственные оси объекта.

## То же самое с компонентом

Компонент делает ту же работу без logic bricks. Это класс Python, прикреплённый к объекту; его параметры можно менять в панели, не трогая код.

1. Создайте в текстовом редакторе текст `mover_componente.py` (имя должно заканчиваться на `.py`) и вставьте код ниже.
2. Выберите объект и откройте в свойствах вкладку компонентов (значок Python). В **Existing Components** выберите **In .Range File** в разделе *Modules*, затем класс **Mover** в разделе *Classes* и нажмите **Register**. Если класс не появился, нажмите кнопку обновления в углу панели.
3. Компонент появится в **Object's Components** с полем **Velocidade**. При желании измените его и нажмите **P** для запуска.

![Компонент Mover, зарегистрированный на объекте, с полем Velocidade, и код в текстовом редакторе](../../../../assets/guias/componente-mover.png)

```python
import Range
from Range import logic, events
from collections import OrderedDict


class Mover(Range.types.KX_PythonComponent):
    # параметры, которые появляются в панели Components
    args = OrderedDict([
        ("Velocidade", 0.1),
    ])

    def start(self, args):
        # выполняется один раз, при запуске игры
        self.velocidade = args["Velocidade"]

    def update(self):
        # выполняется каждый кадр
        teclado = logic.keyboard
        if teclado.inputs[events.WKEY].active:
            self.object.applyMovement((0, self.velocidade, 0), True)   # движение вперёд
        if teclado.inputs[events.SKEY].active:
            self.object.applyMovement((0, -self.velocidade, 0), True)
```

- Класс наследуется от [`KX_PythonComponent`](../../api/types/kx_pythoncomponent/).
- `args` задаёт параметры панели. Порядок в `OrderedDict` — это порядок их отображения.
- `start(args)` получает значения из панели; `update()` выполняется каждый кадр, до logic bricks.
- `self.object` — объект-владелец компонента, вместо `cont.owner` в скрипте.

**Скрипт или компонент?** Используйте скрипт с logic bricks, чтобы визуально соединять сенсоры и актуаторы. Используйте компонент, когда вся логика на Python и вы хотите повторно использовать один класс на нескольких объектах, каждый со своими значениями.
