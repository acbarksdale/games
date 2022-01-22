from chess.chess import Chess

FULL_CHAR = chr(int('02588', 16))
LIGHT_CHAR = chr(int('02591', 16))
MEDIUM_CHAR = chr(int('02592', 16))
DARK_CHAR = chr(int('02593', 16))


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
        self.print_board()

    def print_board(self):
        board = self.chess.get_board()
        y = 0
        for i in range(0, 4):
            for j in range(0, 3):
                if j == 1:
                    x=0
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else DARK_CHAR }{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    x+=1
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else LIGHT_CHAR }{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}',
                          end='')
                    x+=1
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else DARK_CHAR }{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    x+=1
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else LIGHT_CHAR }{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}',
                          end='')
                    x+=1
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else DARK_CHAR }{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    x+=1
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else LIGHT_CHAR }{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}',
                          end='')
                    x+=1
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else DARK_CHAR }{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    x+=1
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else LIGHT_CHAR }{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}')
                else:
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}',
                          end='')
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}',
                          end='')
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}',
                          end='')
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}')
            y += 1
            for k in range(0, 3):
                if k == 1:
                    x=0
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else LIGHT_CHAR }{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}', end='')
                    x+=1
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else DARK_CHAR }{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    x+=1
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else LIGHT_CHAR }{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}', end='')
                    x+=1
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else DARK_CHAR }{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    x+=1
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else LIGHT_CHAR }{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}', end='')
                    x+=1
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else DARK_CHAR }{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    x+=1
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else LIGHT_CHAR }{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}', end='')
                    x+=1
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{PIECE_TYPE_TO_CHAR_MAP[board[x][y].get_type()][board[x][y].get_color()] if board[x][y] else DARK_CHAR }{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}')
                else:
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}', end='')
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}', end='')
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}', end='')
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}', end='')
                    print(f'{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}{LIGHT_CHAR}', end='')
                    print(f'{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}{DARK_CHAR}')
            y += 1


if __name__ == '__main__':
    RunTextChess().run()

