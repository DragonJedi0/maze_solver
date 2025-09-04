import time, random
from graphics import Window
from cell import Cell

class Maze():
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win: Window=None,
                 seed=None,
        ):
        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        if (seed is not None):
            random.seed(seed)

        self.__create_cells()
        self.__at_exit = self.__cells[self.__num_cols - 1][self.__num_rows - 1]
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))

        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        # Calculate cell position
        pos_x1 = self.__x1 + (self.__cell_size_x * i)
        pos_x2 = pos_x1 + self.__cell_size_x
        pos_y1 = self.__y1 + (self.__cell_size_y * j)
        pos_y2 = pos_y1 + self.__cell_size_y
        # Draw cell 
        self.__cells[i][j].draw(pos_x1, pos_y1, pos_x2, pos_y2)

        self.__animate()

    def __animate(self):
        if (self.__win is not None):
            self.__win.redraw()
        time.sleep(0.005)

    def __break_entrance_and_exit(self):
        last_row = len(self.__cells) - 1
        last_col = len(self.__cells[last_row]) - 1
        # Remove top left cell wall as entrance
        self.__cells[0][0].has_top_wall = False
        # Remove bottom right cell wall as exit
        self.__cells[last_row][last_col].has_bottom_wall = False

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            unvisited = []
            # Check Left
            if i - 1 >= 0 and self.__cells[i-1][j].visited == False:
                unvisited.append((i-1,j))
            # Check Right
            if i + 1 < len(self.__cells) and self.__cells[i+1][j].visited == False:
                unvisited.append((i+1,j))
            # Check Top
            if j -1 >= 0 and self.__cells[i][j-1].visited == False:
                unvisited.append((i,j-1))
            # Check Bottom
            if j + 1 < len(self.__cells[i]) and self.__cells[i][j+1].visited == False:
                unvisited.append((i,j+1))

            if unvisited == []:
                self.__draw_cell(i, j)
                return
            else:
                dir = random.randint(0,len(unvisited)-1)

            col, row = unvisited[dir]

            # Move Left
            if col == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i-1][j].has_right_wall = False
            # Move Right
            elif col == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i+1][j].has_left_wall = False
            # Move Top
            elif row == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j-1].has_bottom_wall = False
            # Move Bottom
            else:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j+1].has_top_wall = False

            self.__break_walls_r(col, row)

    def __reset_cells_visited(self):
        for row in self.__cells:
            for col in row:
                col.visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        if self.__cells[i][j] is self.__at_exit:
            return True

        self.__animate()
        self.__cells[i][j].visited = True

        #TODO: Move through the maze

        return False
