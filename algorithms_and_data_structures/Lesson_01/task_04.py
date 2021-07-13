# Задание №4
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

first_char = ord(input('1-я буква: '))
second_char = ord(input('2-я буква: '))
first = first_char - ord('a') + 1
second = second_char - ord('a') + 1
print(f'Порядковый номер 1-й буквы = {first}, 2-й = {second}')
print(f'Число букв между введёнными: {abs(first - second) - 1}')
