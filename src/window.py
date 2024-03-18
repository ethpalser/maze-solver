from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Title"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.is_running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        if not isinstance(line, Line):
            return
        line.draw(self.__canvas, fill_color)