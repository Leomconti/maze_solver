import time

from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_width, cell_height, win=None, seed=None):
        self.win = win
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cells = []
        self.create_cells()
        self.break_entrance_and_exit()
        
    def create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i, j)
    
    def draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_width
        y1 = self.y1 + j * self.cell_height
        x2 = x1 + self.cell_width
        y2 = y1 + self.cell_height
        self.cells[i][j].draw(x1, y1, x2, y2)
        self.animate()

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
        
    def break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self.cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self.draw_cell(0, 0)  # removes the top left cells left wall and redraws it
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)
        self.animate()