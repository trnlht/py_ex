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

        for j in range(i, size - i - 1):

            top = m[i][j]
            left = m[size - j - 1][i]
            bottom = m[size - 1 - i][size - 1 - j]
            right = m[j][size - 1 - i]

            print("\ni = ", i, " j = ", j)
            print("top = ", top)
            print("left = ", left)
            print("bottom ", bottom)
            print("right = ", right)

            m[i][j] = left
            m[size - j - 1][i] = bottom
            m[size - 1 - i][size - 1 - j] = right
            m[j][size - 1 - i] = top

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
    def test_should_rotate_image_4x4_correctly(self):
        self.assertEqual(
                rotate_image_in_place(
                    [
                        [ 1,  2,  3,  4],
                        [ 5,  6,  7,  8],
                        [ 9, 10, 11, 12],
                        [13, 14, 15, 16]
                    ]
                ),
                [
                        [13,  9,  5,  1],
                        [14, 10,  6,  2],
                        [15, 11,  7,  3],
                        [16, 12,  8,  4]
                ]
        )
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
