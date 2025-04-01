from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk.tk()
        self.root.title("xyz")
        self.canvas = Canvas()
        
    