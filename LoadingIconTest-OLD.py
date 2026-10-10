###############################
# Loading Icon Animation Test #
###############################

import MenuDoodle
from MenuDoodleSetup import screen
import turtle
import time
from multiprocessing import Process

'''
loady = MenuDoodle.Ellipse(0, 0, 20, 20, 4, "black")
erasey = MenuDoodle.Ellipse(0, 0, 20, 20, 4, "white")
screen = turtle.Screen()
screen.tracer(1)

loady.color("black")
erasey.color("white")

def func1():
    while True:
        loady.draw()
        erasey.draw()

def func2():
    while True:
        print("hello")

p1 = Process(target = func1())
p1.start()
p2 = Process(target = func2())
p2.start()
'''
loady = MenuDoodle.Ellipse(0, 0, 20, 20, 4, "black")
erasey = MenuDoodle.Ellipse(0, 0, 20, 20, 4, "white")
#screen = turtle.Screen()
screen.tracer(2)


#loady.color("black")
#erasey.color("white")
while True:
    loady.draw()
    erasey.draw()


 
