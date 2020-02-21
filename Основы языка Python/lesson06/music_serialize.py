# Тема 6. Работа с файлами.
#
# 1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
#
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
import pickle
import json
# import yaml    # pip install pyyaml

my_favourite_group = [
    {
        'group': 'Coldplay',
        'album': 'Ghost Stories',
        'song': 'Magic',
        'year': 2014
    },
    {
        'group': 'Coldplay',
        'album': 'Parachutes',
        'song': 'Yellow',
        'year': 2000
    },
    {
        'group': 'Radiohead',
        'album': 'Karma Police',
        'song': 'Karma Police',
        'year': 1997
    },
    {
        'group': 'Сплин',
        'album': '25 кадр',
        'song': 'Линия жизни',
        'year': 2001
    }
]

# Pickle
with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

print(f'Файл group.pickle записан')

# JSON
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

print(f'Файл group.json записан')

# Manual
with open('group.txt', 'w', encoding='utf-8') as f:
    for item in my_favourite_group:
        f.write(f'{item}, ')

print(f'Файл group.txt записан')

# # YAML
# with open('group.yaml', 'w', encoding='utf-8') as f:
#     yaml.dump(my_favourite_group, f)
#
# print(f'Файл group.yaml записан')
