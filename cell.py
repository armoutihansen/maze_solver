from window import Window

class Cell:
    def __init__(self,
                 x1,
                 x2,
                 y1,
                 y2,
                 window: Window,
                 has_left_wall=True,
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True,
                 ):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window.get_canvas()
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        
    def draw(self):
        x1 = self._x1
        y1 = self._y1
        x2 = self._x2
        y2 = self._y2
        if self.has_left_wall:
            self._win.create_line(x1, y1, x1, y2)
        if self.has_right_wall:
            self._win.create_line(x2, y1, x2, y2)
        if self.has_top_wall:
            self._win.create_line(x1, y1, x2, y1)
        if self.has_bottom_wall:
            self._win.create_line(x1, y2, x2, y2)
        