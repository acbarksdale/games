from connect_four.play_connect_four import ConnectFour


class ConnectFourPlayer:

    def __init__(self, player_1_name, player_2_name):
        self.connect_four = ConnectFour(player_1_name, player_2_name)

    def play_game(self):

        while not self.connect_four.is_game_over():
            self.display_game_state()
            try:
                move_column = self.get_user_move_input()
            except:
                print('Please enter an integer value only.')
                continue

            self.connect_four.make_move(move_column)

        #display game over message and final board state
        self.display_game_state()
        print(self.connect_four.get_game_over_message())

    def display_game_state(self):
        print(['{i}'.format(i=val) for val in range(self.connect_four.board.num_cols)])
        for row in self.connect_four.board.get_board_state()[::-1]:
            print(row)

    def get_user_move_input(self):
        return int(input("Please enter a column as an integer: "))


if __name__ == '__main__':
    player_1_name = input("Enter player 1's name: ")
    player_2_name = input("Enter player 2's name: ")
    ConnectFourPlayer(player_1_name, player_2_name).play_game()
