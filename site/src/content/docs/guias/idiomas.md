---
title: Idiomas do jogo (Range.locale)
description: Traduzir os textos do jogo com uma tabela, trocar o idioma na hora e usar outra fonte por idioma.
---

A Anastacio traduz os textos do jogo sem precisar de código. As traduções ficam numa tabela, `locale/translations.csv`, ao lado do `.range`. Ela abre no Excel, no LibreOffice ou no Google Sheets.

## 1. Prepare no editor

1. **Salve o `.range`.** A pasta `locale/` é criada ao lado dele.
2. Abra **Properties > Scene > Game Languages** e clique em **Enable Languages**. Escolha em que idioma os textos estão escritos e qual é a primeira tradução. Todos os textos da cena já entram na tabela.
3. **Escreva as traduções.** **Open Table** abre a tabela no Text Editor (Alt+S salva). Se preferir, abra `locale/translations.csv` numa planilha. Cada linha é um texto e cada coluna é um idioma. Célula vazia mostra o idioma original. O painel mostra quantos textos faltam em cada idioma.
4. **Confira na viewport.** **Preview Language** mostra os textos no idioma escolhido. O arquivo sempre guarda o original.
5. **Menu de idioma.** Selecione um texto e clique em **Make it a Language Button** (aba do texto > **Translation**). No jogo, cada clique nele passa para o próximo idioma, e o texto mostra o nome do idioma ("Português (Brasil)").

A escolha do jogador fica salva. Na primeira vez, o jogo usa o idioma do sistema operacional.

### Mais coisas no painel

- **Texto novo:** clique em **Translate All Texts** de novo. O painel avisa quando há textos fora da tabela.
- **Mais idiomas:** **Add Language**. O `X` ao lado de um idioma remove a coluna.
- **Letras que a fonte não tem (russo, japonês…):** **Generate Atlases** grava as letras de cada idioma. Para usar outra fonte num idioma, preencha `font` no `locale.json` (botão **Config**).
- **Language Button:** em **Game > Components** dá para escolher a ação (Next, Previous ou Set num idioma), uma tecla e se o texto mostra o nome do idioma.

## 2. Os arquivos

`locale/translations.csv`: primeira coluna é a chave, as outras são os idiomas (códigos como `en`, `pt-BR`, `es`, `ru`). Colunas `context`, `note` ou que começam com `_` são ignoradas, então servem para anotações.

```
key,pt-BR,en,ru
menu.play,Jogar,Play,Играть
hud.lap,Volta {lap} de {total},Lap {lap} of {total},Круг {lap} из {total}
```

`locale/locale.json` (opcional): idioma base, nomes e fonte/atlas por idioma.

```json
{
  "base": "pt-BR",
  "languages": {
    "ru": { "font": "Roboto-Regular", "atlas": "LocaleAtlas_ru" }
  }
}
```

Quando falta a tradução, a engine tenta nesta ordem: `pt-BR` → `pt` → idioma base → a própria chave.

## 3. Em scripts (opcional)

```python
import Range

Range.locale.language = "pt-BR"              # troca todos os textos na hora
Range.locale.tr("hud.lap", lap=2, total=3)   # "Volta 2 de 3"
Range.locale.next()                          # próximo idioma da tabela
Range.locale.languages                       # ['pt-BR', 'en', 'ru']
Range.locale.name()                          # 'Português (Brasil)'
```

| Item | O que faz |
|---|---|
| `language` | Código do idioma atual. Mudar atualiza todos os textos traduzidos e salva a escolha. |
| `languages` | Idiomas da tabela, na ordem das colunas. |
| `baseLanguage` | Idioma base (do `locale.json` ou a primeira coluna). |
| `systemLanguage` | Idioma do sistema operacional, ou `""`. |
| `keys` | Todas as chaves da tabela. |
| `tr(key, **valores)` | Texto da chave no idioma atual, com `{campos}` preenchidos. `get` é o mesmo. |
| `has(key)` | `True` se a chave existe na tabela. |
| `set_language(code, save=True)` | Igual a mudar `language`; com `save=False` não salva a escolha. |
| `next()` / `previous()` / `step(n)` | Anda pela lista de idiomas e devolve o novo código. |
| `name(code=None)` | Nome do idioma na própria língua ("Русский"). |
| `reload()` | Lê a tabela e o `locale.json` de novo. |
| `onChange` | Lista de funções `f(codigo)` chamadas depois de trocar o idioma. |

```python
import Range

def atualizar_hud(codigo):
    print("idioma agora é", Range.locale.name(codigo))

Range.locale.onChange.append(atualizar_hud)
```

### Com logic bricks

Sensores **Mouse Over** + **Left Button** → controlador **Python** em modo **Module** com `range_locale.next` (ou `range_locale.previous`). Não precisa de script.

## 4. Textos pelo Python

Cada texto ([`KX_FontObject`](../../api/types/kx_fontobject/)) tem:

- `translationKey`: chave da tabela. Com ela, o texto troca sozinho quando o idioma muda.
- `useLanguageFont`: usa a fonte e o atlas do idioma atual.
- `font` e `atlas`: trocam a fonte ou o Bitmap Atlas na hora.

```python
import Range

texto = Range.logic.getCurrentScene().objects["Titulo"]
texto.translationKey = "menu.play"
texto.useLanguageFont = True
```
