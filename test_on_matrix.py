import unittest
from SquareMatrix import SquareMatrix,BadMatrix

class TestOnMatrix(unittest.TestCase):
    def setUp(self):
        self.identity = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
        self.identity_matrix = SquareMatrix(5)
        self.generic_matrix = SquareMatrix(3)
        self.generic_matrix.set_matrix([[1,2,3],[4,5,6],[9,8,9]])
        self.identity_matrix_transpose = (self.identity_matrix,self.identity_matrix)
        self.transposed = SquareMatrix(3)
        self.transposed.set_matrix([[1,4,9],[2,5,8],[3,6,9]])
        self.matrix_transpose = (self.generic_matrix, self.transposed)
        self.negative_determinant = (self.generic_matrix, -6)
        self.identity_determinant = (self.identity_matrix,1)
        self.sum_by_row_result = (self.generic_matrix,[6,15,26])
        self.sum_by_column = (self.generic_matrix,[14,15,18])
        self.bad_matrix = ([1,2],[3,2],[3,2])
    def test_on_transpose_identity(self):
        (identity, result) = self.identity_matrix_transpose
        self.assertEqual(identity.transpose(), result)

    def test_on_transpose_generic(self):
        (generic, result) = self.matrix_transpose
        self.assertEqual(generic.transpose(),result)
    def test_on_identity_correctness(self):
        self.assertEqual(self.identity_matrix.matrix,self.identity)
    def test_on_sum_by_row(self):
        (matrix, summ) = self.sum_by_row_result
        self.assertEqual(matrix.sum_by_row(), summ)
    def test_on_sum_by_column(self):
        (matrix,sums) = self.sum_by_column
        self.assertEqual(matrix.sum_by_column(), sums)
    def test_on_generic_determinant(self):
        (matrix,deter) = self.negative_determinant
        self.assertEqual(matrix.determinant(),deter)
    def test_on_identity_determinant(self):
        (matrix,deter) = self.identity_determinant
        self.assertEqual(matrix.determinant(), deter)
    def check_bad_matrix_init(self):
        matrix = SquareMatrix(2)
        self.assertRaises(BadMatrix, matrix.set_matrix, self.bad_matrix)




if __name__=='__main__':
    unittest.main(verbosity=2)
