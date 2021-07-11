import statistics
import unittest

from src.Randomgenerator.randomgenerator import genrandlist
from src.Statistics.statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        testdata = genrandlist(0, 1000, 2, 500)
        for num in testdata:
            self.assertIsInstance(num, float)
        self.statcalc = Statistics(testdata)

    def test_instantiate_statcalculator(self):
        self.assertIsInstance(self.statcalc, Statistics)

    def test_results_property(self):
        self.assertEqual(self.statcalc.result, 0)

    def test_mean(self):
        calculated_mean = self.statcalc.mean()
        correct_mean = statistics.mean(self.statcalc.data)
        self.assertAlmostEqual(calculated_mean, correct_mean)
        self.assertEqual(calculated_mean, self.statcalc.result)

    def test_variance(self):
        calculated_variance = self.statcalc.variance()
        correct_var = statistics.variance(self.statcalc.data)
        self.assertAlmostEqual(calculated_variance, correct_var)
        self.assertEqual(calculated_variance, self.statcalc.result)

    def test_standarddev(self):
        calculated_standarddev = self.statcalc.standarddev()
        correct_stddev = statistics.stdev(self.statcalc.data)
        self.assertAlmostEqual(calculated_standarddev, correct_stddev)
        self.assertEqual(calculated_standarddev, self.statcalc.result)
        
    def test_median(self):
        calculated_median = self.statcalc.median()
        correct_median = statistics.median(self.statcalc.data)
        self.assertAlmostEqual(calculated_median, correct_median)
        self.assertEqual(calculated_median, self.statcalc.result)
        
    def test_mode(self):
        calculated_mode = self.statcalc.mode()
        correct_mode = statistics.mode(self.statcalc.data)
        self.assertAlmostEqual(calculated_mode, correct_mode)
        self.assertEqual(calculated_mode, self.statcalc.result)


if __name__ == '__main__':
    unittest.main()