def main():
    text = get_input()
    updated_text = shorten(text)
    print_output(updated_text)


def get_input():
    return input("Input: ")


def shorten(word):

    removed_txt = []

    for c in word:
        if c not in "aAeEiIoOuU":
            removed_txt.append(c)

    my_string = ''
    for c in removed_txt:
        my_string += c

    return my_string


def print_output(text):
    print(f"Output: {text}")


if __name__ == "__main__":
    main()
