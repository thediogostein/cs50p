import sys
import os
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    students_list = get_list()

    save(students_list)


def get_list():
    students = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = [
                    name_part.strip() for name_part in row["name"].split(",")
                ]
                house = row["house"]
                students.append({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {argv[1]}")
    return students


def save(students):
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(
                {
                    "first": student["first"],
                    "last": student["last"],
                    "house": student["house"],
                }
            )


if __name__ == "__main__":
    main()
