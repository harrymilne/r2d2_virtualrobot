from Tkinter import*
import time
from random import randint

window = Tk()
window.title("Traffic Light")
canvas = Canvas (window, width = 750, height = 500, bg = "white")

class TrafficLights:
    global window
    global canvas

    def __init__(self):
        window.title("Traffic Light")

        canvas.pack()
        frame = Frame(window)
        frame.pack()
        self.v1 = IntVar()

        rbRed = Radiobutton(frame, text = "Red", bg = "red",
                variable = self.v1, value = 1,
                command = self.processRadiobutton)
        rbGreen = Radiobutton(frame, text = "Green", bg = "green",
                variable = self.v1, value = 2,              
                command = self.processRadiobutton)

        rbRed.grid(row = 10, column = 1)
        rbGreen.grid(row = 10, column = 2)
        window.mainloop()

    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.lbl["fg"] = "red"
        elif self.v1.get() == 'G':
            elf.lbl["fg"] = "green"

    
    id = canvas.create_rectangle(200, 67, 265, 60)
    def displayRectangle(self):
        rectangle1 = canvas.create_rectangle(200, 67, 265, 60, tags = "rect")
    def displayOval(self):
        canvas.create_oval(10, 10, 10, 10, fill='red')
    def displayOval(self):
        canvas.create_oval(30, 30, 30, 30, fill='green')

TrafficLights()





