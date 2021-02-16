import unittest


def is_palindrome(s):
    """
    Check if string is a palindrome or not. Simple version.

    :param s: string to check
    :return: True if string is a palindrome otherwise False.
    """
    
    if len(s) == 0:
        return True

    i = 0
    j = len(s) - 1

    while (i < j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

def is_palindrome_alpha(s):
    """
    Check if string is a palindrome or not. Only letters count.
    Case doesn't matter

    :param s: string to check
    :return: True if string is a palindrome otherwise False.
    """
    
    if len(s) == 0:
        return True

    i = 0
    j = len(s) - 1

    while (i < j):
        while (not s[i].isalpha()) and (i <= j):
            i += 1

        while (not s[j].isalpha()) and (i <= j):
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True

class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("abcba"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("abccba"))

        self.assertFalse(is_palindrome("abcdef")) 
        self.assertFalse(is_palindrome("abcdba")) 

if __name__ == "__main__":
    unittest.main(verbosity=2)
