import unittest
from polish import PolishCalculator, ExpressionNotValidException
class TestPolish(unittest.TestCase):
    def setUp(self):
        self.polish=PolishCalculator()
        self.good_input=[("2 3 +",5),("3 5 * 1 -",14)]
        self.bad_input=[("2 3 + +", ExpressionNotValidException)]
    def test_easy_expr(self):
        for (expr,value) in self.good_input:
            self.assertEqual(self.polish.eval(expr), value)
    def test_raise_on_bad_input(self):
        for (expr,raises) in self.bad_input:
            self.assertRaises(raises,self.polish.eval,expr)

if __name__=='__main__':
    unittest.main()
