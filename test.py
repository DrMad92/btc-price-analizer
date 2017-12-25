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
        """Test greatest_increase percentage and day"""
        result = main.greatest_increase(self.knownValues)
        self.assertEqual(result, (10, 2))

    def test_greatest_decrease(self):
        """Test greatest_decrease percentage and day"""
        result = main.greatest_decrease(self.knownValues)
        self.assertEqual(result, (30, 10))

    def test_highest_price(self):
        """Test highest_price"""
        result = main.highest_price(self.knownValues)
        self.assertEqual(result, (150, 6))


if __name__ == '__main__':
    unittest.main()
