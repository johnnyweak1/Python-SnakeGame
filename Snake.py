from Head import Head
from TailPart import TailPart


class Snake:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.head = Head(canvas, root)
        self.tail_parts = []

        self.move_tail_parts()

    def add_new_tail_part(self):
        only_head_exists = len(self.tail_parts) == 0
        if only_head_exists:
            prev_tail_part = self.head.square
        else:
            prev_tail_part = self.tail_parts[len(self.tail_parts) - 1].square

        prev_tail_part_position = self.canvas.coords(prev_tail_part)
        self.tail_parts.append(TailPart(self.canvas, prev_tail_part_position[0], prev_tail_part_position[1]))

    def move_tail_parts(self):

        for i in range(len(self.tail_parts) - 1, -1, -1):
            if i == 0:
                prev_tail_part = self.head.square
            else:
                prev_tail_part = self.tail_parts[i - 1].square

            prev_tail_part_position = self.canvas.coords(prev_tail_part)
            self.tail_parts[i].move(prev_tail_part_position)
        self.root.after(80, self.move_tail_parts)

    def remove_tail_parts(self):
        for part in self.tail_parts:
            self.canvas.delete(part.square)
        self.tail_parts.clear()
