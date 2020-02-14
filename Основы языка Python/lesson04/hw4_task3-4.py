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


def attack(unit, target):
    unit['health'] -= target['damage'] // unit['armor']
    return unit['health']


def damage(unit, target):
    unit = target['damage'] // unit['armor']
    return unit

player_name = input('Введите имя Вашего персонажа: ')
player = {
    'name': player_name,
    'health': 175,
    'damage': 55,
    'armor': 1.8
}

enemy_name = input('Введите имя Вашего противника: ')
enemy = {
    'name': enemy_name,
    'health': 100,
    'damage': 75,
    'armor': 1.9
}

count = 0

while player['health'] > 0 or enemy['health'] > 0:
    count += 1
    player_dmg = damage(enemy, player)
    enemy_dmg = damage(player, enemy)
    player['health'] = attack(player, enemy)
    player_battle_info = f'Игрок {player["name"]} получил {enemy_dmg} урона, осталось {player["health"]} здоровья'
    enemy_battle_info = f'Игрок {enemy["name"]} получил {player_dmg} урона, осталось {enemy["health"]} здоровья'
    round_info = f'Раунд {count}'

    if player['health'] < 0:
        print(round_info)
        print(player_battle_info)
        print(f'{enemy["name"]} победил!')
        break
    enemy['health'] = attack(enemy, player)
    if enemy['health'] < 0:
        print(round_info)
        print(enemy_battle_info)
        print(f'{player["name"]} победил!')
        break
    print(round_info)
    print(player_battle_info)
    print(enemy_battle_info)
