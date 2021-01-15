# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle
from random import randint


def generator(start):
    for num in count(start):
        if num > 10:
            break
        yield num


def generator_cycle():
    n = 0
    arr = [randint(0, 50) for el in range(5)]
    for num in cycle(arr):
        n += 1
        if n > 10:
            break
        yield num


g1 = generator(5)
for el in g1:
    print(el, end=', ')
print('')
g2 = generator_cycle()
for el in g2:
    print(el, end=', ')
