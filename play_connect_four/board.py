class Board:

    def __init__(self, num_rows=8, num_cols=8):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board_state = [['_' for i in range(num_cols)] for j in range(num_rows)]


    def drop_piece(self, column_index, piece_char):
        """
        Drops a piece
        :param column_index:
        :return:
        """
        if column_index >= self.num_cols or column_index < 0:
            raise Exception('Column index must be between 0 and {num_cols}'.format(num_cols=self.num_cols-1))

        num_pieces_in_column = self.count_num_pieces_in_column(column_index)
        if num_pieces_in_column == self.num_rows:
            raise Exception('This column is full')

        self.board_state[num_pieces_in_column][column_index] = piece_char

    def count_num_pieces_in_column(self, column_index):

        column = [self.board_state[row_index][column_index] for row_index in range(self.num_rows)]
        return sum([not piece == '_' for piece in column])

    def is_column_full(self, column_index):

        return self.count_num_pieces_in_column(column_index) == self.num_rows

    def get_board_state(self):
        return self.board_state
