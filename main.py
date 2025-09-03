from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)

    start_x = 0
    start_y = 0
    maze_width = 12
    maze_height = 16
    cell_width = 50
    cell_height = 50

    Maze(start_x,
         start_y,
         maze_width,
         maze_height,
         cell_width,
         cell_height,
         win
        )

    win.wait_for_close()


if __name__ == "__main__":
    main()