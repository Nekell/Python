from itertools import count, cycle
start = int(input('Введите число, с которого нужно начать генерацию: '))
end = int(input('Введите число, на котором следует остановиться: '))
counter = count(start)
for i in range(start, end + 1):
    print(next(counter))

list_cycle = cycle(list(map(int, input('Введите числа для списка через пробел: ').split())))
action = None
print('q - для выхода, Enter - для продолжения')
while action != 'q':
    print(next(list_cycle), end='')
    action = input()
