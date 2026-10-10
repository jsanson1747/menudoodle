# menu-doodle
A graphics wrapper around python turtle for building GUIs
```
╔─────────────────────────────────────────────╗
│ How to Use the MenuDoodle Graphics Library  │ 
╚─────────────────────────────────────────────╝
╔────────────────╗
│In MenuDoodle.py│
╚────────────────╝
╔─────────╗
│Box class│
╚─────────╝

EX: box1 = Box(length, width, xPos, yPos, fill = True, fillColor = "black", outline = True, outlineColor = "black", outlineWeight = 4)

length ---------> length of box
width ----------> width of box
xPos -----------> x coordinate of box
yPos -----------> y coordinate of box
fill -----------> boolean of whether or not to fill box
fillColor ------> what color to fill the box with
outline --------> boolean of whether or not to outline the box
outlineColor ---> what color to outline the box with
outlineWeight --> weight of the outline

╔─────────────╗
│Ellipse class│
╚─────────────╝

EX: ellipse1 = Ellipse(xPos, yPos, A, B, thickness, color = "black", fill = False, half = "full")

xPos -----------> x coordinate of the origin of the ellipse
yPos -----------> y coordinate of the origin of the ellipse
A --------------> Length of the major axis of the ellipse
B --------------> Length of the minor axis of the ellipse
outlineWeight --> Thickness of the ellipse
color ----------> Color of the ellipse
fill -----------> Boolean determining whether or not to fill the ellipse
half -----------> What half of the ellipse you want to draw: "full", "top", "bot", "left", "right"

╔─────────────╗
│Button class │
╚─────────────╝

EX: button1 = Button(action, xPos, yPos, length, width, outlineThickness, color, shape = "square", angle = 0)

action ------------> function that executes when the button is clicked
xPos --------------> x coordinate of the center of the button
yPos --------------> y coordinate of the center of the button
length ------------> length stretch factor of button
width -------------> width stretch factir of button
outlineWeight -----> Thickness of button outline
color -------------> Color of button
pressedColor ------> Color of button when pressed
shape -------------> Shape of button: "square", "triangle", "circle", "arrow", "turtle", "classic"

╔───────────╗
│Text class │
╚───────────╝

EX: text1 = Text(xPos, yPos, text, fontColor = "black", alignment = "center", font = "Arial", fontSize = 12, fontType = "normal)

xPos -------> xPos of text
yPos -------> yPos of text
text -------> text to be displayed
fontColor --> color of the font
alignment --> how the text is aligned: "left", "right", "center"
font -------> What font to use
fontSize ---> Size of font
fontType ---> type of font: "normal", "bold", "italic"
```
