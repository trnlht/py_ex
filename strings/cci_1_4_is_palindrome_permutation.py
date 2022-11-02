import unittest
from collections import defaultdict


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


def is_palindrome_permutation_dict(s: str):

    char_counters = defaultdict(int)

    for ch in s:
        char_counters[ch] += 1

    odd_cnt = 0

    for char, cnt in char_counters.items():
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

    def test_is_palindrome_permutation_dict(self):
        self.assertTrue(is_palindrome_permutation_dict(""))
        self.assertTrue(is_palindrome_permutation_dict("a"))
        self.assertTrue(is_palindrome_permutation_dict("aba"))
        self.assertTrue(is_palindrome_permutation_dict("aa"))
        self.assertTrue(is_palindrome_permutation_dict("roserose"))
        self.assertTrue(is_palindrome_permutation_dict("rosenrose"))
        self.assertTrue(is_palindrome_permutation_dict("tacocat"))

        self.assertFalse(is_palindrome_permutation_dict("taco cat"))
        self.assertFalse(is_palindrome_permutation_dict("abcdef"))
        self.assertFalse(is_palindrome_permutation_dict("!840163ef"))




if __name__ == "__main__":
    unittest.main(verbosity=2)
