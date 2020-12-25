# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
isNotInt = True
while isNotInt:
    dat = input('Введите целое число в диапазоне от 0 до 9 - ')
    if dat.isdigit():
        if 0 <= int(dat) < 10:
            isNotInt = False
i = 1
summa = 0
while i < 4:
    summa = summa + int(dat*i)
    i += 1
print(f'{dat} + {dat*2} + {dat*3} = {summa}')
