"""
1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
"""
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
for number in my_list_1[:]:
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)
