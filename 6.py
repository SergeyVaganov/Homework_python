# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class Warehouse:

    def __init__(self):
        self.warehouse = {}

    def add(self, equipment, vol):
        volume = Validator.valid(vol, 100, 0)
        if not (equipment.__class__.__name__ in self.warehouse.keys()):
            self.warehouse[equipment.__class__.__name__] = {}
        if (equipment.name in self.warehouse[equipment.__class__.__name__].keys()):
            self.warehouse[equipment.__class__.__name__][equipment.name] = \
                self.warehouse[equipment.__class__.__name__][equipment.name] + volume
        else:
            self.warehouse[equipment.__class__.__name__][equipment.name] = volume

    def sub(self, equipment, vol):
        volume = Validator.valid(vol,100, 0)
        try:
            quantity = self.warehouse[equipment.__class__.__name__][equipment.name]
            if volume > quantity:
                raise ExceptionValue('Нет такого количества на складе')
            elif volume == quantity:
                del self.warehouse[equipment.__class__.__name__][equipment.name]
            else:
                self.warehouse[equipment.__class__.__name__][equipment.name] = \
                self.warehouse[equipment.__class__.__name__][equipment.name] - volume
        except KeyError:
            print('На складе нет оборудования с таким наименованием')
        except ExceptionValue as ex:
            print(ex.txt)


class Validator:

    @staticmethod
    def valid(param, max_num, min_num):
        try:
            parametr = int(param)
            if not (min_num < parametr < max_num):
                raise ExceptionValue('Параметр выходит за ожидаемый диапазон')
            return parametr
        except ValueError:
            raise ExceptionValue('Параметр не целое число')



class ExceptionValue(Exception):

    def __init__(self, txt):
        self.txt = txt


class Officequipment:

    def __init__(self, name, massa, price):
        self.name = name
        self.massa = massa
        self.price = price

    @property
    def massa(self):
        return self.__massa

    @massa.setter
    def massa(self, mas):
        try:
            massa = round(float(mas),2)
            if (massa < 0 or massa > 200):
                raise ExceptionValue('Масса выходит за рамки доступного диапазона')
            self.__massa = massa
        except ValueError:
            self.__massa = 0
            print('Масса должна быть числом')
        except ExceptionValue as ex:
            self.__massa = 0
            print(ex.txt)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, num):
        try:
            price = round(float(num),2)
            if price < 0:
                raise ExceptionValue('Масса выходит за рамки доступного диапазона')
            self.__price = price
        except ValueError:
            self.__price = 0
            print('Масса должна быть числом')
        except ExceptionValue as ex:
            self.__price = 0
            print(ex.txt)


class Printer(Officequipment):

    def __init__(self, name, massa, price, speed_print, color):
        Officequipment.__init__(self, name, massa, price)
        self.speed_print = speed_print
        self.color = color

    @property
    def speed_print(self):
        return self.__massa

    @speed_print.setter
    def speed_print(self, speed):
        try:
            speed_int = int(speed)
            if (speed_int < 0 or speed_int > 50):
                raise ExceptionValue('Скорость печати указана не корректно')
            self.__speed_print = speed_int
        except ValueError:
            self.__speed_print = 0
            print('Скорость печати должна быть целым число')
        except ExceptionValue as ex:
            self.__speed_print = 0
            print(ex.txt)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, is_color):
        try:
            if is_color != 'цветной' and is_color !='черно-белый':
                raise ExceptionValue('Принтер может быть только цветной или черно-белый')
            self.__color = is_color
        except ExceptionValue as ex:
            self.__color = 'не указан'
            print(ex.txt)


class Scanner(Officequipment):

    def __init__(self, name, massa, price, speed_scaning, permission_scanning):
        Officequipment.__init__(self, name, massa, price)
        self.speed_scaning = speed_scaning
        self.permission_scanning = permission_scanning

    @property
    def speed_scaning(self):
        return self.__massa

    @speed_scaning.setter
    def speed_scaning(self, speed):
        try:
            speed_int = int(speed)
            if (speed_int < 0 or speed_int > 5):
                raise ExceptionValue('Скорость сканирования указана не корректно')
            self.__speed_scaning = speed_int
        except ValueError:
            self.__speed_scaning = 0
            print('Скорость печати должна быть целым число')
        except ExceptionValue as ex:
            self.__speed_scaning = 0
            print(ex.txt)

    @property
    def permission_scanning(self):
        return self.__massa

    @permission_scanning.setter
    def permission_scanning(self, permission):
        try:
            permission_scanning = int(permission)
            if (permission_scanning < 50 or permission_scanning > 800):
                raise ExceptionValue('Разрешение сканирования указана не корректно')
            self.__speed_scaning = permission_scanning
        except ValueError:
            self.__speed_scaning = 0
            print('Разрешение печати должна быть целым число')
        except ExceptionValue as ex:
            self.__speed_scaning = 0
            print(ex.txt)


class Copier(Officequipment):

    def __init__(self, name, massa, price, speed_copy, quantity_copy):
        Officequipment.__init__(self, name, massa, price)
        self.speed_copy = speed_copy
        self.quantity_copy = quantity_copy

    @property
    def speed_copy(self):
        return self.__massa

    @speed_copy.setter
    def speed_copy(self, speed):
        try:
            speed_copy = int(speed)
            if (speed_copy < 0 or speed_copy > 500):
                raise ExceptionValue('Скорость копироваия указана не корректно')
            self.__speed_copy = speed_copy
        except ValueError:
            self.__speed_copy = 0
            print('Скорость копирования должна быть целым число')
        except ExceptionValue as ex:
            self.__speed_copy = 0
            print(ex.txt)

    @property
    def quantity_copy(self):
        return self.__massa

    @quantity_copy.setter
    def quantity_copy(self, quantity):
        try:
            quantity_copy = int(quantity)
            if (quantity_copy < 0 or quantity_copy > 5000):
                raise ExceptionValue('Количество копий указано не корректно')
            self.__quantity_copy = quantity_copy
        except ValueError:
            self.__quantity_copy = 0
            print('Скорость копирования должна быть целым число')
        except ExceptionValue as ex:
            self.__quantity_copy = 0
            print(ex.txt)


w = Warehouse()
co1 = Copier('Копир15-05', 5, 15000, 50, 150)
co2 = Copier('Копир17-05', 15, 15000, 50, 150)
co3 = Copier('Копир20-05', 15, 15000, 50, 150)

try:
    w.add(co1, 'e')
except ExceptionValue:
    print('Ошибка ввода')

w.add(co1, 7)
w.add(co2, 7)
w.add(co3, 7)
pr1 = Printer('HP-1020', 5, 5000, 10, 'цветной')
w.add(pr1, 10)
w.sub(co1, 12)
print(w.warehouse)
