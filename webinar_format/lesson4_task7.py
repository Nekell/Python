"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""


def fact(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


for el in fact(int(input('What number is the factorial to get? '))):
    print(el)