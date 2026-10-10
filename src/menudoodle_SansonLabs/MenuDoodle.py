###############################
# MenuDoodle Graphics Library #
#      Sanson Labs - 2022     #
###############################

##################################
# For Usage Guide, See Usage.txt #
##################################

import time
import tkinter as tk
import turtle

# Main MenuDoodle Class
class MenuDoodle:
    def __init__(self, width=800, height=480, bgcolor="white", tracer=100):
        GUI = tk.Tk()
        GUI.overrideredirect(1)
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

    def getScreen(self):
        return self.__screen

    @property
    def Box(self):
        parent_instance = self

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
                    self.doodler = turtle.RawTurtle(parent_instance.getScreen())
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
                
                parent_instance.getScreen().update()

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

                parent_instance.getScreen().update()
                
                    
            
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
        return Box


def main():
    doodler = MenuDoodle()
    box1 = doodler.Box(200, 100, 0, 0, True, "lime", True, "black", 4)
    box1.draw()
    time.sleep(3)

if(__name__ == "__main__"):
    main()
    