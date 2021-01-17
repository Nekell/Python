distance = int(input('Введите число километров в первый день: '))
last_distance = int(input('Введите желаемое число километров: '))
day = 1
while distance < last_distance:
    print(f'{day}-й день: {round(distance, 2)} км')
    day += 1
    distance *= 1.1
print(f'{day}-й день: {round(distance, 2)} км')
print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {last_distance} км. ')
