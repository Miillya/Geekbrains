# Тема 4. Функции.
#
# 2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
#

def max_number():
    list_number = []
    for i in range(3):
        number = int(input(f'Введите {i+1} число: '))
        list_number.append(number)
    return max(list_number)
print(f'Наибольшее число: {max_number()}')
