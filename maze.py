import random
import time
from re import X

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
        self.random = random.Random(seed)
        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()
        
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
        time.sleep(0.02)
        
    def break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self.cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self.draw_cell(0, 0)  # removes the top left cells left wall and redraws it
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)
        self.animate()
        
    def break_walls_r(self, i, j): # i and j, are the values you need to visit
        curr_cell = self.cells[i][j]
        curr_cell.visited = True 
        while True:
            valid_adj = []
            adjacents = [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]]
            # got to check if the adjacent cells are valid
            for adj in adjacents:
                if adj[0] < 0 or adj[0] >= self.num_cols:
                    continue
                if adj[1] < 0 or adj[1] >= self.num_rows:
                    continue
                
                adj_cell = self.cells[adj[0]][adj[1]] # checl if it is visited
                if adj_cell.visited is not True:
                    valid_adj.append(adj)  # if it is not visited, append it to the list of valid adjacents
                    
            if len(valid_adj) == 0:  # if there are no valid adjacents, return
                self.draw_cell(i, j)
                return
                
            # we will be choosing a random adjacent cell
            chosen_adj = self.random.choice(valid_adj)
            chosen_cell = self.cells[chosen_adj[0]][chosen_adj[1]]

            # break the right wall
            if chosen_adj[0] == i + 1:
                chosen_cell.has_left_wall = False
                curr_cell.has_right_wall = False
            # break the left wall
            elif chosen_adj[0] == i - 1:
                chosen_cell.has_right_wall = False
                curr_cell.has_left_wall = False
            # break the top wall
            elif chosen_adj[1] == j + 1:
                chosen_cell.has_top_wall = False
                curr_cell.has_bottom_wall = False
            # break the bottom wall
            elif chosen_adj[1] == j - 1:
                chosen_cell.has_bottom_wall = False
                curr_cell.has_top_wall = False
            
            self.break_walls_r(chosen_adj[0], chosen_adj[1])
                

    def reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

    def solve(self):
        solve = self.r_solve(0, 0)
        
        return solve
    
    def r_solve(self, i, j):
        self.animate()
        curr_cell = self.cells[i][j]
        curr_cell.visited = True
        print(i, j)
        print(self.num_cols, self.num_rows)
        if (i == self.num_cols - 2 and j == self.num_rows) and curr_cell.has_right_wall is False:
            return True
        
        elif (i == self.num_cols and j == self.num_rows - 2 ) and curr_cell.has_bottom_wall is False:
            return True
        
        elif (i == self.num_cols -1 and j == self.num_rows -1): 
            return True
        
        while True:
            valid_adj = False
            adjacents = [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]]
            for adj in adjacents:
                if adj[0] < 0 or adj[0] >= self.num_cols:
                    continue
                if adj[1] < 0 or adj[1] >= self.num_rows:
                    continue 
                
                adj_cell = self.cells[adj[0]][adj[1]] # checl if it is visited
                # right 
                if adj[0] == i + 1 and adj[1] == j:
                    if curr_cell.has_right_wall is False and adj_cell.has_left_wall is False and not adj_cell.visited:
                        curr_cell.draw_move(adj_cell)
                        solve = self.r_solve(adj[0], adj[1])
                        if solve:
                            return True
                        curr_cell.draw_move(adj_cell, undo=True)
                # left 
                elif adj[0] == i - 1 and adj[1] == j:
                    if curr_cell.has_left_wall is False and adj_cell.has_right_wall is False and not adj_cell.visited:
                        curr_cell.draw_move(adj_cell)
                        solve = self.r_solve(adj[0], adj[1])
                        if solve:
                            return True
                        curr_cell.draw_move(adj_cell, undo=True)
                # top wall
                elif adj[1] == j - 1 and adj[0] == i:
                    if curr_cell.has_top_wall is False and adj_cell.has_bottom_wall is False and not adj_cell.visited:
                        curr_cell.draw_move(adj_cell)
                        solve = self.r_solve(adj[0], adj[1])
                        if solve:
                            return True
                        curr_cell.draw_move(adj_cell, undo=True)
                # bottom wall
                elif adj[1] == j + 1 and adj[0] == i:
                    if curr_cell.has_bottom_wall is False and adj_cell.has_top_wall is False and not adj_cell.visited:
                        curr_cell.draw_move(adj_cell)
                        solve = self.r_solve(adj[0], adj[1])
                        if solve:
                            return True
                        curr_cell.draw_move(adj_cell, undo=True)
            

            return False
                