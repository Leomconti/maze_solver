import tkinter as tk
from tkinter import BOTH, Canvas, Tk

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
        print("Window closed!!...")

    def close(self):
        self.running = False
        
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)
        
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="black"):
        x1, y1, x2, y2 = self.p1.x, self.p1.y, self.p2.x, self.p2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)
