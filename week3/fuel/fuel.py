def main():
    result = fuel_gauge("Fraction? ")

    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result}%")



def fuel_gauge(prompt):
    while True:
        try:
            user_input = input(prompt)
            arr = user_input.split("/")
            x = int(arr[0])
            y = int(arr[1])
            if x <= y:
                return round((x / y) * 100)

        except (ValueError, ZeroDivisionError, IndexError):
            pass



if __name__ == "__main__":
    main()

