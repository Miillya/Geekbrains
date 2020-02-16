# 2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]
import random

my_list1 = [11, 'Al', 14, 5, 77, 'h1', 'b', 9]
my_list2 = []


# Функция выбора случайного элемента из списка
def choice_list(my_list):
    if len(my_list) > 0:
        random_choice = random.choice(my_list)
        return f'Случайный элемент из списка: {random_choice}'
    else:
        return f'Ваш список пуст: {None}'


if __name__ == '__main__':
    print(choice_list(my_list1))
    print(choice_list(my_list2))
