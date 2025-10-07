import unittest

class TestMyUtils(unittest.TestCase):

    def test_mean(self):
        from my_utils import mean
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)
        self.assertEqual(mean([-1, -2, -3, -4, -5]), -3)
        self.assertEqual(mean([]), 0)

    def test_median(self):
        from my_utils import median
        self.assertEqual(median([1, 3, 3, 6, 7, 8, 9]), 6)
        self.assertEqual(median([1, 2, 3, 4, 5, 6, 8, 9]), 4.5)
        self.assertEqual(median([-1, -2, -3, -4, -5, -6, -8, -9]), -4.5)
        self.assertEqual(median([]), 0)

    def test_standard_deviation(self):
        from my_utils import standard_deviation
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4, 5]), 1.4142135623730951)
        self.assertAlmostEqual(standard_deviation([-1, -2, -3, -4, -5, -6, -7, -8, -9]), 2.581988897471611)
        self.assertEqual(standard_deviation([]), 0)

    def test_get_column(self):
        from my_utils import get_column
        result = get_column("unit_tests/Sample_Agrofood.csv", 1, "Zambia", 4)
        self.assertEqual(result, [18296, 18296, 18296, 18296, 18296, 18296, 8418, 8110, 7605]) 

if __name__ == '__main__':
    unittest.main()
