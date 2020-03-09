# 1. Нужно написать генератор, который бы каждый раз возвращал новое случайное значение
def random_gen():
    from random import randint
    while True:
        yield randint(1, 1000)

x = random_gen()
for i in range(10):
    print(next(x), end=' ')
print()


# 2. Нужно написать генератор, который бы работал как range()
def custom_range(*args):
    if len(args) == 0:
        raise TypeError('range expected 1 argument, got 0')
    elif len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        print(len(args))
        raise TypeError('range expected at most 3 arguments, got 4')
    i = start
    while i < stop:
        yield i
        i += step


for i in range(10):
    print(i, end=' ')
print()

for i in range(11, 20):
    print(i, end=' ')
print()

for i in range(30, 100, 10):
    print(i, end=' ')
print()

# 3. Нужно написать генератор, который бы работал как map()
def custom_map(func, obj):
    for item in obj:
        yield func(item)


old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(custom_map(int, old_list))
print(new_list)


# 4. Нужно написать генератор, который бы работал как enumerate()
def custom_enumerate(obj):
    i = 0
    for item in obj:
        yield i, item
        i += 1



for index, elem in custom_enumerate(new_list):
    print(index, elem)


# 5. Нужно написать генератор, который бы работал как zip()
def custom_zip(*args):
    result = []
    for i in range(len(args)):
        try:
            for obj in args:
                result.append(obj[i])
            yield tuple(result)
            result.clear()
        except IndexError:
            StopIteration


a = [1, 2, 3]
b = "xyz"
c = (None, True)
res = list(custom_zip(a, b, c))
print(res)
