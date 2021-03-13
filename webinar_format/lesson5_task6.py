"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


with open('files/l5_t6.txt',  'r', encoding='UTF-8') as file:
    lines = file.readlines()
    school_dict = {}
    for line in lines:
        subj_info_list = line.split()
        subj_name = subj_info_list[0]
        subj_qnt = 0
        for elem in subj_info_list:
            if is_int(elem):
                subj_qnt += int(elem)
        school_dict.update({subj_name: subj_qnt})
    print(school_dict)
