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
        result = get_column("Agrofood_co2_emission.csv", 1, "United States of America", 4)
        self.assertEqual(result, [1999, 1999, 1999, 1999, 1999, 1999, 3286, 1553, 3099, 3578, 3687, 534, 1475, 1224, 1201, 915, 1086, 1558, 2068, 1093, 912, 1330, 1173, 1284, 1336, 2235, 1438, 2664, 2457, 1190, 5405]) 

if __name__ == '__main__':
    unittest.main()
