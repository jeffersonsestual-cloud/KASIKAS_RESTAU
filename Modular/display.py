from config import STORE_NAME, WIDTH


def display_menu(lookup):
    print("=" * WIDTH)
    print(STORE_NAME.center(WIDTH))
    print("=" * WIDTH)
    current_category = None
    for number in lookup:
        name, price, choices, category = lookup[number]
        if category != current_category:
            if current_category is not None:
                print("-" * WIDTH)
            print(f"[ {category} ]")
            current_category = category
        print(f"{number:>2}. {name:<20} PHP {price:>6.2f}")
        if choices:
            print(f"     Choices: {', '.join(choices)}")
    print("=" * WIDTH)