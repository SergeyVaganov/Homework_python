# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
myList = [7, 5, 3, 3, 2]
print(f'исходный список - {myList}')
cycleLife = True
while cycleLife:
    wasInserted = False
    isNotInt = True
    while isNotInt:
        num = input('введите целое число >0 - ')
        if num.isdigit():
            isNotInt = False
            num = int(num)
    for i in range(len(myList)):
        if num >= myList[i]:
            myList.insert(i, num)
            wasInserted = True
            break
    if wasInserted == False:
        myList.append(num)
        wasInserted = True
    print(myList)
    if input('Продолжить? (нажмите клавишу y) - ') != 'y':
        cycleLife = False
