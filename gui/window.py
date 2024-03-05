from tkinter import Tk, BOTH, Canvas
from gui.basic_shapes import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title = "Maze Master 9000"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window closed...")

    def close(self) -> None:
        self.__is_running = False

    def draw_line(self, line: Line, color: str = "black") -> None:
        line.draw(self.__canvas, color)