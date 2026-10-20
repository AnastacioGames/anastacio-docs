---
title: Языки игры (Range.locale)
description: Перевод текстов игры через таблицу, смена языка на лету и отдельный шрифт для каждого языка.
---

Anastacio переводит тексты игры без кода. Переводы хранятся в таблице `locale/translations.csv` рядом с `.range`. Её можно открыть в Excel, LibreOffice или Google Sheets.

## 1. Настройка в редакторе

1. **Сохраните `.range`.** Рядом с ним появится папка `locale/`.
2. Откройте **Properties > Scene > Game Languages** и нажмите **Enable Languages**. Выберите язык, на котором написаны тексты, и первый перевод. Все тексты сцены попадут в таблицу.
3. **Напишите переводы.** **Open Table** открывает таблицу в Text Editor (Alt+S сохраняет). Можно открыть `locale/translations.csv` и в табличном редакторе. Каждая строка — текст, каждый столбец — язык. Пустая ячейка показывает исходный язык. Панель показывает, сколько текстов не переведено на каждый язык.
4. **Проверьте во вьюпорте.** **Preview Language** показывает тексты на выбранном языке. Файл всегда хранит оригинал.
5. **Меню языка.** Выделите текст и нажмите **Make it a Language Button** (вкладка текста > **Translation**). В игре каждый клик переключает на следующий язык, а текст показывает название языка ("Português (Brasil)").

Выбор игрока сохраняется. При первом запуске игра берёт язык операционной системы.

### Ещё в панели

- **Новый текст:** снова нажмите **Translate All Texts**. Панель предупреждает о текстах, которых нет в таблице.
- **Больше языков:** **Add Language**. `X` рядом с языком удаляет столбец.
- **Буквы, которых нет в шрифте (русский, японский…):** **Generate Atlases** сохраняет буквы каждого языка. Чтобы использовать другой шрифт для языка, заполните `font` в `locale.json` (кнопка **Config**).
- **Language Button:** в **Game > Components** можно выбрать действие (Next, Previous или Set на конкретный язык), клавишу и показывать ли название языка.

## 2. Файлы

`locale/translations.csv`: первый столбец — ключ, остальные — языки (коды вроде `en`, `pt-BR`, `es`, `ru`). Столбцы `context`, `note` и начинающиеся с `_` игнорируются, их можно использовать для заметок.

```
key,pt-BR,en,ru
menu.play,Jogar,Play,Играть
hud.lap,Volta {lap} de {total},Lap {lap} of {total},Круг {lap} из {total}
```

`locale/locale.json` (необязательно): базовый язык, названия и шрифт/атлас для каждого языка.

```json
{
  "base": "pt-BR",
  "languages": {
    "ru": { "font": "Roboto-Regular", "atlas": "LocaleAtlas_ru" }
  }
}
```

Если перевода нет, движок пробует по порядку: `pt-BR` → `pt` → базовый язык → сам ключ.

## 3. В скриптах (необязательно)

```python
import Range

Range.locale.language = "ru"                 # сразу меняет все тексты
Range.locale.tr("hud.lap", lap=2, total=3)   # "Круг 2 из 3"
Range.locale.next()                          # следующий язык таблицы
Range.locale.languages                       # ['pt-BR', 'en', 'ru']
Range.locale.name()                          # 'Русский'
```

| Элемент | Что делает |
|---|---|
| `language` | Код текущего языка. Изменение обновляет все переведённые тексты и сохраняет выбор. |
| `languages` | Языки таблицы в порядке столбцов. |
| `baseLanguage` | Базовый язык (из `locale.json` или первый столбец). |
| `systemLanguage` | Язык операционной системы или `""`. |
| `keys` | Все ключи таблицы. |
| `tr(key, **значения)` | Текст ключа на текущем языке с подставленными `{полями}`. `get` — то же самое. |
| `has(key)` | `True`, если ключ есть в таблице. |
| `set_language(code, save=True)` | То же, что изменить `language`; с `save=False` выбор не сохраняется. |
| `next()` / `previous()` / `step(n)` | Переходит по списку языков и возвращает новый код. |
| `name(code=None)` | Название языка на нём самом ("Português"). |
| `reload()` | Заново читает таблицу и `locale.json`. |
| `onChange` | Список функций `f(код)`, вызываемых после смены языка. |

```python
import Range

def obnovit_hud(kod):
    print("теперь язык:", Range.locale.name(kod))

Range.locale.onChange.append(obnovit_hud)
```

### С логическими блоками

Сенсоры **Mouse Over** + **Left Button** → контроллер **Python** в режиме **Module** с `range_locale.next` (или `range_locale.previous`). Скрипт не нужен.

## 4. Тексты из Python

У каждого текста ([`KX_FontObject`](../../api/types/kx_fontobject/)) есть:

- `translationKey`: ключ таблицы. С ним текст сам обновляется при смене языка.
- `useLanguageFont`: использует шрифт и атлас текущего языка.
- `font` и `atlas`: меняют шрифт или Bitmap Atlas на лету.

```python
import Range

tekst = Range.logic.getCurrentScene().objects["Title"]
tekst.translationKey = "menu.play"
tekst.useLanguageFont = True
```
