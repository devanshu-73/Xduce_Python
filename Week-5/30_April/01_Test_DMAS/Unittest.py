from program import addition as a,subtraction as s,multiplication as m,division as d;
import unittest


class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = a(10,5)
        self.assertEqual(res,15,msg='Wrong Output')
    def test_sub(self):
        res = s(10,5)
        self.assertEqual(res,5,msg='Wrong Output')
    def test_mul(self):
        res = m(10,5)
        self.assertEqual(res,50,msg='Wrong Output')
    def test_div(self):
        res = d(10,5)
        self.assertEqual(res,2,msg='Wrong Output')


if __name__ == '__main__':
    unittest.main()