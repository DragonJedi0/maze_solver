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
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if (seed is not None):
            self.seed = random.seed(seed)
        else:
            self.seed = random.seed()
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(self.win))

        self.__break_entrance_and_exit()

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        # Calculate cell position
        pos_x1 = self.x1 + (self.cell_size_x * i)
        pos_x2 = pos_x1 + self.cell_size_x
        pos_y1 = self.y1 + (self.cell_size_y * j)
        pos_y2 = pos_y1 + self.cell_size_y
        # print(f"Drawing Cell [{i}][{j}] at ({pos_x1}, {pos_y1})")
        # Draw cell 
        self.__cells[i][j].draw(pos_x1, pos_y1, pos_x2, pos_y2)

        self.__animate()

    def __animate(self):
        if (self.win is not None):
            self.win.redraw()
        time.sleep(0.005)

    def __break_entrance_and_exit(self):
        last_row = len(self.__cells) - 1
        last_col = len(self.__cells[last_row]) - 1
        # Remove top left cell wall as entrance
        self.__cells[0][0].has_top_wall = False
        # Remove bottom right cell wall as exit
        self.__cells[last_row][last_col].has_bottom_wall = False

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visted = True
        inf = True
        while(inf):
            unvisted_col = []
            unvisted_row = []
            try:
                pass
            except IndexError as e:
                pass
