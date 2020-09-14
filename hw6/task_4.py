# homework lesson: 6, task: 4
"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
 WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
 и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self. color = color
        self. name = name
        self.is_police = is_police

    def go(self, speed: int):
        self.speed += speed
        print(f'Машина поехала со скоростью {self.speed} км/час')

    def stop(self):
        self.speed = 0
        print(f'Машина остановилась')

    def turn(self, direction: str):
        print(f'Машина повернула {direction} со скоростью {self.speed} км/час')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/час')


class TownCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/час')
        if self.speed > 60:
            print(f'Вы превысили скорость')


class SportCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)


class WorkCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/час')
        if self.speed > 40:
            print(f'Вы превысили скорость')


class PoliceCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)


my_car = TownCar('blue', 'Peugeot', True)
print(my_car.speed)
print(my_car.name)
print(my_car.color)
print(my_car.is_police)
my_car.go(70)
my_car.show_speed()
my_car.turn('налево')
my_car.stop()
my_sport_car = SportCar('red', 'Audi', False)
print(my_sport_car.speed)
print(my_sport_car.name)
print(my_sport_car.color)
print(my_sport_car.is_police)
my_sport_car.go(70)
my_sport_car.show_speed()
my_sport_car.turn('налево')
my_sport_car.stop()
work_car = WorkCar('yellow', 'Kamaz', True)
print(work_car.speed)
print(work_car.name)
print(work_car.color)
print(work_car.is_police)
work_car.go(70)
work_car.show_speed()
work_car.turn('налево')
work_car.stop()
police_car = PoliceCar('white', 'Skoda', True)
print(police_car.speed)
print(police_car.name)
print(police_car.color)
print(police_car.is_police)
police_car.go(70)
police_car.show_speed()
police_car.turn('налево')
police_car.stop()
