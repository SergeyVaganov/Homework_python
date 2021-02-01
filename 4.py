# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Warehouse:

    def __init__(self):
        self.warehouse = {}


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
