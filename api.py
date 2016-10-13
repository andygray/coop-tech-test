MEMBERSHIP_REWARD = 0.05
COMMUNITY_REWARD = 0.01

REWARD_MEMBERSHIP_MAPPING = {
    'normal': 0.05,
    'extra': 0.06,
}

REWARD_COMMUNITY_MAPPING = {
    'normal': 0.01,
    'extra': 0.02,
}


def calculate_total(items=[]):
    return reduce(lambda total, item: total + (item.quantity * item.cost_per_unit), items, 0.0)


def calculate_reward(percentage, items=[]):
    # round floating point result to 3 dp
    return round(calculate_total(items) * percentage, 3)


def calculate_reward_from_item_type(mappings, items=[]):
    return round(reduce(lambda total, item: total + ((item.quantity * item.cost_per_unit) * _get_reward_percentage_or_zero(mappings, item.item_type)), items, 0.0), 3)


def _get_reward_percentage_or_zero(mappings, key):
    if key in mappings:
        return mappings.get(key)

    return 0.0
