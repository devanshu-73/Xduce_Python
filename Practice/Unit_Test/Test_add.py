from ad import add,div,mul,sub
import unittest
class SimpleTest(unittest.TestCase):

    def test_add(self):
        res=add(70,10)
        self.assertEqual(res,80, msg="This function is not giving the correct result")
    
    def test_sub(self):
        res=sub(70,10)
        self.assertEqual(res,60, msg="This function is not giving the correct result")

    def test_div(self):
        res=div(70,10)
        self.assertEqual(res,7, msg="This function is not giving the correct result")

    def test_mul(self):
        res= mul(70,10)
        self.assertEqual(res,700, msg="This function is not giving the correct result")


if __name__ == '__main__':
    unittest.main()