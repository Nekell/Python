def division(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на 0!')
        return


dividend, divisor = (int(number) for number in input('Введите делимое и делитель через пробел: ').split())
print(division(dividend, divisor))
