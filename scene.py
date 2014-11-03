##scene.py

from Tkinter import *
from random import randint
import turtle

class Scene(Frame): ##main canvas class (creating the window)
    def __init__(self, master=None, width=750, height=500): ##passing the Tk root + options
        Frame.__init__(self, master) ##constructing the parent class
        self.parent = master ##keeping root for future reference
        self.width = width ##keeping width + height for future reference in class
        self.height = height
        self.obstacles = []


        self.parent.title("R2D2 Virtual Robot") ##naming window
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        file_menu = Menu(menubar)
        file_menu.add_command(label="Repopulate", command=self.repopulate)
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        self.canvas = Canvas(self, width=width, height=height) ##init drawing canvas
        self.canvas.pack()
        self.pack()

        self.populate()
        
    def clear(self):
        self.canvas.clear()

    def check_overlapping(self, x, y):
        return self.canvas.find_overlapping(x-50, y-50, x+150, y+150)
    

    def populate(self, num=5): ##populate obstacles
        self.add_robot()
        for sq in range(num): ##loop for how many obstacles wanted
            x = randint(50, self.width-100) ##random x1 + y1
            y = randint(50, self.height-100)

            while self.check_overlapping(x, y): ##check x, y for existing object
                x = randint(50, self.width-100) ##random x1 + y1
                y = randint(50, self.height-100)

            obst_id = self.canvas.create_rectangle(x, y, x+100, y+100, ##create rectangle
                outline="#f11", fill="#1f1", width=2)
            self.obstacles.append(obst_id)


    def repopulate(self):
        self.canvas.delete("all")
        self.populate()
        self.canvas.pack()

    def add_robot(self): ##temp robot function
        t = turtle.RawTurtle(self.canvas)
        scr = t.getscreen()
        scr.setworldcoordinates(0, 500, 750, 0)
        t.forward(5)
        pass


class Obstacle:
    pass

if __name__ == "__main__":
    root = Tk()
    sc = Scene(master=root)
    root.mainloop()
