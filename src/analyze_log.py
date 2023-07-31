from collections import Counter
import csv


def check_never_orders(orders, client_name, type):
    current_set = set([row[type] for row in orders])
    client_orders = [
        row[type] for row in orders if row["client"] == client_name
    ]
    return current_set.difference(set(client_orders))


def analyze_log(path_to_file: str) -> None:
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, mode="r") as file:
            csv_reader = csv.DictReader(
                file, fieldnames=["client", "order", "weekday"]
            )
            orders = list(csv_reader)

            most_ordered = Counter(
                [row["order"] for row in orders if row["client"] == "maria"]
            ).most_common(1)[0][0]
            hamburger_times = len(
                [
                    row
                    for row in orders
                    if row["client"] == "arnaldo"
                    and row["order"] == "hamburguer"
                ]
            )
            never_ordered = check_never_orders(orders, "joao", "order")
            never_weekdays = check_never_orders(orders, "joao", "weekday")

            with open("data/mkt_campaign.txt", mode="w") as file:
                file.writelines(
                    line + "\n"
                    for line in [
                        most_ordered,
                        str(hamburger_times),
                        str(never_ordered),
                        str(never_weekdays),
                    ]
                )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
