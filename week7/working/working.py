import re


def main():
    print(convert(input("Hours: ")))


def get_matches(s):
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError("Does match the required pattern")

    return matches


def validate(symbol, hour, minutes):
    if minutes > 59 or minutes > 59:
        raise ValueError("Minutes should be less than 59")

    if symbol == "AM":
        if hour > 12 or hour < 1:
            raise ValueError

    if symbol == "PM":
        if hour > 12 or hour < 1:
            raise ValueError

    return True


def convert(s):
    if matches := get_matches(s):
        hour_one = int(matches.group(1))
        if matches.group(2):
            minutes_one = int(matches.group(2))
        else:
            minutes_one = 0
        symbol_one = matches.group(3)

        hour_two = int(matches.group(4))
        if matches.group(5):
            minutes_two = int(matches.group(5))
        else:
            minutes_two = 0
        symbol_two = matches.group(6)

    validate(symbol_one, hour_one, minutes_one)
    validate(symbol_two, hour_two, minutes_two)

    if symbol_one == "AM":
        if hour_one == 12:
            hour_one = 0

    if symbol_one == "PM":
        if hour_one >= 1 and hour_one <= 11:
            hour_one += 12

    if symbol_two == "AM":
        if hour_two == 12:
            hour_two = 0

    if symbol_two == "PM":
        if hour_two >= 1 and hour_two <= 11:
            hour_two += 12

    return f"{hour_one:02}:{minutes_one:02} to {hour_two:02}:{minutes_two:02}"


if __name__ == "__main__":
    main()
