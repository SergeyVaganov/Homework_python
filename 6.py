# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
cycleLife = True
listProduct = []
number = 0
while cycleLife:
    number += 1
    product = {}
    product['название'] = input('введите название товара - ')
    isNotInt = True
    while isNotInt:
        price = input('введите цену товара (целое число > 0) - ')
        if price.isdigit() and int(price) > 0:
            product['цена'] = int(price)
            isNotInt = False
    product['ед'] = input('введите измерения - ')
    isNotInt = True
    while isNotInt:
        quantity = input('введите количество товара (целое число > 0) - ')
        if quantity.isdigit() and int(quantity) > 0:
            product['количество'] = int(quantity)
            isNotInt = False
    productCortege = (number, product)
    listProduct.append(productCortege)
    if input('Продолжить? (нажмите клавишу y) - ') != 'y':
        cycleLife = False
print('У вас введено в базу')
for elem in listProduct:
    print(elem)
print('Аналитика')
report = {}
for key in listProduct[0][1].keys():
    listData = []
    for index in range(len(listProduct)):
        listData.append(listProduct[index][1][key])
    report[key] = listData
report['ед'] = list(set(report['ед']))
for param in report.keys():
    print(f'{param} - {report[param]}')
