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
# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

def attack(p1, p2):
    p1['health'] -= p2['damage'] // p1['armor']
    return p1['health']


def damage(p1, p2):
    p1 = p2['damage'] // p1['armor']
    return p1


player = {'name': '', 'health': 175, 'damage': 55, 'armor': 1.8}
enemy = {'name': '', 'health': 100, 'damage': 75, 'armor': 1.7}

player['name'] = input('Введите имя Вашего персонажа: ')
enemy['name'] = input('Введите имя Вашего противника: ')

count = 0

while player['health'] > 0 or enemy['health'] > 0:
    count += 1
    player_dmg = damage(enemy, player)
    enemy_dmg = damage(player, enemy)
    player['health'] = attack(player, enemy)
    if player['health'] < 0:
        print(f'Раунд {count}')
        print(f'Игрок {player["name"]}, осталось {player["health"]} здоровья')
        print(f'{enemy["name"]} победил!')
        break
    enemy['health'] = attack(enemy, player)
    if enemy['health'] < 0:
        print(f'Раунд {count}')
        print(f'Игрок {enemy["name"]}, осталось {enemy["health"]} здоровья')
        print(f'{player["name"]} победил!')
        break
    print(f'Раунд {count}')
    print(f'Игрок {player["name"]} получил {enemy_dmg} урон(а), осталось {player["health"]} здоровья')
    print(f'Игрок {enemy["name"]} получил {player_dmg} урон(а), осталось {enemy["health"]} здоровья')
