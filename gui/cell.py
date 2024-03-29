from gui.basic_shapes import Point, Line
from gui.window import Window


class Cell:
    def __init__(self, win: Window = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        # Left wall
        line = Line(Point(x1, y1), Point(x1, y2))
        line_color = self.get_wall_color(self.has_left_wall)
        self._win.draw_line(line, line_color)
        # Right wall
        line = Line(Point(x2, y1), Point(x2, y2))
        line_color = self.get_wall_color(self.has_right_wall)
        self._win.draw_line(line, line_color)
        # Top wall
        line = Line(Point(x1, y1), Point(x2, y1))
        line_color = self.get_wall_color(self.has_top_wall)
        self._win.draw_line(line, line_color)
        # Bottom wall
        line = Line(Point(x1, y2), Point(x2, y2))
        line_color = self.get_wall_color(self.has_bottom_wall)
        self._win.draw_line(line, line_color)

    def draw_move(self, to_cell: 'Cell', undo: bool = False):
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2
        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2
        line_color = "gray" if undo else "red"
        if y_mid == to_y_mid or x_mid == to_x_mid:
            line = Line(Point(x_mid, y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, line_color)
        else:
            raise ValueError("Invalid move, moves must be carthesian.")
        
    def get_wall_color(self, has_wall: bool) -> str:
        return "black" if has_wall else "white" 