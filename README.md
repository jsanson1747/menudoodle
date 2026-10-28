# Menu Doodle

A graphics wrapper around Python's `turtle` module for building GUIs.


## Installation

```pip install menudoodle```

***Note:** menudoodle relies on the Tkinter package. Usually this is installed along with python but there is a chance that sometimes it needs to be installed manually

## Usage

Create a window, then create drawing objects from that `MenuDoodle` instance:

```python
from menudoodle import MenuDoodle

doodler = MenuDoodle(width=800, height=480, bgcolor="white", tracer=100)
box = doodler.Box(200, 100, 0, 0, fillColor="lime")
box.draw()
doodler.mainloop()
```

### MenuDoodle

```python
MenuDoodle(width=800, height=480, bgcolor="white", tracer=100)
```

- `width`, `height`: Window dimensions in pixels.
- `bgcolor`: Window background color.
- `tracer`: Turtle screen update interval.

### Box

```python
doodler.Box(length, width, xPos, yPos, *, fill=True, fillColor="black",
		   outline=True, outlineColor="black", outlineWeight=4)
```

- `length`, `width`: Box dimensions in pixels.
- `xPos`, `yPos`: Coordinates of the box's bottom-left corner.
- `fill`: Whether to fill the box.
- `fillColor`: Interior fill color.
- `outline`: Whether to draw the outline.
- `outlineColor`: Outline color.
- `outlineWeight`: Outline thickness.

Call `draw()` to render the box. Call `clear()` to erase it; `draw()` can be called again later to redraw it.

### Ellipse

```python
doodler.Ellipse(xPos, yPos, A, B, *, color="black", fill=False,
			   half="full", outlineWeight=4)
```

- `xPos`, `yPos`: Coordinates of the ellipse's center.
- `A`, `B`: Semi-major and semi-minor axis lengths.
- `color`: Outline and fill color.
- `fill`: Whether to fill the ellipse.
- `half`: Portion to draw: `"full"`, `"top"`, `"bottom"`, `"left"`, or `"right"`.
- `outlineWeight`: Outline thickness.

Call `draw()` to render the ellipse. Call `clear()` to erase it; `draw()` can be called again later to redraw it.

### Button

```python
doodler.Button(xPos, yPos, length, width, *, onClick=None, button=1,
			  color="lime", pressedColor="green", shape="square",
			  angle=0, outlineWeight=4)
```

- `xPos`, `yPos`: Button position.
- `length`, `width`: Turtle shape stretch factors.
- `onClick`: Optional no-argument function called when the mouse button is released.
- `button`: Mouse button binding: `1` for left, `2` for middle, or `3` for right.
- `color`: Default fill color.
- `pressedColor`: Fill color while pressed.
- `shape`: Turtle shape name, such as `"square"`, `"triangle"`, `"circle"`, `"arrow"`, `"turtle"`, or `"classic"`.
- `angle`: Shape heading in degrees.
- `outlineWeight`: Outline thickness.

The button is visible when created. Call `hide()` to hide it (a hidden button doesn't receive clicks) and `show()` to make it visible again.

### Text

```python
doodler.Text(xPos, yPos, text, *, fontColor="black", alignment="center",
			font="Arial", fontSize=12, fontType="normal")
```

- `xPos`, `yPos`: Text anchor coordinates.
- `text`: Text to display.
- `fontColor`: Text color.
- `alignment`: `"left"`, `"center"`, or `"right"`.
- `font`: Font family.
- `fontSize`: Font size.
- `fontType`: Font style, such as `"normal"`, `"bold"`, or `"italic"`.

Call `print()` to render the text. Use `setText(newText)` to change it before printing again. Call `clear()` to erase it; `print()` can be called again later to redraw it.

### Loader

```python
doodler.Loader(xPos, yPos, size, *, loaderColor="black",
			  eraserColor="white", outlineWeight=4)
```

- `xPos`, `yPos`: Loader center coordinates.
- `size`: Radius used for both ellipse axes.
- `loaderColor`: Loader color.
- `eraserColor`: Color used to erase the previous frame.
- `outlineWeight`: Outline thickness.

Call `run()` to start the loader animation.
