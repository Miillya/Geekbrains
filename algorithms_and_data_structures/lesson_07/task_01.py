# Задание №1
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
# сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random


def bubble_sort(array, reverse=False):

    sign = int(reverse) * 2 - 1
    n = 1

    while n < len(array):
        is_sorted = True

        for i in range(len(array) - n):
            if array[i] * sign < array[i + 1] * sign:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1


SIZE = 16
LIMIT = 100
data = [random.randrange(-LIMIT, LIMIT) for _ in range(SIZE)]
print(data)
bubble_sort(data, reverse=True)
print(data)
