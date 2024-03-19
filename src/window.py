from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._root = Tk()
        self._root.title("Title")
        self._root.geometry(f"{width}x{height}+120+80")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, width=width, height=height, borderwidth=0, highlightthickness=0, background="white")
        self._canvas.pack()
        self.is_running = False
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        if not isinstance(line, Line):
            return
        line.draw(self._canvas, fill_color)