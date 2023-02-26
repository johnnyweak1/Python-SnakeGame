from Segment import Segment


class Head(Segment):

    def __init__(self, canvas, root):
        super().__init__()
        self.canvas = canvas
        self.root = root
        self.size = 20
        self.square = self.canvas.create_rectangle(280, 280, 280 + 20, 280 + 20, outline="white", fill="white", width=2)
        self.x = 20
        self.y = 0
        self.move()

    def move_left(self, event):
        if self.x != 20:
            self.x = -20
            self.y = 0

    def move_right(self, event):
        if self.x != -20:
            self.x = 20
            self.y = 0

    def move_up(self, event):
        if self.y != 20:
            self.x = 0
            self.y = -20

    def move_down(self, event):
        if self.y != -20:
            self.x = 0
            self.y = 20

    def move(self):
        self.canvas.move(self.square, self.x, self.y)
        self.root.after(80, self.move)

    def restart_position(self):
        self.canvas.coords(self.square, 280, 280, 280 + self.size, 280 + self.size)
        self.x = 20
        self.y = 0
