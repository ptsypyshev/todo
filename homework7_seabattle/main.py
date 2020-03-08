# -*- coding: utf-8 -*-

from models import Players, Field
from random import randint

"""
Main file. Contains program execution logic.
"""


__author__ = 'ptsypyshev'


def create_field():
    while True:
        # user_input = input('Введите размеры игрового поля через пробел или нажмите Enter для поля 10x10: ')
        user_input = '10 10'
        if not user_input:
            return Field()
        else:
            try:
                x, y = (int(i) for i in user_input.split())
                if x > 20 or y > 20:
                    print('Слишком большой размер поля. Попробуйте ещё раз')
                    continue
                break
            except ValueError:
                print('Введите целые числа для длины и ширины игрового поля, например 10 10')

    return Field(x, y)


def game(p1, p2, p1_ships, p2_ships, sbf):
    shoot_log = []
    comp_turn = True
    x_len = len(sbf.seafield[0]) // 2 - 1
    y_len = len(sbf.seafield)
    print(x_len, y_len)
    while p1_ships and p2_ships:
        if comp_turn:
            x = randint(1, x_len)
            y = randint(1, y_len)
            print(x, y)
            break


def main():
    """
    Main method of seabattle game.
    """
    sb_field = create_field()
    # player1 = Players(input('Введите своё имя: '), 1)
    player1 = Players('Pavel', 1)
    player2 = Players('Python', 2)
    print(player1, player2)
    sb_field.draw()
    # print(len(sb_field.seafield[0]), len(sb_field.seafield))
    player1_ships = sb_field.fast_setup()
    player2_ships = sb_field.fast_setup(shift=12)
    # for ship in player1_ships:
    #     print(ship)
    sb_field.draw()
    game(player1, player2, player1_ships, player2_ships, sb_field)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
