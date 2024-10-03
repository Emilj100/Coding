import pytest
from fuel import convert, gauge

# Test af convert-funktionen
def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/100") == 1

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("ten/ten")
    with pytest.raises(ValueError):
        convert("3.5/7")

def test_convert_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# Test af gauge-funktionen
def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_percentage():
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
