##robot.py
from turtle import RawTurtle
from Tkinter import *
import math


class Robot:

    def __init__(self, scene):
        self.turtle = RawTurtle(scene.canvas)
        self.scene = scene
        self.goal_reached = False

        scr = self.turtle.getscreen()
        scr.setworldcoordinates(0, scene.height, scene.width, 0)

        self.turtle.penup()
        self.turtle.left(45)
        self.turtle.forward(20)

        print (self.turtle.xcor())
        print (self.turtle.ycor())
        print self.turtle.heading()

    def process(self):

    ##sets variables for checking collision
        turtle_x = self.turtle.xcor()
        turtle_y = self.turtle.ycor()
        ##variables used to check right
        xr = turtle_x + 15*math.cos(math.radians(self.turtle.heading()+1.5))
        yr = turtle_y + 15*math.sin(math.radians(self.turtle.heading()+1.5))
        ##variables used to check left
        xl = turtle_x + 15*math.cos(math.radians(self.turtle.heading()-1.5))
        yl = turtle_y + 15*math.sin(math.radians(self.turtle.heading()-1.5))
    ##turns the robot at window boundries
        if turtle_x - 10 < 0:
            self.turtle.setheading(0)
        if turtle_x + 10 > 750:
            self.turtle.setheading(180)
        if turtle_y - 10 < 0:
            self.turtle.setheading(90)
        if turtle_y + 10 > 500:
            self.turtle.setheading(270)
    ##check collisions
        if self.scene.canvas.find_overlapping(xl-1,yl-1,xl+1,yl+1):
            ##turn away
            self.turtle.left(10)
        elif self.scene.canvas.find_overlapping(xr-1,yr-1,xr+1,yr+1):
            ##turn away
            self.turtle.right(10)
        else:
            ##else move forward
            self.turtle.forward(1)
        ##if goal not reached:
        self.scene.master.after(1, self.process)



    pass
