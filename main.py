from window import *
from cell import Cell

def main():
    win = Window(800, 600)

    cell_1 = Cell(win)
    cell_2 = Cell(win)
    cell_3 = Cell(win)

    cell_1.has_top_wall = False
    cell_1.has_bottom_wall = False
    cell_2.has_top_wall = False
    cell_2.has_right_wall = False
    cell_3.has_bottom_wall = False
    cell_2.has_left_wall = False

    cell_1.draw(50, 50, 150, 150)
    cell_2.draw(50, 150, 150, 250)
    cell_3.draw(50, 250, 150, 350)

    cell_1.draw_move(cell_2)

    win.wait_for_close()

if __name__ == '__main__':
    main()