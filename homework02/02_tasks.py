from random import random, randint
from pprint import pprint
# Создать лист из 6 любых чисел. Отсортировать его по возрастанию
lst = [1, 5, 7, 2, 9, 4]
lst.sort()
print(lst)


# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
dct = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f'
}
for k, v in dct.items():
    print(k, v)


# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
tpl = set(random()*100 for i in range(10))
print(max(tpl), min(tpl))


# Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
# чтобы получилось: 'Earth -> Russia -> Moscow'
geo = ['Earth', 'Russia', 'Moscow']
inline = ' -> '.join(geo)
print(inline)


# Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
path = '/bin:/usr/bin:/usr/local/bin'
l = path.split(sep=':')
pprint(l)


# Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
for i in range(1, 101):
    if i % 7 == 0:
        print(f'{i} делится на 7.')
    else:
        print(f'{i} не делится на 7.')


# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
matrix = [[randint(1, 101) for _ in range(3)] for _ in range(4)]
pprint(matrix)
for i in range(4):
    for j in range(3):
        print(matrix[i][j], end=' ')
    print()
for i in range(3):
    for j in range(4):
        print(matrix[j][i], end=' ')
    print()


# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
l2 = [randint(1, 100) for _ in range(10)]
for i in range(len(l2)):
    print(l2[i], i)


# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
l3 = ['mystr', 'to-delete', 'mystr2','mystr3', 'to-delete', 'mystr4', 'mystr5', 'to-delete', 'mystr6']
while 'to-delete' in l3:
    l3.remove('to-delete')
pprint(l3)


# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
iter = 10
while iter > 0:
    print(iter, end = ' ')
    iter -= 1
print()