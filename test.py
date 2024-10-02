from plates import is_valid

# Test for ugyldige nummerplader (False)
def test_invalid_starts_with_number():
    assert not is_valid("123ABC")  # Starter med tal

def test_invalid_too_long():
    assert not is_valid("ABCDEFG")  # Længde større end 6

def test_invalid_punctuation():
    assert not is_valid("ABC!23")  # Indeholder tegnsætning

def test_invalid_middle_number():
    assert not is_valid("ABC12D")  # Tal i midten

def test_invalid_leading_zero():
    assert not is_valid("ABC012")  # Første tal er 0

# Test for gyldige nummerplader (True)
def test_valid_simple():
    assert is_valid("ABC123")  # Gyldig plade

def test_valid_letters_only():
    assert is_valid("ABCDEF")  # Kun bogstaver, ingen tal

def test_valid_mixed_case():
    assert is_valid("AbC123")  # Blandede store og små bogstaver

def test_valid_min_length():
    assert is_valid("AB")  # Minimal længde (2 tegn)

def test_valid_no_numbers():
    assert is_valid("XYZ")  # Kun bogstaver, kort plade

# Test edge cases
def test_valid_edge_case():
    assert is_valid("A1")  # Gyldig med minimal længde og tal

def test_invalid_empty():
    assert not is_valid("")  # Tom streng

def test_invalid_single_letter():
    assert not is_valid("A")  # For kort, kun ét bogstav
