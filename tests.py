import unittest
from gui.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_columns = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_columns, 10, 10)
        self.assertEqual(
            len(maze._cells), 
            num_columns
            )
        self.assertEqual(
            len(maze._cells[0]), 
            num_rows
            )

    def test_maze_break_entrance_and_exit(self):
        num_columns = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_columns, 10, 10)
        self.assertEqual(
            maze._cells[0][0].has_top_wall, 
            False
            )
        self.assertEqual(
            maze._cells[num_columns - 1][num_rows - 1].has_bottom_wall, 
            False
            )
        
    def test_reset_visited_cells(self):
        maze = Maze(0, 0, 10, 12, 10, 10)
        for col in maze._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False
                )


if __name__ == "__main__":
    unittest.main()