from window import *
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)

    m1 = Maze(10, 10, 10, 12, 55,  55, win)

    win.wait_for_close()

if __name__ == '__main__':
    main()