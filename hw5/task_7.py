# homework lesson: 5, task: 7
"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
from json import dump


def profit(revenue: int, expenses: int) -> int:
    """
    Расчет прибыли/убытка

    :param revenue: int
    :param expenses: int
    :return: int
    """
    return revenue - expenses


with open('task_7.txt') as file:
    firms_profit = {}
    ave_profit = {'average_profit': 0}
    count_prof = 0
    for line in file:
        line = line.split()
        firm = line[0]
        prof = profit(int(line[2]), int(line[3]))
        firms_profit.update({firm: prof})
        if prof > 0:
            count_prof += 1
            ave_profit['average_profit'] += prof
    ave_profit['average_profit'] /= count_prof
    ave_profit['average_profit'] = round(ave_profit['average_profit'])

firms_list = [firms_profit, ave_profit]


with open('task_7.json', 'w') as json_file:
    dump(firms_list, json_file)
