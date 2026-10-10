###############################
# MenuDoodle Graphics Library #
#      Sanson Labs - 2022     #
###############################

##################################
# For Usage Guide, See Usage.txt #
##################################

import math
import time
import tkinter as tk
import turtle

# Main MenuDoodle Class
class MenuDoodle:
    def __init__(self, width=800, height=480, bgcolor="white", tracer=100):
        GUI = tk.Tk()
        GUI.overrideredirect(1)
        self.__GUI = GUI
        self.__canvas = tk.Canvas(master = GUI, width = width, height = height)
        self.__canvas.pack()

        self.__screen = turtle.TurtleScreen(self.__canvas)
        self.__screen.bgcolor(bgcolor)
        self.__screen.tracer(tracer)

        self.__windowSize = (self.__canvas.winfo_width(), self.__canvas.winfo_height())
    
    def getWindowSize(self):
        return self.__windowSize
    
    def getCanvas(self):
        return self.__canvas

    def getGUI(self):
        return self.__GUI

    def terminate(self):
        """Destroy the underlying Tk window, closing the MenuDoodle window and ending its mainloop."""
        # Deferred via after(): destroying root directly inside a Tk event callback (e.g. a button's onClick)
        # corrupts Tcl's allocator on Windows, surfacing as "alloc: invalid block" at exit.
        self.__GUI.after(0, self.__GUI.destroy)

    def getScreen(self):
        return self.__screen

    def mainloop(self):
        self.__screen.tracer(1)
        self.__screen.mainloop()

    @property
    def Box(self):
        parent_instance = self

        class Box:
            """
            A rectangular shape drawn on the MenuDoodle screen via a dedicated turtle.
            
            Args:
                length: Width of the box along the turtle's heading (horizontal), in pixels.
                width: Height of the box perpendicular to the heading (vertical), in pixels.
                xPos: X coordinate of the box's bottom-left corner.
                yPos: Y coordinate of the box's bottom-left corner.
                fill: Whether to fill the box's interior when drawn.
                fillColor: Color used to fill the box's interior.
                outline: Whether to draw the box's outline when drawn.
                outlineColor: Color used for the box's outline.
                outlineWeight: Pen thickness used for the box's outline.
            """

            def __init__(self, length, width, xPos, yPos, *, fill = True, fillColor = "black", outline = True, outlineColor = "black", outlineWeight = 4):
                self.length = length
                self.width = width
                self.xPos = xPos
                self.yPos = yPos
                self.fillColor = fillColor
                self.fill = fill
                self.outline = outline
                self.outlineWeight = outlineWeight
                self.outlineColor = outlineColor

                #Define Turtles
                try:
                    self.doodler = turtle.RawTurtle(parent_instance.getScreen())
                except NameError:
                    raise Exception("ERROR: Screen Not Defined: Ensure MenuDoodle is properly initialized")

                #Initialize Turtles
                self.doodler.hideturtle()
                self.doodler.pencolor(self.fillColor)
                self.doodler.penup()
                self.doodler.pensize(self.outlineWeight)

            def __fillShape(self, turt):
                """Fill the box's outline shape with the configured fillColor."""
                turt.begin_fill()
                self.__drawOutline(turt)
                turt.end_fill()
                
                parent_instance.getScreen().update()

            def __drawOutline(self, turt):
                """Trace the box's rectangular perimeter without drawing the fill."""
                turt.penup()
                turt.pensize(self.outlineWeight)
                turt.goto(self.xPos, self.yPos)
                turt.pendown()

                turt.seth(0)
                turt.forward(self.length)
                turt.right(90)
                turt.forward(self.width)
                turt.right(90)
                turt.forward(self.length)
                turt.right(90)
                turt.forward(self.width)
                turt.penup()

                parent_instance.getScreen().update()
                
            def draw(self):
                """Render the box, filling and/or outlining it according to its settings."""
                turt = self.doodler
                turt.goto(self.xPos, self.yPos)
                
                if self.fill:
                    turt.pencolor(self.fillColor)
                    turt.fillcolor(self.fillColor)
                    self.__fillShape(turt)
                if self.outline:
                    turt.pencolor(self.outlineColor)
                    self.__drawOutline(turt)
        return Box

    @property
    def Ellipse(self):
        parent_instance = self

        class Ellipse:
            """
            Represents an ellipse shape that can be drawn on the screen.
            
            Args:
                xPos (float): The x-coordinate of the ellipse's center.
                yPos (float): The y-coordinate of the ellipse's center.
                A (float): The semi-major axis length of the ellipse.
                B (float): The semi-minor axis length of the ellipse.
                color (str, optional): The color of the ellipse's outline and fill. Defaults to "black".
                fill (bool, optional): Whether to fill the ellipse with color. Defaults to False.
                half (str, optional): Specifies which half of the ellipse to draw ("full", "top", "bottom", "left", "right"). Defaults to "full".
                outlineWeight (int, optional): Pen thickness used for the ellipse's outline..
            """

            def __init__(self, xPos, yPos, A, B, *, color = "black", fill = False, half = "full", outlineWeight = 4):
                self.initX = xPos
                self.initY = yPos
                self.A = A
                self.B = B
                self.outlineWeight = outlineWeight
                self.color = color
                self.fill = fill
                self.half = half

                #Define Turtles
                try:
                    self.doodler = turtle.RawTurtle(parent_instance.getScreen())
                except NameError:
                    raise Exception("ERROR: Screen Not Defined: Ensure MenuDoodle is properly initialized")

                #Initialize Turtles
                self.doodler.hideturtle()
                self.doodler.pencolor(self.color)
                self.doodler.fillcolor(self.color)
                self.doodler.penup()
                self.doodler.pensize(self.outlineWeight)

            def draw(self):
                self.doodler.clear()
                initX = self.initX
                initY = self.initY
                turt = self.doodler
                half = self.half
                A = self.A
                B = self.B

                yPos = initY - B
                x = initX
                turt.penup()
                turt.goto(initX, yPos)
                turt.pendown()

                if self.fill:
                    turt.begin_fill()
                while yPos < initY - B + (2 * B):
                    if half == "top":
                        if yPos < initY:
                            turt.penup()
                        else:
                            turt.pendown()
                    if half == "bottom":
                        if yPos > initY:
                            turt.penup()
                        else:
                            turt.pendown()
                    if half == "left":
                        if x >= initX:
                            turt.penup()
                        else:
                            turt.pendown()
                    if half == "right":
                        if x < initX:
                            turt.penup()
                        else:
                            turt.pendown()
                    x = math.sqrt(A ** 2 - ((A ** 2 * (yPos - initY) ** 2)/(B ** 2))) + initX
                    turt.goto(x, yPos)
                    yPos += 0.5
                
                while yPos >= initY - B:
                    if half == "top":
                        if yPos < initY:
                            turt.penup()
                        else:
                            turt.pendown()
                    if half == "bottom":
                        if yPos > initY:
                            turt.penup()
                        else:
                            turt.pendown()
                    if half == "left":
                        if x > initX:
                            turt.penup()
                        else:
                            turt.pendown()
                    if half == "right":
                        if x <= initX:
                            turt.penup()
                        else:
                            turt.pendown()
                    x = -1 * (math.sqrt(A ** 2 - ((A ** 2 * (yPos - initY) ** 2)/(B ** 2)))) + initX
                    turt.goto(x, yPos)
                    yPos -= 0.5
                if self.fill:
                    turt.end_fill()
                parent_instance.getScreen().update()
        return Ellipse

    @property
    def Button(self):
        parent_instance = self

        class Button:
            """
            A clickable shape that changes color while pressed and triggers an action on release.

            Args:
                xPos (float): The x-coordinate of the button's position.
                yPos (float): The y-coordinate of the button's position.
                length (float): The length of the button shape.
                width (float): The width of the button shape.
                onClick (Callable): Callable invoked with no arguments when the button is released.
                button (int): The mouse button that triggers the action (1 for left, 2 for middle, 3 for right).
                color (str): The button's default fill color.
                pressedColor (str): The button's fill color while pressed.
                shape (str, optional): The turtle shape used for the button. Defaults to "square".
                angle (float, optional): The heading angle of the button shape. Defaults to 0.
                outlineWeight (float): The outline thickness of the button shape.
            """

            def __init__(self, xPos, yPos, length, width, *, onClick = None, button = 1, color = "lime", pressedColor = "green", shape = "square", angle = 0, outlineWeight = 4):
                self.__onClick = onClick
                self.xPos = xPos
                self.yPos = yPos
                self.length = length
                self.width = width
                self.outlineWeight = outlineWeight
                self.color = color
                self.pressedColor = pressedColor
                self.shape = shape
                self.angle = angle

                #Define Turtles
                try:
                    self.doodler = turtle.RawTurtle(parent_instance.getScreen())
                except NameError:
                    raise Exception("ERROR: Screen Not Defined: Ensure MenuDoodle is properly initialized")

                #Initialize Turtles
                self.doodler.hideturtle()
                self.doodler.penup()
                self.doodler.goto(self.xPos, self.yPos)
                self.doodler.shape(self.shape)
                self.doodler.fillcolor(self.color)
                self.doodler.seth(self.angle)
                self.doodler.shapesize(self.length, self.width, self.outlineWeight)
                self.doodler.showturtle()

                self.doodler.onclick(self.__colorShift, button)
                self.doodler.onrelease(self.__colorDeShift, button)

                parent_instance.getScreen().update()

            def __colorShift(self, x, y):
                self.doodler.fillcolor(self.pressedColor)
                parent_instance.getScreen().update()

            def __colorDeShift(self, x, y):
                self.doodler.fillcolor(self.color)
                parent_instance.getScreen().update()
                if self.__onClick:
                    self.__onClick()
        return Button

    @property
    def Text(self):
        parent_instance = self

        class Text:
            """
            A line of text drawn on the MenuDoodle screen via a dedicated turtle.

            Args:
                xPos (float): The x-coordinate where the text is anchored.
                yPos (float): The y-coordinate where the text is anchored.
                text (str): The text to display.
                fontColor (str, optional): The color of the text. Defaults to "black".
                alignment (str, optional): Text alignment ("left", "center", "right"). Defaults to "center".
                font (str, optional): The font family used to render the text. Defaults to "Arial".
                fontSize (int, optional): The font size used to render the text. Defaults to 12.
                fontType (str, optional): The font style used to render the text (e.g. "normal", "bold", "italic"). Defaults to "normal".
            """

            def __init__(self, xPos, yPos, text, *, fontColor = "black", alignment = "center", font = "Arial", fontSize = 12, fontType = "normal"):
                self.xPos = xPos
                self.yPos = yPos
                self.text = text
                self.alignment = alignment
                self.font = font
                self.fontSize = fontSize
                self.fontType = fontType
                self.fontColor = fontColor

                #Define Turtles
                try:
                    self.doodler = turtle.RawTurtle(parent_instance.getScreen())
                except NameError:
                    raise Exception("ERROR: Screen Not Defined: Ensure MenuDoodle is properly initialized")

                #Initialize Turtles
                self.doodler.hideturtle()
                self.doodler.pencolor(self.fontColor)
                self.doodler.penup()

            def setText(self, newText):
                """Update the text to display on the next print() call."""
                self.text = newText

            def print(self):
                """Clear any previously drawn text and render the current text."""
                self.doodler.clear()
                self.doodler.goto(self.xPos, self.yPos)
                self.doodler.write(self.text, False, self.alignment, font = (self.font, self.fontSize, self.fontType))
                parent_instance.getScreen().update()
        return Text

    @property
    def Loader(self):
        parent_instance = self

        class Loader:
            """
            A simple loading indicator that redraws an ellipse, erasing the previous frame each run.

            Args:
                xPos (float): The x-coordinate of the loader's center.
                yPos (float): The y-coordinate of the loader's center.
                size (float): The radius of the loader, used for both axes of the ellipse.
                outlineWeight (float): Pen thickness used for the loader's outline.
                loaderColor (str, optional): The color used to draw the loader. Defaults to "black".
                eraserColor (str, optional): The color used to erase the previous frame. Defaults to "white".
            """

            def __init__(self, xPos, yPos, size, *, loaderColor = "black", eraserColor = "white", outlineWeight = 4):
                self.xPos = xPos
                self.yPos = yPos
                self.size = size
                self.outlineWeight = outlineWeight
                self.loaderColor = loaderColor
                self.eraserColor = eraserColor

                self.loady = parent_instance.Ellipse(self.xPos, self.yPos, self.size, self.size, color = self.loaderColor, outlineWeight = self.outlineWeight)
                self.erasey = parent_instance.Ellipse(self.xPos, self.yPos, self.size, self.size, color = self.eraserColor, outlineWeight = self.outlineWeight)

            def run(self):
                """Draw the loader, then erase it, rescheduling itself via Tk's event loop until the window closes."""
                def loaderLoop():
                    try:
                        self.loady.draw()
                        self.erasey.draw()
                    except tk.TclError:
                        return  # Window was destroyed; stop rescheduling.
                    parent_instance.getGUI().after(0, loaderLoop)

                loaderLoop()
        return Loader

def main():
    doodler = MenuDoodle()
    box1 = doodler.Box(200, 100, 0, 0, fillColor = "lime")
    box1.draw()

    ellipse1 = doodler.Ellipse(0, 0, 200, 100, outlineWeight = 4, color = "black")
    ellipse1.draw()
    
    button1 = doodler.Button(-100, 100, 3.5, 2.5, onClick = lambda: print("hi"))
    button2 = doodler.Button(-300, -150, 2.5, 3.5, color = "red", pressedColor = "darkred", onClick = lambda: doodler.terminate())

    text1 = doodler.Text(-300, -200, "Exit")
    text1.print()

    loader1 = doodler.Loader(300, 150, 50)
    loader1.run()

    doodler.mainloop()

if(__name__ == "__main__"):
    main()
    