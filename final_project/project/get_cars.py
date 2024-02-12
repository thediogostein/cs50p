import csv
import requests

def download_cards():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQojfnpU3gv25XMKeZQMnV-ld54-DRGzKJV5NOIQNjnG9S5hL8JFwCNneJI-oDck5bFBS44vCNzzqQn/pub?gid=0&single=true&output=csv"

    try:
        return requests.get(url)
    except:
        sys.exit("Couldn't download list of cars")


def create_csv(res):
    try:
        with open("cars.csv", "w") as f:
            f.write(res.text)
    except:
        sys.exit("Couldn't create the cars.csv file")

def load_csv():
    cards = []

    with open("cars.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cards.append(
                {
                    "name": row["car"],
                    "top_speed": int(row["top_speed"]),
                    "hp": int(row["hp"]),
                    "acceleration": float(row["acceleration"]),
                    "weight": int(row["weight"]),
                }
            )

    return cards
