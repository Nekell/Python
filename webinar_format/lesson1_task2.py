"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
seconds = int(input('Enter the time in seconds: '))
hours = seconds // 3600
minutes = seconds % 3600 // 60
remaining_seconds = seconds % 3600 % 60
print(f'Time: {hours:02}:{minutes:02}:{remaining_seconds:02}')
