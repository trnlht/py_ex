import unittest


def has_repetitive_chars(s):
    """
    Проверяет, есть ли в строке повторяющиеся символы.
    Использует дополнительную таблицу для хранения счётчиков символов.
    Временная сложность: O(N)
    [CCI 1.1]

    :param s: Строка для проверки
    """
    chars = [0 for i in range(128)]

    for ch in s:
        i = ord(ch)
        chars[i] += 1
        if chars[i] > 1:
            return True

    return False

def has_repetitive_chars_sort(s):
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
        self.assertTrue(has_repetitive_chars("abcdeefg"))
        self.assertTrue(has_repetitive_chars("abcdefgg"))
        self.assertTrue(has_repetitive_chars("aabcdefg"))

        self.assertFalse(has_repetitive_chars("abcdefg"))
        self.assertFalse(has_repetitive_chars(""))

    def test_has_repetitive_chars_sort(self):
        self.assertTrue(has_repetitive_chars_sort("abcdeefg"))
        self.assertTrue(has_repetitive_chars_sort("abcdefgg"))
        self.assertTrue(has_repetitive_chars_sort("aabcdefg"))

        self.assertFalse(has_repetitive_chars_sort("abcdefg"))
        self.assertFalse(has_repetitive_chars_sort(""))

if __name__ == "__main__":
    unittest.main(verbosity=2)



