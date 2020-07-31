# homework lesson: 3, task: 1
"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
"""


def my_div(dividend: float, divider: float) -> float:
    """
    Функция возвращает результат деления первого числа на второе.

    Функция пытается поделить делимое на делитель и вернуть результат.
    В случае, если делитель = 0, функция возвращает описание ошибки.

    :param dividend: float
    :param divider: float
    :return float
    """
    try:
        result = dividend / divider
    except ZeroDivisionError:
        result = 'Ошибка. Деление на ноль.'
    return result


user_dividend = float(0)
user_divider = float(1)
while True:
    try:
        user_dividend = float(input("Введите делимое: "))
        user_divider = float(input("Введите делитель: "))
    except ValueError:
        print('Символы недопустимы')
        continue
    break

print(my_div(user_dividend, user_divider))
