"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_func(a: float, b: int):
    res = 1
    for i in range(abs(b)):
        res *= a
    return a ** b, 1 / res
    # also we can use pow()


x = float(input('Enter a valid positive number: '))
y = int(input('Enter a negative integer: '))
print(f'x to the power of y is: {my_func(x, y)}')
