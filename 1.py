# Поработайте с переменными, создайте несколько, выведите на экран, запросите у
# пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
a = 5
b = 3.5
c = True
d = 'Hello World!'
print(f"Переменная a = {a}; тип - {type(a)}")
print(f"Переменная a = {b}; тип - {type(b)}")
print(f"Переменная a = {c}; тип - {type(c)}")
print(f"Переменная a = {d}; тип - {type(d)}")
yesNo = True
while yesNo:
    data = input("Введите данные - ")
    i = 0
    isInt = True
    isFloat = True
    while i < len(data):
        if data[i].isdigit():
            i += 1
        elif data[i] == '.':
            isInt = False
            i += 1
        else:
            isInt = False
            isFloat = False
            break
    if isInt:
        print(f'Вы ввели число {int(data)}; тип - {type(int())}')
    elif isFloat:
        print(f'Вы ввели число {float(data)}; тип - {type(float(data))}')
    else:
        print(f'Вы ввели строку - {data}; тип - {type(data)}')
    yes = input('Нажмите клавишу "у" если хотите продолжить ввод данных - ')
    if yes != 'y':
        yesNo = False

    print('aaaaaaaaaaaaaaaaa')
