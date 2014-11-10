##robot.py
from turtle import RawTurtle
from Tkinter import *
import math


class Robot:

    def __init__(self, scene, robot_id):
        self.robot_id = robot_id
        self.done = False

        self.turtle = RawTurtle(scene.canvas)
        self.scene = scene
        self.goal_reached = False

        scr = self.turtle.getscreen()
        scr.setworldcoordinates(0, scene.height, scene.width, 0)

        self.turtle.penup()
        self.reset()

    def reset(self):
        positions = [((15,15), 45), 
                    ((self.scene.width-15, 15), 135),
                    ((15, self.scene.height-15), 315),
                    ((self.scene.height-15, self.scene.width-15), 135)]

        self.turtle.speed(0)
        self.turtle.setpos(positions[self.robot_id][0])
        print positions[self.robot_id]
        self.turtle.left(positions[self.robot_id][1])
        self.turtle.forward(20)
        self.turtle.speed("normal")

    def process(self):
        ##sets variables for checking collision
        turtle_x = self.turtle.xcor()
        turtle_y = self.turtle.ycor()
        t_heading = self.turtle.heading()
        ##variables used to check right
        xr = turtle_x + 15*math.cos(math.radians(self.turtle.heading()+30))
        yr = turtle_y + 15*math.sin(math.radians(self.turtle.heading()+30))
        ##variables used to check left
        xl = turtle_x + 15*math.cos(math.radians(self.turtle.heading()-30))
        yl = turtle_y + 15*math.sin(math.radians(self.turtle.heading()-30))
        ##turns the robot at window boundries
        st_orient = [0, 90, 180, 270]
        if turtle_x - 10 < 0:
            self.turtle.setheading(180-t_heading)
        if turtle_x + 10 > 750:
            self.turtle.setheading(180-t_heading)
        if turtle_y - 10 < 0:
            self.turtle.setheading(360-t_heading)
        if turtle_y + 10 > 500:
            self.turtle.setheading(360-t_heading)
        ##check collisions
        left = self.scene.canvas.find_overlapping(xl-1,yl-1,xl+1,yl+1)
        right = self.scene.canvas.find_overlapping(xr-1,yr-1,xr+1,yr+1)
        if self.goal_id in left + right:
            self.done = True
            self.turtle.forward(15)
        elif left:
            ##turn away
            self.turtle.left(10)
        elif right:
            ##turn away
            self.turtle.right(10)
        else:
            ##else move forward
            self.turtle.forward(5)
        ##if goal not reached:
        if not self.done:
            self.scene.master.after(20, self.process)

