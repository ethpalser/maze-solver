from window import Window
from line import Line
from point import Point

class Cell:

    def __init__(
        self,
        window,
        x1, y1,
        x2, y2,
        has_left_wall = True,
        has_right_wall = True,
        has_top_wall = True,
        has_bottom_wall = True
    ):
        for point in [x1, x2, y1, y2]:
            if not isinstance(point, int):
                raise ValueError("Points in a cell must be an integer.")
        self._win = window
        self._min_x = min(x1, x2)
        self._min_y = min(y1, y2)
        self._max_x = max(x1, x2)
        self._max_y = max(y1, y2)
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self, fill_color):
        if self._win is None or not isinstance(self._win, Window):
            return
        top_left_point = Point(self._min_x, self._min_y)
        top_right_point = Point(self._max_x, self._min_y)
        bottom_left_point = Point(self._min_x, self._max_y)
        bottom_right_point = Point(self._max_x, self._max_y)

        if self.has_top_wall:
            self._win.draw_line(Line(top_left_point, top_right_point), fill_color)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left_point, bottom_left_point), fill_color)
        if self.has_right_wall:
            self._win.draw_line(Line(top_right_point, bottom_right_point), fill_color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left_point, bottom_right_point), fill_color)