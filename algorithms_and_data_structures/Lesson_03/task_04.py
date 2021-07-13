# Задание №4
# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
SIZE = len(array)
print(array)

num = array[0]
frequency = 1
for i in range(SIZE):
    spam = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            spam += 1
    if spam > frequency:
        frequency = spam
        num = array[i]

if frequency > 1:
    print(f'Число {num} встречается {frequency} раз(а)')
else:
    print('Все элементы уникальны')
