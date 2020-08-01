# homework lesson: 4, task: 4
"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


my_list = [itm for itm in range(100, 1001) if not itm % 2]
mult = reduce(lambda a, b: a * b, my_list)
print(my_list)
print(mult)