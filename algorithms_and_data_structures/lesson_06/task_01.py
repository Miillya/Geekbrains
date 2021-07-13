# Задание №1
#  Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#  Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# 3.4. Определить, какое число в массиве встречается чаще всего.

import random
import sys
from collections import Counter


def decoration():
    print('\n', '=' * 77, '\n')


def show_size_object(x, level=0):
    sum_size = sys.getsizeof(x)
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                sum_size += show_size_object(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                sum_size += show_size_object(y, level + 1)

    if level == 0:
        print(f'Объем памяти объекта - {sum_size} байт')
    return sum_size


def show_size_func(f):
    sum_size = 0
    for key, x in f.items():
        print(f'Объект в переменной "{key}":')
        sum_size += show_size_object(x)
    decoration()
    print(f'Общий объем памяти для всех объектов функции - {sum_size} байт')
    decoration()


def count_num():
    size = 100
    min_item = 0
    max_item = 1000
    array = [random.randint(min_item, max_item) for _ in range(size)]

    # print(f'Случайный массив:\n{array}')
    c = Counter(array)
    # print(f'Массив после подсчёта элементов:\n{c}')
    # print(f'Число в массиве, которое встречается чаще всего:\n{c.most_common(1)}\n')

    return locals()
    # return c.most_common(1)


show_size_func(count_num())


def count_num2():
    size = 100
    min_item = 0
    max_item = 1000
    array = [random.randint(min_item, max_item) for _ in range(size)]
    size = len(array)
    # print(array)

    num = array[0]
    frequency = 1
    for i in range(size):
        spam = 1
        for j in range(i + 1, size):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    # if frequency > 1:
    #     print(f'Число {num} встречается {frequency} раз(а)')
    # else:
    #     print('Все элементы уникальны')
    # return num
    return locals()


show_size_func(count_num2())


def count_num3():
    size = 100
    min_item = 0
    max_item = 1000
    array = [random.randint(min_item, max_item) for _ in range(size)]
    # print(array)

    d = dict.fromkeys(array, 0)

    for num in array:
        d[num] += 1

    count = 0
    for key in d:
        if d[key] > count:
            max_num = key
            count = d[key]

    # print(f'Число {max_num} встречается {count} раз(а)\n')
    # return max_num
    return locals()


show_size_func(count_num3())


def count_num4():
    size = 100
    min_item = 0
    max_item = 1000
    array = [random.randint(min_item, max_item) for _ in range(size)]
    # print(array)

    array_set = set(array)
    max_num = None
    count = 0

    for i in array_set:
        key = array.count(i)
        if key > count:
            count = key
            max_num = i

    # print(f'Число {max_num} встречается {count} раз(а)')
    # return max_num
    return locals()


show_size_func(count_num4())

# Windows 10 Pro x64 | Python 3.7 (32-bit)
# Наименьшее количество памяти использует второй вариант, который наиболее медлительный при исполнении.
