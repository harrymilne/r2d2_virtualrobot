##scene.py

from Tkinter import *
from random import randint

class Scene(Frame): ##main canvas class (creating the window)
    def __init__(self, master=None, width=750, height=500): ##passing the Tk root + options
        Frame.__init__(self, master) ##constructing the parent class
        self.parent = master ##keeping root for future reference
        self.parent.title("R2D2 Virtual Robot") ##naming window
        self.pack()
        self.width = width ##keeping width + height for future reference in class
        self.height = height

        self.canvas = Canvas(self, width=width, height=height) ##init drawing canvas
        self.populate()
        self.canvas.pack()

    def populate(self, num=5): ##populate obstacles
        for i in range(num): ##loop for how many obstacles wanted
            x = randint(0, self.width-100) ##random x1 + y1
            y = randint(0, self.height-100) 
            print(x,y)
            self.canvas.create_rectangle(x, y, x+100, y+100, ##create rectangle
            outline="#f11", fill="#1f1", width=2)

    def start_robot(self):
        ##
        pass


class Obstacle:
    pass

if __name__ == "__main__":
    root = Tk()
    sc = Scene(master=root)
    root.mainloop()