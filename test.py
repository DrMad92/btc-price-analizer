import main
import unittest
from collections import namedtuple

Point = namedtuple('Point', ['day', 'value'])


class KnownValues(unittest.TestCase):
    data = [(1, 100),
            (2, 110),
            (3, 120),
            (4, 130),
            (5, 140),
            (6, 150),
            (7, 140),
            (8, 130),
            (9, 100),
            (10, 70)]
    knownValues = [Point(day=day, value=value) for day, value in data]

    def test_greatest_increase(self):
        """Test greatest_increase with known value"""
        result = main.greatest_increase(self.knownValues)
        self.assertEqual(result, (10, 2))

    def test_greatest_decrease(self):
        """Test greatest_decrease with known value"""
        result = main.greatest_decrease(self.knownValues)
        self.assertEqual(result, (30, 10))

    def test_highest_price(self):
        """Test highest_price with known value"""
        result = main.highest_price(self.knownValues)
        self.assertEqual(result, (150, 6))


class InvalidInput(unittest.TestCase):
    dataNone = [(1, 100),
                (2, 430),
                (3, None)]
    invalidInputNone = [Point(day=day, value=value) for day, value in dataNone]

    def test_greatest_increase_none(self):
        """Test greatest_increase with None input should raise TypeError"""
        self.assertRaises(TypeError, main.greatest_increase, self.invalidInputNone)

    def test_greatest_decrease_none(self):
        """Test greatest_decrease with None input should raise TypeError"""
        self.assertRaises(TypeError, main.greatest_decrease, self.invalidInputNone)

    def test_highest_price_none(self):
        """Test highest_price with None input should raise TypeError"""
        self.assertRaises(TypeError, main.highest_price, self.invalidInputNone)

    dataString = [(1, 100),
                  (2, 430),
                  (3, 'ABcn')]
    invalidInputStr = [Point(day=day, value=value) for day, value in dataString]

    def test_greatest_increase_string(self):
        """Test greatest_increase with String input should raise TypeError"""
        self.assertRaises(TypeError, main.greatest_increase, self.invalidInputStr)

    def test_greatest_decrease_string(self):
        """Test greatest_decrease with String input should raise TypeError"""
        self.assertRaises(TypeError, main.greatest_decrease, self.invalidInputStr)

    def test_highest_price_string(self):
        """Test highest_price with String should raise TypeError"""
        self.assertRaises(TypeError, main.highest_price, self.invalidInputStr)

    dataInf = [(1, 100),
               (2, 430),
               (3, float('inf'))]
    invalidInputInf = [Point(day=day, value=value) for day, value in dataInf]

    def test_greatest_increase_inf(self):
        """Test greatest_increase with Infinity input should raise ValueError"""
        self.assertRaises(ValueError, main.greatest_increase, self.invalidInputInf)

    def test_greatest_decrease_inf(self):
        """Test greatest_decrease with Infinity input should raise ValueError"""
        self.assertRaises(ValueError, main.greatest_decrease, self.invalidInputInf)

    def test_highest_price_inf(self):
        """Test highest_price with Infinity input should raise ValueError"""
        self.assertRaises(ValueError, main.highest_price, self.invalidInputInf)

    dataNan = [(1, 100),
               (2, 430),
               (3, float('nan'))]
    invalidInputNan = [Point(day=day, value=value) for day, value in dataNan]

    def test_greatest_increase_nan(self):
        """Test greatest_increase with NaN input should raise ValueError"""
        self.assertRaises(ValueError, main.greatest_increase, self.invalidInputNan)

    def test_greatest_decrease_nan(self):
        """Test greatest_decrease with NaN input should raise ValueError"""
        self.assertRaises(ValueError, main.greatest_decrease, self.invalidInputNan)

    def test_highest_price_nan(self):
        """Test highest_price with NaN input should raise ValueError"""
        self.assertRaises(ValueError, main.highest_price, self.invalidInputNan)


if __name__ == '__main__':
    unittest.main()
