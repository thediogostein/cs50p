
import random
from get_cars import download_cards
from get_cars import create_csv
from get_cars import load_csv
from helpers import reveal_cards
from helpers import print_rules
from helpers import print_card
from helpers import print_report
from helpers import get_choice_str
from helpers import end_game
from helpers import start_game
from helpers import play_next_round
from helpers import get_player_choice
from helpers import deal_cards
from helpers import get_report_str


def main():

    print_rules()
    start_game()
    response = download_cards()
    create_csv(response)
    cards = load_csv()
    random.shuffle(cards)
    player_deck, ai_deck = deal_cards(cards)
    whose_turn_is_it = "player"
    report = []

    while True:
        n_cards_player = len(player_deck)
        n_cards_ai = len(ai_deck)

        if is_game_over(n_cards_player, n_cards_ai):
            game_winner = get_game_winner(n_cards_player, n_cards_ai)
            end_game(report, game_winner, len(cards))
        else:
            # game goes on
            play_next_round()
            print(card_count_msg(n_cards_player, n_cards_ai))
            player_card = player_deck.pop(0)
            ai_card = ai_deck.pop(0)
            print(f"\nWhose turn: {whose_turn_is_it}\n")

            if whose_turn_is_it == "player":
                print_card(player_card)

                player_choice = get_player_choice()
                print("Player chose:", get_choice_str(player_choice))

                is_winner = is_player_winner(player_choice, player_card, ai_card)

                report_str = get_report_str(
                    whose_turn_is_it, is_winner, player_choice, player_card, ai_card
                )
                report.append(report_str)
                if is_winner:
                    print("\nYou win\n")
                    player_deck.append(player_card)
                    player_deck.append(ai_card)
                else:
                    print("\nYou lose\n")
                    ai_deck.append(ai_card)
                    ai_deck.append(player_card)
                    whose_turn_is_it = "ai"

            elif whose_turn_is_it == "ai":
                ai_choice = get_ai_choice()
                print("AI chose:", get_choice_str(ai_choice))

                is_winner = is_player_winner(ai_choice, player_card, ai_card)

                report_str = get_report_str(
                    whose_turn_is_it, is_winner, ai_choice, player_card, ai_card
                )
                report.append(report_str)

                if is_winner:
                    print("\nYou win\n")
                    player_deck.append(player_card)
                    player_deck.append(ai_card)
                    whose_turn_is_it = "player"
                else:
                    print("\nYou lose\n")
                    ai_deck.append(ai_card)
                    ai_deck.append(player_card)

            reveal_cards(player_card, ai_card)


def get_game_winner(n_cards_player, n_cards_ai):
    if not n_cards_player:
        return "AI"
    elif not n_cards_ai:
        return "Player"


def is_player_winner(choice, p_card, ai_card):
    match choice:
        case 1:
            return p_card["top_speed"] > ai_card["top_speed"]
        case 2:
            return p_card["hp"] > ai_card["hp"]
        case 3:
            return p_card["acceleration"] < ai_card["acceleration"]
        case 4:
            return p_card["weight"] < ai_card["weight"]


def is_game_over(n_player, n_ai):
    return n_player == 0 or n_ai == 0


def get_ai_choice():
    return random.randint(1, 4)


def card_count_msg(player_deck_len, ai_deck_len):
    return f"Player has: {player_deck_len} cards | AI has: {ai_deck_len} cards"


if __name__ == "__main__":
    main()
