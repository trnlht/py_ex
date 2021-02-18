import unittest


def is_permutation(str1, str2):
    """
    Check if str1 is a permutation of str2.

    :param str1: First string to check
    :param str2: Second string to check
    :return: True if first string is permutation of second string, otherwise False.
    """
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)

def is_permutation_fast(str1, str2):
    return True

class TestIsPermutation(unittest.TestCase):

    def test_is_permutation(self):
        self.assertTrue(is_permutation("abc", "bca"))
        self.assertTrue(is_permutation("", ""))
        self.assertTrue(is_permutation("43bcef", "34cbfe"))

        self.assertFalse(is_permutation("abc", "bcd"))
        self.assertFalse(is_permutation("", "bcd"))
        self.assertFalse(is_permutation("gffdda", "gffdga"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
