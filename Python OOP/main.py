from menu import Menu
from order import Order


def main():
    menu = Menu()
    menu.display()
    if not Order.ask_yes_no("Order now? (y/n): "):
        print("Goodbye!")
        return

    while True:
        order = Order(menu)
        order.take_orders()
        order.compute_totals()
        order.print_receipt()

        if not Order.ask_yes_no("Would you like to order again? (y/n): "):
            print("Goodbye!")
            break

        menu.display()


if __name__ == "__main__":
    main()