another_list = input('Введите некоторое количество элементов: ').split()
for i in range(0, len(another_list) - 1, 2):
    another_list[i], another_list[i+1] = another_list[i+1], another_list[i]
print(another_list)
