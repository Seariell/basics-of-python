# homework lesson: 5, task: 4
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""


# соварь перевода
translation = {'One': 'Один',
               'Two': 'Два',
               'Three': 'Три',
               'Four': 'Четыре',
               }


with open('task_4.txt') as file_en:
    with open('task_4_1.txt', 'w') as file_ru:
        for line in file_en:
            line = line.split()
            line[0] = translation[line[0]]
            line = ' '.join(line)
            file_ru.write(line + '\n')
