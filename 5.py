# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала
# с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
isNotInt = True
while isNotInt:
    revenue = input('Введите выручку (целое число >0) - ')
    if revenue.isdigit():
        if 0 <= int(revenue):
            isNotInt = False
isNotInt = True
while isNotInt:
    costs = input('Введите издержки (целое число >0) - ')
    if costs.isdigit():
        if 0 <= int(costs):
            isNotInt = False
revenue = int(revenue)
costs = int(costs)
if revenue > costs:
    print(f'За данный период вы получили прибыль = {revenue - costs}')
    print(f'Рентабильность составила = {round((revenue - costs)/revenue, 2)})')
    isNotInt = True
    while isNotInt:
        personal = input('Введите количество сотрудников (целое число >0) - ')
        if personal.isdigit():
            if 0 <= int(personal):
                isNotInt = False
    print(f'Прибыль на одного сотрудника составила = {round((revenue - costs)/int(personal),2)}')
else:
    print(f'За данный период вы получили убыток = {costs - revenue}')
