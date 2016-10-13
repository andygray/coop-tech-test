import unittest

from api import calculate_total, calculate_reward, calculate_reward_from_item_type, MEMBERSHIP_REWARD, COMMUNITY_REWARD, REWARD_MEMBERSHIP_MAPPING, REWARD_COMMUNITY_MAPPING
from item import Item

items = [
    Item(name='Bread', quantity=2, cost_per_unit=1.25, item_type='normal'),
    Item(name='Coffee', quantity=1, cost_per_unit=2, item_type='extra'),
    Item(name='Lottery ticket', quantity=2, cost_per_unit=2),
]


class TestApi(unittest.TestCase):
    def test_calc_no_items(self):
        self.assertEqual(calculate_total([]), 0.0)

    def test_calc_items(self):
        self.assertEqual(calculate_total(items), 8.5)

    def test_calc_membership_reward(self):
        self.assertEqual(calculate_reward(MEMBERSHIP_REWARD, items), 0.425)

    def test_calc_community_reward(self):
        self.assertEqual(calculate_reward(COMMUNITY_REWARD, items), 0.085)

    def test_calc_membership_reward_from_item_type(self):
        self.assertEqual(calculate_reward_from_item_type(REWARD_MEMBERSHIP_MAPPING, items), 0.245)

    def test_calc_community_reward_from_item_type(self):
        self.assertEqual(calculate_reward_from_item_type(REWARD_COMMUNITY_MAPPING, items), 0.065)
