def my_func(a: float, b: int):
    res = 1
    for i in range(abs(b)):
        res *= a
    return a ** b, 1 / res


x = int(input('Введите целое отрицательное число: '))
y = float(input('Введите действительное положительное число: '))
print(f'x в степени y равно: {my_func(y, x)}')
