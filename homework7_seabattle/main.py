# -*- coding: utf-8 -*-

from models import Players, Field, Shoot
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


def check_shoot(ships, target, field, shift=0):
    for ship in ships:
        for pos in ship.position:
            if target == pos:
                if field.seafield[target[1]][target[0] + shift] != 'X':
                    ship.length -= 1
                    field.seafield[target[1]][target[0] + shift] = 'X'
                    if ship.length == 0:
                        ship.sunken = True
                        field.draw_points(ship, shift)
                        ships.remove(ship)
                        print('Корабль потоплен!!!')
                return True
    if field.seafield[target[1]][target[0] + shift] == ' ':
        field.seafield[target[1]][target[0] + shift] = '.'
    return False


def game(p1, p2, p1_ships, p2_ships, sbf):
    shoot_log = []
    comp_turn = False
    x_len = len(sbf.seafield[0]) // 2 - 2
    y_len = len(sbf.seafield) - 1
    while p1_ships and p2_ships:
        if comp_turn:
            print('Ход компьютера!')
            x = randint(1, x_len)
            y = randint(1, y_len)

            shoot_target = x, y
            check = check_shoot(p1_ships, shoot_target, sbf)
            new_shoot = Shoot(p2, shoot_target)
            if check:
                new_shoot.success = True
            else:
                comp_turn = False
            shoot_log.append(new_shoot)
            sbf.draw()
            print(shoot_log[len(shoot_log) - 1])
        else:
            while True:
                shoot_target = sbf.get_position()
                if shoot_target:
                    break
            check = check_shoot(p2_ships, shoot_target, sbf, 12)
            new_shoot = Shoot(p1, shoot_target)
            if check:
                new_shoot.success = True
            else:
                comp_turn = True
            shoot_log.append(new_shoot)
            print(f'   {p1.name}\'s field' + ' ' * sbf.size_x * 5 + f'   {p2.name}\'s field')
            sbf.draw()
            print(shoot_log[len(shoot_log) - 1])
    if p1_ships:
        print(f'Игрок {p1.name} победил!')
        for shoot in shoot_log:
            print(shoot)
    else:
        for shoot in shoot_log:
            print(shoot)
        print(f'Игрок {p2.name} победил')


def main():
    """
    Main method of seabattle game.
    """
    sb_field = create_field()
    p_name = input('Введите своё имя: ')
    player1 = Players(p_name, 1) if p_name else Players(queue=1)

    # player1 = Players('Pavel', 1)
    player2 = Players('Python', 2)
    print(f'   {player1.name}\'s field' + ' ' * sb_field.size_x * 5 + f'   {player2.name}\'s field')
    sb_field.draw()

    player1_ships = sb_field.setup()
    # player1_ships = sb_field.fast_setup()
    player2_ships = sb_field.fast_setup(shift=12)
    # for ship in player1_ships:
    #     print(ship)
    # for ship in player2_ships:
    #     print(ship)
    print(f'   {player1.name}\'s field' + ' ' * sb_field.size_x * 5 + f'   {player2.name}\'s field')
    sb_field.draw()
    game(player1, player2, player1_ships, player2_ships, sb_field)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
