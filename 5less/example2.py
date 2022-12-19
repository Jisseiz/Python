board = list(range(1, 10))
winner = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
          (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")


def take_input(player):
    while True:
        value = input(f'Куда поставить {player}: ')
        if not (value in '123456789'):
            print('Введите номер клетки, от 1 до 10')
            continue
        if str(board[int(value) - 1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        board[int(value) - 1] = player
        break


def check_win():
    for x in winner:
        if board[x[0] - 1] == board[x[1] - 1] == board[x[2] - 1]:
            return board[x[1] - 1]
    else:
        return False


def main():
    move = 0
    while True:
        draw_board()
        if move % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if move > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(f'{winner}, выиграл')
                break
        move += 1
        if move > 8:
            draw_board()
            print('Ничья')
            break


main()
