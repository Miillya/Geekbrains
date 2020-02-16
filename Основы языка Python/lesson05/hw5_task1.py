# 1. Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую
# директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти
# папки. Проверьте работу функций в этом же модуле.
import os

name = 'dir'


# Функция создания директории:
def create_dir():
    i = 1
    while i < 10:
        dir_name = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        i += 1
        try:
            os.mkdir(dir_name)
            print('Директория', dir_name, 'создана!')
        except FileExistsError:
            print('Директория', dir_name, 'уже существует')


def delete_dir():
    i = 1
    while i < 10:
        dir_name = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
        i += 1
        try:
            os.rmdir(dir_name)
            print('Директория', dir_name, 'удалена!')
        except FileNotFoundError:
            print('Директории', dir_name, 'не существует')


if __name__ == '__main__':
    create_dir()
    delete_dir()
