income = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if income > costs:
    profit = (income - costs) / income
    print(f'Фирма приносит прибыль! Рентабельность выручки {round(profit, 2)}')
    staff = int(input('Введите количество сотрудников фирмы: '))
    margin = profit / staff
    print(f'Прибыль фирмы в расчете на одного сотрудника: {round(margin, 2)}')
elif income < costs:
    print('Фирма работает в убыток!')
else:
    print('Доходы равны расходам.')
