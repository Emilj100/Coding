from fuel import convert, gauge

def test_convert_inputs():
    assert convert("37/88") == 42
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_symbols():
    assert convert("37.88") == 42
    assert convert("3-4") == 75
    assert convert("1*4") == 25

def test_convert_str():
    assert convert(37/88) == 42
    assert convert(3/4) == 75
    assert convert(1/4) == 25

def test_convert_x():
    assert convert(88/37) == 42
    assert convert(4/3) == 75
    assert convert(4/1) == 25

def test_convert_100():
    assert convert(75/125) == 100
    assert convert(-25/-30) == 50
    assert convert(25/0) == 25

def test_gauge_E():
    assert gauge(1/100) == "E"
    assert gauge(100/1) == "E"

def test_gauge_F():
    assert gauge(99/100) == "F"
    assert gauge(100/100) == "F"
    assert gauge(100/99) == "F"

def test_gauge_percentage():
    assert gauge(3/4) == "25%"

