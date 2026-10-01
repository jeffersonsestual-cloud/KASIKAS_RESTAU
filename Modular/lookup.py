def build_item_lookup(menu):
    lookup = {}
    number = 1
    for category in menu:
        for item in menu[category]:
            data = menu[category][item]
            lookup[number] = (item, data["price"], data.get("choices"), category)
            number += 1
    return lookup