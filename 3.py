# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
isNotInt = True
while isNotInt:
    dat = input('Введите номер месяца 1..12 - ')
    if dat.isdigit() and 0 < int(dat) < 13:
        isNotInt = False

# решение через список
listDat = int(dat)
mounthList = ["зима", "весна", "лето", "осень"]
listDat = listDat % 12
print(f'Время года - {mounthList[listDat//3]} - метод list')

# решение через словарь
dictDat = int(dat)
mounthDict = {"зима": [12, 1, 2],
        "весна": [3, 4, 5],
        "лето": [6, 7, 8],
        "осень": [9, 10, 11]}
for mon in mounthDict.keys():
    for mounth in mounthDict[mon]:
        if mounth == dictDat:
            print(f'Время года - {mon} - метод dict')
