from graphics import Window
from maze import Maze

def main():
    win = Window(900, 700)

    margin = 50
    maze_height = 1
    maze_width = 1
    cell_width = 50
    cell_height = 50

    maze = Maze(margin,
         margin,
         maze_height,
         maze_width,
         cell_width,
         cell_height,
         win,
         seed=None
        )
    print("Maze created")

    is_solvable = maze.solve()
    if not is_solvable:
        print("Maze is not solveable")
    else:
        print("Maze is solveable")

    win.wait_for_close()


if __name__ == "__main__":
    main()