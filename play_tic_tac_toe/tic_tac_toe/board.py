class Board:

    def __init__(self):
        self.board_state = [['_' for i in range(3)] for j in range(3)]

    def get_board_state(self):
        return self.board_state

    def place_piece(self, player_character, x, y):
        self.board_state[x][y] = player_character

    def get_piece(self, x, y):
        return self.board_state[x][y]

    def is_location_empty(self, x, y):
        return self.board_state[x][y] == '_'


