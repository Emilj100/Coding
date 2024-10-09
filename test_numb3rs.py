from numb3rs import validate

def test_validate():
    assert validate("2.3.4.5") == True
    assert validate("226.953.245.541") == False

def test_validate_string():
    assert validate("cat") == False
    assert validate("test") == False


