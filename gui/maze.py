import random
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
            win: Window = None,
            seed: int = None
            ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._cells: list[list[Cell]] = []
        self._animation_time = 0.0005
        self._create_cells()
        self._animation_time = 0.005
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

    def solve(self) -> None:
        self._solve_r(0, 0)
    
    def _solve_r(self, x: int, y: int) -> bool:
        self._animation_time = 0.005
        self._animate()
        matrix = self._cells
        curr_cell = matrix[x][y]
        curr_cell.visited = True

        # Check if we are the the exit cell
        if x == self._num_columns - 1 and y == self._num_rows - 1:
            return True
        
        # Try going left recursively
        if x > 0 and not curr_cell.has_left_wall and not matrix[x - 1][y].visited:
            curr_cell.draw_move(matrix[x - 1][y])
            if self._solve_r(x - 1, y):
                return True
            else:
                curr_cell.draw_move(matrix[x - 1][y], True)
        # Try going right recursively
        if x < self._num_columns - 1 and not curr_cell.has_right_wall and not matrix[x + 1][y].visited:
            curr_cell.draw_move(matrix[x + 1][y])
            if self._solve_r(x + 1, y):
                return True
            else:
                curr_cell.draw_move(matrix[x + 1][y], True)
        # Try going up recursively
        if y > 0 and not curr_cell.has_top_wall and not matrix[x][y - 1].visited:
            curr_cell.draw_move(matrix[x][y - 1])
            if self._solve_r(x, y - 1):
                return True
            else:
                curr_cell.draw_move(matrix[x][y - 1], True)
        # Try going down recursively
        if y < self._num_rows - 1 and not curr_cell.has_bottom_wall and not matrix[x][y + 1].visited:
            curr_cell.draw_move(matrix[x][y + 1])
            if self._solve_r(x, y + 1):
                return True
            else:
                curr_cell.draw_move(matrix[x][y + 1], True)
        # Dead end
        self._animation_time = 0.05
        self._animate()        
        return False

    def _create_cells(self) -> None:
        # Create cells
        for _ in range(self._num_columns):
            column_cells = []
            for _ in range(self._num_rows):
                column_cells.append(Cell(self._win))
            self._cells.append(column_cells)
        # Draw cells
        for col in range(self._num_columns):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, x: int, y: int) -> None:
        if self._win is None:
            return 
        cell_x1 = self._x1 + x * self._cell_size_x
        cell_y1 = self._y1 + y * self._cell_size_y
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[x][y].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(self._animation_time)

    def _break_entrance_and_exit(self) -> None:
        # Break first cell
        x, y = 0, 0
        self._cells[x][y].has_top_wall = False
        self._draw_cell(x, y)
        # Break last cell
        x, y = self._num_columns - 1, self._num_rows - 1
        self._cells[x][y].has_bottom_wall = False
        self._draw_cell(x, y)

    def _break_walls_r(self, x: int, y: int) -> None:
        matrix = self._cells
        curr_cell = matrix[x][y]
        curr_cell.visited = True
        while True:
            # Determine not visited neighbors
            neighbors_coords: list[tuple] = []
            # Check left
            if x > 0 and matrix[x - 1][y].visited == False:
                neighbors_coords.append((x - 1, y))
            # Check right
            if x < self._num_columns - 1 and matrix[x + 1][y].visited == False:
                neighbors_coords.append((x + 1, y))
            # Check up
            if y > 0 and matrix[x][y - 1].visited == False:
                neighbors_coords.append((x, y - 1))
            # Check down
            if y < self._num_rows - 1 and matrix[x][y + 1].visited == False:
                neighbors_coords.append((x, y + 1))

            # Draw cell when stop condition is met
            if len(neighbors_coords) == 0:
                self._draw_cell(x, y)
                return             
            
            # Randomly pick next cell and break towards it
            next_cell_coords = neighbors_coords[random.randrange(len(neighbors_coords))]
            next_x: int = next_cell_coords[0]
            next_y: int = next_cell_coords[1]
            next_cell = matrix[next_x][next_y]
            # Break to the left
            if next_x == x - 1:
                curr_cell.has_left_wall = False
                next_cell.has_right_wall = False
            # Break to the right
            if next_x == x + 1:
                curr_cell.has_right_wall = False
                next_cell.has_left_wall = False
            # Break to the top
            if next_y == y - 1:
                curr_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            # Break to the bottom
            if next_y == y + 1:
                curr_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
                
            # Recursive call
            self._break_walls_r(next_x, next_y)
    
    def _reset_visited_cells(self) -> None:
        for col in self._cells:
            for cell in col:
                cell.visited = False  