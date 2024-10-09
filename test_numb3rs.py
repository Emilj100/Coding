from numb3rs import validate

def test_validate():
    assert validate("2.3.4.5") == True
