from chess_api.board import Board
from chess_api.piece import WHITE, BLACK
from chess_api.piece import PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING


class NonePieceException(Exception):
    #Selected square is a NoneType instead of a Piece
    pass

class WrongColorPieceException(Exception):
    #Selected piece is a wrong color
    pass

class InvalidMoveForPieceException(Exception):
    pass

valid_base_moves = {
    WHITE: {
        PAWN: [[0,1], [0,2], [-1, 1], [1, 1]],
        KNIGHT: [[i, j] for i in [1,-1,2,-2] for j in [1, -1, 2, -2]
                 if abs(i) != abs(j)],
        BISHOP: [[m*i, m*j] for i, j in [(1,1), (1,-1), (-1,1), (-1,1)] for m in range(1,8)],
        ROOK: [[m*i, m*j] for i, j in [(1,0), (-1,0), (0,1), (0,-1)] for m in range(1,8)],
        QUEEN: [[m * i, m * j] for i, j in [(1, 1), (1, -1), (-1, 1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)] for min range(1, 8)]
        KING: [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]
    },
    BLACK: {
        PAWN: [[0,1], [0,2], [-1, 1], [1, 1]],
        KNIGHT: [[i, j] for i in [1,-1,2,-2] for j in [1, -1, 2, -2]
                 if abs(i) != abs(j)],
        BISHOP: [[m*i, m*j] for i, j in [(1,1), (1,-1), (-1,1), (-1,1)] for m in range(1,8)],
        ROOK: [[m*i, m*j] for i, j in [(1,0), (-1,0), (0,1), (0,-1)] for m in range(1,8)],
        QUEEN: [[m * i, m * j] for i, j in [(1, 1), (1, -1), (-1, 1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)] for min range(1, 8)]
        KING: [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1] if i != 0 or j != 0]
    }
}




class Chess(object):

    def __init__(self):
        self.board = Board()
        self.whose_turn_it_is = WHITE


    def get_board(self):
        return self.board.get_board()

    def make_move(self, initial_square, final_square):

        try:
            self._is_valid_move(initial_square, final_square)
            self.board.move_piece(initial_square, final_square)
            self._change_whose_turn_it_is()

        except Exception as e:
            print(str(e))


    def _is_valid_move(self, initial_square, final_square):
        """

        :param initial_square:
        :param final_square:
        :return:
        """
        # to be a valid move, we have to meet the following criteria:
        # 1) the initial square must be a piece
        # 2) the piece must be the proper move color
        # 4) check that the final square is within the valid piece moves
        #    from the initial square
        # 3) if not a pawn:
        #    the piece in the final square must be of the opposite
        #    color or be None (or it is a piece and the same color as the
        #    the current move
        #    if a pawn:
                a. if moving 2, the pawn must not have moved already
                b. if x displacement = 0, must not have a piece there
                c. if x != 0, must have oppostive color piece there

        # 5) check that there are no pieces obstructing the path from
        #    initial square to the final square (unless it is a knight)
        # 6) the move must not place your own king in danger
        # 7) or the piece belongs to a special class of moves
        #   a. King Side Castling
        #   b. Queen Side Castling
        #   c. En-passant - keep track of how many times the pawn has moved since last move

        piece_to_move = self.board.get_piece_at_square(initial_square)
        #Condition 1)
        if piece_to_move is None:
            raise NonePieceException()

        #Condition 2)
        if piece_to_move.get_color() != self.whose_turn_it_is:
            raise WrongColorPieceException()

        move_displacement_vector = [ord(final_square[0]) - ord(initial_square[0]),
                                    ord(final_square[1]) - ord(initial_square[1])]

        if not move_displacement_vector in valid_base_moves[self.whose_turn_it_is][piece_to_move.get_type()]:
            raise InvalidMoveForPieceException()
        #Condition 3)
        piece_to_take = self.board.get_piece_at_square(final_square)
        if not piece_to_take is None and piece_to_take.get_color() == self.whose_turn_it_is:
            raise WrongColorPieceException()



    def _change_whose_turn_it_is(self):
        self.whose_turn_it_is = WHITE if self.whose_turn_it_is == BLACK else WHITE