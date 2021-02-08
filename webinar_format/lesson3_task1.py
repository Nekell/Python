"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        print('Division by 0!')
        return


dividend, divisor = (int(number) for number in input('Введите делимое и делитель через пробел: ').split())
print(division(dividend, divisor))
