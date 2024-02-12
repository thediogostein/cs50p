from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(4)
    assert jar.capacity == 4


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3


def test_withdraw():
    jar = Jar(10)
    jar.deposit(9)
    jar.withdraw(9)
    assert jar.size == 0


def test_deposit_raises_value_error():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)


def test_withdraw_raises_value_error():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(6)
