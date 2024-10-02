from plates import is_valid

# Denne del tester om for ting der gerne skulle returnere False korrekt

def test_is_valid_many_digits():
    assert is_valid("test123") == False

def test_is_valid_punctuation():
    assert is_valid("udb.21") == False

def test_is_valid_uppercase():
    assert is_valid("HEJ123") == False

def test_is_valid_lowercase():
    assert is_valid("hej123") == False


