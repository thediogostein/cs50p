"""
    Input : month/day/year
    Output: year/month/day

    Input : 9/8/1636
    Output: 1636-09-08

    Input : September 8, 1636
    Output: 1636-09-08
"""


def main():
    get_date("Date: ")


def get_date(prompt):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # prompt the user until a valid format is inputed
    while True:
        try:
            # valid month / day / year
            date = input(prompt)
            if "/" in date:
                # VALID: month/day/year
                """
                    Input : month/day/year
                    Output: year/month/day
                """
                date_arr = date.split("/")

                month = int(date_arr[0])
                day = int(date_arr[1])
                year = int(date_arr[2])

                # if valid
                    # print
                    # break
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
        except ValueError:
            pass


        else:
            try:
                # VALID: September 8, 1636
                date_arr = date.split()
                month = date_arr[0]
                month_index = months.index(month) + 1
                day = date_arr[1]
                day_without_comma = int(''.join([char for char in date_arr[1] if char.isdigit()]))
                year = date_arr[2]

                if month in months and 1 <= int(day_without_comma) <= 31 and ',' in day:
                    print(f"{year}-{month_index:02}-{day_without_comma:02}")
                    break
            except ValueError:
                pass

if __name__ == "__main__":
    main()
