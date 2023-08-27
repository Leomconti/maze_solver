from window import Line, Point


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
        if self.win is None:
            return 
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        # we draw the white wall because it is the background color
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line, "white")
            
    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return 
        # we will be drawing a line from the middle of one cell to the other
        from_x = (self.x1 + self.x2) / 2
        from_y = (self.y1 + self.y2) / 2
        
        to_x = (to_cell.x1 + to_cell.x2) / 2
        to_y = (to_cell.y1 + to_cell.y2) / 2
        
        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self.x1 > to_cell.x1:
            line = Line(Point(self.x1, from_y), Point(from_x, from_y))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_x, to_y), Point(to_cell.x2, to_y))
            self.win.draw_line(line, fill_color)

        # moving right
        elif self.x1 < to_cell.x1:
            line = Line(Point(from_x, from_y), Point(self.x2, from_y))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_cell.x1, to_y), Point(to_x, to_y))
            self.win.draw_line(line, fill_color)

        # moving up
        elif self.y1 > to_cell.y1:
            line = Line(Point(from_x, from_y), Point(from_x, self.y1))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_x, to_cell.y2), Point(to_x, to_y))
            self.win.draw_line(line, fill_color)

        # moving down
        elif self.y1 < to_cell.y1:
            line = Line(Point(from_x, from_y), Point(from_x, self.y2))
            self.win.draw_line(line, fill_color)
            line = Line(Point(to_x, to_y), Point(to_x, to_cell.y1))
            self.win.draw_line(line, fill_color)