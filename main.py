from gui.maze import Maze
from gui.window import Window


def main():
    screen_x = 900
    screen_y = 700
    win = Window(screen_x, screen_y)
    num_rows = 24
    num_cols = 32
    margin = 50
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    maze = Maze(
        margin, 
        margin, 
        num_rows, 
        num_cols, 
        cell_size_x, 
        cell_size_y, 
        win)
    win.wait_for_close()


main()