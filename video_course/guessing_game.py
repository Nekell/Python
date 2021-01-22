import random
number = random.randit(1, 100)
user_number = None
while user_number =! number:
    user_number = int(input("Угадайте число от 1 до 100: "))
    if user_number < number:
        print("Ваше число меньше загаданного")
    elif user_number > number:
        print("Ваше число больше загаданного")
print("Верно!")
