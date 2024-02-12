import json
import requests
import sys

def main():
    ## Check for arguments
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    n = convert_to_float()
    result = n * get_price()

    print(f"${result:,.4f}")


def convert_to_float():
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
        

def get_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        return o["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error connecting to api")


if __name__ == "__main__":
    main()
