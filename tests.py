import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 18
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._Maze__cells[1][1].has_bottom_wall,
            False
        )
        self.assertNotEqual(
            m1._Maze__cells[1][0].has_bottom_wall,
            False
        )
        self.assertNotEqual(
            m1._Maze__cells[0][1].has_top_wall,
            False
        )

    def test_break_walls(self):
        num_cols = 2
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        for i in range(len(m1._Maze__cells)):
            for j in range(len(m1._Maze__cells[i])):
                self.assertTrue(m1._Maze__cells[i][j].visited)
                self.assertEqual(
                    m1._Maze__cells[i][j].has_top_wall,
                    m2._Maze__cells[i][j].has_top_wall,
                    )
                self.assertEqual(
                    m1._Maze__cells[i][j].has_bottom_wall,
                    m2._Maze__cells[i][j].has_bottom_wall,
                    )
                self.assertEqual(
                    m1._Maze__cells[i][j].has_left_wall,
                    m2._Maze__cells[i][j].has_left_wall,
                    )
                self.assertEqual(
                    m1._Maze__cells[i][j].has_right_wall,
                    m2._Maze__cells[i][j].has_right_wall,
                    )


if __name__ == "__main__":
    unittest.main()