# homework lesson: 4, task: 4
"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
повторение элементов списка будет прекращено.
"""
from sys import argv
from itertools import count
from itertools import cycle


def lets_count(first_number: int) -> None:
    """
    Посчитать 10 раз с указанного числа

    :param first_number:
    :return: None
    """
    for number in count(first_number):
        if number > first_number + 10:
            return
        else:
            print(number)
    return


def lets_cycle(some_list: list) -> None:
    """
    Повтор эл-тов списка some_list по кругу 10 раз

    :param some_list: list
    :return: None
    """
    c = 0
    for itm in cycle(some_list):
        if c > 10:
            return
        print(itm)
        c += 1
    return


my_list = list('Првет!')
try:
    script = argv[1]
    if script == 'count':
        my_iter = int(argv[2])
        lets_count(my_iter)

    elif script == 'cycle':
        lets_cycle(my_list)
    else:
        print('Неверные значения')
except ValueError:
    print('Ошибка: неверный формат')
