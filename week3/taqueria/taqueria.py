def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    add_to_total(menu)


def add_to_total(menu):
    total = 0
    while True:
        try:
            total += get_price(menu)
            print(f"Total: ${format(total, '.2f')}")
        except EOFError:
            print("\n")
            break


def get_price(menu):
    while True:
        try:
            user_choice = input("Item: ").title()
            price = menu[user_choice]
            return price
        except KeyError:
            pass


if __name__ == "__main__":
    main()
