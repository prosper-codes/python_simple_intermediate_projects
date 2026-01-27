import unittest
import simple_testing.unit_testing.calculate as calculate

class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.calculate = calculate.Calculate()
        
    def tearDown(self):
        return super().tearDown()

    def test_add(self):
        self.assertEqual(self.calculate.add(2, 5), 7)

    def test_subt(self):
        self.assertEqual(self.calculate.subt(6, 4), 2)

    def test_mult(self):
        self.assertEqual(self.calculate.mult(3, 2), 6)
        self.assertEqual(self.calculate.mult(1, 4), 4)

    def test_div(self):
        self.assertEqual(self.calculate.div(4, 2), 2)
        with self.assertRaises(ValueError):
            self.calculate.div(10,0)     

if __name__ == '__main__':
    unittest.main()
