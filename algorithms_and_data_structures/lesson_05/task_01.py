# Задание №1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль
# ниже среднего.

from collections import namedtuple

list_co = []


def company_profit():
    count = 1
    while count <= n:

        name = input(f'\nВведите наименование предприятия: ')
        while True:
            if name in list_co:
                print('Такое предприятие уже существует!')
                return company_profit()
            else:
                list_co.append(name)
                print(f'Предприятие "{name}" успешно добавлено!\n')
                break
        count += 1

        q_1 = float(input(f'Введите прибыль предприятия {name} за 1-й квартал: '))
        q_2 = float(input(f'Введите прибыль предприятия {name} за 2-й квартал: '))
        q_3 = float(input(f'Введите прибыль предприятия {name} за 3-й квартал: '))
        q_4 = float(input(f'Введите прибыль предприятия {name} за 4-й квартал: '))

        profit = q_1 + q_2 + q_3 + q_4
        total_profit = [name, q_1, q_2, q_3, q_4, profit]

        return total_profit


while True:
    try:
        n = int(input('Введите количество предприятий: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = []
Company = namedtuple('Company', 'name q_1 q_2 q_3 q_4 profit')
average_profit = 0

for i in range(n):
    c = Company._make(company_profit())
    companies.append(c)
    average_profit += companies[i].profit / n

profitable = []
unprofitable = []

for i in range(n):

    if companies[i].profit > average_profit:
        profitable.append(companies[i].name)

    else:
        unprofitable.append(companies[i].name)

print(f'\nСредняя прибыль всех предприятий: {round(average_profit)}')

print('Прибыль выше среднего у предприятий:')
for i in range(len(profitable)):
    print(profitable[i])

print('Прибыль ниже среднего у предприятий:')
for i in range(len(unprofitable)):
    print(unprofitable[i])
