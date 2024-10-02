from bank import value

def test_value_uppercase():
    assert value("HELLO") == "$0"
    assert value("HEY") == "$20"
    assert value("Do you need help?")


def test_value_lowercase():
    assert value("hello") == "$0"
    assert value("hey") == "$20"

def test_value_punctuation():
    assert value("hello, how are you?") == "$0"
    assert value("hey, how are you?") == "$0"


def test_value_number():
    assert value("hello, give me $100") == "$0"
    assert value("hey, give me $100") == "$20"

