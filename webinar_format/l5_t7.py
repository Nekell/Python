import json

with open('files/l5_t7.txt', 'r', encoding='UTF-8') as file:
    income_sum = 0
    res = {}
    lines = file.readlines()
    for line in lines:
        name, form, gain, outcome = line.split()
        income = float(gain) - float(outcome)
        res[name] = income
        if income > 0:
            income_sum += income

res['average_income'] = round(income_sum / len(lines), 2)

with open('files/l5_t7.json', 'w', encoding='UTF-8') as file:
    json.dump(res, file)
