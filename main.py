from gui.window import Window
from gui.basic_shapes import Line, Point

def main():
    win = Window(800, 600)
    line = Line(Point(10,10), Point(20,30))
    win.draw_line(line)
    win.wait_for_close()

main()