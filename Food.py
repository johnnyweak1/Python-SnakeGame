from random import randint


class Food:

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = randint(10, 590)
        self.y = randint(10, 590)
        self.radius = 5
        self.circle = self.canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius,
                                              self.y + self.radius, fill='red')

    def change_position(self):
        self.x = randint(10, 590)
        self.y = randint(10, 590)
        self.canvas.coords(self.circle, self.x - self.radius, self.y - self.radius, self.x + self.radius,
                           self.y + self.radius)

    def get_center_coords(self):
        return [self.x, self.y]
