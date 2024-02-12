def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print_answer(answer)


def print_answer(str):
    match str.lower().strip():
        case "forty-two" | "forty two" | "42":
            print("Yes")
        case _:
            print("No")


main()
