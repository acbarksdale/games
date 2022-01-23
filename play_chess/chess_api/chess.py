from chess_api.board import Board
from chess_api.piece import WHITE, BLACK


class Chess(object):

    def __init__(self):
        self.board = Board()
        self.whos_turn_it_is = WHITE


    def get_board(self):
        return self.board.get_board()

    def make_move(self, initial_square, final_square):

        try:
            self._is_valid_move(initial_square, final_square)
            self.board.move_piece(initial_square, final_square)
            self._change_whos_turn_it_is()

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
        # 3) the piece in the final square must be of the opposite
        #    color or be None
        # 4a) If the piece is not a knight,

        piece_to_move = self.board.get_piece_at_square()
        if piece_to_move is None:
            raise Exception("Please select a square containing a piece.")

        if piece_to_move.get_color() != self.whos_turn_it_is:
            raise Exception("Please select a piece of the color" + str(self.whos_turn_it_is))


