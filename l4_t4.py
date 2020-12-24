def no_repetitions(some_list):
    numbers_counter = {number: some_list.count(number) for number in some_list}
    for number in some_list:
        if numbers_counter[number] == 1:
            yield number


input_list = list(map(int, input('Введите числа для списка через пробел: ').split()))
print(input_list)
new_list = [number for number in no_repetitions(input_list)]
print(new_list)
