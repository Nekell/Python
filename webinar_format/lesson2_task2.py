"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
another_list = input('Enter a number of elements separated by a space: ').split()
for i in range(0, len(another_list) - 1, 2):
    another_list[i], another_list[i + 1] = another_list[i + 1], another_list[i]
print(another_list)
