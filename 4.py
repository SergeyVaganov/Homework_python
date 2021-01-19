# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
# pip install googletrans==3.1.0a0
from googletrans import Translator


try:
    translator = Translator()
    with open('text4.txt', 'r') as f:
        with open ('text4_new.txt', 'w') as fn:
            while (True):
                str = f.readline()
                if not str:
                    break
                str_new = str.split()
                result = translator.translate(str_new[0], src='en', dest='ru')
                str_new[0] = result.text
                fn.write(' '.join(str_new)+'\n')
except IOError:
    print('Ошибка ввода-вывода')
