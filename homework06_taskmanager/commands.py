# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import inspect
import json

# import custom_exceptions
from custom_exceptions import UserExitException
from models import BaseItem
from utils import get_input_function

__author__ = 'sobolevn'


class BaseCommand(object):
    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print('{}: {}'.format(index, str(obj)))


class DoneCommand(BaseCommand):
    @staticmethod
    def label():
        return 'done'

    def print_result(self, obj):
        print('{} marked as {}'.format(str(obj), self.label()))
        print()

    def change_status(self, obj):
        print(self.label())
        obj.make_done() if self.label() == 'done' else obj.make_undone()

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return
        tasks = {}
        for index, obj in enumerate(objects):
            tasks[index] = obj
            print('{}: {}'.format(index, str(obj)))

        input_function = get_input_function()

        while True:
            try:
                selection = int(input_function('Input number: '))
                selected_key = list(tasks.keys())[selection]

                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        selected_task = tasks[selected_key]
        self.change_status(selected_task)
        self.print_result(selected_task)


class UndoneCommand(DoneCommand):
    @staticmethod
    def label():
        return 'undone'


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():
        # Dynamic load:
        # def class_filter(klass):
        #     return inspect.isclass(klass) \
        #            and klass.__module__ == BaseItem.__module__ \
        #            and issubclass(klass, BaseItem) \
        #            and klass is not BaseItem

        # classes = inspect.getmembers(
        #         sys.modules[BaseItem.__module__],
        #         class_filter,
        # )
        # return dict(classes)

        from models import ToDoItem, ToBuyItem, ToReadItem

        return {
            'ToDoItem': ToDoItem,
            'ToBuyItem': ToBuyItem,
            'ToReadItem': ToReadItem,
        }

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print('{}: {}'.format(index, name))

        input_function = get_input_function()
        selection = None
        selected_key = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                selected_key = list(classes.keys())[selection]

                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        selected_class = classes[selected_key]
        print('Selected: {}'.format(selected_class.__name__))
        print()

        new_object = selected_class.construct()

        objects.append(new_object)
        print('Added {}'.format(str(new_object)))
        print()
        return new_object


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')
