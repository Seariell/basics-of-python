# homework lesson: 5, task: 3
"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

# извлекаем строки из файла
with open('task_3.txt') as my_file:
    salaries = my_file.readlines()


# преобразуем формат окладов
for ind, line in enumerate(salaries):
    salaries[ind] = line.split(' ')
for ind, line in enumerate(salaries):
    if '\n' in salaries[ind][1]:
        salaries[ind][1] = salaries[ind][1][0:-1]
    salaries[ind][1] = float(salaries[ind][1])


# сотрудики с окладом < 20 тыс
small_sal = []
for ind, worker in enumerate(salaries):
    if salaries[ind][1] < 20000:
        small_sal.append(worker[0])
small_sal = " ".join(small_sal)


# средний оклад
average_sal = 0
for worker in salaries:
    average_sal += worker[1]
average_sal /= len(salaries)


print(f'Сотрудники с окладом менее 20 тыс: {"".join(small_sal)}')
print(f'Средняя величина дохода сотрудникв: {average_sal}')
