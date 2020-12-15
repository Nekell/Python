seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
minutes = seconds % 3600 // 60
remaining_seconds = seconds % 3600 % 60
print(f'Время: {hours:02}:{minutes:02}:{remaining_seconds:02}')
