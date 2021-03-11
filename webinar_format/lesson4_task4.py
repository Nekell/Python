"""
4. Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


def no_repetitions(some_list):
    numbers_counter = {number: some_list.count(number) for number in some_list}
    for number in some_list:
        if numbers_counter[number] == 1:
            yield number


input_list = list(map(int, input('Enter numbers for the list, separated by a space: ').split()))
print(input_list)
new_list = [number for number in no_repetitions(input_list)]
print(new_list)
