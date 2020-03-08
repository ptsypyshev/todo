# -*- coding: utf-8 -*-

from models import Players, Field

"""
Main file. Contains program execution logic.
"""


__author__ = 'ptsypyshev'


def create_field():
    while True:
        user_input = input('Введите размеры игрового поля через пробел или нажмите Enter для поля 10x10: ')
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


def main():
    """
    Main method of seabattle game.
    """
    sb_field = create_field()
    # sb_field.draw_field()
    player1 = Players(input('Введите своё имя: '), 1)
    player2 = Players('Python', 2)
    print(player1, player2)
    sb_field.draw()
    player1_ships = sb_field.setup()
    print(player1_ships)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
