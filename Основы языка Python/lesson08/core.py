# Тема 8. Практикум file manager.
"""
1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами (на уроке
разбирали на примере одной функции).
2. Добавить возможность изменения текущей рабочей директории.
3. Добавить возможность развлечения в процессе работы с менеджером. Для этого добавить в менеджер запуск одной из игр:
 “угадай число” или “угадай число (наоборот)”.
"""

import os
# import sys
import shutil
import datetime


# print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <name> - создание директории')
    print('create_file <name> - создание директории')
    print('get_list <False/True> - список файлов и директорий в папке')
    print('cp <name, new_name> - создает копию директории')
    print('cpf <name, new_name> - создает копию файла')
    print('rm <name> - удаляет указанный файл или директорию')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('game - запуск игры')


def make_dir(name):
    if not name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print(f'Директория {dir_path} создана')
    except FileExistsError:
        print(f'Директория {dir_path} уже существует')


def create_file(name, text=None):
    if not name:
        print('Необходимо указать имя файла вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), name)
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
    print(f'Файл {dir_path} создан')


def get_list(folders_only=False):
    dir_path = os.path.join(os.getcwd())
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(f'Путь директории:\n{dir_path}\nСодержимое директории:\n{result}')


def copy_folder(name, new_name):
    if not name:
        print('Необходимо указать имя вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), new_name)
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
            print(f'Копия - {dir_path} директории {name} создана')
        except FileExistsError:
            print(f'Директория {dir_path} уже существует')
    else:
        print(f'Директория {name} не существует, создать автоматически?')
        answer = input(f'1 - создать директорию 2 - отмена операции: ')
        if answer == '1':
            make_dir(name)
            copy_file(name, new_name)
        else:
            print('Ошибка ввода / Отмена операции!')


def copy_file(name, new_name):
    if not name:
        print('Необходимо указать имя вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), new_name)
    if os.path.isfile(name):
        try:
            shutil.copy(name, new_name)
            print(f'Копия - {dir_path} файла {name} создана')
        except FileExistsError:
            print(f'Директория {dir_path} уже существует')
    else:
        print(f'Файл {name} не существует, создать автоматически?')
        answer = input(f'1 - создать файл 2 - отмена операции: ')
        if answer == '1':
            create_file(name, text=None)
            copy_file(name, new_name)
        else:
            print('Ошибка ввода / Отмена операции!')


def remove_file(name):
    if not name:
        print('Необходимо указать имя файла вторым параметром')
        return
    file_path = os.path.join(os.getcwd(), name)
    if os.path.isdir(name):
        try:
            os.rmdir(file_path)
            print(f'Директория {name} удалена')
        except FileNotFoundError:
            print(f'Директория {name} не существует')
    else:
        try:
            os.remove(file_path)
            print(f'Файл {name} удалён')
        except FileNotFoundError:
            print(f'Файл {name} не существует')


def change_dir(name):
    if not name:
        print("Необходимо указать имя вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.chdir(dir_path)
        print(f'Вы перешли в директорию {dir_path}')
    except FileNotFoundError:
        print(f'Директория {dir_path} не существует')


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')
