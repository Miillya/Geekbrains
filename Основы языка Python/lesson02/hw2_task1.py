# 1. Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#     Примечание. Списки создайте вручную, например так:

# my_list_1 = [22, 5, 8, 2, 112, 12, 4, 209, 77]
# my_list_2 = [22, 7, 112, 3, 155, 209]
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

print(my_list_1)
print(my_list_2)

# Вариант №1
for item in my_list_2:
    if item in my_list_1:
        my_list_1.remove(item)
print(f'Вариант №1\n', my_list_1)

# Вариант №2
for next_value in my_list_2:
    while my_list_1.count(next_value)!=0:
        my_list_1.remove(next_value)
print(f'Вариант №2\n', my_list_1)