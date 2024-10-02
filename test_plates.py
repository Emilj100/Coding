from plates import is_valid

# Denne del tester om for ting der gerne skulle returnere False korrekt

def test_is_valid_many_digits():
    assert is_valid("test123") == False

def test_is_valid_punctuation():
    assert is_valid("udb.21") == False

def test_is_valid_uppercase():
    assert is_valid("HEJ023") == False

def test_is_valid_lowercase():
    assert is_valid("hej023") == False

# Denne del tester for ting der gerne skulle returnere True korrekt

def test_is_valid_many_digits1():
    assert is_valid("abc123") == True

def test_is_valid_uppercase1():
    assert is_valid("ABCDEF") == True

def test_is_valid_lowercase1():
    assert is_valid("ab12") == True
