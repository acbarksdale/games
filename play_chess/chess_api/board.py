from chess_api.piece import WHITE, Rook, BLACK, Bishop, Knight, King, Queen, Pawn


class Board(object):

    def __init__(self):
        self.board = self._init_board()

    def _init_board(self):
        board = [[None for i in range(8)] for j in range(8)]

        board[0][0] = Rook(BLACK)
        board[1][0] = Knight(BLACK)
        board[2][0] = Bishop(BLACK)
        board[3][0] = King(BLACK)
        board[4][0] = Queen(BLACK)
        board[5][0] = Bishop(BLACK)
        board[6][0] = Knight(BLACK)
        board[7][0] = Rook(BLACK)

        for i in range(8):
            board[i][1] = Pawn(BLACK)
            board[i][6] = Pawn(WHITE)

        board[0][7] = Rook(WHITE)
        board[1][7] = Knight(WHITE)
        board[2][7] = Bishop(WHITE)
        board[3][7] = King(WHITE)
        board[4][7] = Queen(WHITE)
        board[5][7] = Bishop(WHITE)
        board[6][7] = Knight(WHITE)
        board[7][7] = Rook(WHITE)

        return board


    def move_piece(self, initial_square, final_square):
        """
        initial_square: input as 'A1' for example, human readable
                        coordinates. Square to move piece from
        final_square: square to move piece to
        """
        initial_coords = self._convert_coords_human_to_programmatic(initial_square)
        final_coords = self._convert_coords_human_to_programmatic(final_square)

        #grab the piece from the board
        piece = self.board[initial_coords[0]][initial_coords[1]]
        self.board[initial_coords[0]][initial_coords[1]] = None

        #place the piece on the new square
        self.board[final_coords[0]][initial_coords[1]] = piece


    def _convert_coords_human_to_programmatic(self, human_coords):
        """

        """
        x_coord = ord(human_coords[0]) - ord('A')
        # subtract 1 from y_coord because chess boards 1 indexed
        # while our internal data structure is 0 indexed
        y_coord = human_coords[1] - 1

        return x_coord, y_coord


    def _convert_coords_programmatic_to_human(self, programmatic_coords):

       return chr(programmatic_coords[0] + ord('A')) + str(programmatic_coords[1] + 1)



    def get_board(self):
        return self.board


    def get_piece_at_square(self, square):
        """
        make better docstring...
        this function can handle booth programmatic and human coordinates
        althought the intended use is with human coordinates

        :param square:
        :return:
        """
        try:
            if not type(square) == tuple:
                square = self._convert_coords_human_to_programmatic()

            return self.board[square[0]][square[1]]

        except:
            raise Exception("Please check the input squares are valid and within the board.")
