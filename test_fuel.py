from fuel import convert, gauge

def test_convert_inputs():
    assert convert("37/88") == 42
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_symbols()
    assert convert("37.88") == 42
    assert convert("3-4") == 75
    assert convert("1*4") == 25

def test_convert_


