import unittest
from gui.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_columns = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_columns, 10, 10)
        self.assertEqual(len(m1._cells), num_columns)
        self.assertEqual(len(m1._cells[0]), num_rows)

if __name__ == "__main__":
    unittest.main()