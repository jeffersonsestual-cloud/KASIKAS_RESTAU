import datetime
from config import STORE_NAME, WIDTH


def print_receipt(orders, subtotal, discount, discount_label, total):
    print("\n" + "=" * WIDTH)
    print(STORE_NAME.center(WIDTH))
    print(datetime.datetime.now().strftime("%b %d, %Y %I:%M %p").center(WIDTH))
    print("-" * WIDTH)
    for item, qty, price in orders:
        line_total = qty * price
        detail = f"{qty:>2} x {price:>6.2f} = {line_total:>7.2f}"
        print(item)
        print(f"{detail:>{WIDTH}}")
    print("-" * WIDTH)
    print(f"{'SUBTOTAL':<25}{subtotal:>15.2f}")
    if discount_label:
        print(f"{discount_label:<25}{-discount:>15.2f}")
    print(f"{'TOTAL':<25}{total:>15.2f}")
    print("=" * WIDTH)
    print("Thank you, come again!".center(WIDTH))
    print("=" * WIDTH + "\n")