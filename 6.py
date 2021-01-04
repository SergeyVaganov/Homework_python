def int_func(text):
    """Делает первый символ слова прописным"""
    a = text[0].upper()
    return a+text[1:]


def int_func_str(text):
    """Делает все первые символы слов в строке прописными"""
    words = str(text).split()
    for index in range(len(words)):
        words[index] = int_func(words[index])
    return ' '.join(words)


txt = input('Введите строку - ')
print(int_func_str(txt))
