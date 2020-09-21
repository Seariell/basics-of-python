# homework lesson: 7, task: 1
"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, *args: list):
        self.__strings = 0
        self.__columns = []
        self.__matrix = []
        for itm_list in args:
            self.__strings += 1
            self.__columns.append(len(itm_list))
            for itm in itm_list:
                self.__matrix.append(itm)

    def __str__(self):
        result = ''
        for string in range(self.__strings):
            for col in range(self.__columns[string]):
                idx = col
                for st in range(string):
                    idx += self.__columns[st]
                result += f'{self.__matrix[idx]} \t'
            result += f'\n'
        return result

    def __add__(self, other):
        if self.__columns == other.__columns:
            result = Matrix([])
            result.__columns = self.__columns
            result.__strings = self.__strings
            for ind in range(len(self.__matrix)):
                result.__matrix.append(self.__matrix[ind] + other.__matrix[ind])
        else:
            raise IndexError
        return result


q = Matrix([1, 2, 3], [4, 5], [6, 7, 8])
print(q)
p = Matrix([1, 1, 1], [1, 1], [1, 1, 1])
print(p+q)
