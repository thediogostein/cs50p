def main():
    greeting = input("Greeting: ").lower()
    prize = get_prize(greeting)
    print(f"${prize}")


def get_prize(sentence):
    if sentence.count("hello"):
        return 0
    elif sentence.startswith("h"):
        return 20
    else:
        return 100


main()
