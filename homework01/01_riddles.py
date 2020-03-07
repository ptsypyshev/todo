# Задача: реализовать игру в загадки
#
# Требования:
# Программа выводить в консоль текст загадки и ждать ввода пользователя
# Программа после ввода пользователя ответа должна вывести в консоль результат: правильный ли ответ дал пользователь
# Загадок должно быть 10, тематика вопросов должна быть по первому занятию
# Дополнительные требования (со звездочкой или сложные, необязательно для выполнения):
# Программа должна в конце игры сказать, сколько ответов дал пользователь: сколько из них было верных
# Программа должна не учитывать регистр ответа: "Python" и "python" оба должны быть правильным ответом на вопрос
# "Какой язык мы учим?"

# # Riddles start #
# count_answers = 10
# correct_answers = 0
# answer = input("Какой язык мы учим? ").lower()
# if answer == 'python':
#     correct_answers = correct_answers + 1
# answer = input("Как называется тип данных для целых чисел? ").lower()
# if answer == 'int' or answer == 'integer':
#     correct_answers = correct_answers + 1
# answer = input("Как называется тип данных для дробных чисел? ").lower()
# if answer == 'float':
#     correct_answers = correct_answers + 1
# answer = input("Как называется тип данных для строк? ").lower()
# if answer == 'str' or answer == 'string':
#     correct_answers = correct_answers + 1
# answer = input("Какое булево значение соответствует выражению 3 > 5? ").lower()
# if answer == 'false':
#     correct_answers = correct_answers + 1
# answer = input("Как называется цикл с неопределенным количеством повторений? ").lower()
# if answer == 'while':
#     correct_answers = correct_answers + 1
# answer = input("Можно ли складывать переменные разного типа? ").lower()
# if answer == 'no' or answer == 'нет':
#     correct_answers = correct_answers + 1
# answer = input("Можно ли умножить строку на число? ").lower()
# if answer == 'yes' or answer == 'да':
#     correct_answers = correct_answers + 1
# answer = input("Какая функция используется для ввода данных? ").lower()
# if answer == 'print':
#     correct_answers = correct_answers + 1
# answer = input("Какая функция используется для определения длины строки? ").lower()
# if answer == 'len':
#     correct_answers = correct_answers + 1
#
# print('Вы ответили на {} вопросов, из них правильно на {}'.format(count_answers, correct_answers))
#
# # Riddles end #

# Riddles dict start #

riddles_dict = {
    "Какой язык мы учим?": ['python'],
    "Как называется тип данных для целых чисел?": ['int', 'integer'],
    "Как называется тип данных для дробных чисел?": ['float'],
    "Как называется тип данных для строк?": ['str', 'string'],
    "Какое булево значение соответствует выражению 3 > 5?": ['false'],
    "Как называется цикл с неопределенным количеством повторений?": ['while'],
    "Можно ли складывать переменные разного типа?": ['no', 'нет'],
    "Можно ли умножить строку на число?": ['yes', 'да'],
    "Какая функция используется для ввода данных?": ['input'],
    "Какая функция используется для определения длины строки?": ['len']
}

len_riddles_dict = len(riddles_dict)
correct_answers = 0
for k, v in riddles_dict.items():
    answer = input(k + ' ')
    if answer.lower() in v:
        correct_answers += 1

print(f'Вы ответили на {len_riddles_dict} вопросов, из них правильно на {correct_answers}')

# Riddles dict end #

# Задача: Напишите программу, которая находит все простые числа между 0 и пользовательским числом
# # Prime numbers start #
# limit = int(input('Введите целое число больше нуля: '))
# if 1 < limit:
#     for i in range(2, limit):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i, end=' ')
# elif limit == 1:
#     print('В диапазоне от 0 до 1 нет простых чисел.')
# else:
#     print('Некорректный запрос.')
# # Prime numbers end #
