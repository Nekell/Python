number = input('Введите целое положительное число: ')
numeral = 0
i = 0
while i != len(number):
    if int(number[i]) > numeral:
        numeral = int(number[i])
    i += 1
print(f'Самая большая цифра в числе: {numeral}')
