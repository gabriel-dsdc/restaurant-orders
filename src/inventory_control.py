from collections import Counter


class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.orders = []

    def add_new_order(self, customer, order, day):
        self.orders.append(dict(customer=customer, order=order, day=day))

    def get_quantities_to_buy(self):
        ingredients_to_buy = {key: 0 for key in self.MINIMUM_INVENTORY.keys()}
        orders_qty = Counter([order["order"] for order in self.orders])
        for order, qty in orders_qty.items():
            for ingredient in self.INGREDIENTS[order]:
                ingredients_to_buy[ingredient] += qty
        return ingredients_to_buy
