from tkinter import Tk, BOTH, Canvas

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

    def draw_line(self, line, fill="black"):
        line.draw(self.__canvas, fill)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, start_point: Point, end_point: Point):
        self.p1 = start_point
        self.p2 = end_point

    def draw(self, canvas: Canvas, fill="black"):
        canvas.create_line(self.p1.x, self.p1.y,
                           self.p2.x, self.p2.y,
                           fill=fill, width=2)
