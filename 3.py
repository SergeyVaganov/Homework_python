# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
try:
    with open('text3.txt', 'r') as f:
        summa = 0
        i = 0
        while (True):
            str = f.readline()
            if not str:
                break
            if float(str.split()[1]) < 20000:
                print(str, end='')
            summa += float(str.split()[1])
            i += 1
    print(f'Cредний доход = {summa/i:.2f}')
except IOError:
    print('Ошибка ввода-вывода')
