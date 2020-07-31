# homework lesson: 3, task: 3
"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(number1: any, number2: any, number3: any) -> any:
    """
    Функция возвращает сумму наибольших двух аргументов из трех.

    Функция пытается вернуть сумму двух максимальных аргументов.
    Если типы аргументов не позволяют провести их сложение,
    функция возвращает строку с ошибкой.
    :param number1: any
    :param number2: any
    :param number3: any
    :return: any
    """
    numbers = [number1, number2, number3]
    try:
        numbers.remove(min(numbers))
    except TypeError:
        result = 'Ошибка. Не поддерживаемые типы данных.'
        return result
    result = numbers[0] + numbers[1]
    return result


print(my_func(12, 7, 90))
