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
        ingredients_in_use = self.get_quantities_to_buy()

        for ingredient in self.INGREDIENTS[order]:
            if (ingredients_in_use[ingredient] + 1) > self.MINIMUM_INVENTORY[
                ingredient
            ]:
                return False
        self.orders.append(dict(customer=customer, order=order, day=day))

    def get_quantities_to_buy(self) -> dict[str, int]:
        ingredients_to_buy = {key: 0 for key in self.MINIMUM_INVENTORY.keys()}
        orders_qty = Counter([order["order"] for order in self.orders])
        for order, qty in orders_qty.items():
            for ingredient in self.INGREDIENTS[order]:
                ingredients_to_buy[ingredient] += qty
        return ingredients_to_buy

    def get_available_dishes(self) -> set[str]:
        available_dishes = set()
        ingredients_in_use = self.get_quantities_to_buy()

        for order, ingredients in self.INGREDIENTS.items():
            is_dish_valid = True

            for ingredient in ingredients:
                if (
                    self.MINIMUM_INVENTORY[ingredient]
                    - ingredients_in_use[ingredient]
                ) == 0:
                    is_dish_valid = False
            if is_dish_valid:
                available_dishes.add(order)
        return available_dishes
