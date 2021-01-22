import random
number = random.randit(1, 100)
while True:
    user_number = int(input("Угадайте число от 1 до 100: "))
    if user_number == number:
        print("Верно!")
    elif user_number < number:
        print("Ваше число меньше загаданного")
    else:
        print("Ваше число больше загаданного")
