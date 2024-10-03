import pytest

from fuel import convert, gauge

# Test af convert funktionen

def test_convert_inputs():
    assert convert("37/88") == 42
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_convert_x():
    with pytest.raises(ValueError):
        convert("88/37")
        convert("4/3")
        convert("4/1")

def test_convert_100():
    with pytest.raises(ValueError):
        convert("75/125")
        convert("-25/-30")
    with pytest.raises(ZeroDivisionError):
        convert("25/0")

# Test af gauge funktionen

def test_gauge_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(99.5) == "F"

def test_gauge_percentage():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"

