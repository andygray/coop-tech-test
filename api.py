def calculate_total(items=[]):
    return reduce(lambda total, item: total + (item.quantity * item.cost_per_unit), items, 0.0)


def calculate_membership_reward(items=[], membership_percentage=0.05):
    # round floating point result to 3 dp
    return round(calculate_total(items) * membership_percentage, 3)
