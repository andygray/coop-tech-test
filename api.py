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


def calculate_membership_reward_from_item_type(items=[]):
    return reduce(lambda total, item: total + ((item.quantity * item.cost_per_unit) * _get_reward_percentage_or_zero(REWARD_MEMBERSHIP_MAPPING, item.item_type)), items, 0.0)


def calculate_community_reward_from_item_type(items=[]):
    return reduce(lambda total, item: total + ((item.quantity * item.cost_per_unit) * _get_reward_percentage_or_zero(REWARD_COMMUNITY_MAPPING, item.item_type)), items, 0.0)


def _get_reward_percentage_or_zero(mappings, key):
    if key in mappings:
        return mappings.get(key)

    return 0.0
