def main():
    user_input = input("camelCase: ")
    print(get_snake_case(user_input))


def get_snake_case(input_str):
    new = []
    for c in input_str:
        if c.isupper():
            new.append("_")
            new.append(c.lower())
        else:
            new.append(c)

    return "".join(new)


main()
