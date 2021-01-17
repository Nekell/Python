numbers_en_to_ru = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
with open('files/l5_t4_English.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    ru_lines = [f'{numbers_en_to_ru[line.split(" - ")[0]]} - {line.split(" - ")[1]}' for line in lines]
with open('files/l5_t4_Russian.txt', 'w', encoding='UTF-8') as file:
    file.writelines(ru_lines)
