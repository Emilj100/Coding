import pytest

from fuel import convert, gauge

# Test af convert funktionen

def test_convert_inputs():
    assert convert("37/88") == 42
    assert convert("3/4") == 75
    assert convert("1/4") == 25




# KIG I NOTER OMKRING ET INPUT ER LIG MED EN BESTEMT TYPE FEJL




def test_convert_x():
    assert convert("88/37") == ValueError
    assert convert("4/3") == ValueError
    assert convert("4/1") == ValueError

def test_convert_100():
    assert convert("75/125") == ValueError
    assert convert("-25/-30") == ValueError
    assert convert("25/0") == ZeroDivisionError

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

