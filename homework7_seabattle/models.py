# -*- coding: utf-8 -*-

__author__ = 'ptsypyshev'

import os


class Players:
    """
    Defines player object and its properties.
    """

    def __init__(self, name, queue=0):
        self.name = name
        self.queue = queue

    def __str__(self):
        return f'Player name is {self.name}, queue is {self.queue}'


class Field:
    """
    Defines Field object and its properties.
    """
    default_x = 10
    default_y = 10
    default_ships = {
        4: 1,
        3: 2,
        2: 3,
        1: 4,
    }

    def __init__(self, size_x=default_x, size_y=default_y, ships=default_ships):
        self.size_x = size_x
        self.size_y = size_y
        self.ships = ships
        alphas = [chr(i) for i in range(1040, 1070) if i != 1049]
        alphas = alphas[:self.size_x]
        alphas.insert(0, '  ')
        digits = tuple(i for i in range(1, self.size_y + 1))
        self.seafield = [[' ' for j in range(size_y)] for i in range(size_x)]
        self.seafield.insert(0, alphas)
        for i in range(0, size_y + 1):
            if 0 < i < 10:
                self.seafield[i].insert(0, ' ' + str(i))
            if 10 <= i:
                self.seafield[i].insert(0, i)
            self.seafield[i].append('          ')
            self.seafield[i].extend(self.seafield[i])

    def draw(self):
        os.system('cls')
        for i in range(self.size_x + 1):
            for j in range((self.size_y + 1) * 2 + 1):
                print(self.seafield[i][j], end=' | ')
            print()

    def check_neighbours(self, x, y):
        try:
            for i in range(y - 1, y + 1):
                for j in range(x - 1, x + 1):
                    if self.seafield[i][j] == '█' or self.seafield[i][j] == '*':
                        return False
        except IndexError:
            print(f'Корабль выходит за пределы поля сражения {self.size_x}x{self.size_y}')
            return False
        return True

    def get_position(self, ship):
        inp = input(f'Введите через пробел координаты начала для {ship}-x палубного корабля, например Д7: ')
        x_str, *y_str = inp
        x = ''.join(self.seafield[0]).find(x_str.upper()) - 1
        try:
            y = int(''.join(y_str))
            if x == -1 or x == 0 or y == 0:
                raise ValueError
        except ValueError:
            print('Введите корректные координаты.')
            return False
        return x, y

    def setup(self):
        player_ships = []
        for ship_type, count in self.ships.items():
            for i in range(count):
                while True:
                    position = self.get_position(ship_type)
                    if not position:
                        continue
                    x, y = position
                    if 0 < x < self.size_x + 1 or 0 < self.size_y + 1 < 11:
                        direction = input('Расположение горизонтальное? [Y/N] ')
                        if direction.lower() == '' or direction.lower() == 'y' or direction.lower() == 'yes' or \
                                direction.lower() == 'да':
                            for j in range(ship_type):
                                if not self.check_neighbours(x + j, y):
                                    print(f'Невозможно установить корабль по этим координатам.')
                                    break
                            else:
                                for j in range(ship_type):
                                    self.seafield[y][x + j] = '█'
                                player_ships.append(Ships(ship_type, (x, y), True))
                                print(player_ships[len(player_ships) - 1])
                                self.draw()
                                break
                        else:
                            for j in range(ship_type):
                                if not self.check_neighbours(x, y + j):
                                    print(f'Невозможно установить корабль по этим координатам.')
                                    break
                            else:
                                for j in range(ship_type):
                                    self.seafield[y + j][x] = '█'
                                player_ships.append(Ships(ship_type, (x, y), False))
                                print(player_ships[len(player_ships) - 1])
                                self.draw()
                                break
                    else:
                        print(f'Введенные координаты находятся за пределами поля сражения {self.size_x}x{self.size_y}. Попробуйте ещё раз')
        return player_ships

    def fast_setup(self, shift=0):
        player_ships = []
        player_ships.append(Ships(length=4, position=(1, 1), hor_direction=False, sunken=False))
        player_ships.append(Ships(length=3, position=(1, 6), hor_direction=False, sunken=False))
        player_ships.append(Ships(length=3, position=(3, 3), hor_direction=True, sunken=False))
        player_ships.append(Ships(length=2, position=(3, 1), hor_direction=True, sunken=False))
        player_ships.append(Ships(length=2, position=(2, 10), hor_direction=True, sunken=False))
        player_ships.append(Ships(length=2, position=(6, 9), hor_direction=False, sunken=False))
        player_ships.append(Ships(length=1, position=(8, 2), hor_direction=True, sunken=False))
        player_ships.append(Ships(length=1, position=(10, 8), hor_direction=True, sunken=False))
        player_ships.append(Ships(length=1, position=(4, 5), hor_direction=True, sunken=False))
        player_ships.append(Ships(length=1, position=(3, 7), hor_direction=True, sunken=False))
        for ship in player_ships:
            x, y = ship.position
            length = ship.length
            if ship.hor_direction:
                for j in range(length):
                    self.seafield[y][x + j + shift] = '█'
                    # print(x, y, length, True)
            else:
                for j in range(length):
                    # print(x, y, length, False)
                    self.seafield[y + j][x + shift] = '█'
        return player_ships


class Ships:
    """
    Defines ship object and its properties.
    """
    default_position = (0, 0)

    def __init__(self, length=1, position=default_position, hor_direction=False, sunken=False):
        self.length = length
        self.position = position
        self.hor_direction = hor_direction
        self.sunken = sunken

    def __str__(self):
        return f'Ship length={self.length}, position={self.position}, hor_direction={self.hor_direction}, sunken={self.sunken}'


class Shoot:
    """
    Defines shoot object and its properties.
    """
    default_position = (0, 0)

    def __init__(self, player, position=default_position, miss=True):
        self.player = player
        self.position = position
        self.miss = miss


class Storage:
    """
    Defines storage object and its properties.
    """
    default_position = (0, 0)

    def __init__(self):
        self.player = []
        self.ships_position = {}
        self.shoots = []




