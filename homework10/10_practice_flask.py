# 1. Повторить пример с юзером
# 2. Принимать 2 числа, складывать их и возвращать сумму
# 3. Принимать 3 строки и возвращать самую длинную
# 4* (сложное). Введите путь до файла относительно текущей папки, проверьте существует ли такой файл, верните "да" или "нет"
from flask import Flask
import os


app = Flask(__name__)


@app.route('/hello/<user>')
def home(user):
    return 'Hello user: ' + user


@app.route('/calc/<int:first>+<int:second>')
def calc(first, second):
    return str(first + second)


@app.route('/longest/<first>&<second>&<third>')
def longest(first, second, third):
    max_arg = max(len(first), len(second), len(third))
    if max_arg == len(first):
        return first
    elif max_arg == len(second):
        return second
    else:
        return third


@app.route('/path/<path:fpath>')
def pathfinder(fpath):
    dirpath = os.getcwd()
    fullpath = os.path.join(dirpath, fpath)
    if os.path.isfile(fullpath):
        return 'Да'
    else:
        return 'Нет'


if __name__ == '__main__':
    app.run()