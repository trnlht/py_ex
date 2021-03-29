import unittest


def compress_string(s):
    """
    Compress repeating chars in string.
    Example: "aaaa" -> "a4"
    Return source string if compressed string is bigger than source string

    :param s: string to compress

    :return: compressed string or source string

    """
    i = 0
    res = ""
    while i < len(s):
        cnt = 1

        while (i != len(s) - 1) and s[i] == s[i+1]:
            cnt += 1
            i += 1

        if cnt > 1:
            res += s[i] + str(cnt)
        else:
            res += s[i]

        i += 1

    return res if len(res) < len(s) else s


class CompressStringTester(unittest.TestCase):
    def test_compress_string(self):
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string("aaa"), "a3")
        self.assertEqual(compress_string("aa"), "aa")
        self.assertEqual(compress_string("aaabbc"), "a3b2c")
        self.assertEqual(compress_string("aaaabbbbccccc"), "a4b4c5")



if __name__ == "__main__":
    unittest.main(verbosity=2)
