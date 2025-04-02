import time
from cell import Cell
import random

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 window=None,
                 seed = None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        if seed:
            random.seed(seed)
            

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0, 0)
        self._reset_cells_visited()
        
    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
                
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.025)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        self._animate
        
    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            lst = []
            if i < self._num_cols - 1:
                if not self._cells[i+1][j].visited:
                    lst.append((i+1, j))
            if i > 0:
                if not self._cells[i-1][j].visited:
                    lst.append((i-1, j))
            if j < self._num_rows - 1:
                if not self._cells[i][j+1].visited:
                    lst.append((i, j+1))
            if j > 0:
                if not self._cells[i][j-1].visited:
                    lst.append((i, j-1))
            
            if len(lst) == 0:
                self._draw_cell(i, j)
                return
            else:
                rand_dir = random.choice(lst)
                i_, j_ = rand_dir[0], rand_dir[1]
                if i_ > i:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i_][j_].has_left_wall = False
                elif i_ < i:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i_][j_].has_right_wall = False
                elif j_ > j:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i_][j_].has_top_wall = False
                else:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i_][j_].has_bottom_wall = False
                self._draw_cell(i_, j_)
                self._break_walls(i_, j_)
                
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
                
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        if (
            i > 0 
            and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
            
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
            
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        
        return False
                
                        
                        