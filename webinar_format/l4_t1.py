from sys import argv
script_name, hours, rate, premium = argv
print(f'Зароботная плата сотрудникад составляет: {hours} * {rate} + {premium}'
      f'= {float(hours) * float(rate) + float(premium)}')
