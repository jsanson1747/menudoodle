######################
# MenuDoodleSetup.py #
######################

import tkinter as tk
import turtle

GUI = tk.Tk()
GUI.overrideredirect(1)
global canvas
canvas = tk.Canvas(master = GUI, width = 800, height = 480)    # For Laptop width = 1534, height = 794
canvas.pack()
global screen
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")
screen.tracer(100)
global windowSize
windowSize = (canvas.winfo_width(), canvas.winfo_height())
