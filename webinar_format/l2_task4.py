and_another_list = input('Введите слова через пробел: ').split()
for i, word in enumerate(and_another_list):
    print(f'{i+1}: {word[:10]}')
