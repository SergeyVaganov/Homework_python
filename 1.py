# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.
arr = input("введите через пробел элементы - ").split()
arrNew = []
for elem in arr:
    i = 0
    isInt = True
    isFloat = True
    while i < len(elem):
        if elem[i].isdigit():
            i += 1
        elif elem[i] == '.':
            isInt = False
            i += 1
        else:
            isInt = False
            isFloat = False
            break
    if isInt:
        arrNew.append(int(elem))
    elif isFloat:
        arrNew.append(float(elem))
    else:
        arrNew.append(elem)
for index in range(len(arrNew)):
    print(f'{index}-й элемент массива - {arrNew[index]}, тип элемнта - {type(arrNew[index])}')
