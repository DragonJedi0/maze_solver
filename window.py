from tkinter import Tk, BOTH, Canvas
from line import Line

class Window():
    def __init__(self, width, height):
        # Create root using Tk
        self.__root = Tk()
        # Set root's title
        self.__root.title("Maze Solver")
        # Create Canvas using Canvas(root, bg, height, width)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        # Pack the canvas using pack(fill=BOTH, expand=1)
        self.__canvas.pack(fill=BOTH, expand=1)
        # Set private running state boolean
        self.__running = False
        # call root's protocol to connect close() to "delete window" action
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while (self.__running):
            self.redraw()
        print("Maze Solver has been closed")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill="black"):
        line.draw(self.__canvas, fill)
