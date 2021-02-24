import unittest


def replace_spaces(s):
    """
    Replace all spaces in string by string "%20".

    :param s: string to modify.
    """
    return s.strip().replace(" ", "%20")


class ReplaceSpacesTester(unittest.TestCase):
    def test_replace_spaces(self):
        self.assertEqual(replace_spaces("Mr John Smith    "), "Mr%20John%20Smith")


if __name__ == "__main__":
    unittest.main(verbosity=2)
