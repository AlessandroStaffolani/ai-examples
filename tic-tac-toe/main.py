from games import *
import time

WINNING = [
    [(1, 1), (1, 2), (1, 3)],
    [(2, 1), (2, 2), (2, 3)],
    [(3, 1), (3, 2), (3, 3)],
    [(1, 1), (2, 1), (3, 1)],
    [(1, 2), (2, 2), (3, 2)],
    [(1, 3), (2, 3), (3, 3)],
    [(1, 1), (2, 2), (3, 3)],
    [(1, 3), (2, 2), (3, 1)],
]

ticTacToe = TicTacToe()

x_pos = []
o_pos = []


def gen_state(to_move='X', x_positions=[], o_positions=[], h=3, v=3, k=3):
    """Given whose turn it is to move, the positions of X's on the board, the
    positions of O's on the board, and, (optionally) number of rows, columns
    and how many consecutive X's or O's required to win, return the corresponding
    game state"""

    moves = set([(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]) \
        - set(x_positions) - set(o_positions)
    moves = list(moves)
    board = {}
    for pos in x_positions:
        board[pos] = 'X'
    for pos in o_positions:
        board[pos] = 'O'

    return GameState(to_move=to_move, utility=0, board=board, moves=moves)


def gen_move(difficulty, state, game):
    if difficulty == 'r':
        a, b = random_player(game, state)
    elif difficulty == 'p':
        a, b = minimax_decision(state, game)
    else:
        a, b = alphabeta_player(game, state)

    return tuple((a, b))


def check_win(position):
    for win_positions in WINNING:
        win_count = 0
        for win_cell in win_positions:
            if win_cell in position:
                win_count += 1
        if win_count == 3:
            return True

    return False


ticTacToe.display(ticTacToe.initial)

x_diff = input("Write X player ability [r = random, p = pro, l = legend]\n")
o_diff = input("Write O player ability [r = random, p = pro, l = legend]\n")

current_state = ticTacToe.initial
turn = 'X'
round = 0
while not ticTacToe.terminal_test(current_state) and not check_win(x_pos) and not check_win(o_pos):
    round += 1
    if turn == 'X':
        x_pos.append(gen_move(x_diff, current_state, ticTacToe))
        turn = 'O'
    else:
        o_pos.append(gen_move(o_diff, current_state, ticTacToe))
        turn = 'X'

    current_state = gen_state(to_move=turn, x_positions=x_pos, o_positions=o_pos)
    ticTacToe.display(current_state)
    print('\n----- Round ' + str(round) + ' ----\n')
    time.sleep(2)  # 2 secondi

    
#
# state = gen_state(to_move='X', x_positions=[(1, 1), (3, 3)], o_positions=[(1, 2), (3, 2)])
# ticTacToe.display(state)
#
# assert alphabeta_search(state, ticTacToe) == (2, 2)
#
# state = gen_state(to_move='O', x_positions=[(1, 1), (3, 1), (3, 3)], o_positions=[(1, 2), (3, 2)])
# assert alphabeta_search(state, ticTacToe) == (2, 2)
# ticTacToe.display(state)
#
# state = gen_state(to_move='O', x_positions=[(1, 1)], o_positions=[])
# assert alphabeta_search(state, ticTacToe) == (2, 2)
# ticTacToe.display(state)
#
# state = gen_state(to_move='X', x_positions=[(1, 1), (3, 1)], o_positions=[(2, 2), (3, 1)])
# assert alphabeta_search(state, ticTacToe) == (1, 3)
# ticTacToe.display(state)
