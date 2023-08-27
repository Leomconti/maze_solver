from re import M

from cell import Cell
from maze import Maze
from window import Window


def main():
    win = Window(800, 600)
    
    m1 = Maze(50, 50, 10, 10, 50, 50, win, seed=999)

    win.wait_for_close()


main()
