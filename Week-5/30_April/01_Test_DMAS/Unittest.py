from program import addition as a,subtraction as s,multiplication as m,division as d;
import unittest

# before test function 'test' word is mandatory and '_' is not mandatory  
# Every unit test run independently and if it gives error then it does not impact of another unit test output
 
class TestCalculations1(unittest.TestCase):
    def test_add(self):
        res = a(10,5)
        self.assertEqual(res,15,msg='Wrong Output')
    def test_sub(self):
        res = s(10,5)
        self.assertEqual(res,5,msg='Wrong Output')
    def testmul(self):
        res = m(10,5)
        self.assertEqual(res,50,msg='Wrong Output')
    def testdiv(self):
        res = d(10,5)
        self.assertEqual(res,2,msg='Wrong Output')
        
class TestCalculations2(unittest.TestCase):
    def test_add(self):
        res = a(100,50)
        self.assertEqual(res,150,msg='Wrong Output')
    def test_sub(self):
        res = s(100,50)
        self.assertEqual(res,50,msg='Wrong Output')
    def testmul(self):
        res = m(100,50)
        self.assertEqual(res,5000,msg='Wrong Output')
    def testdiv(self):
        res = d(100,50)
        self.assertEqual(res,2.0,msg='Wrong Output')


if __name__ == '__main__':
    unittest.main()