---
title: Idiomas del juego (Range.locale)
description: Traducir los textos del juego con una tabla, cambiar el idioma al instante y usar otra fuente por idioma.
---

Anastacio traduce los textos del juego sin código. Las traducciones viven en una tabla, `locale/translations.csv`, junto al `.range`. Se abre en Excel, LibreOffice o Google Sheets.

## 1. Prepáralo en el editor

1. **Guarda el `.range`.** La carpeta `locale/` se crea junto a él.
2. Abre **Properties > Scene > Game Languages** y haz clic en **Enable Languages**. Elige en qué idioma están escritos los textos y la primera traducción. Todos los textos de la escena entran en la tabla.
3. **Escribe las traducciones.** **Open Table** abre la tabla en el Text Editor (Alt+S guarda). También puedes abrir `locale/translations.csv` en una hoja de cálculo. Cada fila es un texto y cada columna es un idioma. Una celda vacía muestra el idioma original. El panel muestra cuántos textos faltan por idioma.
4. **Revisa en el viewport.** **Preview Language** muestra los textos en el idioma elegido. El archivo siempre guarda el original.
5. **Menú de idioma.** Selecciona un texto y haz clic en **Make it a Language Button** (pestaña del texto > **Translation**). En el juego, cada clic pasa al siguiente idioma y el texto muestra el nombre del idioma ("Português (Brasil)").

La elección del jugador se guarda. La primera vez, el juego usa el idioma del sistema operativo.

### Más en el panel

- **Texto nuevo:** haz clic otra vez en **Translate All Texts**. El panel avisa cuando hay textos fuera de la tabla.
- **Más idiomas:** **Add Language**. La `X` junto a un idioma quita la columna.
- **Letras que la fuente no tiene (ruso, japonés…):** **Generate Atlases** guarda las letras de cada idioma. Para usar otra fuente en un idioma, completa `font` en `locale.json` (botón **Config**).
- **Language Button:** en **Game > Components** puedes elegir la acción (Next, Previous o Set a un idioma), una tecla y si el texto muestra el nombre del idioma.

## 2. Los archivos

`locale/translations.csv`: la primera columna es la clave y las demás son idiomas (códigos como `en`, `pt-BR`, `es`, `ru`). Las columnas `context`, `note` o que empiezan con `_` se ignoran, así que sirven para notas.

```
key,pt-BR,en,ru
menu.play,Jogar,Play,Играть
hud.lap,Volta {lap} de {total},Lap {lap} of {total},Круг {lap} из {total}
```

`locale/locale.json` (opcional): idioma base, nombres y fuente/atlas por idioma.

```json
{
  "base": "pt-BR",
  "languages": {
    "ru": { "font": "Roboto-Regular", "atlas": "LocaleAtlas_ru" }
  }
}
```

Cuando falta una traducción, el motor intenta en este orden: `pt-BR` → `pt` → idioma base → la propia clave.

## 3. En scripts (opcional)

```python
import Range

Range.locale.language = "pt-BR"              # cambia todos los textos al instante
Range.locale.tr("hud.lap", lap=2, total=3)   # "Volta 2 de 3"
Range.locale.next()                          # siguiente idioma de la tabla
Range.locale.languages                       # ['pt-BR', 'en', 'ru']
Range.locale.name()                          # 'Português (Brasil)'
```

| Elemento | Qué hace |
|---|---|
| `language` | Código del idioma actual. Cambiarlo actualiza todos los textos traducidos y guarda la elección. |
| `languages` | Idiomas de la tabla, en el orden de las columnas. |
| `baseLanguage` | Idioma base (de `locale.json` o la primera columna). |
| `systemLanguage` | Idioma del sistema operativo, o `""`. |
| `keys` | Todas las claves de la tabla. |
| `tr(key, **valores)` | Texto de la clave en el idioma actual, con los `{campos}` completados. `get` es lo mismo. |
| `has(key)` | `True` si la clave está en la tabla. |
| `set_language(code, save=True)` | Igual que cambiar `language`; con `save=False` no guarda la elección. |
| `next()` / `previous()` / `step(n)` | Recorre la lista de idiomas y devuelve el nuevo código. |
| `name(code=None)` | Nombre del idioma en su propia lengua ("Русский"). |
| `reload()` | Vuelve a leer la tabla y `locale.json`. |
| `onChange` | Lista de funciones `f(codigo)` llamadas después de cambiar el idioma. |

```python
import Range

def actualizar_hud(codigo):
    print("el idioma ahora es", Range.locale.name(codigo))

Range.locale.onChange.append(actualizar_hud)
```

### Con logic bricks

Sensores **Mouse Over** + **Left Button** → controlador **Python** en modo **Module** con `range_locale.next` (o `range_locale.previous`). No hace falta script.

## 4. Textos desde Python

Cada texto ([`KX_FontObject`](../../api/types/kx_fontobject/)) tiene:

- `translationKey`: clave de la tabla. Con ella, el texto se actualiza solo cuando cambia el idioma.
- `useLanguageFont`: usa la fuente y el atlas del idioma actual.
- `font` y `atlas`: cambian la fuente o el Bitmap Atlas al instante.

```python
import Range

texto = Range.logic.getCurrentScene().objects["Titulo"]
texto.translationKey = "menu.play"
texto.useLanguageFont = True
```
