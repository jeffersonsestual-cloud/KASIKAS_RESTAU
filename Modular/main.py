from config import MENU
from lookup import build_item_lookup
from display import display_menu
from prompts import ask_yes_no
from orders import take_orders
from totals import compute_totals
from receipt import print_receipt


def main():
    lookup = build_item_lookup(MENU)

    display_menu(lookup)
    if not ask_yes_no("Order now? (y/n): "):
        print("Goodbye!")
        return

    while True:
        orders = take_orders(lookup)
        is_student = ask_yes_no("Are you a student? (y/n): ")
        subtotal, discount, label, total = compute_totals(orders, is_student)
        print_receipt(orders, subtotal, discount, label, total)

        if not ask_yes_no("Would you like to order again? (y/n): "):
            print("Goodbye!")
            break

        display_menu(lookup)


if __name__ == "__main__":
    main()