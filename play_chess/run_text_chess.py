from math import floor

from chess_api.chess import Chess

FULL_CHAR = chr(int('02588', 16))
LIGHT_CHAR = chr(int('02591', 16))
MEDIUM_CHAR = chr(int('02592', 16))
DARK_CHAR = chr(int('02593', 16))

SQUARE_WIDTH = 7
SQUARE_HEIGHT = 3


PIECE_TYPE_TO_CHAR_MAP = {
    'rook': {
        'white': 'R',
        'black': 'r'
    },
    'pawn': {
        'white': 'P',
        'black': 'p'
    },
    'knight': {
        'white': 'N',
        'black': 'n'
    },
    'bishop': {
        'white': 'B',
        'black': 'b'
    },
    'queen': {
        'white': 'Q',
        'black': 'q'
    },
    'king': {
        'white': 'K',
        'black': 'k'
    },

}


class RunTextChess(object):

    def __init__(self):
        pass
        self.chess = Chess()

    def run(self):
        
        while True:
            self.print_board()
            # selected_coordinates = input('print some coordinates!')
            # x = selected_coordinates[0]
            # y = selected_coordinates[1]
            # valid_moves = self.chess.get_valid_moves(self._convert_coords_human_to_programmatic((x, y)))
            # self.print_board(valid_moves=valid_moves)
            print("Welcome to chess. Follow the prompts, or enter Q to quit")
            print(self.chess.get_whose_turn_it_is().upper() + "'s turn!")
            source_coords = input('Enter source coordinates (Ex. E2): ')
            if source_coords == 'Q': 
                break
            target_coords = input('Enter target square (Ex. E2): ')
            if target_coords == 'Q':
                break

            self.chess.make_move(self._convert_coords_human_to_programmatic(source_coords),
                                 self._convert_coords_human_to_programmatic(target_coords))
                                  



    def _convert_coords_human_to_programmatic(self, human_coords):
        """

        """
        x_coord = ord(human_coords[0]) - ord('A')
        # subtract 1 from y_coord because chess boards 1 indexed
        # while our internal data structure is 0 indexed
        y_coord = 8 - int(human_coords[1])
        print(x_coord)
        print(y_coord)
        return x_coord, y_coord

    def print_board(self, valid_moves=None):

        if valid_moves == None:
            valid_moves = []
        print('  ' + '-' * (SQUARE_WIDTH * 8 + 24))

        for y in range(0, 8):
            for sub_y in range(0, SQUARE_HEIGHT):
                if sub_y == floor(SQUARE_HEIGHT / 2):
                    print(f'{8 - y} ', end='')
                else:
                    print('  ', end='')

                for x in range(0, 8):
                    print(' | ', end='')
                    for sub_x in range(0, SQUARE_WIDTH):
                        piece = self.chess.get_board_array()[x][y]
                        if sub_x == floor(SQUARE_WIDTH / 2) and sub_y == floor(SQUARE_HEIGHT / 2) and piece is not None:
                            print(PIECE_TYPE_TO_CHAR_MAP[piece.get_type()][piece.get_color()], end='')
                        else:
                            if (x + y) % 2 == 1:
                                perimeter_char = LIGHT_CHAR
                            else:
                                perimeter_char = DARK_CHAR

                            if (x, y) in valid_moves:
                                perimeter_char = ' '

                            print(perimeter_char, end='')
                        
                print(' | ', end='')    
                print('')
            print('  ' + '-' * (SQUARE_WIDTH * 8 + 24))
        x_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        print(' ' * floor(SQUARE_WIDTH / 2), end='  ')
        for i in range(0, 8):
            print('   ' + x_letters[i], end=' ' * (SQUARE_WIDTH - 1))
        print('')


if __name__ == '__main__':
    RunTextChess().run()

