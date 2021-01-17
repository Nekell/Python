with open('files/l5_t3.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    poor_employee = []
    average_salary = 0
    for line in lines:
        employee, salary = line.split()
        salary = float(salary)
        average_salary += salary
        if salary < 20000:
            poor_employee.append(employee)

    print(f'Сотрудники с окладом меньше 20000: {poor_employee}')
    print(f'Средняя величина дохода сотрудников: {round(average_salary / len(lines), 1)}')
