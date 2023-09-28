from math import inf as infinity
from random import choice
import platform
import time
from os import system

from matplotlib.pyplot import pause

cont = 0

total = 0

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluate(state):

    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


# terminal states
def wins(state, player):

    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


# IMPLEMENTAÇÃO DO MINIMAX SEM A PODA ALPHA BETA

# def minimax(state, depth, alpha, beta ,player):
#     global cont
#     if player == COMP:
#         best = [-1, -1, -infinity]
#     else:
#         best = [-1, -1, +infinity]

#     if depth == 0 or game_over(state):
#         score = evaluate(state)
#         return [-1, -1, score]

#     for cell in empty_cells(state):
#         x, y = cell[0], cell[1]
#         state[x][y] = player

#         score = minimax(state, depth - 1, alpha, beta , -player)
#         state[x][y] = 0
#         score[0], score[1] = x, y

#         if player == COMP:
#             if score[2] > best[2]:
#                 best = score  # max value
#         else:
#             if score[2] < best[2]:
#                 best = score  # min value

#     cont = cont + 1
#     print(cont)
#     return best


# IMPLEMENTAÇÃO DO MINIMAX COM A PODA ALPHA BETA

def minimax(state, depth, alpha, beta, player):
    global cont
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player

        score = minimax(state, depth - 1, alpha, beta, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
            alpha = max(alpha, score[2])
            if beta <= alpha:
                break
        else:
            if score[2] < best[2]:
                best = score  # min value
            beta = min(beta, score[2])
            if beta <= alpha:
                break

    cont = cont + 1
    # print(cont)
    return best


def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def reset_board():
    global board
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def render(state, c_choice, h_choice):

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice, user):

    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, -infinity, infinity, user)
        x, y = move[0], move[1]

    set_move(x, y, user)
    time.sleep(1)


def human_turn(c_choice, h_choice, wannaPlay):

    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    # clean()
    print(f'Jogada do humano [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Digite de (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Movimento inválido')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Adeus')
            exit()
        except (KeyError, ValueError):
            print('Escolha errada')


# ...

def main():

    clean()
    h_choice = ''  # X ou O
    c_choice = ''  # X ou O
    first = ''  # se o humano começa

    # O humano escolhe X ou O para jogar
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Escolha X ou O\n: ').upper()
            wannaPlay = input("Quer Jogar?[s/n]:")
        except (EOFError, KeyboardInterrupt):
            print('Tchau')
            exit()
        except (KeyError, ValueError):
            print('Escolha inválida\n')
        else:
            print('Escolha inválida digite algo válido\n')

    # Definindo a escolha do computador
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # O humano pode começar primeiro
    clean()
    while first != 'S' and first != 'N':
        try:
            first = input('O humano começa?[s/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Tchau')
            exit()
        except (KeyError, ValueError):
            print('Escolha inválida')

    # Loop principal do jogo
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice, COMP)
            first = ''
        if wannaPlay == 's' or wannaPlay == 'S':
            human_turn(c_choice, h_choice, wannaPlay)
        else:
            ai_turn(c_choice, h_choice, HUMAN)

        ai_turn(c_choice, h_choice, COMP)

    # Mensagem de fim de jogo
    if wins(board, HUMAN):
        clean()
        print(f'Vez do Humano [{h_choice}]')
        render(board, c_choice, h_choice)
        print('VOCÊ VENCEU!')
    elif wins(board, COMP):
        clean()
        print(f'Vez do Computador [{c_choice}]')
        render(board, c_choice, h_choice)
        print('VOCÊ PERDEU!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('EMPATE!')
    while True:
        print("Quer jogar novamente?")
        restart = input("s/n:").upper()
        if restart == 'N':
            print("Obrigado por jogar")
            break
        elif(restart == 'S'):
            reset_board()  # Reinicia o tabuleiro
            main()
        else:
            print("Escolha inválida")
    exit()

# ...


if __name__ == '__main__':
    main()
