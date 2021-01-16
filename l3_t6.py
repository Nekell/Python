def capitalize_func(text: str):
    def int_func(word: str):
        return f'{word[0].upper()}{word[1:]}'
    words = text.split()
    return ' '.join(list(map(lambda word: int_func(word), words)))


print(capitalize_func(input('Введите текст: ')))
