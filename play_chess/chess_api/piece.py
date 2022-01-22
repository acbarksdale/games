WHITE = 'white'
BLACK = 'black'

PAWN = 'pawn'
KNIGHT = 'knight'
BISHOP = 'bishop'
ROOK = 'rook'
QUEEN = 'queen'
KING = 'king'


class Piece(object):

    def __init__(self, color):
        self.color = color
        self.type = None


    def get_type(self):
        return self.type

    def get_color(self):
        return self.color


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = PAWN


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = KNIGHT


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = BISHOP


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = ROOK


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = QUEEN


class King(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = KING

