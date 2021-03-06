# -*- coding: utf-8 -*-

__author__ = 'ptsypyshev'

import os


class Players:
    """
    Defines player object and its properties.
    """

    def __init__(self, name='Player', queue=0):
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

    def draw_points(self, ship, shift):
        print(ship)
        for pos in ship.position:
            print(pos)
            x, y = pos
            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    try:
                        print(j, i)
                        if self.seafield[i][j + shift] == ' ':
                            self.seafield[i][j + shift] = '*'
                        else:
                            raise IndexError
                    except IndexError:
                        continue
        return True

    def check_neighbours(self, x, y):
        try:
            for i in range(y - 1, y + 1):
                for j in range(x - 1, x + 2):
                    if j > self.size_x and self.seafield[i][j] != '          ':
                        return False
                    if self.seafield[i][j] == '█' or self.seafield[i][j] == '*':
                        return False
        except IndexError:
            print(f'Корабль выходит за пределы поля сражения {self.size_x}x{self.size_y}')
            return False
        return True

    def get_position(self, ship=0):
        if ship == 0:
            inp = input('Введите координаты цели, например Д7: ')
        else:
            inp = input(f'Введите координаты начала для {ship}-x палубного корабля, например Д7: ')
        try:
            x_str, *y_str = inp
            x = ''.join(self.seafield[0]).find(x_str.upper()) - 1
            y = int(''.join(y_str))
            if x < 1 or y < 1:
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
                    ship_position = []
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
                                    ship_position.append((x + j, y))
                                player_ships.append(Ships(ship_type, ship_position, True))
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
                                    ship_position.append((x, y + j))
                                player_ships.append(Ships(ship_type, ship_position, False))
                                print(player_ships[len(player_ships) - 1])
                                self.draw()
                                break
                    else:
                        print(f'Введенные координаты находятся за пределами поля сражения {self.size_x}x{self.size_y}. Попробуйте ещё раз')
        return player_ships

    def fast_setup(self, shift=0):
        player_ships = []
        player_ships.append(Ships(length=4, position=[(1, 1), (1, 2), (1, 3), (1, 4)], hor_direction=False, sunken=False))
        player_ships.append(Ships(length=3, position=[(1, 6), (1, 7), (1, 8)], hor_direction=False, sunken=False))
        player_ships.append(Ships(length=3, position=[(3, 3), (4, 3), (5, 3)], hor_direction=True, sunken=False))
        player_ships.append(Ships(length=2, position=[(3, 1), (4, 1)], hor_direction=True, sunken=False))
        player_ships.append(Ships(length=2, position=[(2, 10), (3, 10)], hor_direction=True, sunken=False))
        player_ships.append(Ships(length=2, position=[(6, 9), (6, 10)], hor_direction=False, sunken=False))
        player_ships.append(Ships(length=1, position=[(8, 2)], hor_direction=True, sunken=False))
        player_ships.append(Ships(length=1, position=[(10, 8)], hor_direction=True, sunken=False))
        player_ships.append(Ships(length=1, position=[(4, 5)], hor_direction=True, sunken=False))
        player_ships.append(Ships(length=1, position=[(3, 7)], hor_direction=True, sunken=False))
        for ship in player_ships:
            for point in ship.position:
                self.seafield[point[1]][point[0] + shift] = ' ' if shift else '█'
        return player_ships


class Ships:
    """
    Defines ship object and its properties.
    """
    default_position = [(0, 0)]

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

    def __init__(self, player, position=default_position, success=False):
        self.player = player
        self.position = position
        self.success = success

    def __str__(self):
        return f'Игрок {self.player.name} выстрелил в цель {self.position} - {self.success}.'


class Storage:
    """
    Defines storage object and its properties.
    """
    default_position = (0, 0)

    def __init__(self):
        self.player = []
        self.ships_position = {}
        self.shoots = []




