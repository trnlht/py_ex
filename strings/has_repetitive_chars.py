import unittest


def has_repetitive_chars(s):
    chars = [0 for i in range(128)]

    for ch in s:
        i = ord(ch)
        chars[i] += 1
        if chars[i] > 1:
            return True

    return False

    
class TestHasRepetitiveChars(unittest.TestCase):

    def test_has_repetitive_chars(self):
        self.assertTrue(has_repetitive_chars("abcdeefg"))
        self.assertTrue(has_repetitive_chars("abcdefgg"))
        self.assertTrue(has_repetitive_chars("aabcdefg"))

        self.assertFalse(has_repetitive_chars("abcdefg"))
        self.assertFalse(has_repetitive_chars(""))

if __name__ == "__main__":
    unittest.main(verbosity=2)



