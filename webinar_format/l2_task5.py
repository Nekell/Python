my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг: {my_list}')
newbie = int(input('Введите новый элемент рейтинга: '))
for i in range(1, len(my_list)):
    if newbie <= min(my_list):
        my_list.append(newbie)
        break
    elif newbie >= max(my_list):
        my_list.insert(0, newbie)
        break
    elif my_list[i - 1] >= newbie >= my_list[i]:
        my_list.insert(i, newbie)
        break
print(f'Новый рейтинг: {my_list}')
