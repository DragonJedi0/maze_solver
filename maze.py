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
                 win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(self.win))

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        print(f"Cell [{i}][{j}] at ({self.x1}, {self.y1})")
        # Calculate current cell position
        pos_x1 = self.x1
        pos_x2 = self.x1 + self.cell_size_x
        pos_y1 = self.y1
        pos_y2 = self.y1 + self.cell_size_y
        # Draw cell 
        self.__cells[i][j].draw(pos_x1, pos_y1, pos_x2, pos_y2)
        # Update next cell position
        self.x1 = (self.cell_size_x * i)
        if (j == 0):
            self.y1 = self.cell_size_y
        else:
            self.y1 = (self.cell_size_y * (j + 1))

        #TODO: call self.__animate()

