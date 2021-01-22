# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина едет")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        return self.speed if self.speed < 60 else "Скорость превышает 60 км/ч"


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        return self.speed if self.speed < 40 else "Скорость превышает 40 км/ч"


class PoliceCar(Car):
    pass


p = PoliceCar(100, 'white', 'ford', True)
t = TownCar(90, 'black', 'lada', False)
s = SportCar(300, 'red', 'ferrari', False)
w = WorkCar(30, 'yellow', 'кран', False)
listCars = [p, t, s, w]
for el in listCars:
    print(f'Атрибуты класса - {type(el)}:\n '
          f'автомобиль: скорость -  {el.speed}, цвет  - {el.color}, '
          f'марка -  {el.name}, полицейский -  {el.is_police}')
    print(f"скорость = {el.show_speed()}")
