def fact(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


for el in fact(int(input('Факториал какого числа получить? '))):
    print(el)
