def total():
    numbers = []
    while True:
        string = input('Введите числа через пробел: ')
        new_numbers = string.split()
        for digit in new_numbers:
            if digit == 'q':
                print(sum(numbers))
                return
            else:
                numbers.append(int(digit))
        print(sum(numbers))


total()
