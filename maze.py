import time

from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_width, cell_height, win=None):
        self.win = win
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cells = []
        self.create_cells()
        
    def create_cells(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                cell = Cell(self.win)
                cell.draw(self.x1 + j * self.cell_width, self.y1 + i * self.cell_height, 
                          self.x1 + (j + 1) * self.cell_width, self.y1 + (i + 1) * self.cell_height)
                self.cells.append(cell)
    
    def animate(self):
        self.win.redraw()
        time.sleep(0.05)