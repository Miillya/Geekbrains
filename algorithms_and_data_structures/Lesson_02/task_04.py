# Задание №4
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
previous_number = 1*(-2)
next_number = 0
step = -0.5
summa = 0

if n > 0:

    while n > 0:
        n -= 1
        next_number = previous_number * step
        summa += next_number
        previous_number = next_number

    print(f'Сумма всех элементов ряда чисел: {summa}')

elif n == 0:

    print('Сумма всех элементов ряда чисел равна нулю.')

else:
    print('Число должно быть положительным или равным нулю.')
