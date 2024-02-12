from numb3rs import validate

def test_validate_str():
    assert validate(r"168.0.0.1") == True
    assert validate(r"cat") == False
    assert validate(r"cat.0.0.1") == False
    assert validate(r"168.0.1") == False
    assert validate(r"168.0") == False
    assert validate(r"168") == False


def test_validate_nrs():
    assert validate(r"192.168.0.1") == True
    assert validate(r"192.256.0.1") == False
    assert validate(r"192.168.256.1") == False
    assert validate(r"192.168.0.256") == False