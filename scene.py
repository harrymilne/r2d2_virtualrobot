##scene.py

from Tkinter import *
from random import randint
import time
import Queue
import threading

class Scene(Frame): ##main canvas class (creating the window)
    def __init__(self, master=None, width=750, height=500): ##passing the Tk root + options
        Frame.__init__(self, master) ##constructing the parent class
        self.parent = master ##keeping root for future reference
        self.width = width ##keeping width + height for future reference in class
        self.height = height


        self.parent.title("R2D2 Virtual Robot") ##naming window
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        file_menu = Menu(menubar)
        file_menu.add_command(label="Repopulate", command=self.repopulate)
        file_menu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.pack()

        self.canvas = Canvas(self, width=width, height=height) ##init drawing canvas
        self.populate()
        self.canvas.pack()

    def on_exit(self):
        print "bye"
        self.quit()

    def clear(self):
        self.canvas.clear()

    def check_overlapping(self, x, y):
        tested = []
        for i in range(-50, 60, 50):
            tested.append(self.canvas.find_overlapping(x+i, y+i, x+i+100, y+i+100))

        return any(tested)

    def populate(self, num=5): ##populate obstacles
        for sq in range(num): ##loop for how many obstacles wanted
            x = randint(0, self.width-100) ##random x1 + y1
            y = randint(0, self.height-100)

            while self.check_overlapping(x, y):
                x = randint(0, self.width-100) ##random x1 + y1
                y = randint(0, self.height-100)
            self.canvas.create_rectangle(x, y, x+100, y+100, ##create rectangle
                outline="#f11", fill="#1f1", width=2)

    def repopulate(self):
        self.canvas.delete("all")
        self.populate()
        self.canvas.pack()

    def start_robot(self):
        ##
        pass


class Obstacle:
    pass

if __name__ == "__main__":
    root = Tk()
    sc = Scene(master=root)
    root.mainloop()
