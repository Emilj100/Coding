from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(3)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(5)



def test_withdraw():
    jar = Jar()

    jar.deposit(3)

    with pytest.raises(ValueError):
        jar.withdraw(5)
