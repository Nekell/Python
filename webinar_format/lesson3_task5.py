"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


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