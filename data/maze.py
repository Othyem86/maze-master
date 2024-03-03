import time
from gui.cell import Cell
from gui.window import Window


class Maze:
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_columns: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Window = None
            ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list[Cell]] = []

    def _create_cells(self) -> None:
        for _ in range(self._num_columns):
            column_cells = []
            for _ in range(self._num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)
        for col in range(self._num_columns):
            for row in range(self._num_rows):
                print(self._draw_cells(col, row))
                
    def _draw_cells(self, col: int, row: int) -> None:
        if self._win is None:
            return
        cell_x1 = self._x1 + col * self._cell_size_x
        cell_y1 = self._y1 + row * self._cell_size_y
        cell_x2 = cell_x1 + col * self._cell_size_x
        cell_y2 = cell_y1 + row * self._cell_size_y
        self._cells[col][row].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)