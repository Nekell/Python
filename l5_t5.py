some_file = 'files/l5_t5.txt'
with open(some_file, 'w', encoding='UTF-8') as file:
    numbers = input('Введите числа через пробел: ')
    file.write(numbers)

with open(some_file, 'r', encoding='UTF-8') as file:
    numbers_string = file.read()
    print(sum([float(number) for number in numbers_string.split()]))
