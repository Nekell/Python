def numbers_in_order(some_list):
    for i in range(1, len(some_list)):
        if some_list[i] > some_list[i - 1]:
            yield some_list[i]


input_list = input('Введите числа для списка через пробел: ').split()
input_list = list(map(int, input_list))
print(input_list)
new_list = [number for number in numbers_in_order(input_list)]
print(new_list)
