from seasons import get_words
from seasons import validate_dob

def test_get_words():
    assert get_words(100) == "One hundred minutes"


def test_validate_dob():
    assert validate_dob("1983-03-31") == True
