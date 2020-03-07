# -*- coding: utf-8 -*-

__author__ = 'ptsypyshev'


class Players:
    """
    Defines player object and its properties.
    """

    def __init__(self, name, queue=0):
        self.name = name
        self.queue = queue


class Field:
    """
    Defines Field object and its properties.
    """
    default_size = (10, 10)
    default_ships = {
        '4x': 1,
        '3x': 2,
        '2x': 3,
        '1x': 4,
    }

    def __init__(self, size=default_size, ships=default_ships):
        self.size = size
        self.ships = ships


class Ships:
    """
    Defines ship object and its properties.
    """
    default_position = (0, 0)

    def __init__(self, length=1, position=default_position, sunken=False):
        self.length = length
        self.position = position
        self.sunken = sunken


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




