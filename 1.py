# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import re
import datetime


class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def parser_date(cls, data):
        mach = re.fullmatch(r'\d{2}\D\d{2}\D\d{4}', data)
        return (list(map(int, data.split('-'))) if (mach) else 'Not valid')

    @staticmethod
    def validation_date(data):
        try:
            res = datetime.datetime(data[2], data[1], data[0])
            return True
        except:
            ValueError
            return False


arr = [Data('22-12-2020'), Data('22-12-YYYY'), Data('29-02-2020'), Data('29-02-2019')]
for el in arr:
    print(f'Введённая дата {el.data}, \nparser_date => {Data.parser_date(el.data)}'
          f'\nvalidation_date => {Data.validation_date(Data.parser_date(el.data))}\n\n')
