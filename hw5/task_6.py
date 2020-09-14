# homework lesson: 5, task: 6
"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def my_int(string: str) -> int:
    """
    Приведение строки типа 123qwerty к числу 123.

    :param string: str
    :return: int
    """
    result = ['0']
    for letter in string:
        if letter.isdigit():
            result.append(letter)
        else:
            break
    result = ''.join(result)
    return int(result)


with open('task_6.txt') as file:
    subjects = {}
    for line in file:
        line = line.split()
        key = line[0][0:-1]
        value = 0
        for word in line[1:-1]:
            value += my_int(word)
        subjects.update({key: value})
    print(subjects)
