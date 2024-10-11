from working import convert
import pytest

def test_convert():
    assert convert("9:30 PM to 9:30 AM") == "21:30 to 09:30"
    assert convert("10 AM to 5 PM") == "10:00 to 17:00"

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:71 PM")
        convert("13:00 PM to 21:00 AM")

def test_convert_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("9:30 AM - 5:30 PM")
