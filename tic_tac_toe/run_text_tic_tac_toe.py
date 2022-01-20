from tic_tac_toe.tic_tac_toe import TicTacToe

class TextTicTacToePlayer:

    def __init__(self):
        self.tic_tac_toe = TicTacToe('stephen', 'alex')

    def display_board(self):
        board = self.tic_tac_toe.get_board()
        board_state = board.get_board_state()
        for y in range(3):
            for x in range(3):
                print(board_state[x][y], end='')
                if x < 2:
                    print(' ', end='')
            print()

    def play_game(self):
        print()
        # while the game isnt terminal
        while not self.tic_tac_toe.is_game_over():
            #get desired location to put piece
            self.display_board()
            move_location = input("now its {whose_turn_is_it}'s turn, please type input in format x,y".format(whose_turn_is_it=self.tic_tac_toe.get_whose_turn_is_it().capitalize()))

            try:
                x, y = self.parse_move_location(move_location)
            except Exception as e:
                print("you done fucked up the input")
                continue

            try:
                self.tic_tac_toe.make_move(x, y)
            except Exception as e:
                print(str(e))
                continue

            #execute move
        # display game over message
        print(self.tic_tac_toe.get_victory_message())

    def parse_move_location(self, move_location):
        return int(move_location.split(',')[0]), int(move_location.split(',')[1])


if __name__ == '__main__':
    TextTicTacToePlayer().play_game()
