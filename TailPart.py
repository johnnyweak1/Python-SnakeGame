from Segment import Segment


class TailPart(Segment):
    def __init__(self, canvas, position_x, position_y):
        super().__init__()
        self.canvas = canvas
        self.size = 20
        self.square = self.canvas.create_rectangle(position_x, position_y, position_x + self.size,
                                                   position_y + self.size, outline="white", fill="white", width=2)

    def move(self, positions):
        self.canvas.moveto(self.square, positions[0] - 1, positions[1] - 1)
