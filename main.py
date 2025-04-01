from window import Window
from point import Point, Line
from cell import Cell

win = Window(800, 600)
win.draw_line(Line(Point(), Point(100, 100)))
win.draw_line(Line(Point(800, 600), Point(700, 500)))
cell = Cell(100, 200, 100, 200, win)
cell.draw()
win.wait_for_close()