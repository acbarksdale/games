from tic_tac_toe.board import Board


class TicTacToe:

    def __init__(self, player1name, player2name):
        self.player1name = player1name
        self.player2name = player2name

        self.player_char_map = {
            self.player1name: 'x',
            self.player2name: 'o'
        }

        self.board = Board()

        self.whose_turn_is_it = self.player1name

        self.game_over = False

        self.victory_message = None

    def get_board(self):
        return self.board

    def get_whose_turn_is_it(self):
        return self.whose_turn_is_it

    def is_game_over(self):
        return self.game_over

    def switch_turn(self):
        if self.whose_turn_is_it == self.player1name:
            self.whose_turn_is_it = self.player2name
        else:
            self.whose_turn_is_it = self.player1name

    def make_move(self, x, y):
        if x not in [0, 1, 2] or y not in [0, 1, 2]:
            raise Exception('x and y must be one of [0, 1, 2]')

        if not self.board.is_location_empty(x, y):
            raise Exception('put yo piece where there aint another piece')
        #assuming valid move

        player_character = self.player_char_map[self.whose_turn_is_it]
        self.board.place_piece(player_character, x, y)
        if self.check_for_victory(player_character):
            return
        self.switch_turn()


    def check_for_victory(self, player_character):
        #is three in a row of the character found in the board
        victory_condition = player_character + player_character + player_character
        possible_victories = [
            self.board.get_piece(0, 0) + self.board.get_piece(0, 1) + self.board.get_piece(0, 2),
            self.board.get_piece(1, 0) + self.board.get_piece(1, 1) + self.board.get_piece(1, 2),
            self.board.get_piece(2, 0) + self.board.get_piece(2, 1) + self.board.get_piece(2, 2),
            self.board.get_piece(0, 0) + self.board.get_piece(1, 0) + self.board.get_piece(2, 0),
            self.board.get_piece(0, 1) + self.board.get_piece(1, 1) + self.board.get_piece(2, 1),
            self.board.get_piece(0, 2) + self.board.get_piece(1, 2) + self.board.get_piece(2, 2),
            self.board.get_piece(0, 0) + self.board.get_piece(1, 1) + self.board.get_piece(2, 2),
            self.board.get_piece(2, 0) + self.board.get_piece(1, 1) + self.board.get_piece(0, 2)
        ]

        self.game_over = victory_condition in possible_victories

        self.victory_message = "{player_name} beat the shit out of {other_player_name}".format(
            player_name=self.whose_turn_is_it,
            other_player_name=self.player1name if self.whose_turn_is_it == self.player2name else self.player2name
        )

        return self.is_game_over()


    def get_victory_message(self):
        return self.victory_message







