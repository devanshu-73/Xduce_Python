from program import addition as add,subtraction as sub,multiplication as mul,division as div;
import unittest

# before test function 'test' word is mandatory and '_' is not mandatory  
# Every unit test run independently and if it gives error then it does not impact of another unit test output

class TestCalculations1(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5
        self.x = 100
        self.y = 50
        print('SetUp Called')

    def tearDown(self):
        print('TearDown Called')

    def test_add(self):
        res = add(self.a,self.b)
        self.assertEqual(res,self.a+self.b,msg='Wrong Output')
        print('test_add Completed Successfully')
    def test_sub(self):
        res = sub(self.a,self.b)
        self.assertEqual(res,self.a-self.b,msg='Wrong Output')
        print('test_sub Completed Successfully')
    def testmul(self):
        res = mul(self.a,self.b)
        self.assertEqual(res,self.a*self.b,msg='Wrong Output')
        print('testmul Completed Successfully')
    def testdiv(self):
        res = div(self.a,self.b)
        self.assertEqual(res,self.a/self.b,msg='Wrong Output')
        print('testdiv Completed Successfully')

        
# class TestCalculations2(unittest.TestCase,Setup_Teardown):
#     def test_add(self):
#         res = add(self.x,self.y)
#         self.assertEqual(res,self.a+self.b,msg='Wrong Output')
#         print('test_add Completed Successfully') 
#     def test_sub(self):
#         res = sub(self.x,self.y)
#         self.assertEqual(res,self.a+self.b,msg='Wrong Output')
#         print('test_sub Completed Successfully')
#     def testmul(self):
#         res = mul(self.x,self.y)
#         self.assertEqual(res,self.a+self.b,msg='Wrong Output')
#         print('testmul Completed Successfully')
#     def testdiv(self):
#         res = div(self.x,self.y)
#         self.assertEqual(res,self.a+self.b,msg='Wrong Output')
#         print('testdiv Completed Successfully')


if __name__ == '__main__':
    unittest.main()
