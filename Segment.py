from abc import ABC


class Segment(ABC):

    def __init__(self):
        self.square = None
        self.size = None
        self.canvas = None

    def get_center_coords(self):
        left_bottom_coords = self.canvas.coords(self.square)
        center_coords = [left_bottom_coords[0] + self.size, left_bottom_coords[1] + self.size]
        return center_coords
