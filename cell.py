from graphics import Window, Line, Point

class Cell:
    def __init__(self, window: Window = None):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
        
    def draw_move(self, to_cell, undo=False):
        if not undo:
            fill_color = "red"
        else:
            fill_color = "white"
        half_length1 = abs(self._x2 - self._x1) // 2
        cen_x1 = half_length1 + self._x1
        cen_y1 = half_length1 + self._y1
        
        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        cen_x2 = half_length2 + to_cell._x1
        cen_y2 = half_length2 + to_cell._y1
        
        line = Line(Point(cen_x1, cen_y1), Point(cen_x2, cen_y2))
        self._win.draw_line(line, fill_color)
            