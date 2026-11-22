# Range.imgui

> **Veja também:**
[`Range.render`](Range.render.md), [`Range.logic`](Range.logic.md)

Módulo `Range.imgui` da Anastacio Engine. Também acessível como `bge.imgui`.

```python
# Uma janela de pausa, desenhada a cada quadro por um componente.
import Range
import Range.imgui as imgui

class PauseMenu(Range.types.KX_PythonComponent):
    args = {}

    def start(self, args):
        self.volume = 0.5
        imgui.set_game_ui_open(True)

    def update(self):
        w, h = imgui.get_display_size()
        imgui.set_next_window_size(300, 200, imgui.COND_FIRST_USE_EVER)
        imgui.set_next_window_pos(w / 2 - 150, h / 2 - 100)

        is_open, want_close = imgui.begin("Pause", closable=True)
        if is_open:
            changed, self.volume = imgui.slider_float("Volume", self.volume, 0.0, 1.0)
            imgui.separator()
            if imgui.button("Quit", width=240):
                Range.logic.endGame()
        imgui.end()
```

```python
# Os widgets comuns retornam se mudaram e o novo valor.
changed, self.fullscreen = imgui.checkbox("Full screen", self.fullscreen)
changed, self.quality = imgui.slider_int("Quality", self.quality, 0, 3)
imgui.same_line()
imgui.text("Level: {}".format(self.quality))
```

```python
# Muda a cor de um botão.
imgui.push_style_color(imgui.COL_BUTTON, 0.8, 0.2, 0.2, 1.0)
imgui.button("Delete save")
imgui.pop_style_color()
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### begin(name, closable=False)

 `função`

Abre uma janela com o título `name`. Tudo que você desenhar até `end()` fica dentro dela. Com `closable=True` a janela ganha o botão X, e `want_close` vira True quando ele é clicado. Sempre chame `end()` depois, mesmo se `is_open` for False.

**Retorna:** `(is_open, want_close)`

### begin_popup_modal(name, closable=False)

 `função`

Desenha o popup modal aberto antes com `open_popup(name)`. Só chame `end_popup()` quando `is_open` for True.

**Retorna:** `(is_open, want_close)`

### button(label, width=0, height=0)

 `função`

Botão com o texto `label`. Devolve True no quadro em que é clicado. Largura e altura 0 ajustam ao texto.

**Retorna:** `bool`

### checkbox(label, value)

 `função`

Caixa de marcar. Passe o valor atual em `value` e guarde `new_value`; `changed` é True quando o jogador clicou.

**Retorna:** `(changed, new_value)`

### close_current_popup()

 `função`

Fecha o popup aberto.

### color_edit3(label, r, g, b)

 `função`

Seletor de cor RGB (valores de 0 a 1). Devolve a cor nova.

**Retorna:** `(changed, r, g, b)`

### color_edit4(label, r, g, b, a)

 `função`

Seletor de cor RGBA com transparência (valores de 0 a 1).

**Retorna:** `(changed, r, g, b, a)`

### combo(label, current_item, items)

 `função`

Lista suspensa. `items` é uma lista de textos e `current_item` o índice escolhido.

**Retorna:** `(changed, new_item)`

### draw_rect_filled(x1, y1, x2, y2, r, g, b, a)

 `função`

-- desenhado acima de todas as janelas, para fades

### end()

 `função`

Fecha a janela começada com `begin()`.

### end_popup()

 `função`

Fecha o bloco de um popup.

### get_cursor_pos()

 `função`

Posição onde o próximo item será desenhado, relativa à janela atual.

**Retorna:** `(x, y)`

### get_cursor_screen_pos()

 `função`

Posição onde o próximo item será desenhado, em pixels da tela.

**Retorna:** `(x, y)`

### get_display_size()

 `função`

Tamanho da área de desenho em pixels. Útil para posicionar janelas e HUD.

**Retorna:** `(width, height)`

### get_io_want_capture_keyboard()

 `função`

True quando a interface está usando o teclado (por exemplo, digitando num campo). Use para não mover o personagem nessa hora.

**Retorna:** `bool`

### get_io_want_capture_mouse()

 `função`

True quando o mouse está sobre a interface. Use para ignorar cliques do jogo nessa hora.

**Retorna:** `bool`

### image(texture_id, w, h)

 `função`

-- texture_id é um bind code OpenGL puro

### input_text(label, value, max_length=256)

 `função`

Campo de texto editável. `max_length` limita o número de caracteres.

**Retorna:** `(changed, new_value)`

### invisible_button(label, width, height)

 `função`

Área clicável sem desenho. Bom para colocar sobre uma imagem. Devolve True quando clicada.

**Retorna:** `bool`

### listbox(label, current_item, items, height_items=-1)

 `função`

Lista com rolagem. `height_items` é quantas linhas aparecem (-1 = automático).

**Retorna:** `(changed, new_item)`

### load_default_font(size)

*(novo na Anastacio)* `função`

**Retorna:** `font_id or None -- engine font with icons; None until built next frame`

### load_font(path, size)

 `função`

Carrega uma fonte .ttf/.otf no tamanho dado. Chame uma vez só; a fonte fica pronta no quadro seguinte. Use o id em `push_font()`.

**Retorna:** `font_id`

### open_popup(name)

 `função`

Abre o popup com esse nome.

### pop_font()

 `função`

Volta à fonte anterior a `push_font()`.

### pop_item_width()

*(novo na Anastacio)* `função`

Volta à largura anterior a `push_item_width()`.

### pop_style_color(count=1)

 `função`

Desfaz as últimas `count` cores de `push_style_color()`.

### pop_style_var(count=1)

*(novo na Anastacio)* `função`

Desfaz os últimos `count` estilos de `push_style_var()`.

### push_font(font_id)

 `função`

Usa outra fonte até `pop_font()`.

### push_item_width(width)

*(novo na Anastacio)* `função`

-- >0 pixels, <0 alinhado à direita da borda da janela (-1 = largura total)

### push_style_color(idx, r, g, b, a)

 `função`

-- idx é uma das constantes imgui.COL_*

### push_style_var(idx, value)

*(novo na Anastacio)* `função`

ou push_style_var(idx, x, y) -- idx é uma das imgui.STYLE_*

### radio_button(label, active)

 `função`

Botão de opção. `active` diz se ele é o escolhido; quando `pressed` for True, guarde essa opção como a escolhida do grupo.

**Retorna:** `pressed`

### same_line()

 `função`

Coloca o próximo item na mesma linha do anterior.

### separator()

 `função`

Desenha uma linha separadora.

### set_cursor_pos(x, y)

 `função`

-- posição relativa à janela atual

### set_game_ui_open(open)

 `função`

-- liga/desliga a entrada + libera o mouse para a UI de jogo desenhada em Python

### set_next_item_width(width)

*(novo na Anastacio)* `função`

-- mesma convenção de push_item_width, só para o próximo widget

### set_next_window_pos(x, y, cond=COND_ALWAYS)

 `função`

Posição da próxima janela, em pixels.

### set_next_window_size(w, h, cond=COND_ALWAYS)

 `função`

Tamanho da próxima janela, em pixels.

### slider_float(label, value, min, max)

 `função`

Barra deslizante para número decimal entre `min` e `max`.

**Retorna:** `(changed, new_value)`

### slider_int(label, value, min, max)

 `função`

Barra deslizante para número inteiro entre `min` e `max`.

**Retorna:** `(changed, new_value)`

### text(text)

 `função`

Mostra um texto.
