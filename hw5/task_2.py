# homework lesson: 5, task: 2
"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open('task_2.txt') as my_file:
    lines = my_file.readlines()
    num_lines = len(lines)
    words = []
    for ind, line in enumerate(lines):
        # print(f'{ind} {line}')
        words.append([f'Строка {ind + 1}', f'{len(line.split(" "))} слов(а)'])
    print(f'Файл содержит: {num_lines} строк')
    for itm in words:
        print(f'{itm[0]} содержит: {itm[1]}')
