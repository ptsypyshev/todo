# 1. Создать класс корзина у которого можно выставить разную вместимость для разных объектов. В объекты класса корзина можно помещать разные объекты.
# class Basket:
#     def __init__(self, capacity=100):
#         self.capacity = capacity
#         self.content = []
#
#     def get(self):
#         return self.content
#
#     def put(self, item):
#         try:
#             if self.capacity - item.size >= 0:
#                 self.content.append(item)
#                 self.capacity -= item.size
#             else:
#                 print(f'It is not enough capasity of {self} to put in {item}')
#                 return f'It is not enough capasity of {self} to put in {item}'
#         except:
#             print(f'{item} has no atribute "size"')
#             return f'{item} has no atribute "size"'

# 2. Создать класс "пакет", в который тоже можно помещать предметы. У него тоже есть вместимость.


# 3. Создать любой класс, объект которого можно помещать в корзину или пакет.
# class Item:
#     def __init__(self, size=1):
#         self.size = size


# 4. Если вместимость пакета или корзины недостаточна для помещения объекта - выдать сообщение, что объект поместить нельзя.

# apple = Item(20)
# banana = Item(10)
# orange = Item(20)
# watermelon = Item(120)
# pear = Item(25)
#
# mybasket = Basket(50)
#
# mybasket.put(apple)
# print(mybasket.content, mybasket.capacity)
# mybasket.put(apple)
# print(mybasket.content, mybasket.capacity)
# mybasket.put(apple)
# print(mybasket.content, mybasket.capacity)

# Stepik
# def fraction(dividend, divider):
#     if dividend % divider == 0:
#         return int(dividend / divider)
#     else:
#         return f'{dividend // divider} {fraction(divider, dividend % divider)}'
#
#
# dividend, divider = (int(i) for i in input().split('/'))
# print(fraction(dividend, divider))

# Stepik
# def hanoi(n, i, k):
#     if n == 1:
#         print(f'{i} - {k}')
#         return
#     tmp = 6 - i - k
#     hanoi(n - 1, i, tmp)
#     print(f'{i} - {k}')
#     hanoi(n - 1, tmp, k)
#
#
# hanoi(int(input()), 1, 3)

# Stepik UpperCamelCase
# for elem in input().split('_'):
#     print(elem.capitalize(), end='')
# print()

# Stepik Kokh
# kokh = '.'
# num = int(input())
# for i in range(num):
#     kokh = kokh.replace('.', '.turn 60.turn -120.turn 60.')
# result = kokh[1:-1].replace('.', '\n')
# print(result)

# Stepik Unicode Caesar
# def caesar(shift, string):
#     start, end = 0x1F600, 0x1F64F
#     new_string = []
#     for elem in string:
#         new_string.append(chr(start + (ord(elem) - start + shift) % (end - start + 1)))
#     result = ''.join(new_string)
#     return f'Result: "{result}"'
#
#
# print(caesar(int(input()), input()))

# Stepik Base RLE encode
# def rle(string):
#     counter = 0
#     tmp_char = ''
#     result = []
#     for char in string:
#         if char != tmp_char:
#             if counter:
#                 if counter > 1:
#                     result.append(str(counter))
#                 result.append(tmp_char)
#             tmp_char = char
#             counter = 1
#         else:
#             counter += 1
#     else:
#         if counter > 1:
#             result.append(str(counter))
#         result.append(tmp_char)
#     return ''.join(result)
#
#
# print(rle(input()))

# Stepik index_finder
# def finder(string, find):
#     l = string.split()
#     if find not in l:
#         print('None')
#         return
#     for index, elem in enumerate(l):
#         if elem == find:
#             print(index, end=' ')
#
#
# finder(input(), input())

# Stepik Collatz
# def collatz(number):
#     if number == 1:
#         return 1
#     if number % 2:
#         return f'{number} {collatz(number * 3 + 1)}'
#     return f'{number} {collatz(number // 2)}'
#
#
# print(collatz(int(input())))

# Stepik Length statistic
# def len_counter(string):
#     lst = string.split()
#     dct = {}
#     for elem in lst:
#         dct[len(elem)] = dct.get(len(elem), 0) + 1
#     for k in sorted(dct.keys()):
#         print(f'{k}: {dct[k]}')
#
#
# len_counter(input())

# Stepik Game of life
# def nb_counter(matrix, x, y):
#     counter = 0
#     for i in range(x - 1, x + 2):
#         for j in range(y - 1, y + 2):
#             if i == x and j == y:
#                 continue
#
#             if j == len(matrix[0]):
#                 y1 = 0
#             elif j < 0:
#                 y1 = len(matrix[0]) + j
#             else:
#                 y1 = j
#
#             if i == len(matrix):
#                 x1 = 0
#             elif i < 0:
#                 x1 = len(matrix) + i
#             else:
#                 x1 = i
#
#             try:
#                 if matrix[x1][y1] == 'X':
#                     counter += 1
#             except IndexError:
#                 continue
#
#     if counter == 3:
#         return 'X'
#     if counter == 2:
#         return matrix[x][y]
#     return '.'
#
#
# n, m = (int(i) for i in input().split())
# matrix = [[i for i in input()] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(nb_counter(matrix, i, j), end='')
#     print()

# Stepik anagram
# def anagram(first, second):
#     first = first.lower()
#     second = second.lower()
#     for char in first:
#         if first.count(char) != second.count(char):
#             return False
#     return True
#
#
# print(anagram(input(), input()))

# Stepic RIM2ARAB
# def converter(string):
#     result = 0
#     rim_first = {
#         'IV': 4,
#         'IX': 9,
#         'XL': 40,
#         'XC': 90,
#         'CD': 400,
#         'CM': 900
#     }
#     rim = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     lenght = len(string)
#     i = 0
#     while i < lenght:
#         if i < lenght - 1:
#             tmp = string[i] + string[i + 1]
#             if tmp in rim_first:
#                 result += rim_first[tmp]
#                 i += 2
#                 continue
#         result += rim[string[i]]
#         i += 1
#     return result
#
#
# print(converter(input()))
# Stepik Poker
# class Card:
#     def __init__(self, string):
#         *value_list, suit = string
#         self.suit = suit
#         value = ''.join(value_list)
#         try:
#             self.value = int(value)
#         except ValueError:
#             if value == 'J':
#                 self.value = 11
#             elif value == 'Q':
#                 self.value = 12
#             elif value == 'K':
#                 self.value = 13
#             else:
#                 self.value = 14
#
#     def get_suit(self):
#         return self.suit
#
#     def get_value(self):
#         return self.value
#
#
# def same_suit(values):
#     for index, value in enumerate(values):
#         if index == 0:
#             continue
#         if value != values[index - 1] + 1:
#             break
#     else:
#         if value == 14:
#             return 'Royal Flush'
#         return 'Straight Flush'
#     return 'Flush'
#
#
# def diff_suit(values):
#     # print(values)
#     counter = {}
#     for value in values:
#         counter[value] = counter.get(value, 0) + 1
#     for index, value in enumerate(values):
#         if index == 0:
#             continue
#         if value != values[index - 1] + 1:
#             break
#     else:
#         return 'Straight'
#     # print(counter)
#     if 4 in counter.values():
#         return 'Four of a Kind'
#     if 3 in counter.values() and 2 in counter.values():
#         return 'Full House'
#     if 3 in counter.values():
#         return 'Three of a Kind'
#     if len(counter) == 3:
#         return 'Two Pairs'
#     if len(counter) == 4:
#         return 'Pair'
#     return 'High Card'
#
#
# def combination(cards):
#     suits = set()
#     values = []
#     for card in cards:
#         suits.add(card.get_suit())
#         values.append(card.get_value())
#     if len(suits) == 1:
#         return same_suit(sorted(values))
#     return diff_suit(sorted(values))
#
#
# poker_hand = [Card(i) for i in input().split()]
# print(combination(poker_hand))
