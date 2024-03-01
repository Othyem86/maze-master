from tkinter import Tk, Canvas

class Point:
     def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.__start = p1
        self.__end = p2
    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__start.x,
            self.__start.y,
            self.__end.x,
            self.__end.y,
            fill = fill_color,
            width = 2
        )
        canvas.pack()