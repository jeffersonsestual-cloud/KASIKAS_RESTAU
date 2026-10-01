from prompts import ask_yes_no, choose_option


def get_item_and_qty(lookup):
    while True:
        raw = input("Item number: ").strip()
        if raw.isdigit() and int(raw) in lookup:
            break
        print("  Invalid item number.")
    name, price, choices, category = lookup[int(raw)]

    if choices:
        selected = choose_option(choices)
        name = f"{name} ({selected})"

    while True:
        raw_qty = input("Quantity: ").strip()
        if raw_qty.isdigit() and int(raw_qty) > 0:
            break
        print("  Invalid quantity.")

    return name, int(raw_qty), price


def take_orders(lookup):
    orders = []
    while True:
        orders.append(get_item_and_qty(lookup))
        if not ask_yes_no("Order another item? (y/n): "):
            break
    return orders