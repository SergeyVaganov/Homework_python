# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
class Warehouse:

    def __init__(self):
        self.warehouse = {}

    def add(self, equipment, volume):
        if not (equipment.__class__.__name__ in self.warehouse.keys()):
            self.warehouse[equipment.__class__.__name__] = {}
        if (equipment.name in self.warehouse[equipment.__class__.__name__].keys()):
            self.warehouse[equipment.__class__.__name__][equipment.name] = \
                self.warehouse[equipment.__class__.__name__][equipment.name] + volume
        else:
            self.warehouse[equipment.__class__.__name__][equipment.name] = volume

    def sub(self, equipment, volume):
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
            print('Ошибка наименования')
        except ExceptionValue:
            print('Ошибка количества')


class ExceptionValue(Exception):

    def __init__(self, txt):
        self.txt = txt


class Officequipment:

    def __init__(self, name, massa, price):
        self.name = name
        self.massa = massa
        self.price = price


class Printer(Officequipment):

    def __init__(self, name, massa, price, speed_print, color):
        Officequipment.__init__(self, name, massa, price)
        self.speed_print = speed_print
        self.color = color


class Scanner(Officequipment):

    def __init__(self, name, massa, price, speed_scaning, permission_scanning):
        Officequipment.__init__(self, name, massa, price)
        self.speed_scaning = speed_scaning
        self.permission_scanning = permission_scanning


class Copier(Officequipment):

    def __init__(self, name, massa, price, speed_copy, quantity_copy):
        Officequipment.__init__(self, name, massa, price)
        self.speed_copy = speed_copy
        self.quantity_copy = quantity_copy


