import unittest
from ast import Num
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
        
    def test_maze_reset_visited(self):
        num_cols = 30
        num_rows = 30
        m1 = Maze(10, 40, num_rows, num_cols, 50, 50)
        qtd_visited = 0
        for i in range(num_cols):
            for j in range(num_rows):
                if m1.cells[i][j].visited:
                    qtd_visited += 1
        self.assertEqual(
            0,
            qtd_visited,
        )
        
    def test_maze_reset_visited_2(self):
        num_cols = 30
        num_rows = 30
        m1 = Maze(10, 40, num_rows, num_cols, 50, 50)
        qtd_visited = 0
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(
                    False,
                    m1.cells[i][j].visited,
                    )

        
if __name__ == "__main__":
    unittest.main()