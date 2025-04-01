from cell import Cell

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 window):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows,
        self.num_cols = num_cols,
        self.cell_size_x = cell_size_x,
        self.win = window.get_canvas()
        
    def _create_cells(self):
        self._cells = [[] for i in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell()
    
    def _draw_cell(self, i, j):
        pass
    
    def _animate(self):
        pass