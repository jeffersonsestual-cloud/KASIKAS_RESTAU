import datetime


class Order:
    BULK_QTY = 5
    BULK_RATE = 0.05
    STUDENT_RATE = 0.10

    def __init__(self, menu):
        self.menu = menu
        self.items = []          # list of (name, qty, price)
        self.is_student = False
        self.subtotal = 0.0
        self.discount = 0.0
        self.discount_label = None
        self.total = 0.0

    @staticmethod
    def ask_yes_no(prompt):
        while True:
            answer = input(prompt).strip().lower()
            if answer in ("y", "yes"):
                return True
            if answer in ("n", "no"):
                return False
            print("  Invalid choice! Please enter 'y' or 'n'.")

    @staticmethod
    def choose_option(choices):
        while True:
            print("  Choose one:")
            for i, choice in enumerate(choices, 1):
                print(f"    {i}. {choice}")
            raw = input("  Option : ").strip()
            if raw.isdigit() and 1 <= int(raw) <= len(choices):
                return choices[int(raw) - 1]
            print("  Invalid option.")

    def get_item_and_qty(self):
        while True:
            raw = input("Item number: ").strip()
            if raw.isdigit() and int(raw) in self.menu.items:
                break
            print("  Invalid item number.")
        name, price, choices, category = self.menu.items[int(raw)]

        if choices:
            name = f"{name} ({self.choose_option(choices)})"

        while True:
            raw_qty = input("Quantity: ").strip()
            if raw_qty.isdigit() and int(raw_qty) > 0:
                break
            print("  Invalid quantity.")

        self.items.append((name, int(raw_qty), price))

    def take_orders(self):
        while True:
            self.get_item_and_qty()
            if not self.ask_yes_no("Order another item? (y/n): "):
                break
        self.is_student = self.ask_yes_no("Are you a student? (y/n): ")

    def compute_totals(self):
        self.subtotal = sum(qty * price for _, qty, price in self.items)
        total_qty = sum(qty for _, qty, _ in self.items)

        # Priority: Student > Bulk (only one discount applies)
        if self.is_student:
            self.discount = self.subtotal * self.STUDENT_RATE
            self.discount_label = "Student Discount (10%)"
        elif total_qty >= self.BULK_QTY:
            self.discount = self.subtotal * self.BULK_RATE
            self.discount_label = "Discount (5%)"
        else:
            self.discount = 0.0
            self.discount_label = None

        self.total = self.subtotal - self.discount

    def print_receipt(self):
        w = self.menu.width
        print("\n" + "=" * w)
        print(self.menu.store_name.center(w))
        print(datetime.datetime.now().strftime("%b %d, %Y %I:%M %p").center(w))
        print("-" * w)
        for item, qty, price in self.items:
            detail = f"{qty:>2} x {price:>6.2f} = {qty * price:>7.2f}"
            print(item)
            print(f"{detail:>{w}}")
        print("-" * w)
        print(f"{'SUBTOTAL':<25}{self.subtotal:>15.2f}")
        if self.discount_label:
            print(f"{self.discount_label:<25}{-self.discount:>15.2f}")
        print(f"{'TOTAL':<25}{self.total:>15.2f}")
        print("=" * w)
        print("Thank you, come again!".center(w))
        print("=" * w + "\n")