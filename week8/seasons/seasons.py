import datetime
import re
import sys
import inflect

p = inflect.engine()


def main():
    dob = get_dob()
    if validate_dob(dob):
        words = get_words(get_difference(dob))
        print(words)
    else:
        sys.exit("Invalid")


def get_words(min):
    w = p.number_to_words(min, andword="")
    return f"{w.capitalize()} minutes"


def get_dob():
    return input("Date of Birth: ").strip()


def validate_dob(dob):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", dob):
        return True
    else:
        return False


def get_difference(dob):
    today = datetime.date.today()
    year, month, day = dob.split("-")
    birthday = datetime.date(int(year), int(month), int(day))
    difference = today - birthday
    return difference.days * 24 * 60


if __name__ == "__main__":
    main()
