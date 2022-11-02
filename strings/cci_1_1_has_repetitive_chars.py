import unittest
from collections import defaultdict


def has_repetitive_chars(s: str):
    """
    Проверяет, есть ли в строке повторяющиеся символы.
    Использует дополнительную таблицу (список) для хранения счётчиков символов.
    Список chars состоит из 128 элементов (размер таблицы ascii - рассчитываем на то что в строке
    только ascii-символы), в начале заполнен нулями. Индекс элемента - код символа ascii, а значение счетчик.
    Проходим по строке и увеличиваем счетчик для каждого символа, если счетчик больше 1 - значит символ повторяется.
    Временная сложность: O(N)
    [CCI 1.1]

    :param s: Строка для проверки
    :return: True если есть повторяющиеся символы, иначе - False.
    """
    chars = [0 for i in range(128)]

    for ch in s:
        i = ord(ch)
        chars[i] += 1
        if chars[i] > 1:
            return True

    return False


def has_repetitive_chars_dict(s: str):
    """
    Аналог предыдущей функции, но со словарем в качестве таблицы. В словаре ключом является символ,
    а значением - его счетчик.
    Временная сложность: O(N)
    [CCI 1.1]

    :param s: Строка для проверки
    :return: True если есть повторяющиеся символы, иначе - False.
    """
    char_counters = defaultdict(int)

    for ch in s:
        char_counters[ch] += 1
        if char_counters[ch] > 1:
            return True

    return False


def has_repetitive_chars_set(s: str):
    """
    Аналог предыдущей функции, но с множеством в качестве таблицы. В множестве хранятся сами символы.
    При появлении в множестве повторного символа поиск прекращается.
    Временная сложность: O(N)
    [CCI 1.1]

    :param s: Строка для проверки
    :return: True если есть повторяющиеся символы, иначе - False.
    """
    char_counters = set()

    for ch in s:
        if ch not in char_counters:
            char_counters.add(ch)
        else:
            return True

    return False


def has_repetitive_chars_sort(s: str):
    """
    Проверяет, есть ли в строке повторяющиеся символы.
    Сортирует строку и смотрит соседние символы.
    Временная сложность: O(Nlog(N))
    [CCI 1.1]

    :param s: Строка для проверки
    """
    sorted_str = sorted(s)

    for i in range(len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i+1]:
            return True

    return False


class TestHasRepetitiveChars(unittest.TestCase):

    def test_has_repetitive_chars(self):
        for func in [
                        has_repetitive_chars,
                        has_repetitive_chars_sort,
                        has_repetitive_chars_dict,
                        has_repetitive_chars_set]:
            self.assertTrue(func("abcdeefg"))
            self.assertTrue(func("abcdefgg"))
            self.assertTrue(func("aabcdefg"))

            self.assertFalse(func("abcdefg"))
            self.assertFalse(func(""))


if __name__ == "__main__":
    unittest.main(verbosity=2)



