
class Piece:

    def __init__(self, is_head, x, y, next_piece):
        self.type = "head" if is_head else "body"

        self.x = x
        self.y = y

        self.prev_x = x
        self.prev_y = y

        self.direction = 0

        self.next_piece = next_piece

    def get_pos(self):
        return (self.x, self.y)

    def get_type(self):
        return self.type

    def update_x(self, x):
        self.prev_x = self.x
        self.x = x

    def update_y(self, y):
        self.prev_y = self.y
        self.y = y

    def propogate_position(self):
        if self.next_piece:
            self.next_piece.update_x(self.prev_x)
            self.next_piece.update_y(self.prev_y)
            self.next_piece.propogate_position()

    def __repr__(self):
        return str(self.get_pos()) + "  " + str(self.next_piece)