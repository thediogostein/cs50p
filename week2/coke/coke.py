# 25, 10, 5

def main():
    amount_due = 50
    while amount_due > 0:
        coin = get_coin(amount_due)
        amount_due -= coin
    print(f"Change Owed: {abs(amount_due)}")


def get_coin(amount_d):
    while True:
        print(f"Amount Due: {amount_d}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            return coin


main()
