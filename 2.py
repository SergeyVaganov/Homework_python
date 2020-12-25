# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.
isNotInt = True
while isNotInt:
    dat = input('Введите время в секундах - ')
    if dat.isdigit():
        isNotInt = False
time = int(dat)
ss = time % 60
mm = time // 60
hh = mm // 60
mm = mm % 60
if ss < 10:
    ss = '0' + str(ss)
else:
    ss = str(ss)
if mm < 10:
    mm = '0' + str(mm)
else:
    mm = str(mm)
if hh < 10:
    hh = '0' + str(hh)
else:
    hh = str(hh)
print(f'Ваше время - {hh}:{mm}:{ss}')
