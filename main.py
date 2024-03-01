from gui.shapes import *
from gui.window import *

def main():
    win = Window(800, 600)
    line = Line(Point(10,10), Point(20,30))
    win.draw_line(line)
    win.wait_for_close()

main()