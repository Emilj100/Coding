from bank import value

def test_value_uppercase():
    assert value("HELLO") == 0
    assert value("HEY") == 20
    assert value("DO YOU NEED HELP?") == 100


def test_value_lowercase():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("do you need help?") == 100

def test_value_punctuation():
    assert value("hello, how are you?") == 0
    assert value("hey, how are you?") == 20
    assert value("My friend, do you need help?") == 100


def test_value_number():
    assert value("hello, give me $100") == 0
    assert value("hey, give me $100") == 20
    assert value("give me $100 now") == 100

