# homework lesson: 2, task: 5
"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, ​ 3 ​ , 2.
Пользователь ввел число 8. Результат: ​ 8 ​ , 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, ​ 1 ​ .
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""


my_list = [7, 5, 3, 3, 2]
print(my_list)
number = input('Введие натуральное число: ')
while not number.isdigit():
    number = input('Введие натуральное число: ')
number = int(number)
if number in my_list:
    i = my_list.index(number) + my_list.count(number)
    my_list.insert(i, number)
elif number > my_list[0]:
    my_list.insert(0, number)
elif number < my_list[-1]:
    my_list.append(number)
else:
    for idx, itm in enumerate(my_list):
        if number > itm:
            my_list.insert(idx, number)
            break
print(my_list)
