from chess_api.piece import WHITE, Rook, BLACK, Bishop, Knight, King, Queen, Pawn

BOARD_SIZE = 8

class Board(object):

    def __init__(self):
        self.board_array = self._init_board_array()

    def _init_board_array(self):
        board_array = [[None for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

        board_array[0][0] = Rook(BLACK, self)
        board_array[1][0] = Knight(BLACK, self)
        board_array[2][0] = Bishop(BLACK, self)
        board_array[4][0] = King(BLACK, self)
        board_array[3][0] = Queen(BLACK, self)
        board_array[5][0] = Bishop(BLACK, self)
        board_array[6][0] = Knight(BLACK, self)
        board_array[7][0] = Rook(BLACK, self)

        for i in range(BOARD_SIZE):
            board_array[i][1] = Pawn(BLACK, self)
            board_array[i][6] = Pawn(WHITE, self)

        board_array[0][7] = Rook(WHITE, self)
        board_array[1][7] = Knight(WHITE, self)
        board_array[2][7] = Bishop(WHITE, self)
        board_array[4][7] = King(WHITE, self)
        board_array[3][7] = Queen(WHITE, self)
        board_array[5][7] = Bishop(WHITE, self)
        board_array[6][7] = Knight(WHITE, self)
        board_array[7][7] = Rook(WHITE, self)

        return board_array


    def move_piece(self, initial_square, final_square):
        """

        """

        #grab the piece from the board
        piece = self.board_array[initial_square[0]][initial_square[1]]
        self.board_array[initial_square[0]][initial_square[1]] = None

        #place the piece on the new square
        self.board_array[final_square[0]][final_square[1]] = piece


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

