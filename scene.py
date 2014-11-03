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

    def check_overlapping(self, x, y, size):
        
        return self.canvas.find_overlapping(x-20, y-20, x+size+20, y+size+20)
    

    def populate(self, num=15): ##populate obstacles
        self.add_robot()
        for sq in range(num): ##loop for how many obstacles wanted
            sq_size = randint(30, 100) ##random size
            x = randint(20, self.width - sq_size - 20) ##random x1 + y1
            y = randint(20, self.height - sq_size - 20)
            while self.check_overlapping(x, y, sq_size): ##check x, y for existing object
                sq_size = randint(30, 100) ##random size
                x = randint(20, self.width - sq_size - 20) ##random x1 + y1
                y = randint(20, self.height - sq_size - 20)
            obst_id = self.canvas.create_rectangle(x, y, x + sq_size, y + sq_size,
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
        t.left(45)
        t.forward(50)
        pass


class Obstacle:
    pass

if __name__ == "__main__":
    root = Tk()
    sc = Scene(master=root)
    root.mainloop()
