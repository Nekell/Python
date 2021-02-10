"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(first: int, second: int, third: int) -> int:
    numbers = [first, second, third]
    numbers.remove(min(numbers))
    return sum(numbers)


a, b, c = (int(number) for number in input('Enter 3 numbers separated by spaces: ').split())
print(f'Sum of the two largest arguments: {my_func(a, b, c)}')
