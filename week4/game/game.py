import random


def main():
    random_number = random.randint(1, get_level())

    while True:
        guess = get_guess(random_number)
        result = compare(random_number, guess)
        print(result)
        if result == "Just right!":
            break


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass


def get_guess(n):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess >= 0:
                return guess
        except ValueError:
            pass


def compare(r_num, guess):
    if guess < r_num:
        return "Too small!"
    elif guess > r_num:
        return "Too large!"
    else:
        return "Just right!"


if __name__ == "__main__":
    main()
