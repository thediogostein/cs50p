from validator_collection import validators, errors


def main():
    str = input("What's your email address? ")
    try:
        result = validators.email(str, allow_empty=True)
    except:
        print("Invalid")
    else:
        print("Valid")


if __name__ == "__main__":
    main()
