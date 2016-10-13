MEMBERSHIP_REWARD = 0.05
COMMUNITY_REWARD = 0.01


def calculate_total(items=[]):
    return reduce(lambda total, item: total + (item.quantity * item.cost_per_unit), items, 0.0)


def calculate_reward(percentage, items=[]):
    # round floating point result to 3 dp
    return round(calculate_total(items) * percentage, 3)
