# homework lesson: 4, task: 2
"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_gen = (list[i] for i in range(1, len(list)) if list[i] > list[i-1])

print(list)
print(list_gen)
new_list = []
for itm in list_gen:
    new_list.append(itm)
print(new_list)
