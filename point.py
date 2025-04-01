from tkinter import Canvas

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.__p1 = p1
        self.__p2 = p2
        
    def draw(self, canvas: Canvas, fill_color):
        x1 = self.__p1.x
        y1 = self.__p1.y
        x2 = self.__p2.x
        y2 = self.__p2.y
        
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
            
        