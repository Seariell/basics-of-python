# homework lesson: 5, task: 5
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint


with open('task_5.txt', 'w') as file:
    my_sum = 0
    for i in range(randint(0, 30)):
        number = randint(0, 30)
        file.write(f'{number} ')
        my_sum += number
    print(my_sum)
