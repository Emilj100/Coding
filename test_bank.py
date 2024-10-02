from bank import value

def test_value_uppercase():
    assert value("HELLO") == "$0"
    assert value("HEY") == "$20"


def test_value_lowercase():
