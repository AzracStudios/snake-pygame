from piece import Piece


class Snake:

    def __init__(self, m):
        self.head = Piece(True, m // 2, m // 2 + int(0.3 * m), None)
        self.max = m

        self.direction = 0
        self.delta_x = 0
        self.delta_y = 0

        self.snake_length = 1

    def move(self, direction):
        _dir = self.direction

        if direction == 0 and _dir != 2:
            self.delta_y = -1
            self.delta_x = 0

        elif direction == 1 and _dir != 3:
            self.delta_x = -1
            self.delta_y = 0

        elif direction == 2 and _dir != 0:
            self.delta_y = 1
            self.delta_x = 0

        elif direction == 3 and _dir != 1:
            self.delta_x = 1
            self.delta_y = 0

        if not ((_dir == 3 and direction == 1) or
                (_dir == 1 and direction == 3) or
                (_dir == 0 and direction == 2) or
                (_dir == 2 and direction == 0)):

            self.direction = direction

        self.head.update_y(self.head.y + self.delta_y)
        self.head.update_x(self.head.x + self.delta_x)

        self.head.propogate_position()

    def grow(self):
        delta_x = 0
        delta_y = 0

        if self.direction == 0:
            delta_y = -1
            delta_x = 0

        elif self.direction == 1:
            delta_x = -1
            delta_y = 0

        elif self.direction == 2:
            delta_y = 1
            delta_x = 0

        elif self.direction == 3:
            delta_x = 1
            delta_y = 0

        ## INSERT NEW PIECE TO THE END OF THE ARRAY

        new_piece = Piece(False, self.head.x - delta_x, self.head.y - delta_y,
                          None)

        last_piece = self.head

        while last_piece.next_piece:
            last_piece = last_piece.next_piece

        last_piece.next_piece = new_piece

    def hit_wall(self):
        if self.head.x < 0 or self.head.x > self.max - 1 or self.head.y < 0 or self.head.y > self.max - 1:
            return True

        return False

    def hit_self(self, other):
        if self.head.x == other.x and self.head.y == other.y:
            return True

        return False
