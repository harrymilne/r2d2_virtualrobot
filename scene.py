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
        self.goal_id = None
        self.traffic_state = None
        self.robot_stopped = None

        self.obst_color = "#7109AA"


        self.parent.title("R2D2 Virtual Robot") ##naming window
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        
        self.file_menu = Menu(menubar)
        self.file_menu.add_command(label="Add Robot", command=self.add_robot)
        self.file_menu.add_command(label="Stop Robots", command=self.stop_robots)
        self.file_menu.add_command(label="Start Traffic Lights", command=self.start_traffic)
        self.file_menu.add_command(label="Stop Traffic Lights", command=self.stop_traffic)
        self.file_menu.add_command(label="Repopulate", command=self.repopulate)
        self.file_menu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=self.file_menu)

        self.canvas = Canvas(self, width=width, height=height, bg="black") ##init drawing canvas
        self.canvas.pack()
        self.pack()

        self.populate()
        self.process_robot(0)


    def check_overlapping(self, x, y, size):
        return self.canvas.find_overlapping(x-20, y-20, x+size+20, y+size+20)

    def populate(self, num=25): ##populate obstacles
        self.add_robot()
        
        y_gap = randint(self.height*0.3, self.height*0.6)
        obst_id = self.canvas.create_rectangle(self.width/2-15, 25, self.width/2+15, y_gap, fill=self.obst_color)
        obst_id = self.canvas.create_rectangle(self.width/2-15, y_gap+150, self.width/2+15, self.height-25, fill=self.obst_color)

        goal = randint(0, num-1)

        for sq in range(num): ##loop for how many obstacles wanted
            sq_size = randint(30, 100) ##random size
            x = randint(30, self.width - sq_size - 30) ##random x1 + y1
            y = randint(30, self.height - sq_size - 30)
            while self.check_overlapping(x, y, sq_size): ##check x, y for existing object
                sq_size = randint(30, 100) ##random size
                x = randint(30, self.width - sq_size - 30) ##random x1 + y1
                y = randint(30, self.height - sq_size - 30)
            if sq == goal:
                self.goal_id = self.canvas.create_rectangle(x, y, x + sq_size, y + sq_size, fill="#FFCC33", width=1)
            else:
                obst_id = self.canvas.create_rectangle(x, y, x + sq_size, y + sq_size, fill=self.obst_color, width=1)
            self.obstacles.append(obst_id)



    def repopulate(self):
        self.stop_robots()
        self.robots = []
        self.canvas.delete("all")
        self.canvas.pack()
        self.reset_menu()
        self.populate()
        for robot in self.robots:
            robot.scr.bgcolor("white")
        self.process_robot(0)

    def reset_menu(self):
        self.file_menu.entryconfig("Add Robot", state="normal")
        self.file_menu.entryconfig("Stop Robots", state="normal")

    def add_robot(self): ##temp robot function
        robot_id = len(self.robots)
        if robot_id < 2:
            self.robots.append(Robot(self, robot_id))
        if robot_id >= 1:
            self.process_robot(robot_id)
        if len(self.robots) == 2:
            self.file_menu.entryconfig("Add Robot", state="disabled")

    def stop_robots(self):
        for robot in self.robots:
            robot.signal = "STOP"
        self.file_menu.entryconfig("Stop Robots", state="disabled")

    def process_robot(self, r_id):
        self.robots[r_id].goal_id = self.goal_id
        self.robots[r_id].process()

    def start_traffic(self):
        #self.traffic_state = None
        if not self.traffic_state:
            self.toggle_traffic()
        self.file_menu.entryconfig("Add Robot", state="disabled")


    def toggle_traffic(self):
        if self.traffic_state == "go":
            for robot in self.robots:
                robot.signal = "STOP"
                robot.scr.bgcolor("red")
            self.traffic_state = "stop"
            print("stopping")
        elif self.traffic_state == "stop":
            for robot in self.robots:
                robot.process()
                robot.scr.bgcolor("green")
            self.traffic_state = "go"
            print("starting")
        if not self.traffic_state:
            for robot in self.robots:
                robot.signal = "STOP"
                robot.scr.bgcolor("red")
            self.traffic_state = "stop"
            print("stopping")
        rand_sec = randint(2,5)*1000
        print rand_sec
        if not self.traffic_state == "cancel":
            self.master.after(rand_sec, self.toggle_traffic)
        else:
            for robot in self.robots:
                robot.scr.bgcolor("white")
            if self.robot_stopped == "YES":
                for robot in self.robots:
                    robot.process()
                self.robot_stopped = None



    def stop_traffic(self):
        if self.traffic_state == "stop":
            self.robot_stopped = "YES"
        self.traffic_state = "cancel"



if __name__ == "__main__":
    root = Tk()
    sc = Scene(master=root)
    root.mainloop()

