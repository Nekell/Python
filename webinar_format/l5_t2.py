with open('files/l5_t2.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(f'Количество строк в файле: {len(lines)}')
    for i, line in enumerate(lines):
        print(f'Количество слов в {i+1} строке: {len(line.split())}')
