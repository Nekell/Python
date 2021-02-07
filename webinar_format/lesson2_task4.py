"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
and_another_list = input('Enter words separated by space: ').split()
for i, word in enumerate(and_another_list):
    print(f'{i + 1}: {word[:10]}')
