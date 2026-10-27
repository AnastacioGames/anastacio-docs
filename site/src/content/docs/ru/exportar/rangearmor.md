---
title: Экспорт на ПК (RangeArmor)
description: Пошаговая сборка исполняемого файла игры для Windows и Linux с помощью RangeArmor.
---

**RangeArmor** — инструмент, который упаковывает игру для ПК. Он объединяет рантайм движка, ваш защищённый `.range` и лаунчер в исполняемый файл, который игрок открывает двойным щелчком. Один экспорт может создать сборки и для **Windows 64-bit**, и для **Linux 64-bit**.

:::note
Панель RangeArmor работает в Windows и Linux (начиная с 0.5.3). В обеих системах она экспортирует под Windows и Linux.
:::

## 1. Установка RangeArmor

RangeArmor скачивается отдельно от движка, на той же странице релиза: `RangeArmor-<version>-windows-x64.zip` для Windows или `RangeArmor-<version>-linux-x86_64.tar.xz` для Linux.

1. Распакуйте архив.
2. Переименуйте распакованную папку в **`rangearmor`** и положите её **внутрь папки движка**, рядом с `AnastacioEngine.exe` (в Linux — рядом с `AnastacioEngine`):

```
AnastacioEngine-0.6.0-windows-x64/
├── AnastacioEngine.exe
├── AnastacioRuntime.exe
└── rangearmor/
    ├── RangeArmor Panel.exe
    └── release/
```

Движок ищет именно `rangearmor/RangeArmor Panel.exe` (в Linux — `rangearmor/RangeArmor Panel`) в этом месте. Если папка называется иначе, кнопки экспорта не найдут инструмент.

## 2. Создание проекта

RangeArmor работает с папкой проекта фиксированной структуры. Проще всего создать её из движка:

![Меню File](../../../../assets/exportar/menu_file.png)

В меню **File** есть **Create Project**, **Export Game With RANGEARMOR** и **Save .Range Protected File**.

1. **File > Create Project**.
2. Выберите, где создать, и дайте имя (без `< > : " / \ | ? *`).
3. Движок создаст такую структуру и откроет новый `.range`:

```
MyGame/
├── data/            ← .range игры кладётся СЮДА
│   ├── MyGame.range
│   ├── scripts/  textures/  models/  audio/  fonts/  scenes/  libloads/
├── engine/          ← рантайм, копируемый при экспорте
├── launcher/        ← config.json и лаунчер
├── icons/
└── release/         ← результат экспорта
```

:::caution[Самое важное правило]
Главный `.range` должен находиться **внутри папки проекта `data/`**. Если он в другом месте, экспорт сообщит: *"Current file is not inside a RangeArmor project"*.
:::

Уже есть готовая игра? Создайте проект, затем скопируйте ваш `.range` и его файлы (текстуры, звуки, скрипты) в `data/`, сохранив те же подпапки, чтобы относительные пути продолжали работать.

![Панель RangeArmor](../../../../assets/exportar/armor_en.png)

## 3. Настройка панели Export (RangeArmor)

В **Properties > Export Game > Export (RangeArmor)**:

| Поле | Что делает |
|---|---|
| **Windows 64-bit / Linux 64-bit** | Платформы для сборки. Можно включить обе. |
| **Product Name** | Название игры, используется для исполняемого файла и пакета. |
| **Version** | Версия пакета, например `1.0.0`. |
| **Company Name** | Ваше имя или студия. |
| **Icon** | Файл `.ico` для исполняемого файла. Если пусто — значок по умолчанию. |
| **Cook before export** | Собирает «запечённый» кэш (готовые физика и шейдеры), чтобы игра открывалась быстрее. Оставьте включённым. |

Пустые поля сохраняют значения RangeArmor по умолчанию.

## 4. Экспорт

Есть две кнопки:

- **Export Game (1 Click)**: сохраняет защищённую копию, запекает кэш и собирает всё прямо в `MyGame/release/`. По завершении папка открывается. **Это рекомендуемый путь.**
  Также собирается **Universal**-пакет: одна папка (и zip) с Windows и Linux вместе. Игрок запускает `MyGame.exe` в Windows или `MyGame` в Linux. *(начиная с 0.6.0)*
- **Open RangeArmor Panel**: открывает полный инструмент с дополнительными параметрами. Настройки панели движка передаются в него.

Та же панель открывается и через **File > Export Game With RANGEARMOR**.

:::tip
Если видите *"Could not find a Python interpreter for the export"*, откройте RangeArmor Panel один раз, нажмите **Get RanGE** и попробуйте 1 Click снова.
:::

## Другой способ: RangeArmor Panel отдельно

Можно экспортировать и без кнопок движка, открыв внешний инструмент напрямую. Это полезно, чтобы экспортировать старый проект или изменить параметры, которых нет в панели движка.

![Стартовый экран RangeArmor Panel](../../../../assets/exportar/rangearmor_inicio.png)

Стартовый экран RangeArmor Panel: **Open Project**, **New Project** и список **Recent projects**.

1. Откройте **`rangearmor/RangeArmor Panel.exe`** (в Linux — `rangearmor/RangeArmor Panel`) в папке движка. Он также открывается кнопкой **Open RangeArmor Panel** или через **File > Export Game With RANGEARMOR**.
2. На стартовом экране нажмите **New Project**, чтобы создать новую папку проекта, или **Open Project**, чтобы открыть существующую (например, созданную через **File > Create Project**). Ранее открытые проекты отображаются в **Recent projects**.
3. В движке откройте ваш `.range` и сохраните защищённую копию через **File > Save .Range Protected File** в папку проекта `data/`. У неё расширение `.rasec`.
4. Вернувшись в панель, на вкладке **Project**:

| Поле | Что делает |
|---|---|
| **Game Name** | Название игры. |
| **Version** | Версия игры. |
| **Main File** | Файл `.rasec` из шага 3. Пока там пример, экспорт заблокирован. |
| **Data Source** | Папка с файлами игры (обычно `data`). |
| **Compile Python scripts** | Поставляет скомпилированные скрипты вместо исходного кода. |

5. На вкладке **Paths** проверьте **Engine executables** (рантайм для каждой платформы) и **Python for authoring tools**. Если они пусты, используйте **Copy Available Range Engine Files** на вкладке **Tasks** — это копирует рантайм движка в папку проекта `engine/`.
   ![Вкладка Paths в RangeArmor Panel](../../../../assets/exportar/rangearmor_paths.png)

   Пути **красного** цвета с пустым флажком — это файлы, которых ещё нет в папке проекта `engine/`. После **Copy Available Range Engine Files** они отмечаются (✓), и платформа внизу считается готовой.

6. Нажмите **Save**, чтобы сохранить настройки.
7. На вкладке **Tasks**:
   - **Run game**: запускает игру так, как её увидит игрок, чтобы сначала проверить.
   - **Set Icons**: выбирает значки `.ico` для лаунчера и исполняемого файла.
   - **Export to**: экспортирует одну платформу или **All Platforms**. **Compress targets after export** создаёт zip.
   - **Universal (Win + Linux)**: помимо папок каждой платформы создаёт `MyGame-<версия>-Universal/` — одну папку для обеих систем. Нужны оба рантайма на вкладке **Paths**. *(начиная с 0.6.0)*
   ![Вкладка Tasks в RangeArmor Panel](../../../../assets/exportar/rangearmor_tasks.png)

   Серые кнопки платформ и надпись *0/2 platform(s) ready* внизу означают, что не хватает рантайма. Нажмите **Copy Available Range Engine Files** (шаг 5) и проверьте **Main File** и **Data Source**; кнопки загорятся, когда платформа будет готова.

8. Результат попадает в папку проекта `release/`. **Explore** открывает папку, а **Copy Log** копирует лог, если что-то пошло не так.

:::note
Кнопка движка **Export Game (1 Click)** выполняет шаги 3–7 сама и вдобавок запекает кэш. Используйте внешнюю панель, когда нужен ручной контроль.
:::

## 5. Проверка и выпуск

1. Откройте `release/` и **распакуйте созданный zip в любую папку вне проекта**.
2. Запустите исполняемый файл игры и пройдите её от начала до конца.
3. Если всё работает, этот zip и отправляйте игрокам (itch.io, Steam, Google Drive...).

Проверка вне проекта важна: внутри него игра может находить файлы, которые так и не попали в пакет.

## Защита файла

Экспортированная игра использует **защищённую** копию `.range` (расширение `.rasec`), которая не открывается в редакторе. Эту копию можно создать и вручную через **File > Save .Range Protected File**. Всегда храните оригинальный `.range`: только его можно редактировать.

## Частые проблемы

| Сообщение | Решение |
|---|---|
| *Save the .blend file inside the project's data/ folder first* | Сохраните файл внутри `data/`. |
| *Current file is not inside a RangeArmor project* | `.range` не находится в `<project>/data/`. Используйте **File > Create Project**. |
| *build_release.py not found next to RangeArmor Panel* | Папка `rangearmor/` отсутствует или названа неправильно. См. шаг 1. |
| *Export finished with errors* | Откройте консоль (**Window > Toggle System Console**), чтобы увидеть полную ошибку. |
| *Universal package skipped: no runtime for ...* | Не хватает рантайма одной из платформ. Укажите Windows и Linux на вкладке **Paths** (или нажмите **Copy Available Range Engine Files**). |
