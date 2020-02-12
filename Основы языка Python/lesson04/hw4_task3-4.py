# Тема 4. Функции.
#
# 3. Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
#

def attack(p1, p2):
    p1['health'] = p1['health'] - p2['damage'] // p1['armor']
    return p1['health']


player = {'name': '', 'health': 150, 'damage': 50, 'armor': 1.4}
enemy = {'name': '', 'health': 100, 'damage': 75, 'armor': 1.7}

player['name'] = input('Введите имя Вашего персонажа: ')
enemy['name'] = input('Введите имя Вашего противника: ')

count = 0

while player['health'] > 0 or enemy['health'] > 0:
    count += 1
    player['health'] = attack(player, enemy)
    if player['health'] < 0:
        print(player)
        print(f'{enemy["name"]} победил!')
        break
    enemy['health'] = attack(enemy, player)
    if enemy['health'] < 0:
        print(enemy)
        print(f'{player["name"]} победил!')
        break
    print(player)
    print(enemy)
