# Тема 4. Функции.
#
# Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них
# информацию. И получить объект: словарь из предыдущего задания.
import pickle
import json
# import yaml

# Pickle
with open('group.pickle', 'rb') as f:
    mf_group_pickle = pickle.load(f)

print(f'Pickle:\n{mf_group_pickle}')
print(type(mf_group_pickle))

# JSON
with open('group.json', 'r') as f:
    mf_group_json = json.load(f)

print(f'JSON:\n{mf_group_json}')
print(type(mf_group_json))

# Manual
with open('group.txt', 'r', encoding='utf-8') as f:
    mf_group_txt = f.readlines()

print(f'Manual:\n{mf_group_txt}')
print(type(mf_group_txt))

# # YAML
# with open('group.yaml') as f:
#     mf_group_yaml = yaml.safe_load(f)
#
# print(f'YAML:\n{mf_group_yaml}')
# print(type(mf_group_yaml))
