# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.
try:
    with open('text2.txt', 'r') as f:
        i = 0
        text = f.readlines()
        print(f'количество строк - {len(text)}')
        for sent in text:
            i += 1
            print(f'количество слов в {i} строке - {len(sent.split())}')
except IOError:
    print('ошибка ввода-вывода')
