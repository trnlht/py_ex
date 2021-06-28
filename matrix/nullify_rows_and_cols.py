import unittest


def nullify_rows_and_cols(m):
    """
    Nullify corresponding row and column of MxN matrix if element of matrix is equal to zero.
    [CCI 1.8]
    :param m: Matrix
    """
    M = len(m)
    N = len(m[0])
    rows = set()
    cols = set()

    for i in range(M):
        for j in range(N):
            if m[i][j] == 0:
                rows.add(i)
                cols.add(j)


    for row in rows: 
        for i in range(N):
            m[row][i] = 0

    for col in cols:
        for i in range(M):
            m[i][col] = 0

    return m

class NullifyRowsAndColsTester(unittest.TestCase):
    def test_should_nullify_2x2_matrix_correctly(self):
        self.assertEqual(
                nullify_rows_and_cols(
                    [
                        [1, 2],
                        [0, 4]
                    ]
                ),
                [
                    [0, 2],
                    [0, 0]
                ]
        )

        self.assertEqual(
                nullify_rows_and_cols(
                    [
                        [0, 2],
                        [0, 4]
                    ]
                ),
                [
                    [0, 0],
                    [0, 0]
                ]
        )

    def test_should_nullify_3x3_matrix_correctly(self):
        self.assertEqual(
                nullify_rows_and_cols(
                    [
                        [1, 2, 3],
                        [4, 0, 6],
                        [7, 8, 9]
                    ]
                ),
                [
                        [1, 0, 3],
                        [0, 0, 0],
                        [7, 0, 9]
                ]
        )

        self.assertEqual(
                nullify_rows_and_cols(
                    [
                        [0, 2, 3],
                        [4, 5, 6],
                        [7, 8, 0]
                    ]
                ),
                [
                        [0, 0, 0],
                        [0, 5, 0],
                        [0, 0, 0]
                ]
        )
if __name__ == "__main__":
    unittest.main(verbosity=2)
