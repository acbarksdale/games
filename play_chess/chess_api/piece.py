
WHITE = 'white'
BLACK = 'black'

PAWN = 'pawn'
KNIGHT = 'knight'
BISHOP = 'bishop'
ROOK = 'rook'
QUEEN = 'queen'
KING = 'king'


class Piece(object):

    def __init__(self, color, board):
        self.color = color
        self.type = None
        self.valid_moves = None
        self.board = board

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color

    def get_valid_target_coordinates(self, src_coordinates):
        """
        :return: list of tuples
        """
        board_size = len(self.board.get_board_array())
        possible_move_displacements = self.valid_moves
        x_coord, y_coord = src_coordinates[0], src_coordinates[1]
        possible_moves = [(x_coord + delta_x, y_coord + delta_y) for delta_x, delta_y in possible_move_displacements]
        return [move for move in possible_moves if move[0] in range(board_size) and move[1] in range(board_size)]


class Pawn(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)
        self.type = PAWN
        self.valid_moves = [[0,-1], [0,-2], [-1, -1], [1, -1]] if self.color == WHITE else [[0,1], [0,2], [-1, 1], [1, 1]]

class Knight(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)
        self.type = KNIGHT
        self.valid_moves = [[i, j] for i in [1,-1,2,-2] for j in [1, -1, 2, -2] if abs(i) != abs(j)]

class Bishop(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)
        self.type = BISHOP
        self.valid_moves = [[m*i, m*j] for i, j in [(1,1), (1,-1), (-1,1), (-1,-1)] for m in range(1,8)]

class Rook(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)
        self.type = ROOK
        self.valid_moves = [[m*i, m*j] for i, j in [(1,0), (-1,0), (0,1), (0,-1)] for m in range(1,8)]

class Queen(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)
        self.type = QUEEN
        self.valid_moves = [[m * i, m * j] for i, j in [(1,1), (1,-1), (-1,1), (-1,-1), (1, 0), (-1, 0), (0, 1), (0, -1)] for m in range(1, 8)]

class King(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)
        self.type = KING
        self.valid_moves = [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0] + [[-2, 0], [2,0]]


