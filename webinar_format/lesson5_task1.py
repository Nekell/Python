"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('files/l5_t1.txt', 'w', encoding='UTF-8') as file:
    while True:
        s = input('Enter data. Or press Enter to end the recording: ')
        if s == '':
            break
        file.write(f'{s}\n')
