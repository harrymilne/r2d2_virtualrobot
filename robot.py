##robot.py
from turtle import RawTurtle

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

    def process(self):
        self.turtle.forward(10)
        ##if goal not reached:
        self.scene.master.after(500, self.process)



    pass