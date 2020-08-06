# homework lesson: 6, task: 5
"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')


class Pencil(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')


class Handle(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')


brush = Stationery('Фигурная кисть')
brush.draw()
my_pen = Pen('0.3')
my_pen.draw()
my_pencil = Pencil('2B')
my_pencil.draw()
my_handle = Handle('желтый')
my_handle.draw()