def calculate_total(items=[]):
    return reduce(lambda total, item: total + (item.quantity * item.cost_per_unit), items, 0.0)
