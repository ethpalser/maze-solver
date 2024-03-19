from window import Window
from cell import Cell
from time import sleep
import random

class Maze:

    def __init__(
        self,
        x1:int, y1:int,
        num_rows:int,
        num_cols:int,
        cell_size_x:int,
        cell_size_y:int,
        window:Window = None,
        seed = None
    ):
        if window is not None and not isinstance(window, Window):
            raise ValueError("Window must be a window class")
        if num_rows <= 0 or num_cols <= 0:
            raise ValueError("Maze cannot have zero or less rows nor columns")
        if cell_size_x <= 0 or cell_size_y <= 0:
            raise ValueError("Cell size must be greater than 0")
        
        self._rand = random.Random(seed)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window

        self._cells = self._create_cells()
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                self._draw_cell(i, j)

        self._break_enterance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        list = [[] for i in range(0, self._num_rows)]
        for y in range(0, self._num_rows):
            for x in range(0, self._num_cols):
                cell_x1 = self._x1 + x * self._cell_size_x
                cell_x2 = cell_x1 + self._cell_size_x
                cell_y1 = self._y1 + y * self._cell_size_y
                cell_y2 = cell_y1 + self._cell_size_y
                list[y].append(Cell(cell_x1, cell_y1, cell_x2, cell_y2, window=self._win))
        return list
    
    def _draw_cell(self, i, j):
        if self._win is None or not isinstance(self._win, Window):
            return
        cell = self._cells[i][j]
        if isinstance(cell, Cell):
            cell.draw()
            self._animate()

    def _animate(self):
        if self._win is None or not isinstance(self._win, Window):
            return
        self._win.redraw()
        sleep(0.02)

    def _remove_wall(self, i, j, direction):
        self._cells[i][j].draw("white") # Erase all walls
        if direction == "top":
            self._cells[i][j].has_top_wall = False
        elif direction == "left":
            self._cells[i][j].has_left_wall = False
        elif direction == "bottom":
            self._cells[i][j].has_bottom_wall = False
        elif direction == "right":
            self._cells[i][j].has_right_wall = False
        else:
            raise ValueError("Direction is not one of 'top', 'left', 'bottom' or 'right'")
        self._cells[i][j].draw() # Redraw all walls except removed wall
        self._animate()


    def _break_enterance_and_exit(self):
        self._remove_wall(0, 0, "top")
        self._remove_wall(self._num_rows - 1, self._num_cols - 1, "bottom")

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        if not isinstance(cell, Cell):
            raise Exception(f"Maze does not have a cell at ({i},{j})")
        cell.visited = True
        while True:
            unvisited_neighbors = []
            unvisited_directions = []
            if i-1 >= 0 and not self._cells[i - 1][j].visited:
                unvisited_neighbors.append((i - 1, j))
                unvisited_directions.append("top")
            if j-1 >= 0 and not self._cells[i][j - 1].visited:
                unvisited_neighbors.append((i, j - 1))
                unvisited_directions.append("left")
            if i+1 < self._num_rows and not self._cells[i + 1][j].visited:
                unvisited_neighbors.append((i + 1, j))
                unvisited_directions.append("bottom")
            if j+1 < self._num_cols and not self._cells[i][j + 1].visited:
                unvisited_neighbors.append((i, j + 1))
                unvisited_directions.append("right")
            
            if len(unvisited_neighbors) == 0:
                return

            next_cell = self._rand.randrange(0, len(unvisited_neighbors))
            direction = unvisited_directions[next_cell]
            self._remove_wall(i, j, direction)
            if direction == "top":
                self._remove_wall(i - 1, j, "bottom")
            elif direction == "left":
                self._remove_wall(i, j - 1, "right")
            elif direction == "bottom":
                self._remove_wall(i + 1, j, "top")
            elif direction == "right":
                self._remove_wall(i, j + 1, "left")
            self._break_walls_r(*unvisited_neighbors[next_cell])

    def _reset_cells_visited(self):
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_dfs(0, 0)

    def _solve_dfs(self, i:int, j:int):
        cell = self._cells[i][j]
        if not isinstance(cell, Cell):
            raise Exception(f"Maze does not have a cell at ({i},{j})")
        
        cell.visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True

        unvisited_neighbors = []
        if i-1 >= 0 and not cell.has_top_wall and not self._cells[i - 1][j].visited:
            unvisited_neighbors.append((i - 1, j))
        if j-1 >= 0 and not cell.has_left_wall and not self._cells[i][j - 1].visited:
            unvisited_neighbors.append((i, j - 1))
        if i+1 < self._num_rows and not cell.has_bottom_wall and not self._cells[i + 1][j].visited:
            unvisited_neighbors.append((i + 1, j))
        if j+1 < self._num_cols and not cell.has_right_wall and not self._cells[i][j + 1].visited:
            unvisited_neighbors.append((i, j + 1))

        if len(unvisited_neighbors) == 0:
            return False

        has_path_to_end = False
        for neighbor in unvisited_neighbors:
            neighbor_cell = self._cells[neighbor[0]][neighbor[1]]
            self._cells[i][j].draw_move(neighbor_cell)
            self._animate()
            path_to_end = self._solve_dfs(*neighbor)
            if not path_to_end:
                self._cells[i][j].draw_move(neighbor_cell, True)
                self._animate()
            else:
                has_path_to_end = True
        return has_path_to_end

        