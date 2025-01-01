from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = False
        
        self.root = Tk()
        self.root.title('Main Window')

        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running is True:
            self.redraw()

    def close(self):
        self.running = False