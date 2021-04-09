import unittest


def rotate_image(m):

    size = len(m[0])

    res = [[0 for i in range(size)] for i in range(size)]

    for i in range(size):
        for j in range(size):
            res[j][size - i - 1] = m[i][j]

    return res

def rotate_image_in_place(m):
    size = len(m[0])

    if size < 2:
        return m

    layer_size = size

    i = 0

    while layer_size > 1:

        for j in range(i, size - i):

            top = m[i][j]
            left = m[size - i - 1][j]
            bottom = m[size - i - 1][size - i - 1]
            right = m[i][size - i - 1]

            m[i][j] = left
            m[size - i - 1][j] = bottom
            m[size - i - 1][size - i - 1] = right
            m[i][size - i - 1] = top

        i += 1
        layer_size -= 2

    return m



class RotateImageTester(unittest.TestCase):
    def test_should_rotate_image_3x3_correctly(self):
        self.assertEqual(
                rotate_image(
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]
                ),
                [
                    [7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]
                ]
        )

    def test_should_rotate_image_2x2_correctly(self):
        self.assertEqual(
                rotate_image(
                    [
                        [1, 2],
                        [3, 4]
                    ]
                ),
                [
                    [3, 1],
                    [4, 2]
                ]
        )

    def test_should_rotate_image_1x1_correctly(self):
        self.assertEqual(
                rotate_image(
                    [
                        [1]
                    ]
                ),
                [
                    [1]
                ]
        )

class RotateImageInPlaceTester(unittest.TestCase):
    def test_should_rotate_image_3x3_correctly(self):
        self.assertEqual(
                rotate_image_in_place(
                    [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]
                ),
                [
                    [7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]
                ]
        )

    def test_should_rotate_image_2x2_correctly(self):
        self.assertEqual(
                rotate_image_in_place(
                    [
                        [1, 2],
                        [3, 4]
                    ]
                ),
                [
                    [3, 1],
                    [4, 2]
                ]
        )

    def test_should_rotate_image_1x1_correctly(self):
        self.assertEqual(
                rotate_image_in_place(
                    [
                        [1]
                    ]
                ),
                [
                    [1]
                ]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
