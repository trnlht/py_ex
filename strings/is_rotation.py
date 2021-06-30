import unittest


def is_rotation(s1, s2):
    """
    Проверяет, является ли строка s2 циклической перестановкой строки s1,
    используя один вызов метода isSubstring (усолвие задачи - в данном случае
    использовался метод str.find)
    [CCI 1.9]
    :param s1: Первая строка
    :param s2: Вторая строка
    """
    if len(s1) == len(s2) and len(s1) != 0:
        s1s1 = s1 + s1
        if s1s1.find(s2) != -1:
            return True

    return False


class IsRotationTester(unittest.TestCase):
    def test_should_return_false_if_not_rotation(self):
        self.assertFalse(is_rotation("", ""))
        self.assertFalse(is_rotation("", "abc"))
        self.assertFalse(is_rotation("abcd", "bacd"))
        
    def test_should_return_true_if_rotation(self):
        self.assertTrue(is_rotation("abcdef", "bcdefa"))
        self.assertTrue(is_rotation("abcdef", "cdefab"))
        self.assertTrue(is_rotation("abcdef", "defabc"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
