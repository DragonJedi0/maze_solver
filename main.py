from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    x_point1 = 100
    y_point1 = 100
    x_point2 = 200
    y_point2 = 200

    cell1 = Cell(win)
    cell2 = Cell(win)
    
    cell1.has_bottom_wall = False
    cell1.draw(x_point1, y_point1, x_point2, y_point2)

    cell2.has_top_wall = False
    cell2.draw(x_point2, y_point2, x_point2+100, y_point2+100)

    cell1.draw_move(cell2, False)

    win.wait_for_close()


if __name__ == "__main__":
    main()