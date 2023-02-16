import random as r


class Apple:

    def __init__(self, m):
        self.x = m // 2
        self.y = m // 2 - int (0.3 * m)
        self.max = m

    def randomize_position(self):
        x = r.randrange(0, self.max - 1)
        y = r.randrange(0, self.max - 1)

        if x == self.x: x = min(x + 1, self.max - 1)
        if y == self.y: y = min(y + 1, self.max - 1)

        self.x = x
        self.y = y

    def was_eaten(self, snake_position):
        if (self.x, self.y) == snake_position:
            return True
        return False
