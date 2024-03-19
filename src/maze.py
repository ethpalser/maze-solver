from window import Window
from cell import Cell
from time import sleep

class Maze:

    def __init__(
        self,
        x1, y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window = None
    ):
        if window is not None and not isinstance(window, Window):
            raise ValueError("Window must be a window class")
        if num_rows <= 0 or num_cols <= 0:
            raise ValueError("Maze cannot have zero or less rows nor columns")
        if cell_size_x <= 0 or cell_size_y <= 0:
            raise ValueError("Cell size must be greater than 0")
        
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window

        self._cells = self._create_cells()
        for j in range(0, num_cols):
            for i in range(0, num_rows):
                self._draw_cell(i, j)

    def _create_cells(self):
        list = [[] for i in range(0, self._num_cols)]
        for y in range(0, self._num_cols):
            for x in range(0, self._num_rows):
                cell_x1 = self._x1 + x * self._cell_size_x
                cell_x2 = cell_x1 + self._cell_size_x
                cell_y1 = self._y1 + y * self._cell_size_y
                cell_y2 = cell_y1 + self._cell_size_y
                list[y].append(Cell(cell_x1, cell_y1, cell_x2, cell_y2, self._win))
        return list
    
    def _draw_cell(self, i, j):
        if self._win is None or not isinstance(self._win, Window):
            return
        cell = self._cells[i][j]
        if isinstance(cell, Cell):
            cell.draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)