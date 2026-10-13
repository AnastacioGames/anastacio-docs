---
title: "Range.imgui"
description: "Range.imgui module reference"
---

:::tip[See also]
[`Range.render`](../../modulos/render/), [`Range.logic`](../../modulos/logic/)
:::

Anastacio Engine module `Range.imgui`. Also available as `bge.imgui`.

## Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### begin(name, closable=False)

 <small>function</small>

Opens a window titled `name`. Everything you draw until `end()` goes inside it. With `closable=True` the window gets the X button, and `want_close` becomes True when it is clicked. Always call `end()` afterwards, even if `is_open` is False.

**Returns:** `(is_open, want_close)`

### begin_popup_modal(name, closable=False)

 <small>function</small>

Draws the modal popup opened before with `open_popup(name)`. Only call `end_popup()` when `is_open` is True.

**Returns:** `(is_open, want_close)`

### button(label, width=0, height=0)

 <small>function</small>

Button with the text `label`. Returns True on the frame it is clicked. Width and height 0 fit the text.

**Returns:** `bool`

### checkbox(label, value)

 <small>function</small>

Checkbox. Pass the current value in `value` and keep `new_value`; `changed` is True when the player clicked.

**Returns:** `(changed, new_value)`

### close_current_popup()

 <small>function</small>

Closes the open popup.

### color_edit3(label, r, g, b)

 <small>function</small>

RGB color picker (values from 0 to 1). Returns the new color.

**Returns:** `(changed, r, g, b)`

### color_edit4(label, r, g, b, a)

 <small>function</small>

RGBA color picker with transparency (values from 0 to 1).

**Returns:** `(changed, r, g, b, a)`

### combo(label, current_item, items)

 <small>function</small>

Dropdown list. `items` is a list of strings and `current_item` the chosen index.

**Returns:** `(changed, new_item)`

### draw_rect_filled(x1, y1, x2, y2, r, g, b, a)

 <small>function</small>

-- drawn above every window, for fades

### end()

 <small>function</small>

Closes the window started with `begin()`.

### end_popup()

 <small>function</small>

Closes a popup block.

### get_cursor_pos()

 <small>function</small>

Where the next item will be drawn, relative to the current window.

**Returns:** `(x, y)`

### get_cursor_screen_pos()

 <small>function</small>

Where the next item will be drawn, in screen pixels.

**Returns:** `(x, y)`

### get_display_size()

 <small>function</small>

Size of the drawing area in pixels. Useful to place windows and HUD.

**Returns:** `(width, height)`

### get_io_want_capture_keyboard()

 <small>function</small>

True when the interface is using the keyboard (e.g. typing in a field). Use it to not move the character at that moment.

**Returns:** `bool`

### get_io_want_capture_mouse()

 <small>function</small>

True when the mouse is over the interface. Use it to ignore game clicks at that moment.

**Returns:** `bool`

### image(texture_id, w, h)

 <small>function</small>

-- texture_id is a raw OpenGL bind code

### input_text(label, value, max_length=256)

 <small>function</small>

Editable text field. `max_length` limits the number of characters.

**Returns:** `(changed, new_value)`

### invisible_button(label, width, height)

 <small>function</small>

Clickable area with no drawing. Good to place over an image. Returns True when clicked.

**Returns:** `bool`

### listbox(label, current_item, items, height_items=-1)

 <small>function</small>

Scrolling list. `height_items` is how many lines show (-1 = automatic).

**Returns:** `(changed, new_item)`

### load_default_font(size)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

**Returns:** `font_id or None -- engine font with icons; None until built next frame`

### load_font(path, size)

 <small>function</small>

Loads a .ttf/.otf font at the given size. Call it only once; the font is ready on the next frame. Use the id in `push_font()`.

**Returns:** `font_id`

### open_popup(name)

 <small>function</small>

Opens the popup with that name.

### pop_font()

 <small>function</small>

Goes back to the font before `push_font()`.

### pop_item_width()

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Goes back to the width before `push_item_width()`.

### pop_style_color(count=1)

 <small>function</small>

Undoes the last `count` colors from `push_style_color()`.

### pop_style_var(count=1)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

Undoes the last `count` styles from `push_style_var()`.

### push_font(font_id)

 <small>function</small>

Uses another font until `pop_font()`.

### push_item_width(width)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

-- >0 pixels, <0 right-aligned to the window edge (-1 = full width)

### push_style_color(idx, r, g, b, a)

 <small>function</small>

-- idx is one of the imgui.COL_* constants

### push_style_var(idx, value)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

or push_style_var(idx, x, y) -- idx is one of imgui.STYLE_*

### radio_button(label, active)

 <small>function</small>

Option button. `active` says whether it is the chosen one; when `pressed` is True, store this option as the group choice.

**Returns:** `pressed`

### same_line()

 <small>function</small>

Puts the next item on the same line as the previous one.

### separator()

 <small>function</small>

Draws a separator line.

### set_cursor_pos(x, y)

 <small>function</small>

-- position relative to the current window

### set_game_ui_open(open)

 <small>function</small>

-- enable/disable input + free mouse for Python-drawn game UI

### set_next_item_width(width)

<span class="ae-badge novo">new in Anastacio</span> <small>function</small>

-- same convention as push_item_width, next widget only

### set_next_window_pos(x, y, cond=COND_ALWAYS)

 <small>function</small>

Position of the next window, in pixels.

### set_next_window_size(w, h, cond=COND_ALWAYS)

 <small>function</small>

Size of the next window, in pixels.

### slider_float(label, value, min, max)

 <small>function</small>

Slider for a float between `min` and `max`.

**Returns:** `(changed, new_value)`

### slider_int(label, value, min, max)

 <small>function</small>

Slider for an integer between `min` and `max`.

**Returns:** `(changed, new_value)`

### text(text)

 <small>function</small>

Shows a text.

