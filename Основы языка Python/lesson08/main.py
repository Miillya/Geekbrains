# Тема 8. Практикум file manager.
"""
1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами (на уроке
разбирали на примере одной функции).
2. Добавить возможность изменения текущей рабочей директории.
3. Добавить возможность развлечения в процессе работы с менеджером. Для этого добавить в менеджер запуск одной из игр:
 “угадай число” или “угадай число (наоборот)”.
"""
# import os
import sys
from core import print_help, make_dir, create_file, get_list, copy_folder, copy_file, remove_file, change_dir, save_info
from guess_the_number import guess_the_number

save_info('Начало')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду')
else:
    if command == 'help':
        print_help()
    elif command == 'mkdir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсуствует название директории')
        else:
            make_dir(name)
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсуствует название файла')
        else:
            create_file(name)
    elif command == 'get_list':
        try:
            folders_only = sys.argv[2]
        except IndexError:
            get_list()  # только папки
        else:
            print(folders_only)
            if folders_only == '0' or folders_only == 'False' or folders_only == 'false' or folders_only == ' ':
                get_list()
            else:
                get_list(True)  # файлы и папки
    elif command == 'cp':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Введите имя копируемой и новой директории')
        else:
            copy_folder(name, new_name)
    elif command == 'cpf':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Введите имя копируемого и нового файла')
        else:
            copy_file(name, new_name)
    elif command == 'rm':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсуствует название директории или файла')
        else:
            remove_file(name)
    elif command == 'cd':
        change_dir()
    elif command == 'game':
        guess_the_number()

save_info('Конец')
