import unittest

from api import calculate_total
from item import Item


class TestApi(unittest.TestCase):
    def test_calc_no_items(self):
        self.assertEqual(calculate_total([]), 0.0)

    def test_calc_items(self):
        items = [
            Item(name='Bread', quantity=2, cost_per_unit=1.25),
            Item(name='Coffee', quantity=1, cost_per_unit=2),
            Item(name='Lottery ticket', quantity=2, cost_per_unit=2),
        ]

        self.assertEqual(calculate_total(items), 8.5)
