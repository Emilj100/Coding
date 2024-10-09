from numb3rs import validate

def test_validate():
    # Gyldige IPv4-adresser
    assert validate("192.168.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

    # Ugyldige IPv4-adresser
    assert validate("256.256.256.256") == False  # 256 er uden for det gyldige interval
    assert validate("123.456.78.90") == False    # 456 er uden for det gyldige interval
    assert validate("192.168.1") == False        # Mangler en oktet
    assert validate("192.168.one.1") == False    # Indeholder bogstaver
    assert validate("...") == False              # Ingen tal, kun punktummer
    assert validate("192.168.0.01") == True      # Gyldigt format, da 01 betragtes som 1
    assert validate("1234.1.1.1") == False       # Første oktet har for mange cifre
