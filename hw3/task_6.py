# homework lesson: 3, task: 5
"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
использовать написанную ранее функцию int_func().
"""


def int_func(word: str) -> str:
    """
    Преобразуем первую букву в слове в прописную

    :param word: str
    :return: str
    """
    list_of_char = list(word)
    list_of_char[0] = chr(ord(word[0]) - 32)
    new_word = ''.join(list_of_char)
    return new_word


def sentence_transform(sentence: str) -> str:
    """
    Сделаь каждое слово начинающимся с заглавной буквы

    :param sentence: str
    :return: str
    """
    list_of_words = sentence.split()
    new_list_of_words = list(map(int_func, list_of_words))
    return ' '.join(new_list_of_words)


print(int_func('word'))
print(sentence_transform('my test sentence'))
