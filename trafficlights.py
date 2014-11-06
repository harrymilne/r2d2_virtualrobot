from Tkinter import*
import time

class TrafficLights:
    def __init__(self):
        window = Tk()
        window.title("Traffic Light")

        self.canvas = Canvas (window, width = 750, height = 500, bg = "white")
        self.canvas.pack()
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

    
    id = self.canvas.create_rectangle(200, 67, 265, 60)
    def displayRectangle(self):
        self.canvas.create_rectangle(200, 67, 265, 60, tags = "rect")
    def displayOval(self):
        self.canvas.create_oval(10, 10, 10, 10, fill='red')
    def displayOval(self):
        self.canvas.create_oval(30, 30, 30, 30, fill='green')

TrafficLights()





