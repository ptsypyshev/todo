from random import randint


def guessing(number):
    while True:
        guess = input('Введите число: ')
        if guess == 'q':
            print('До скорых встреч!')
            return False
        else:
            try:
                guess_int = int(guess)
            except ValueError:
                print('Вы ввели не число, попробуйте снова. Для выхода нажмите q')
                continue
            if guess_int < number:
                print('Ваше число меньше загаданного. Попробуйте ещё раз.')
            elif guess_int > number:
                print('Ваше число больше загаданного. Попробуйте ещё раз.')
            else:
                print(f'Вы угадали, это число {number}')
                return True


def game_guess():
    num = randint(1, 101)
    manual = "Python загадал число от 1 до 10. Попытайтесь угадать это число. Для выхода нажмите q"
    print()
    print('*' * len(manual), manual, '*' * len(manual), sep='\n')
    result = guessing(num)
    return result


if __name__ == '__main__':
    while True:
        if not game_guess():
            break
