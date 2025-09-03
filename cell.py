from graphics import Window, Point, Line

class Cell():
    def __init__(self, window: Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        def line_to_draw(p1: Point, p2: Point, win: Window, fill):
            line = Line(p1, p2)
            if (win is not None):
                win.draw_line(line, fill)

        # Left Wall
        line_to_draw(
            Point(self.__x1, self.__y1),
            Point(self.__x1, self.__y2),
            self.__win,
            "black" if self.has_left_wall else "white",
            )

        # Right Wall
        line_to_draw(
            Point(self.__x2, self.__y1),
            Point(self.__x2, self.__y2),
            self.__win,
            "black" if self.has_right_wall else "white",
            )

        # Top Wall
        line_to_draw(
            Point(self.__x1, self.__y1),
            Point(self.__x2, self.__y1),
            self.__win,
            "black" if self.has_top_wall else "white",
            )

        # Bottom Wall
        line_to_draw(
            Point(self.__x1, self.__y2),
            Point(self.__x2, self.__y2),
            self.__win,
            "black" if self.has_bottom_wall else "white",
            )

    def center(self):
        x_center = (self.__x1 + self.__x2) / 2
        y_center = (self.__y1 + self.__y2) / 2

        return Point(x_center, y_center) 

    def draw_move(self, to_cell, undo=False):
        if not undo:
            fill = "red"
        else:
            fill = "gray"

        move_line = Line(self.center(), to_cell.center())
        if (self.__win is not None):
            self.__win.draw_line(move_line, "black")
