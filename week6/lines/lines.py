import sys
import os


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    name, extension = os.path.splitext(sys.argv[1])

    if extension != ".py":
        sys.exit("Not a Python file")

    try:
        lines = count_lines(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(lines)


def count_lines(filename):
    nr_of_lines = 0
    with open(filename, "r") as file:
        for line in file:
            if not line.isspace() and not line.lstrip().startswith("#"):
                nr_of_lines += 1

    return nr_of_lines


if __name__ == "__main__":
    main()
