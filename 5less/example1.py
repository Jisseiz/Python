# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

import random
import collections

candy = 117
player1 = input('Введите имя игрока 1: ')
player2 = input('Введите имя игрока 2: ')
team = collections.deque()
draw = random.randint(1, 2)
move = 0


def queue_players(x):
    if x == 1:
        team.append(player1)
        team.append(player2)
    else:
        team.append(player2)
        team.append(player1)


def run(x, y):
    x = int(
        input(f'Ход игрока {player}, Введите количество конфет: '))
    if x > 28:
        x = int(
            input(f'Нельзя взять больше 28 конфет, введите количество заново: '))
    elif x <= 0:
        x = int(
            input(f'Нельзя брать менее 1 конфеты, введите количество заново: '))
    y = y - x
    return y


queue_players(draw)
while candy > 0:
    player = team.popleft()
    candy = run(move, candy)
    if candy <= 0:
        break
    team.append(player)
    print(f'Конфет осталось {candy}')


print(f'Победил игрок {player}')
print(team)
