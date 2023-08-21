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