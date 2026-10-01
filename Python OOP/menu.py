MENU = {
    "Platters": {
        "Chicken Platter": {
            "price": 200.00,
            "choices": ["|BBQ Sauce|", "|Sweet and Spicy|", "|Honey Glaze|"],
        },
        "Pancit Canton Platter": {
            "price": 120.00,
            "choices": ["|Sotanghon|", "|Pancit Guisado|"],
        },
    },
    "Drinks": {
        "Shake": {
            "price": 90.00,
            "choices": ["|Chocolate|", "|Strawberry|", "|Mango|"],
        },
    },
}


class Menu:
    def __init__(self, store_name="KASIKAS NI SUPER JEFF", width=40):
        self.store_name = store_name
        self.width = width
        self.items = self.build_item_lookup()

    def build_item_lookup(self):
        lookup = {}
        number = 1
        for category in MENU:
            for item in MENU[category]:
                data = MENU[category][item]
                lookup[number] = (item, data["price"], data.get("choices"), category)
                number += 1
        return lookup

    def display(self):
        print("=" * self.width)
        print(self.store_name.center(self.width))
        print("=" * self.width)
        current_category = None
        for number in self.items:
            name, price, choices, category = self.items[number]
            if category != current_category:
                if current_category is not None:
                    print("-" * self.width)
                print(f"[ {category} ]")
                current_category = category
            print(f"{number:>2}. {name:<20} PHP {price:>6.2f}")
            if choices:
                print(f"     Choices: {', '.join(choices)}")
        print("=" * self.width)