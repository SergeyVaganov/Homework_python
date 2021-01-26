# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:

    def __init__(self, mrx):
        self.mrx = mrx

    def __add__(self, other):
        result = []
        for row in range(len(self.mrx)):
            result.append(list(map(lambda x,y: x+y, self.mrx[row], other.mrx[row])))
        return Matrix(result)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.mrx)


m1 = Matrix([[1,2,3],[1,2,3],[4,5,6]])
m2 = Matrix([[2,3,4],[1,2,3],[6,7,8]])
print(m1)
print('+')
print(m2)
print('-----------')
print(m1+m2)
