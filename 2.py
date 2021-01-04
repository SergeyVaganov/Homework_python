def user(name='Нет данных', surname='Нет данных',
         year=None, sity=None, email=None,
         phone=None):
    """
    Выводит данные о пользователе одной строкой
    :param name: имя
    :param surname: фамилия
    :param year: год рождения
    :param sity: город проживания
    :param email: email
    :param phone: телефон
    """
    print(f'Имя = {name}, Фамилия = {surname}, год рождения - {year}, город проживания - {sity},'
          f' email - {email}, телефон - {phone}.')


help(user)
user(name='Сергей', year=1975, phone='451-456-456')
