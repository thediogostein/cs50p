import random


def main():
    level = get_level()
    score = 0

    # 10 questions
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        attempts = 0
        while True:
            user_answer = get_input(x, y)
            correct_answer = x + y
            if user_answer == correct_answer:
                score += 1
                break
            else:
                print("EEE")
                attempts += 1

            if attempts == 3:
                print(f"{x} + {y} = {correct_answer}")
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            raise ValueError


def get_input(n1, n2):
    str = input(f"{n1} + {n2} = ")
    # if user doesn't input a number then the return number is set to a negative number
    # and this will not equal to the correct answer
    if str.isdigit():
        return int(str)
    else:
        return -100


if __name__ == "__main__":
    main()
