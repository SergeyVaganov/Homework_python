# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint


try:
    with open('text5.txt', 'w') as fw:
        i = 0
        while i < 10:
            var = randint(0, 50)
            fw.writelines(str(var)+' ')
            i += 1
    with open('text5.txt', 'r') as fr:
        summa = 0
        num = fr.read().split()
        for el in num:
            summa += int(el)
        print('сумма чисел = ', summa)
except IOError:
    print('Ошибка ввода вывода')
