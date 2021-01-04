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


def input_int():
    """Осуществляет ввод отрицательного числа типа int"""
    while True:
        try:
            var = int(input('Введите число - '))
            if var >= 0:
                raise ValueError
        except ValueError:
            print('Вы не правильно ввели числo')
            continue
        break
    return var


def my_func_rec(x, y):
    """Возводит аргумент x в степень y c рекурсивным методом"""
    if x == 0:
        return 0
    y += 1
    if y == 0:
        return 1/x
    return 1/x*my_func_rec(x, y)


def my_func_op(x, y):
    """Возводит аргумент x в степень y c помощью оператора **"""
    if x == 0:
        return 0
    return x**y


def my_func_loop(x, y):
    """Возводит аргумент x в степень y c помощью цикла"""
    if x == 0:
        return 0
    result = 1
    for index in range(0, abs(y)):
        result *= x
    return 1/result


print('Расчёт рекурсивным методом 2 в степени - 3 = ', my_func_rec(2, -3))
print('Расчёт методом оператора ** 2 в степени - 3 = ', my_func_op(2, -3))
print('Расчёт методом цикла 2 в степени - 3 = ', my_func_loop(2, -3))
print('Расчёт при ручном вводе - ', my_func_loop(input_float(), input_int()))
