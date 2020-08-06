# homework lesson: 6, task: 1
"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        colors = {'красный': 7,
                  'желтый': 2,
                  'зеленый': 7,
                  }
        count = 0
        for color in cycle(colors.keys()):
            self.__color = color
            print(f'Цвет светофора: {self.__color}')
            sleep(colors.get(self.__color))
            count += 1
            if count == 5:
                break

    def running2(self):
        colors = {'красный': 7,
                  'желтый': 2,
                  'зеленый': 5,
                  }
        order_colors = list(colors.keys())
        print(order_colors)
        count = 0
        for color in cycle(colors.keys()):
            prev_color = self.__color
            self.__color = color
            if not prev_color:
                pass
            elif order_colors[order_colors.index(self.__color) - 1] != prev_color:
                print('Ошибка')
                break

            print(f'Цвет светофора: {self.__color}')
            sleep(colors.get(self.__color))

            count += 1
            if count == 5:
                break


crossing = TrafficLight()
crossing.running2()
