##scene.py

from Tkinter import *
from random import randint
from turtle import RawTurtle

from robot import Robot

class Scene(Frame): ##main canvas class (creating the window)
    def __init__(self, master=None, width=750, height=500): ##passing the Tk root + options
        Frame.__init__(self, master) ##constructing the parent class
        self.parent = master ##keeping root for future reference
        self.width = width ##keeping width + height for future reference in class
        self.height = height
        self.obstacles = []
        self.robots = []


        self.parent.title("R2D2 Virtual Robot") ##naming window
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        self.file_menu = Menu(menubar)
        self.file_menu.add_command(label="Add Robot", command=self.add_robot)
        self.file_menu.add_command(label="Stop Robots", command=self.stop_robots)
        self.file_menu.add_command(label="Repopulate", command=self.repopulate)
        self.file_menu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=self.file_menu)

        self.canvas = Canvas(self, width=width, height=height) ##init drawing canvas
        self.canvas.pack()
        self.pack()

        self.populate()
        
    def clear(self):
        self.canvas.clear()

    def check_overlapping(self, x, y, size):
        return self.canvas.find_overlapping(x-20, y-20, x+size+20, y+size+20)
    

    def populate(self, num=20): ##populate obstacles
        self.add_robot()
        
        x_gap = randint(self.width*0.3, self.width*0.6)
        y_gap = randint(self.height*0.3, self.height*0.6)
        obst_id = self.canvas.create_rectangle(self.width/2, -1, self.width/2+10, y_gap, fill="#000")
        obst_id = self.canvas.create_rectangle(self.width/2, y_gap+100, self.width/2+10, self.height, fill="#000")

        for sq in range(num): ##loop for how many obstacles wanted
            sq_size = randint(30, 100) ##random size
            x = randint(20, self.width - sq_size - 20) ##random x1 + y1
            y = randint(20, self.height - sq_size - 20)
            while self.check_overlapping(x, y, sq_size): ##check x, y for existing object
                sq_size = randint(30, 100) ##random size
                x = randint(20, self.width - sq_size - 20) ##random x1 + y1
                y = randint(20, self.height - sq_size - 20)
            obst_id = self.canvas.create_rectangle(x, y, x + sq_size, y + sq_size,
                outline="#000", fill="#1f1", width=2)
            self.obstacles.append(obst_id)



    def repopulate(self):
        self.robots = []
        self.canvas.delete("all")
        self.populate()
        self.canvas.pack()
        self.process_robots()

    def add_robot(self): ##temp robot function
        robot_id = len(self.robots)
        if len(self.robots) < 2:
            self.robots.append(Robot(self, robot_id))
        if len(self.robots) == 2:
            self.file_menu.entryconfig("Add Robot", state="disabled")
        self.robots[-1].process()

    def stop_robots(self):
        for robot in self.robots:
            robot.done = True

    def process_robots(self):
        for robot in self.robots:
            robot.process()


if __name__ == "__main__":
    root = Tk()
    sc = Scene(master=root)
    root.mainloop()
