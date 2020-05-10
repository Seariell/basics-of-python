# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию ​ type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [123, 128.5, complex(1, 6), 'qwer', [1, 2], (3, 4), {'q', 'w', 8}, {1: 'один', 2: 'два'}, True, b'qwerty',
           None, ZeroDivisionError]

for item in my_list:
    print(f'Type of {item} is {type(item)}')