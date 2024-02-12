from project import is_player_winner
from project import get_ai_choice
from project import card_count_msg
from project import is_game_over
from project import get_game_winner

p_card = {"top_speed": 100, "hp": 100, "acceleration": 10, "weight": 1000}
ai_card = {"top_speed": 90, "hp": 120, "acceleration": 20, "weight": 730}


def test_get_game_winner():
    assert get_game_winner(10, 0) == "Player"
    assert get_game_winner(0, 10) == "AI"


def test_is_player_winner():
    assert is_player_winner(1, p_card, ai_card) == True
    assert is_player_winner(2, p_card, ai_card) == False
    assert is_player_winner(3, p_card, ai_card) == True
    assert is_player_winner(4, p_card, ai_card) == False


def test_is_game_over():
    assert is_game_over(10, 0) == True
    assert is_game_over(0, 10) == True
    assert is_game_over(4, 6) == False


def test_get_ai_choice():
    assert 1 <= get_ai_choice() <= 4


def test_card_count_msg():
    assert card_count_msg(10, 15) == f"Player has: 10 cards | AI has: 15 cards"





