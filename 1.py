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


def division(var1, var2):
    """Делит первый аргумент на второй
    и производит проверку деления на 0"""
    try:
        var3 = var1/var2
    except ZeroDivisionError:
        print('Деление на 0')
        return
    return var3


print(division(input_float(), input_float()))
