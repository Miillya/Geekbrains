# Задание №3
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
import statistics


def partition(array, pivot):
    smaller = []
    equally = []
    bigger = []
    for item in array:
        if item < pivot:
            smaller.append(item)
        elif item > pivot:
            bigger.append(item)
        else:
            equally.append(item)
    return smaller, equally, bigger


def top_key(array, key):
    pivot = array[random.randrange(len(array))]
    left, middle, right = partition(array, pivot)

    if len(left) == key:
        return left
    if len(left) < key <= len(left) + len(middle):
        return middle
    if len(left) > key:
        return top_key(left, key)

    return top_key(right, key - len(left) - len(middle))


def median(array):
    result_list = top_key(array, len(array) // 2 + 1)
    return max(result_list)


SIZE = 4
LIMIT = 100
data = [random.randrange(0, LIMIT) for _ in range(2 * SIZE + 1)]
print(data)
print(f'Медиана = {median(data)}')
print(data)
print(sorted(data))


# Альтернативный вариант
print(f'\nАльтернативный вариант')
data = [random.randrange(0, LIMIT) for _ in range(2 * SIZE + 1)]
print(data)
print(f'Медиана = {statistics.median(data)}')
print(sorted(data))
