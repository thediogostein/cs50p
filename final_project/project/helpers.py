import os
import sys


def reveal_cards(p_card, ai_card):
    print()
    print(f"{'YOUR CARD':27}{'|':5}{'AIs CARD':27}")
    print(f"{'-----':27}{'|':5}{'-----':27}")
    print(f"{p_card['name']:27}{'|':5}{ai_card['name']:27}")
    print(
        f"{'Top Speed:':12}{p_card['top_speed']:5} {'km/h':4}{'':5}{'|':5}{'Top Speed:':12}{ai_card['top_speed']:5} {'km/h':4}"
    )
    print(
        f"{'Horsepower:':12}{p_card['hp']:5} {'hp':4}{'':5}{'|':5}{'Horsepower:':12}{ai_card['hp']:5} {'hp':4}"
    )
    print(
        f"{'0-100 km/h:':12}{p_card['acceleration']:5} {'sec':4}{'':5}{'|':5}{'0-100 km/h:':12}{ai_card['acceleration']:5} {'sec':4}"
    )
    print(
        f"{'Weight:':12}{p_card['weight']:5} {'kg':4}{'':5}{'|':5}{'Weight:':12}{ai_card['weight']:5} {'kg':4}"
    )
    print()


def print_rules():
    os.system("clear")
    print("\nRules of the game: \n")
    print(
        "There are 10 cards in this game, they are shuffled and then the player and the AI get 5 cards each."
    )
    print("The player is the first to play, and is prompted to pick from a list.")
    print()
    print("The fastest car wins the round.")
    print("The car with the most HP wins the round.")
    print("The car that goes from 0 - 100 km/h in less time wins the round.")
    print("The lightest car wins the round.")
    print("----")
    print("The game ends when either the player or the AI has 0 cards.")
    print("The winner is the one with all the cards")
    print()


def print_card(card):
    print()
    print(f"Car: {card['name']}")
    print(f"----------------------------------")
    print(f"1 - Top speed:  {card['top_speed']} km/h")
    print(f"2 - Horsepower: {card['hp']}")
    print(f"3 - 0-100 km/h: {card['acceleration']} seconds")
    print(f"4 - Weight:     {card['weight']} kg")
    print()


def print_report(report):
    print("\nReport:\n")
    for i, sentence in enumerate(report, start=1):
        print(
            "------------------------------------------------------------------------------------------------------"
        )
        print(f"Round: {i} ---", sentence)
        print(
            "------------------------------------------------------------------------------------------------------"
        )
    print("\n\n")


def get_choice_str(n):
    match n:
        case 1:
            return "Top speed"
        case 2:
            return "HP"
        case 3:
            return "0-100 km/h"
        case 4:
            return "weight"


def start_game():
    while True:
        try:
            str = input("Type play to start game: ")
            if str == "play":
                os.system("clear")
                break
        except ValueError:
            pass


def end_game(report, winner, n_cards):
    os.system("clear")
    print("Game over")
    print(f"{winner} wins!")
    print(f"{winner} has all {n_cards} cards.")
    print_report(report)
    sys.exit()


def play_next_round():
    while True:
        try:
            str = input("Type n to play round: ")
            if str == "n":
                os.system("clear")
                return str
        except ValueError:
            pass


def get_player_choice():
    while True:
        try:
            n = int(input("Choose 1-4: "))
            if 1 <= n <= 4:
                return n
        except ValueError:
            pass


def deal_cards(deck):
    mid_index = len(deck) // 2

    player = deck[:mid_index]
    ai = deck[mid_index:]

    return player, ai


def get_report_str(whose_turn, is_winner, choice, p_card, ai_card):
    p_value = ""
    ai_value = ""
    match choice:
        case 1:
            p_value = p_card["top_speed"]
            ai_value = ai_card["top_speed"]
            choice_str = "Top speed"
        case 2:
            p_value = p_card["hp"]
            ai_value = ai_card["hp"]
            choice_str = "HP"
        case 3:
            p_value = p_card["acceleration"]
            ai_value = ai_card["acceleration"]
            choice_str = "0-100 km/h"
        case 4:
            p_value = p_card["weight"]
            ai_value = ai_card["weight"]
            choice_str = "Weight"

    if is_winner:
        winner_str = "yes"
    else:
        winner_str = "no"

    return f"Turn: {whose_turn:6} | Is player winner: {winner_str:5} | Choice: {choice_str:10} | Player: {p_value:3} - AI: {ai_value:3}"
