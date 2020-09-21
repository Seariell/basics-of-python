# homework lesson: 7, task: 2
"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC
from abc import abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size: int, name: str):
        self.size = size
        self.name = name

    @property
    def fabric_consumption(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height, name):
        self.height = height
        self.name = name

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


class Store(Clothes):
    def __init__(self):
        self._store = []

    def add_clothes_to_store(self, stuff):
        self._store.append(stuff)

    @property
    def fabric_consumption(self):
        result = 0
        for itm in self._store:
            result += itm.fabric_consumption
        return result


violetta = Coat(48, 'Mango')
briks = Suit(1.76, 'lamoda')
wardrobe = Store()
wardrobe.add_clothes_to_store(violetta)
wardrobe.add_clothes_to_store(briks)
print(violetta.fabric_consumption)
print(briks.fabric_consumption)
print(wardrobe.fabric_consumption)
