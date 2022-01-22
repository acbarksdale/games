from connect_four.board import Board


class ConnectFour:

    def __init__(self, player_1_name, player_2_name):
        self.board = Board()
        self.game_over = False
        self.game_over_message = None
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name

        self.which_players_turn = 'player_1'

        self.player_pieces = {
            'player_1': 'r',
            'player_2': 'b'
        }

        self.move_count = 0

    def is_game_over(self):
        return self.game_over

    def get_game_over_message(self):
        return self.game_over_message

    def make_move(self, column_index):
        """

        """
        if not self.make_move_exception_handling(column_index):
            return

        self.game_over = self.check_for_game_over()
        self.switch_player_turn()

    def make_move_exception_handling(self, column_index):
        try:
            self.board.drop_piece(column_index, self.player_pieces[self.which_players_turn])
            return True

        except Exception as e:
            print(str(e))
            return False

        return True

    def check_for_game_over(self):
        # using brute force approach: check for all horizontal, vertical, diagonal cases
        connect_four = [self.player_pieces[self.which_players_turn]] * 4
        curr_board = self.board.get_board_state()

        for i in range(self.board.num_rows):
            for j in range(self.board.num_cols):
                # right horizontal condition
                if j + 4 <= self.board.num_cols:
                    horizontal_four_to_check = curr_board[i][j:j + 4]
                    if horizontal_four_to_check == connect_four:
                        self.update_game_over_message()
                        return True

                # upwards vertical condition
                if i + 4 <= self.board.num_rows:
                    vertical_four_to_check = [curr_board[i + k][j] for k in range(4)]
                    if vertical_four_to_check == connect_four:
                        self.update_game_over_message()
                        return True

                # upper right diagonal condition
                if j + 4 <= self.board.num_cols and i + 4 <= self.board.num_rows:
                    ur_diagonal_four_to_check = [curr_board[i + k][j + k] for k in range(4)]
                    if ur_diagonal_four_to_check == connect_four:
                        self.update_game_over_message()
                        return True

                # upper_left_diagonal_condition
                if j - 4 >= 0 and i + 4 <= self.board.num_rows:
                    ul_diagonal_four_to_check = [curr_board[i + k][j - k] for k in range(4)]
                    if ul_diagonal_four_to_check == connect_four:
                        self.update_game_over_message()
                        return True

        return False

    def update_game_over_message(self):
        self.game_over_message = '{player_name} wins!'.format(player_name=self.player_1_name if self.which_players_turn == 'player_1'
                                                              else self.player_2_name)

    def switch_player_turn(self):

        self.which_players_turn = 'player_1' if self.which_players_turn == 'player_2' else 'player_2'

