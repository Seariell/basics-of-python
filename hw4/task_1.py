# homework lesson: 4, task: 1
"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def salary(hours: float, rate: float) -> tuple:
    """
    Расчет зарплаты

    :param hours: flat
    :param rate: float
    :return: tuple
    """
    result = hours * rate
    premium = result * 0.1
    return result, premium

try:
    my_hours = float(argv[1])
    my_rate = float(argv[2])
    my_salary, my_premium = salary(my_hours, my_rate)
    print(f'Ваша зарплата составила: {my_salary + my_premium} руб. Включая премию в размере {my_premium} руб.')
except ValueError:
    print('Ошибка: неверный формат')
