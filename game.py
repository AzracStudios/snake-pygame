from snake import Snake
from apple import Apple


class Game:

    def __init__(self, n, r):
        self.score = 0
        self.board_res = n
        self.max = r

        self.snake = Snake(r)
        self.apple = Apple(r)

        self.game_over = False

    def reset(self):
        self.score = 0

        self.snake = Snake(self.max)
        self.apple = Apple(self.max)

        self.game_over = False

    def make_apple(self, pos):
        self.grid[pos[0]][pos[1]] = "apple"

    def make_snake_head(self, pos):
        self.grid[pos[0]][pos[1]] = "snake_head"

    def make_snake_body(self, pos):
        self.grid[pos[0]][pos[1]] = "snake_body"

    def next(self, direction):
        self.snake.move(direction)

        if self.apple.was_eaten(
            (self.snake.head.x, self.snake.head.y)):

            self.snake.grow()
            self.apple.randomize_position()

            self.score += 1

        if self.snake.hit_wall():
            self.game_over = True

        return self.game_over
