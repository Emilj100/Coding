import pytest
from jar import Jar

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
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
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(5)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(5)
