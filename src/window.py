from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title('Main Window')

        self._canvas = Canvas(self._root, height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)

        self._running = False

        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)
