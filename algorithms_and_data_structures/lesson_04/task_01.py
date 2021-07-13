# Задание №1
# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их

# 3.4. Определить, какое число в массиве встречается чаще всего.

import cProfile
import random
from collections import Counter


def count_num(size):
    min_item = 0
    max_item = 1000
    array = [random.randint(min_item, max_item) for _ in range(size)]

    # print(f'Случайный массив:\n{array}')
    c = Counter(array)
    # print(f'Массив после подсчёта элементов:\n{c}')
    # print(f'Число в массиве, которое встречается чаще всего:\n{c.most_common(1)}\n')
    return c.most_common(1)

# timeit
# 100 loops, best of 5: 19.2 usec per loop  -10
# 100 loops, best of 5: 33.5 usec per loop  -20
# 100 loops, best of 5: 149 usec per loop   -100
# 100 loops, best of 5: 1.46 msec per loop  -1000
# 100 loops, best of 5: 13.4 msec per loop  -10000
# 100 loops, best of 5: 134 msec per loop   -100000

# cProfile
# 84 function calls (76 primitive calls) in 0.000 seconds           -10
# 536 function calls (528 primitive calls) in 0.001 seconds         -100
# 5057 function calls (5049 primitive calls) in 0.006 seconds       -1000
# 50265 function calls (50257 primitive calls) in 0.065 seconds     -10000
# 1    0.000    0.000    0.000    0.000 task_1.py:12(count_num)     -10
# 1    0.000    0.000    0.001    0.001 task_1.py:12(count_num)     -100
# 1    0.000    0.000    0.007    0.007 task_1.py:12(count_num)     -1000
# 1    0.000    0.000    0.080    0.080 task_1.py:12(count_num)     -10000


def count_num2(size):
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
    return num

# timeit
# 100 loops, best of 5: 21 usec per loop        -10
# 100 loops, best of 5: 49.5 usec per loop      -20
# 100 loops, best of 5: 607 usec per loop       -100
# 100 loops, best of 5: 53.1 msec per loop      -1000
# 100 loops, best of 5: 5.2 sec per loop        -10000 / ~45 minutes
# cProfile
# 56 function calls in 0.000 seconds            -10
# 510 function calls in 0.002 seconds           -100
# 5025 function calls in 0.137 seconds          -1000
# 50229 function calls in 13.045 seconds        -10000
# 1    0.000    0.000    0.000    0.000 task_1.py:43(count_num2)    -10
# 1    0.001    0.001    0.002    0.002 task_1.py:34(count_num2)    -100
# 1    0.119    0.119    0.125    0.125 task_1.py:34(count_num2)    -1000
# 1   11.999   11.999   12.068   12.068 task_1.py:34(count_num2)    -10000


def count_num3(size):
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
    return max_num

# timeit
# 100 loops, best of 5: 16.4 usec per loop  -10
# 100 loops, best of 5: 30.6 usec per loop  -20
# 100 loops, best of 5: 144 usec per loop   -100
# 100 loops, best of 5: 1.47 msec per loop  -1000
# 100 loops, best of 5: 14.5 msec per loop  -10000
# 100 loops, best of 5: 145 msec per loop   -100000
# cProfile
# 56 function calls in 0.000 seconds        -10
# 507 function calls in 0.001 seconds       -100
# 5025 function calls in 0.007 seconds      -1000
# 50229 function calls in 0.074 seconds     -10000
# 1    0.000    0.000    0.000    0.000 task_1.py:85(count_num3)    -10
# 1    0.000    0.000    0.001    0.001 task_1.py:69(count_num3)    -100
# 1    0.000    0.000    0.005    0.005 task_1.py:69(count_num3)    -1000
# 1    0.004    0.004    0.078    0.078 task_1.py:69(count_num3)    -10000


def count_num4(size):
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
    return max_num

# timeit
# 100 loops, best of 5: 16.4 usec per loop  -10
# 100 loops, best of 5: 34.9 usec per loop  -20
# 100 loops, best of 5: 279 usec per loop   -100
# 100 loops, best of 5: 10.4 msec per loop  -1000
# 100 loops, best of 5: 156 msec per loop   -10000

# cProfile
# 65 function calls in 0.000 seconds        -10
# 599 function calls in 0.001 seconds       -100
# 5671 function calls in 0.032 seconds      -1000
# 51211 function calls in 0.428 seconds     -10000
# 1    0.000    0.000    0.000    0.000 task_1.py:124(count_num4)   -10
# 1    0.000    0.000    0.001    0.001 task_1.py:101(count_num4)   -100
# 1    0.001    0.001    0.028    0.028 task_1.py:101(count_num4)   -1000
# 1    0.002    0.002    0.412    0.412 task_1.py:101(count_num4)   -10000


# cProfile.run('count_num4(10)')
