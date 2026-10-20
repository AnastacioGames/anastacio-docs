---
title: Game languages (Range.locale)
description: Translate the game's texts with a table, switch language on the fly and use a different font per language.
---

Anastacio translates the game's texts without code. Translations live in a table, `locale/translations.csv`, next to the `.range`. It opens in Excel, LibreOffice or Google Sheets.

## 1. Set it up in the editor

1. **Save the `.range`.** The `locale/` folder is created next to it.
2. Open **Properties > Scene > Game Languages** and click **Enable Languages**. Pick the language your texts are written in and the first translation. Every text in the scene goes into the table.
3. **Write the translations.** **Open Table** opens the table in the Text Editor (Alt+S saves). You can also open `locale/translations.csv` in a spreadsheet. Each row is a text and each column is a language. An empty cell shows the original language. The panel shows how many texts are missing per language.
4. **Check in the viewport.** **Preview Language** shows the texts in the chosen language. The file always keeps the original.
5. **Language menu.** Select a text and click **Make it a Language Button** (text tab > **Translation**). In the game, each click moves to the next language, and the text shows the language name ("Português (Brasil)").

The player's choice is saved. On first launch the game uses the operating system language.

### More in the panel

- **New text:** click **Translate All Texts** again. The panel warns about texts missing from the table.
- **More languages:** **Add Language**. The `X` next to a language removes the column.
- **Letters the font lacks (Russian, Japanese…):** **Generate Atlases** stores the letters of each language. To use a different font for a language, fill `font` in `locale.json` (**Config** button).
- **Language Button:** in **Game > Components** you can pick the action (Next, Previous or Set to a language), a key, and whether the text shows the language name.

## 2. The files

`locale/translations.csv`: the first column is the key, the others are languages (codes like `en`, `pt-BR`, `es`, `ru`). Columns named `context`, `note` or starting with `_` are ignored, so you can use them for notes.

```
key,pt-BR,en,ru
menu.play,Jogar,Play,Играть
hud.lap,Volta {lap} de {total},Lap {lap} of {total},Круг {lap} из {total}
```

`locale/locale.json` (optional): base language, names and font/atlas per language.

```json
{
  "base": "pt-BR",
  "languages": {
    "ru": { "font": "Roboto-Regular", "atlas": "LocaleAtlas_ru" }
  }
}
```

When a translation is missing, the engine tries in this order: `pt-BR` → `pt` → base language → the key itself.

## 3. In scripts (optional)

```python
import Range

Range.locale.language = "pt-BR"              # updates every text at once
Range.locale.tr("hud.lap", lap=2, total=3)   # "Volta 2 de 3"
Range.locale.next()                          # next language in the table
Range.locale.languages                       # ['pt-BR', 'en', 'ru']
Range.locale.name()                          # 'Português (Brasil)'
```

| Item | What it does |
|---|---|
| `language` | Current language code. Setting it updates every translated text and saves the choice. |
| `languages` | Languages in the table, in column order. |
| `baseLanguage` | Base language (from `locale.json` or the first column). |
| `systemLanguage` | Operating system language, or `""`. |
| `keys` | Every key in the table. |
| `tr(key, **values)` | Text for the key in the current language, with `{fields}` filled in. `get` is the same. |
| `has(key)` | `True` if the key is in the table. |
| `set_language(code, save=True)` | Same as setting `language`; with `save=False` the choice is not saved. |
| `next()` / `previous()` / `step(n)` | Moves through the language list and returns the new code. |
| `name(code=None)` | Language name in its own language ("Русский"). |
| `reload()` | Reads the table and `locale.json` again. |
| `onChange` | List of functions `f(code)` called after the language changes. |

```python
import Range

def update_hud(code):
    print("language is now", Range.locale.name(code))

Range.locale.onChange.append(update_hud)
```

### With logic bricks

**Mouse Over** + **Left Button** sensors → **Python** controller in **Module** mode with `range_locale.next` (or `range_locale.previous`). No script needed.

## 4. Texts from Python

Each text ([`KX_FontObject`](../../api/types/kx_fontobject/)) has:

- `translationKey`: table key. With it, the text updates by itself when the language changes.
- `useLanguageFont`: uses the font and atlas of the current language.
- `font` and `atlas`: switch the font or Bitmap Atlas on the fly.

```python
import Range

text = Range.logic.getCurrentScene().objects["Title"]
text.translationKey = "menu.play"
text.useLanguageFont = True
```
