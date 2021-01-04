def input_float():
    """Осуществляет ввод числа типа float"""
    while True:
        try:
            var = float(input('Введите число - '))
        except ValueError:
            print('Вы не правильно ввели числo')
            continue
        break
    return var


def my_func(*var):
    """Bозвращает сумму наибольших двух аргументов"""
    sorted_var = sorted(list(var), reverse=True)
    try:
        result = sorted_var[0] + sorted_var[1]
    except IndexError:
        print('Введено менее двух аргументов')
        return
    return result


print('один аргумент - ', my_func(12))
print('два аргумента - ', my_func(12, 2))
print('три аргумента - ', my_func(input_float(), input_float(), input_float()))
print('четыре аргумента - ', my_func(45, 1, 2, 3))
