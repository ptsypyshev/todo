import os
from random import randint

fruits = ('apple', 'banana', 'orange', 'grapes', 'pear')
health = 6


def img_print(img):
    os.system('cls')
    print('*' * 17, '    ВИСЕЛИЦА     ', '     ФРУКТЫ     ', '*' * 17, sep='\n')
    for elem in img:
        # print(elem)
        # print(len(elem))
        for item in elem:
            print(item, end='')
        print()


def hangman_img(img, count):
    if count == 6:
        img[2][-2] = '0'
        return
    if count == 5:
        img[3][-2] = '|'
        return
    if count == 4:
        img[3][-3] = '\\'
        return
    if count == 3:
        img[3][-1] = '/'
        return
    if count == 2:
        img[4][-3] = '/'
        return
    if count == 1:
        img[4][-1] = '\\'
        return


def masked(word, guess):
    result = []
    for char in word:
        if char in guess:
            result.append(char)
        else:
            result.append('*')
    return ''.join(result)


def hangman_game(words, health):
    img = [
        [' ', ' ', ' ', ' ', ' ', '┌', '─', '─', '─', '─', '─', '─', '─', '─', '┐', ' '],
        [' ', ' ', ' ', ' ', ' ', '│', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '│', ' '],
        [' ', ' ', ' ', ' ', ' ', '│', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', '│', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', '│', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', '│', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─', '─'],
    ]
    word = words[randint(0, len(words) - 1)]
    guess_set = set()

    while health > 0:
        masked_word = masked(word, guess_set)
        if not '*' in masked_word:
            break
        img_print(img)
        print(f'Попробуйте угадать слово: {masked_word}', f'У Вас осталось {health} попыток.')
        print('Для выхода введите пробел.')
        guess_char = input('Введите букву: ')[0]
        if guess_char == ' ':
            return False
        if guess_char in word:
            guess_set.add(guess_char)
        else:
            hangman_img(img, health)
            health -= 1
    else:
        img_print(img)
        print(f'Вы не угадали слово "{word}"')
        press_any_key = input('Для продолжения нажмите Enter ... ')
        return True
    img_print(img)
    print(f'Вы угадали слово "{word}"')
    press_any_key = input('Для продолжения нажмите Enter ... ')
    return True


if __name__ == '__main__':
    loop = True
    while loop:
        loop = hangman_game(fruits, health)
    print('До скорых встреч!!!')