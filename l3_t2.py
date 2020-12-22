def info(first_name, last_name, year_of_birth, city, email, phone):
    # return f'{last_name} {first_name}\n' \
    #        f'Дата рождения: {year_of_birth}\n' \
    #        f'Город: {city}\n' \
    #        f'Почта: {email}\n' \
    #        f'Телефон: {phone}'
    return f'{last_name} {first_name}, год рождения: {year_of_birth}, место жительства {city}. ' \
           f'Контакты: {email} , {phone} .'


print(info(
    first_name=input('Введите имя: '),
    last_name=input('Введите фамилию: '),
    year_of_birth=input('Введите год рождения: '),
    city=input('Введите город проживания: '),
    email=input('Введите email: '),
    phone=input('Введите телефон: '),
))
