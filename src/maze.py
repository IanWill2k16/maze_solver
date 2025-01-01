from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed = None):
        self._seed = seed
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if self._seed is not None:
             random.seed(self._seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(self._win))
            self._cells.append(row)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * i)
        y1 = self._y1 + (self._cell_size_y * j)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        # time.sleep(0.05)

    def _break_entrance_and_exit(self):
        start_cell = self._cells[0][0]
        start_cell.has_top_wall = False
        self._draw_cell(0, 0)

        end_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        end_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current._visited = True

        while True:
            to_visit = []

            if i + 1 < self._num_cols and self._cells[i + 1][j]._visited == False:
                    to_visit.append((i + 1, j, "right"))
            if i - 1 >= 0 and self._cells[i - 1][j]._visited == False:
                    to_visit.append((i - 1, j, "left"))
            if j + 1 < self._num_rows and self._cells[i][j + 1]._visited == False:
                    to_visit.append((i, j + 1, "down"))
            if j - 1 >= 0 and self._cells[i][j - 1]._visited == False:
                    to_visit.append((i, j - 1, "up"))
            if not to_visit:
                return
            
            direction = random.randint(0, len(to_visit) - 1)

            next_visited_cell = self._cells[to_visit[direction][0]][to_visit[direction][1]]

            if to_visit[direction][2] == "right":
                current.has_right_wall = False
                next_visited_cell.has_left_wall = False
            if to_visit[direction][2] == "left":
                current.has_left_wall = False
                next_visited_cell.has_right_wall = False
            if to_visit[direction][2] == "down":
                current.has_bottom_wall = False
                next_visited_cell.has_top_wall = False
            if to_visit[direction][2] == "up":
                current.has_top_wall = False
                next_visited_cell.has_bottom_wall = False

            self._draw_cell(i, j)
            self._draw_cell(to_visit[direction][0], to_visit[direction][1])

            self._break_walls_r(to_visit[direction][0], to_visit[direction][1])

    def _reset_cells_visited(self):
         for i in range(len(self._cells)):
              for j in range(len(self._cells[i])):
                   self._cells[i][j].visited = False