from graphics import Window

class Cell:
    def __init__(self, window: Window):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window.get_canvas()
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            self._win.create_line(x1, y1, x1, y2)
        if self.has_right_wall:
            self._win.create_line(x2, y1, x2, y2)
        if self.has_top_wall:
            self._win.create_line(x1, y1, x2, y1)
        if self.has_bottom_wall:
            self._win.create_line(x1, y2, x2, y2)
        
    def draw_move(self, to_cell, undo=False):
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"
            
        if not self._x1 or not self._y1 or not self._x2 or not self._y2:
            raise Exception(f"Cell {self} has not been drawn")

        if not to_cell._x1 or not to_cell._y1 or not to_cell._x2 or not to_cell._y2:
            raise Exception(f"Cell {self} has not been drawn")
            
        cen_x1 = self._x2 - (self._x2 - self._x1)/2
        cen_y1 = self._y1 - (self._y1 - self._y2)/2
        
        cen_x2 = to_cell._x2 - (to_cell._x2 - to_cell._x1)/2
        cen_y2 = to_cell._y1 - (to_cell._y1 - to_cell._y2)/2
        
        self._win.create_line(cen_x1, cen_y1, cen_x2, cen_y2, fill=fill_color)
