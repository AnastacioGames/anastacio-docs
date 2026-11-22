# Range.imgui

> **See also:**
[`Range.render`](Range.render.md), [`Range.logic`](Range.logic.md)

Anastacio Engine module `Range.imgui`. Also available as `bge.imgui`.

```python
# A pause window, drawn every frame by a component.
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
# Common widgets return if they changed and the new value.
changed, self.fullscreen = imgui.checkbox("Full screen", self.fullscreen)
changed, self.quality = imgui.slider_int("Quality", self.quality, 0, 3)
imgui.same_line()
imgui.text("Level: {}".format(self.quality))
```

```python
# Change the color of one button.
imgui.push_style_color(imgui.COL_BUTTON, 0.8, 0.2, 0.2, 1.0)
imgui.button("Delete save")
imgui.pop_style_color()
```

# Not in the Range documentation

These items exist in the engine but were not in the Range documentation. The ones marked **new in Anastacio** were added by Anastacio Engine.

### begin(name, closable=False)

 `function`

Opens a window titled `name`. Everything you draw until `end()` goes inside it. With `closable=True` the window gets the X button, and `want_close` becomes True when it is clicked. Always call `end()` afterwards, even if `is_open` is False.

**Returns:** `(is_open, want_close)`

### begin_popup_modal(name, closable=False)

 `function`

Draws the modal popup opened before with `open_popup(name)`. Only call `end_popup()` when `is_open` is True.

**Returns:** `(is_open, want_close)`

### button(label, width=0, height=0)

 `function`

Button with the text `label`. Returns True on the frame it is clicked. Width and height 0 fit the text.

**Returns:** `bool`

### checkbox(label, value)

 `function`

Checkbox. Pass the current value in `value` and keep `new_value`; `changed` is True when the player clicked.

**Returns:** `(changed, new_value)`

### close_current_popup()

 `function`

Closes the open popup.

### color_edit3(label, r, g, b)

 `function`

RGB color picker (values from 0 to 1). Returns the new color.

**Returns:** `(changed, r, g, b)`

### color_edit4(label, r, g, b, a)

 `function`

RGBA color picker with transparency (values from 0 to 1).

**Returns:** `(changed, r, g, b, a)`

### combo(label, current_item, items)

 `function`

Dropdown list. `items` is a list of strings and `current_item` the chosen index.

**Returns:** `(changed, new_item)`

### draw_rect_filled(x1, y1, x2, y2, r, g, b, a)

 `function`

-- drawn above every window, for fades

### end()

 `function`

Closes the window started with `begin()`.

### end_popup()

 `function`

Closes a popup block.

### get_cursor_pos()

 `function`

Where the next item will be drawn, relative to the current window.

**Returns:** `(x, y)`

### get_cursor_screen_pos()

 `function`

Where the next item will be drawn, in screen pixels.

**Returns:** `(x, y)`

### get_display_size()

 `function`

Size of the drawing area in pixels. Useful to place windows and HUD.

**Returns:** `(width, height)`

### get_io_want_capture_keyboard()

 `function`

True when the interface is using the keyboard (e.g. typing in a field). Use it to not move the character at that moment.

**Returns:** `bool`

### get_io_want_capture_mouse()

 `function`

True when the mouse is over the interface. Use it to ignore game clicks at that moment.

**Returns:** `bool`

### image(texture_id, w, h)

 `function`

-- texture_id is a raw OpenGL bind code

### input_text(label, value, max_length=256)

 `function`

Editable text field. `max_length` limits the number of characters.

**Returns:** `(changed, new_value)`

### invisible_button(label, width, height)

 `function`

Clickable area with no drawing. Good to place over an image. Returns True when clicked.

**Returns:** `bool`

### listbox(label, current_item, items, height_items=-1)

 `function`

Scrolling list. `height_items` is how many lines show (-1 = automatic).

**Returns:** `(changed, new_item)`

### load_default_font(size)

*(new in Anastacio)* `function`

**Returns:** `font_id or None -- engine font with icons; None until built next frame`

### load_font(path, size)

 `function`

Loads a .ttf/.otf font at the given size. Call it only once; the font is ready on the next frame. Use the id in `push_font()`.

**Returns:** `font_id`

### open_popup(name)

 `function`

Opens the popup with that name.

### pop_font()

 `function`

Goes back to the font before `push_font()`.

### pop_item_width()

*(new in Anastacio)* `function`

Goes back to the width before `push_item_width()`.

### pop_style_color(count=1)

 `function`

Undoes the last `count` colors from `push_style_color()`.

### pop_style_var(count=1)

*(new in Anastacio)* `function`

Undoes the last `count` styles from `push_style_var()`.

### push_font(font_id)

 `function`

Uses another font until `pop_font()`.

### push_item_width(width)

*(new in Anastacio)* `function`

-- >0 pixels, <0 right-aligned to the window edge (-1 = full width)

### push_style_color(idx, r, g, b, a)

 `function`

-- idx is one of the imgui.COL_* constants

### push_style_var(idx, value)

*(new in Anastacio)* `function`

or push_style_var(idx, x, y) -- idx is one of imgui.STYLE_*

### radio_button(label, active)

 `function`

Option button. `active` says whether it is the chosen one; when `pressed` is True, store this option as the group choice.

**Returns:** `pressed`

### same_line()

 `function`

Puts the next item on the same line as the previous one.

### separator()

 `function`

Draws a separator line.

### set_cursor_pos(x, y)

 `function`

-- position relative to the current window

### set_game_ui_open(open)

 `function`

-- enable/disable input + free mouse for Python-drawn game UI

### set_next_item_width(width)

*(new in Anastacio)* `function`

-- same convention as push_item_width, next widget only

### set_next_window_pos(x, y, cond=COND_ALWAYS)

 `function`

Position of the next window, in pixels.

### set_next_window_size(w, h, cond=COND_ALWAYS)

 `function`

Size of the next window, in pixels.

### slider_float(label, value, min, max)

 `function`

Slider for a float between `min` and `max`.

**Returns:** `(changed, new_value)`

### slider_int(label, value, min, max)

 `function`

Slider for an integer between `min` and `max`.

**Returns:** `(changed, new_value)`

### text(text)

 `function`

Shows a text.
