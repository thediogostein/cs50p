import sys
import os
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename, extension = get_filename()

    if extension != ".csv":
        sys.exit("Not a CSV file")

    try:
        table, headers = create_table(filename)
        print(tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


def create_table(f):
    table = []
    with open(f, "r") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            table.append([row[headers[0]], row[headers[1]], row[headers[2]]])
    return table, headers


def get_filename():
    name, extension = os.path.splitext(sys.argv[1])
    filename = f"{name}{extension}"

    return filename, extension


if __name__ == "__main__":
    main()
