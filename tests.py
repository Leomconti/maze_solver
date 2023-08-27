import unittest
from email.charset import QP

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                        len(m1.cells), 
                        num_cols,
                        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells_2(self):
        num_cols = 30
        num_rows = 30
        m1 = Maze(10, 40, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(m1.cells), # quantidade de colunas ok
            num_cols,
            )
        self.assertEqual(
            len(m1.cells[0]),  # quantidade de linhas ok
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()