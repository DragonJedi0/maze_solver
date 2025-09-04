from graphics import Window
from maze import Maze

def main():
    win = Window(900, 700)

    start_x = 50
    start_y = 50
    maze_height = 12
    maze_width = 16
    cell_width = 50
    cell_height = 50

    Maze(start_x,
         start_y,
         maze_height,
         maze_width,
         cell_width,
         cell_height,
         win,
         seed=None
        )

    win.wait_for_close()


if __name__ == "__main__":
    main()