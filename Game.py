
from Food import Food
from Snake import Snake
import math


class Game:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.snake = Snake(canvas, root)
        self.food = Food(self.canvas)
        self.head = self.snake.head
        self.score = 0
        self.score_label = self.canvas.create_text(300, 50, text=f"Score: {self.score}", fill="white",
                                                   font=('Helvetica 15 bold'))

        self.root.bind("<Left>", self.head.move_left)
        self.root.bind("<Right>", self.head.move_right)
        self.root.bind("<Up>", self.head.move_up)
        self.root.bind("<Down>", self.head.move_down)

        self.detect_collision_with_wall()
        self.detect_collision_with_food()
        self.detect_collision_with_body()

    def add_point(self):
        self.score += 1

    def update_score(self):
        self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")

    def detect_collision_with_wall(self):
        head_pos = self.head.get_center_coords()
        collision_with_wall = head_pos[0] < 10 or head_pos[0] > 590 or head_pos[1] < 10 or head_pos[1] > 590
        if collision_with_wall:
            self.restart_game()
        self.root.after(20, self.detect_collision_with_wall)

    def detect_collision_with_food(self):
        distance = math.dist(self.head.get_center_coords(), self.food.get_center_coords())
        if distance < 30:
            self.food.change_position()
            self.add_point()
            self.update_score()
            self.snake.add_new_tail_part()
        self.root.after(20, self.detect_collision_with_food)

    def detect_collision_with_body(self):
        for part in self.snake.tail_parts[2:]:
            distance = math.dist(self.head.get_center_coords(), part.get_center_coords())
            if distance < 1:
                self.restart_game()
                break
        self.root.after(20, self.detect_collision_with_body)

    def restart_game(self):
        self.score = 0
        self.update_score()
        self.snake.remove_tail_parts()
        self.head.restart_position()
        self.food.change_position()
