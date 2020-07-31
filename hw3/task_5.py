# homework lesson: 3, task: 5
"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""


def sum_of_string(*args: str) -> tuple:
    """
    Сумма введенных чисел и проверка на спец символ завершения.

    :param args: str
    :return: tuple
    """
    sum_of_num = 0
    flag_of_end = False
    for itm in args:
        if itm == "q":
            flag_of_end = True
            return sum_of_num, flag_of_end
        else:
            try:
                sum_of_num += float(itm)
            except ValueError:
                print('Неверный тип данных')
                return 0, flag_of_end
    return sum_of_num, flag_of_end


my_sum = 0
end = False
while not end:
    my_string = input('Введите числа через пробел. Для завершения введите q\n')
    result, end = sum_of_string(*my_string.split())
    my_sum += result
    print(f'Сумма ваших чисел = {my_sum}')
