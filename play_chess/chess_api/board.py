from chess_api.piece import WHITE, Rook, BLACK, Bishop, Knight, King, Queen, Pawn


class Board(object):

    def __init__(self):
        self.board_array = self._init_board_array()

    def _init_board_array(self):
        board_array = [[None for i in range(8)] for j in range(8)]

        board_array[0][0] = Rook(BLACK)
        board_array[1][0] = Knight(BLACK)
        board_array[2][0] = Bishop(BLACK)
        board_array[3][0] = King(BLACK)
        board_array[4][0] = Queen(BLACK)
        board_array[5][0] = Bishop(BLACK)
        board_array[6][0] = Knight(BLACK)
        board_array[7][0] = Rook(BLACK)

        for i in range(8):
            board_array[i][1] = Pawn(BLACK)
            board_array[i][6] = Pawn(WHITE)

        board_array[0][7] = Rook(WHITE)
        board_array[1][7] = Knight(WHITE)
        board_array[2][7] = Bishop(WHITE)
        board_array[3][7] = King(WHITE)
        board_array[4][7] = Queen(WHITE)
        board_array[5][7] = Bishop(WHITE)
        board_array[6][7] = Knight(WHITE)
        board_array[7][7] = Rook(WHITE)

        return board_array


    def move_piece(self, initial_square, final_square):
        """

        """

        #grab the piece from the board
        piece = self.board_array[initial_square[0]][initial_square[1]] = piece
        self.board_array[initial_square[0]][initial_square[1]] = None

        #place the piece on the new square
        self.board_array[final_square[0]][final_square[1]] = piece

    def get_valid_moves_for_selected_coordinate(self, coordinate):

        piece = self.board_array[coordinate[0]][coordinate[1]]
        if piece is None:
            raise Exception("The piece selected is NoneType.")

        possible_moves = piece.get_valid_target_coordinates()
        moves_within_board = [move for move in possible_moves if move[0] in range(8) and move[1] in range(8)]

        return moves_within_board


    def get_board_array(self):
        return self.board_array


    def get_piece_at_coordinates(self, coordinates):
        """
        make better docstring...
        this function can handle both programmatic and human coordinates
        althought the intended use is with human coordinates

        :param square:
        :return:
        """
        return self.board_array[coordinates[0]][coordinates[1]]


    def set_piece_at_coordinates(self, piece, coordinates):
        """

        :param coordinates:
        :return:
        """
        self.board_array[coordinates[0]][coordinates[1]] = piece

