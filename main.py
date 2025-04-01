from window import Window
from point import Point, Line

win = Window(800, 600)
win.draw_line(Line(Point(), Point(100, 100)))
win.draw_line(Line(Point(800, 600), Point(700, 500)))
win.wait_for_close()