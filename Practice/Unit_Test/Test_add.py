from ad import add,div,mul,sub
import unittest
class SimpleTest(unittest.TestCase):

    def test_add(self):
        res=add(7,10)
        self.assertEqual(res,17, msg="This function is not giving the correct result")
    
    def test_sub(self):
        res=sub(7,10)
        self.assertEqual(res,-4, msg="This function is not giving the correct result")

    def test_div(self):
        res=div(7,10)
        self.assertEqual(res,0.9, msg="This function is not giving the correct result")

    def test_mul(self):
        res= mul(7,10)
        self.assertEqual(res,700, msg="This function is not giving the correct result")


if __name__ == '__main__':
    unittest.main()