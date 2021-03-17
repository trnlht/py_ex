import unittest

def is_palindrome_permutation(s):

    if len(s) <= 1:
        return True

    char_counters = [0 for i in range(128)]

    for ch in s:
        char_counters[ord(ch)] += 1

    odd_cnt = 0

    for cnt in char_counters:
        if cnt % 2 != 0:
            odd_cnt += 1

        if odd_cnt > 1:
            return False

    return True


class IsPalindromePermutationTester(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        self.assertTrue(is_palindrome_permutation(""))
        self.assertTrue(is_palindrome_permutation("a"))
        self.assertTrue(is_palindrome_permutation("aba"))
        self.assertTrue(is_palindrome_permutation("aa"))
        self.assertTrue(is_palindrome_permutation("roserose"))
        self.assertTrue(is_palindrome_permutation("rosenrose"))
        self.assertTrue(is_palindrome_permutation("tacocat"))

        self.assertFalse(is_palindrome_permutation("taco cat"))
        self.assertFalse(is_palindrome_permutation("abcdef"))
        self.assertFalse(is_palindrome_permutation("!840163ef"))





if __name__ == "__main__":
    unittest.main(verbosity=2)
