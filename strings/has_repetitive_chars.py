import unittest


def has_repetitive_chars(s):
    chars = [0 for i in range(128)]

    for ch in s:
        i = ord(ch)
        chars[i] += 1
        if chars[i] > 1:
            return True

    return False

def has_repetitive_chars_sort(s):
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



