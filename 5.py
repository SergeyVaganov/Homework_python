def input_str_num():
    """
    Выполняет ввод строки чисел и возвращает их сумму
    В случае попадания в строке символа Q выводит промежуточную сумму до символа
    и флаг завершения выполнения.
    :return summa, end
    end = True - наличие символа останова Q в строке
    end = False - символа Q не обнаружено
    """
    in_str = input('Введите строку c чисел - ').split()
    end = False
    summa = 0
    try:
        for index in range(len(in_str)):
            if in_str[index].upper() == 'Q':
                end = True
                break
            summa += float(in_str[index])
    except ValueError:
        print('В списке имеются не правильные данные')
        return 0, end
    return summa, end


print('Для завершения программы введите в строку чисел символ "q" либо "Q"')
summ = 0
end_input = False
while not end_input:
    new_sum, end_input = input_str_num()
    summ += new_sum
    print('Общая сумма составляет - ', summ)
