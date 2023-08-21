from line import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)
            
    def draw_move(self, to_cell, undo=False):
        # we will be drawing a line from the middle of one cell to the other
        x1 = (self.x1 + self.x2) / 2
        y1 = (self.y1 + self.y2) / 2
        x2 = (to_cell.x1 + to_cell.x2) / 2
        y2 = (to_cell.y1 + to_cell.y2) / 2
        self.win.draw_line(Line(Point(x1, y1), Point(x2, y2)), "red" if not undo else "gray")