# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.
class Comlex:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    @property
    def re(self):
        return self.__re

    @re.setter
    def re(self, real):
        try:
            self.__re = float(real)
        except ValueError:
            self.__re = 0
            print('Действительная часть не число')

    @property
    def im(self):
        return self.__im

    @re.setter
    def im(self, imaginary):
        try:
            self.__im = float(imaginary)
        except ValueError:
            self.__im = 0
            print('Мнимая часть не число')

    def __add__(self, other):
        return Comlex(self.__re + other.__re, self.__im + other.__im)

    def __mul__(self, other):
        return Comlex(self.__re * other.__re - self.__im * other.__im,
               self.__re * other.__im + self.__im * other.__re)

    def __str__(self):
        return f"{format(self.__re, '-')} {format(self.__im, '+')}i"


print(Comlex(-5, '-5k'))
print(Comlex(5, -5) + Comlex(5, 15))
print(Comlex(5, -5) * Comlex(5, 5))
