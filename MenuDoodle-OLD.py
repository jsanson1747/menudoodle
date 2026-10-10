###############################
# MenuDoodle Graphics Library #
#      Sanson Labs - 2022     #
###############################

##################################
# For Usage Guide, See Usage.txt #
##################################

import tkinter as tk
import turtle
import math
from MenuDoodleSetup import *



#Box Class
class Box:
    def __init__(self, length, width, xPos, yPos, fill = True, fillColor = "black", outline = True, outlineColor = "black", outlineWeight = 4):
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
            self.doodler = turtle.RawTurtle(screen)
        except NameError:
            raise Exception("ERROR: Screen Not Defined: Ensure setup.py has been imported")

        #Initialize Turtles
        self.doodler.hideturtle()
        self.doodler.pencolor(self.fillColor)
        self.doodler.penup()
        self.doodler.pensize(self.outlineWeight)

    def __fillShape(self, turt):
        turt.begin_fill()
        self.__drawOutline(turt)
        turt.end_fill()
        
        screen.update()

    def __drawOutline(self, turt):
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

        screen.update()
        
            
    
    def draw(self):
        turt = self.doodler
        turt.goto(self.xPos, self.yPos)
        
        if self.fill:
            turt.pencolor(self.fillColor)
            turt.fillcolor(self.fillColor)
            self.__fillShape(turt)
        if self.outline:
            turt.pencolor(self.outlineColor)
            self.__drawOutline(turt)

#Ellipse Class           
class Ellipse:
    def __init__(self, xPos, yPos, A, B, thickness, color = "black", fill = False, half = "full"):
        self.initX = xPos
        self.initY = yPos
        self.A = A
        self.B = B
        self.thickness = thickness
        self.color = color
        self.fill = fill
        self.half = half

        #Define Turtles
        try:
            self.doodler = turtle.RawTurtle(screen)
        except NameError:
            raise Exception("ERROR: Screen Not Defined: Ensure setup.py has been imported")

        #Initialize Turtles
        self.doodler.hideturtle()
        self.doodler.pencolor(self.color)
        self.doodler.fillcolor(self.color)
        self.doodler.penup()
        self.doodler.pensize(self.thickness)

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
            if half == "bot":
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
            if half == "bot":
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
        screen.update()

#Button Class 
class Button:
    def __init__(self, action, xPos, yPos, length, width, outlineThickness, color, pressedColor, shape = "square", angle = 0):
        self.action = action
        self.xPos = xPos
        self.yPos = yPos
        self.length = length
        self.width = width
        self.outlineThickness = outlineThickness
        self.color = color
        self.pressedColor = pressedColor
        self.shape = shape
        self.angle = angle

        #Define Turtle
        try:
            self.doodler = turtle.RawTurtle(screen)
        except NameError:
            raise Exception("ERROR: Screen Not Defined: Ensure setup.py has been imported")

        #Initialize Turtles
        self.doodler.hideturtle()
        self.doodler.penup()
        self.doodler.goto(self.xPos, self.yPos)
        self.doodler.shape(self.shape)
        self.doodler.fillcolor(self.color)
        self.doodler.seth(angle)
        self.doodler.shapesize(self.length, self.width, self.outlineThickness)
        self.doodler.showturtle()
        screen.update()

    def __colorShift(self, x, y):
        self.doodler.fillcolor(self.pressedColor)

    def __colorDeShift(self, x, y):
        self.doodler.fillcolor(self.color)
        self.action()
    
    def clicked(self, button = 1):
        self.doodler.onclick(self.__colorShift, button)
        self.doodler.onrelease(self.__colorDeShift, button)

#Text Class
class Text:
    def __init__(self, xPos, yPos, text, fontColor = "black", alignment = "center", font = "Arial", fontSize = 12, fontType = "normal"):
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
            self.doodler = turtle.RawTurtle(screen)
        except NameError:
            raise Exception("ERROR: Screen Not Defined: Ensure setup.py has been imported")

        #Initialize Turtles
        self.doodler.hideturtle()
        self.doodler.pencolor(self.fontColor)
        self.doodler.penup()
        
    def setText(self, newText):
        self.text = newText
    
    def print(self):
        self.doodler.clear()
        self.doodler.goto(self.xPos, self.yPos)
        self.doodler.write(self.text, False, self.alignment, font = (self.text, self.fontSize, self.fontType))
        screen.update()
        
#Loader Class
class Loader:
    def __init__(self, xPos, yPos, size, thickness, loaderColor = "black", eraserColor = "white"):
        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.thickness = thickness
        self.loaderColor = loaderColor
        self.eraserColor = eraserColor

        self.loady = Ellipse(self.xPos, self.yPos, self.size, self.size, self.thickness, self.loaderColor)
        self.erasey = Ellipse(self.xPos, self.yPos, self.size, self.size, self.thickness, self.eraserColor)

    def run(self):
        self.loady.draw()
        self.erasey.draw()
        
        
    

#Demonstation of Functionality
def main():
    box1 = Box(200, 100, 0, 0, True, "lime", True, "black", 4)
    box1.draw()


    ellipse1 = Ellipse(0, 0, 200, 100, 4, "black")
    ellipse1.draw()

    text1 = Text(100, 100, "Hello There")
    text1.print()
    
    def button1FN():
        print("hi")

    button1 = Button(button1FN, -100, 100, 3.5, 2.5, 4, "lime", "green", "triangle", -90)

    #Main Loop
    while True:
        button1.clicked(1)
     


if __name__ == "__main__":
    main()


