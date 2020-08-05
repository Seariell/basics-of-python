# homework lesson: 5, task: 1
"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


with open('task_1.txt', 'w') as my_file:
    end = False
    while not end:
        new_string = input("Введите сторку. Для завершения введите пустую строку. \n")
        if new_string:
            my_file.write(new_string + '\n')
        else:
            end = True
