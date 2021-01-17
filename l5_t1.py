with open('files/l5_t1.txt', 'w', encoding='UTF-8') as file:
    while True:
        s = input('Введите данные. Для завершения ввода нажмите Enter: ')
        if s == '':
            break
        file.write(f'{s}\n')
