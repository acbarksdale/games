WHITE = 'white'
BLACK = 'black'

PAWN = 'pawn'
KNIGHT = 'knight'
BISHOP = 'bishop'
ROOK = 'rook'
QUEEN = 'queen'
KING = 'king'


valid_base_moves = {
    WHITE: {
        PAWN: [[0,1], [0,2], [-1, 1], [1, 1]],
        KNIGHT: [[i, j] for i in [1,-1,2,-2] for j in [1, -1, 2, -2]
                 if abs(i) != abs(j)],
        BISHOP: [[m*i, m*j] for i, j in [(1,1), (1,-1), (-1,1), (-1,1)] for m in range(1,8)],
        ROOK: [[m*i, m*j] for i, j in [(1,0), (-1,0), (0,1), (0,-1)] for m in range(1,8)],
        QUEEN: [[m * i, m * j] for i, j in [(1, 1), (1, -1), (-1, 1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)] for m in range(1, 8)],
        KING: [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]
    },

    BLACK: {
        PAWN: [[0,1], [0,2], [-1, 1], [1, 1]],
        KNIGHT: [[i, j] for i in [1,-1,2,-2] for j in [1, -1, 2, -2]
                 if abs(i) != abs(j)],
        BISHOP: [[m*i, m*j] for i, j in [(1,1), (1,-1), (-1,1), (-1,1)] for m in range(1,8)],
        ROOK: [[m*i, m*j] for i, j in [(1,0), (-1,0), (0,1), (0,-1)] for m in range(1,8)],
        QUEEN: [[m * i, m * j] for i, j in [(1, 1), (1, -1), (-1, 1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)] for m in range(1, 8)],
        KING: [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]
    }
}

class Piece(object):

    def __init__(self, color):
        self.color = color
        self.type = None

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def get_valid_target_coordinates(self, src_coordinates):
        """
        :return: list of tuples
        """
        raise Exception('this method must be implemented by each subclass of Piece')


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = PAWN

    def get_valid_target_coordinates(self, src_coordinates):
        return [(4, 4), (6, 6)]  # TODO implement this


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = KNIGHT

    def get_valid_target_coordinates(self, src_coordinates):
        """
        :param src_coordinates:
        :return:
        """

        return [(1,1)]




class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = BISHOP

    def get_valid_target_coordinates(self, src_coordinates):
        return []  # TODO implement this


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = ROOK

    def get_valid_target_coordinates(self, src_coordinates):
        return []  # TODO implement this


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = QUEEN

    def get_valid_target_coordinates(self, src_coordinates):
        return []  # TODO implement this


class King(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.type = KING

    def get_valid_target_coordinates(self, src_coordinates):
        return []  # TODO implement this

