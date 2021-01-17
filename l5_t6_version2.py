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
