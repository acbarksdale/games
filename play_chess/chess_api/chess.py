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






class Chess(object):

    def __init__(self):
        self.board = Board()
        self.whose_turn_it_is = WHITE

    def get_board(self):
        return self.board

    def get_board_array(self):
        return self.get_board().get_board_array()

    def get_valid_moves(self, src_coordinates):
        return self.board.get_piece_at_coordinates(src_coordinates).get_valid_target_coordinates(src_coordinates)

    def make_move(self, initial_square, final_square):

        try:
            self._is_valid_input(initial_square, final_square)
            self._is_valid_move(initial_square, final_square)
            self.board.move_piece(initial_square, final_square)
            self._change_whose_turn_it_is()

        except Exception as e:
            print(str(e))


    def _convert_coords_programmatic_to_human(self, programmatic_coords):
       return chr(programmatic_coords[0] + ord('A')) + str(programmatic_coords[1] + 1)


    def _convert_coords_human_to_programmatic(self, human_coords):
        """

        """
        x_coord = ord(human_coords[0]) - ord('A')
        # subtract 1 from y_coord because chess boards 1 indexed
        # while our internal data structure is 0 indexed
        y_coord = int(human_coords[1]) - 1

        return x_coord, y_coord


    def _is_valid_input(self, initial_square, final_square):
        if not self._are_coordinates_between_0_an_7(initial_square, final_square):
            return False
        return True

    def _are_coordinates_between_0_an_7(self, initial_square, final_square):
        """
        TODO: IMPLEMENT

        :param final_square:
        :return:
        """
        return True

    def _is_valid_move(self, initial_square, final_square):
        """

        :param initial_square:
        :param final_square:
        :return:
        """
        # to be a valid move, we have to meet the following criteria:
        # 1) the initial square must be a piece
        # 2) the piece must be the proper move color
        # 3) check that the final square is within the valid piece moves
        #    from the initial square
        # 4) if not a pawn:
        #    the piece in the final square must be of the opposite
        #    color or be None (or it is a piece and the same color as the
        #    the current move
        #    if a pawn:
        #       a. if moving 2, the pawn must not have moved already
        #       b. if x displacement = 0, must not have a piece there
        #      c. if x != 0, must have oppostive color piece there

        # 5) check that there are no pieces obstructing the path from
        #    initial square to the final square (unless it is a knight)
        # 6) the move must not place your own king in danger
        # 7) or the piece belongs to a special class of moves
        #   a. King Side Castling
        #   b. Queen Side Castling
        #   c. En-passant - keep track of how many times the pawn has moved since last move

        piece_to_move = self.board.get_piece_at_coordinates(initial_square)
        #Condition 1)
        if piece_to_move is None:
            raise NonePieceException()
        print("Passed none piece")
        #Condition 2)
        if piece_to_move.get_color() != self.whose_turn_it_is:
            raise WrongColorPieceException()
        print("Passed correct color")
        if not final_square in piece_to_move.get_valid_target_coordinates(initial_square):
            raise InvalidMoveForPieceException()
        print("Passed in valid moves")
        #Condition 4)
        piece_to_take = self.board.get_piece_at_coordinates(final_square)
        if not piece_to_take is None and piece_to_take.get_color() == self.whose_turn_it_is:
            raise WrongColorPieceException()
        print("target is correct color")


    def _change_whose_turn_it_is(self):
        self.whose_turn_it_is = WHITE if self.whose_turn_it_is == BLACK else BLACK

    def get_whose_turn_it_is(self):
        return self.whose_turn_it_is