def my_func(first: int, second: int, third: int) -> int:
    numbers = [first, second, third]
    numbers.remove(min(numbers))
    return sum(numbers)


a, b, c = (int(number) for number in input('Введите 3 числа через пробел: ').split())
print(f'Сумма наибольших двух аргументов: {my_func(a, b, c)}')
