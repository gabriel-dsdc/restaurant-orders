from collections import Counter


class TrackOrders:
    def __init__(self) -> None:
        self.orders = []

    def __len__(self) -> int:
        return len(self.orders)

    def get_all_info(self, type):
        return set([order[type] for order in self.orders])

    def add_new_order(self, customer: str, order: str, day: str):
        self.orders.append({"customer": customer, "order": order, "day": day})

    def get_most_ordered_dish_per_customer(self, customer):
        return Counter(
            [
                order["order"]
                for order in self.orders
                if order["customer"] == customer
            ]
        ).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        all_orders_by_order = self.get_all_info("order")
        customer_orders = [
            order["order"]
            for order in self.orders
            if order["customer"] == customer
        ]
        return all_orders_by_order.difference(set(customer_orders))

    def get_days_never_visited_per_customer(self, customer):
        all_orders_by_day = self.get_all_info("day")
        customer_orders = [
            order["day"]
            for order in self.orders
            if order["customer"] == customer
        ]
        return all_orders_by_day.difference(set(customer_orders))

    def get_busiest_day(self):
        return Counter([order["day"] for order in self.orders]).most_common(1)[
            0
        ][0]

    def get_least_busy_day(self):
        return Counter([order["day"] for order in self.orders]).most_common()[
            -1
        ][0]
