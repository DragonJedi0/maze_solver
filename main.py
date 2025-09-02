from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)

    start_point = Point(0, 0)
    end_point = Point(100, 100)

    line1 = Line(start_point, end_point)

    start_point = Point(100, 100)
    end_point = Point(200, 100)

    line2 = Line(start_point, end_point)

    start_point = Point(200, 100)
    end_point = Point(300, 300)

    line3 = Line(start_point, end_point)

    win.draw_line(line1)
    win.draw_line(line2)
    win.draw_line(line3)


    win.wait_for_close()


if __name__ == "__main__":
    main()