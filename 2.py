# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# то могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from random import randint
from abc import abstractmethod


class Clothes:

    @abstractmethod
    def expense_cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f'пальто {self.size}раз.'
    @property
    def size (self):
        return self.__size

    @size.setter
    def size (self, size):
        if size > 60:
            self.__size = 60
        elif size < 30:
            self.__size = 30
        else:
            self.__size = size

    def expense_cloth(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    def __str__(self):
        return f'костюм {self.height}см.'

    @property
    def height (self):
        return self.__height

    @height.setter
    def height (self, height):
        if height >= 210:
            self.__height = 210
        elif height <= 140:
            self.__height = 140
        else:
            self.__height = height

    def expense_cloth(self):
        return round(2 * self.height / 100 + 0.3, 2)


summa = 0
list_coat = [Coat(randint(25,65)) for i in range(5)]
list_suit = [Suit(randint(135,215)) for i in range(5)]
list = list_coat + list_suit
for el in list:
    print(el, end = '\t')
    summa += el.expense_cloth()
    print(el.expense_cloth())
print(f'\nРасход ткани на пошив 5 костюмов и 5 пальто = {round(summa, 2)}')
