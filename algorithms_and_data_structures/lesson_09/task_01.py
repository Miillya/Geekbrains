# Задание №1
# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
# вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.

import hashlib


def count_substring(str_val):
    subs = set()

    for i in range(1, len(str_val)):
        for j in range(len(str_val) - i + 1):
            h_sub = hashlib.sha1(str_val[j:j+i].encode('utf-8')).hexdigest()
            subs.add(h_sub)

    return len(subs)


my_str = input('Введите строку: ')
print(f'Количество подтсрок: {count_substring(my_str)}')
