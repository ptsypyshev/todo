from random import randint


# 1. Написать функцию, которая выбрасывает случайным образом, одно из трех исключений:
# ValueError, TypeError, RuntimeError.
# В месте вызова функции обрабатывать все три исключения.
def throw_exceptions():
    rand = randint(0, 3)
    if rand == 0:
        raise ValueError('It is a value error.')
    if rand == 2:
        raise TypeError('It is a type error.')
    else:
        raise RuntimeError('It is a runtime error.')


try:
    throw_exceptions()
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except RuntimeError as e:
    print(e)


# 2. Написать функцию, которая принимает на вход список. Если в списке все объекты int, то сортирует его.
# Иначе выбрасывает исключение ValueError
def int_sort(list_to_be_sorted):
    for item in list_to_be_sorted:
        if not isinstance(item, int):
            raise ValueError(f'Incorrect element in list - {item} is not a number')
    return sorted(list_to_be_sorted)


print(int_sort([3, 6, 0, 9, 1, 7, 2]))


# 3. Написать функцию, которая принимает на вход словарь и преобразует все ключи словаря к строкам и возвращает новый.
def keys_to_string(d):
    result = {}
    for k, v in d.items():
        result[str(k)] = v
    return result


mydict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e'
}
print(keys_to_string(mydict))


# 4. Написать функцию, которая принимает список чисел и возвращает их произведение.
def multiply(*args):
    result = 1
    for item in args:
        result *= item
    return result


print(multiply(1, 2, 3, 4, 5))
