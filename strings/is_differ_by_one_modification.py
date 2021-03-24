import unittest


def is_differ_by_one_modification(s1, s2):
    """
    Check if s1 and s2 differ by one modification.
    Allowable modifications:
        - inserting
        - deleting
        - replacing
    :param s1: First string
    :param s2: Second string
    :return: True if s1 and s2 differ by one modification, otherwise False
    """
    if len(s1) == len(s2):
        return is_differ_by_one_char(s1, s2)
    else:
        if len(s1) < len(s2):
            return is_one_char_miss(s1, s2)
        else:
            return is_one_char_miss(s2, s1)


def is_differ_by_one_char(s1, s2):
    different_chars_cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            different_chars_cnt += 1
            if different_chars_cnt > 1:
                return False

    return True


def is_one_char_miss(less_str, bigger_str):

    if len(bigger_str) - len(less_str) > 1:
        return False

    i = 0
    j = 0
    cnt = 0

    while i < len(less_str):
        if less_str[i] != bigger_str[j]:
            cnt += 1
            if cnt > 1:
                return False

            j += 1
        else:
            i += 1
            j += 1

    return True



class TestIfDifferByOneModification(unittest.TestCase):
    def test_is_one_char_replaced(self):
        self.assertTrue(is_differ_by_one_modification("aaa", "aba"))
        self.assertTrue(is_differ_by_one_modification("aaa", "baa"))
        self.assertTrue(is_differ_by_one_modification("aaa", "aab"))

        self.assertFalse(is_differ_by_one_modification("aaa", "abc"))
        self.assertFalse(is_differ_by_one_modification("aaa", "bac"))
        self.assertFalse(is_differ_by_one_modification("aaa", "bca"))

    def test_is_one_char_inserted(self):
        self.assertTrue(is_differ_by_one_modification("aaa", "aaab"))
        self.assertTrue(is_differ_by_one_modification("aaa", "aaba"))
        self.assertTrue(is_differ_by_one_modification("aaa", "baaa"))

        self.assertFalse(is_differ_by_one_modification("aaa", "aaabb"))
        self.assertFalse(is_differ_by_one_modification("aaa", "abaab"))
        self.assertFalse(is_differ_by_one_modification("aaa", "babaab"))

    def test_is_one_char_deleted(self):
        self.assertTrue(is_differ_by_one_modification("abcdef", "abcde"))
        self.assertTrue(is_differ_by_one_modification("abcdef", "bcdef"))
        self.assertTrue(is_differ_by_one_modification("abcdef", "abdef"))

        self.assertFalse(is_differ_by_one_modification("abcdef", "abcd"))
        self.assertFalse(is_differ_by_one_modification("abcdef", "cdef"))
        self.assertFalse(is_differ_by_one_modification("abcdef", "abef"))




if __name__ == "__main__":
    unittest.main(verbosity=2)
