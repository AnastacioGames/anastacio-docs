---
title: UI Tree (меню и HUD в Node Editor)
description: Создавайте 2D-меню и HUD игры из нод без кода. Работает на ПК, в Web и на Android.
---

**UI Tree** — тип дерева в Node Editor для 2D-интерфейса игры: главное меню, настройки, пауза и HUD. Всё рисуется поверх игры и работает на ПК, в Web и на Android.

## Быстрый старт

1. В Node Editor выберите тип **UI Tree** и нажмите **New**.
2. В панели **UI Tree** (клавиша N или вкладка на полке T) нажмите **+ Menu** и/или **+ HUD**.
   - **Menu**: экраны `Menu` (Играть, Настройки, Выход) и `Opcoes` (Звук, Громкость, Назад).
   - **HUD**: полоса и текст здоровья сверху, спидометр снизу, кнопка **II** (пауза) внизу по центру и кнопки **A** и **B** внизу слева — для сенсорного экрана.
3. Нажмите **Setup Game Logic**. Он добавляет камере сцены сенсор Always (пульс) с контроллером Python Module `range_ui_runtime.main` и создаёт свойства `ui_screen`, `ui_hud`, `som`, `volume`, `vida`, `velocidade`, `botao_a` и `botao_b`. Повторный запуск ничего не дублирует.
4. Нажмите **P**. Bake выполняется автоматически при запуске и сохранении.

## Элементы

- **Screen**: Frame, помеченный как экран (**Add > Widgets > Screen**): Fade, стандартные звуки, Scale Mode (**Stretch** или **Keep Aspect**), фон только для редактора (**Capture Camera**).
- **HUD Screen**: всегда под меню. С заполненным **Camera** рисуется только во вьюпорте этой камеры (split screen).
- **Виджеты**: Button, Toggle, Slider, Panel, Image; для HUD: Progress Bar, Label (`{vida:.0f}`) и Gauge. Поле **Object** позволяет читать свойства другого объекта.
- **События Button**: On Enter, On Exit, On Over, On Press, On Release, On Click. У Toggle и Slider есть **On Change**.
- **Действия**: Print, Send Message, Go To Screen, Change Scene, Quit Game, Play Sound, Set/Add/Toggle Property, Run Python (`module.function(ui)`).
- **Состояния**: **Enabled If** и **Selected If** (свойство bool).
- **Якорь**: в Keep Aspect каждый виджет привязан к одной из 9 точек экрана.

## Управление из игры

- Свойство `ui_screen`: имя экрана; `""` скрывает меню. Свойство `ui_hud` (bool) показывает или скрывает HUD.
- Клавиатура и геймпад: стрелки или стик меняют фокус; Enter, Пробел или A нажимают.

```python
import range_ui_runtime

range_ui_runtime.show("Menu")
range_ui_runtime.hide()
range_ui_runtime.set_hud(True)
```

## Спидометр и кнопки HUD

- **Спидометр без скрипта**: укажите в поле **Object** у Gauge имя машины или персонажа. HUD измеряет, насколько объект сместился за кадр, и выдаёт км/ч как `velocidade` (и `speed`). Работает с физикой, Motion и прыжками.
- **II**: пауза — возврат в меню и скрытие HUD.
- **A** и **B**: пока нажаты, `botao_a` и `botao_b` на камере равны `True`; читайте их в своём скрипте.
