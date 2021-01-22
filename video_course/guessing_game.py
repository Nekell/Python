import random

number = random.randit(1, 100)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input("Выберите уровнь сложности 1-3: "))
max_count = levels[level]

while user_number != number:
    count += 1
    if count > max_count
        print("Вы проиграли")
        break
    print(f"Попытка №{count}")
    user_number = int(input("Угадайте число от 1 до 100: "))
    if user_number < number:
        print("Ваше число меньше загаданного")
    elif user_number > number:
        print("Ваше число больше загаданного")
else:
    print("Победа!")
