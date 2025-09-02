from tkinter import Canvas
from point import Point

class Line():
    def __init__(self, start_point: Point, end_point: Point):
        self.__start_point = start_point
        self.__end_point = end_point

    def draw(self, canvas: Canvas, fill: str):
        canvas.create_line(self.__start_point.x, self.__start_point.y,
                           self.__end_point.x, self.__end_point.y,
                           fill=fill, width=2)
