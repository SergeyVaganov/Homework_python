# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
isNotInt = True
while isNotInt:
    dat = input('Введите целое положительное число - ')
    if dat.isdigit():
        if 0 <= int(dat):
            isNotInt = False
ost = int(dat)
maximum = 0
while ost != 0:
    num = ost % 10
    if num > maximum:
        maximum = num
    ost = ost // 10
print(f'Максимальная цифра в числе = {maximum}')
