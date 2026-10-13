---
title: "Range.imgui"
description: "Referência do módulo Range.imgui"
---

:::tip[Veja também]
[`Range.render`](../../modulos/render/), [`Range.logic`](../../modulos/logic/)
:::

Módulo `Range.imgui` da Anastacio Engine. Também acessível como `bge.imgui`.

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### begin(name, closable=False)

 <small>função</small>

Abre uma janela com o título `name`. Tudo que você desenhar até `end()` fica dentro dela. Com `closable=True` a janela ganha o botão X, e `want_close` vira True quando ele é clicado. Sempre chame `end()` depois, mesmo se `is_open` for False.

**Retorna:** `(is_open, want_close)`

### begin_popup_modal(name, closable=False)

 <small>função</small>

Desenha o popup modal aberto antes com `open_popup(name)`. Só chame `end_popup()` quando `is_open` for True.

**Retorna:** `(is_open, want_close)`

### button(label, width=0, height=0)

 <small>função</small>

Botão com o texto `label`. Devolve True no quadro em que é clicado. Largura e altura 0 ajustam ao texto.

**Retorna:** `bool`

### checkbox(label, value)

 <small>função</small>

Caixa de marcar. Passe o valor atual em `value` e guarde `new_value`; `changed` é True quando o jogador clicou.

**Retorna:** `(changed, new_value)`

### close_current_popup()

 <small>função</small>

Fecha o popup aberto.

### color_edit3(label, r, g, b)

 <small>função</small>

Seletor de cor RGB (valores de 0 a 1). Devolve a cor nova.

**Retorna:** `(changed, r, g, b)`

### color_edit4(label, r, g, b, a)

 <small>função</small>

Seletor de cor RGBA com transparência (valores de 0 a 1).

**Retorna:** `(changed, r, g, b, a)`

### combo(label, current_item, items)

 <small>função</small>

Lista suspensa. `items` é uma lista de textos e `current_item` o índice escolhido.

**Retorna:** `(changed, new_item)`

### draw_rect_filled(x1, y1, x2, y2, r, g, b, a)

 <small>função</small>

-- desenhado acima de todas as janelas, para fades

### end()

 <small>função</small>

Fecha a janela começada com `begin()`.

### end_popup()

 <small>função</small>

Fecha o bloco de um popup.

### get_cursor_pos()

 <small>função</small>

Posição onde o próximo item será desenhado, relativa à janela atual.

**Retorna:** `(x, y)`

### get_cursor_screen_pos()

 <small>função</small>

Posição onde o próximo item será desenhado, em pixels da tela.

**Retorna:** `(x, y)`

### get_display_size()

 <small>função</small>

Tamanho da área de desenho em pixels. Útil para posicionar janelas e HUD.

**Retorna:** `(width, height)`

### get_io_want_capture_keyboard()

 <small>função</small>

True quando a interface está usando o teclado (por exemplo, digitando num campo). Use para não mover o personagem nessa hora.

**Retorna:** `bool`

### get_io_want_capture_mouse()

 <small>função</small>

True quando o mouse está sobre a interface. Use para ignorar cliques do jogo nessa hora.

**Retorna:** `bool`

### image(texture_id, w, h)

 <small>função</small>

-- texture_id é um bind code OpenGL puro

### input_text(label, value, max_length=256)

 <small>função</small>

Campo de texto editável. `max_length` limita o número de caracteres.

**Retorna:** `(changed, new_value)`

### invisible_button(label, width, height)

 <small>função</small>

Área clicável sem desenho. Bom para colocar sobre uma imagem. Devolve True quando clicada.

**Retorna:** `bool`

### listbox(label, current_item, items, height_items=-1)

 <small>função</small>

Lista com rolagem. `height_items` é quantas linhas aparecem (-1 = automático).

**Retorna:** `(changed, new_item)`

### load_default_font(size)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

**Retorna:** `font_id or None -- engine font with icons; None until built next frame`

### load_font(path, size)

 <small>função</small>

Carrega uma fonte .ttf/.otf no tamanho dado. Chame uma vez só; a fonte fica pronta no quadro seguinte. Use o id em `push_font()`.

**Retorna:** `font_id`

### open_popup(name)

 <small>função</small>

Abre o popup com esse nome.

### pop_font()

 <small>função</small>

Volta à fonte anterior a `push_font()`.

### pop_item_width()

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Volta à largura anterior a `push_item_width()`.

### pop_style_color(count=1)

 <small>função</small>

Desfaz as últimas `count` cores de `push_style_color()`.

### pop_style_var(count=1)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

Desfaz os últimos `count` estilos de `push_style_var()`.

### push_font(font_id)

 <small>função</small>

Usa outra fonte até `pop_font()`.

### push_item_width(width)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

-- >0 pixels, <0 alinhado à direita da borda da janela (-1 = largura total)

### push_style_color(idx, r, g, b, a)

 <small>função</small>

-- idx é uma das constantes imgui.COL_*

### push_style_var(idx, value)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

ou push_style_var(idx, x, y) -- idx é uma das imgui.STYLE_*

### radio_button(label, active)

 <small>função</small>

Botão de opção. `active` diz se ele é o escolhido; quando `pressed` for True, guarde essa opção como a escolhida do grupo.

**Retorna:** `pressed`

### same_line()

 <small>função</small>

Coloca o próximo item na mesma linha do anterior.

### separator()

 <small>função</small>

Desenha uma linha separadora.

### set_cursor_pos(x, y)

 <small>função</small>

-- posição relativa à janela atual

### set_game_ui_open(open)

 <small>função</small>

-- liga/desliga a entrada + libera o mouse para a UI de jogo desenhada em Python

### set_next_item_width(width)

<span class="ae-badge novo">novo na Anastacio</span> <small>função</small>

-- mesma convenção de push_item_width, só para o próximo widget

### set_next_window_pos(x, y, cond=COND_ALWAYS)

 <small>função</small>

Posição da próxima janela, em pixels.

### set_next_window_size(w, h, cond=COND_ALWAYS)

 <small>função</small>

Tamanho da próxima janela, em pixels.

### slider_float(label, value, min, max)

 <small>função</small>

Barra deslizante para número decimal entre `min` e `max`.

**Retorna:** `(changed, new_value)`

### slider_int(label, value, min, max)

 <small>função</small>

Barra deslizante para número inteiro entre `min` e `max`.

**Retorna:** `(changed, new_value)`

### text(text)

 <small>função</small>

Mostra um texto.

