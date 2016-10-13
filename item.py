
class Item(object):

    def __init__(self, name=None, quantity=1, cost_per_unit=0.0, item_type=None):
        self.name = name
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit
        self.item_type = item_type