from seasons import user_input
import pytest

def test_user_input_wrong():
    with pytest.raises(SystemExit):
        user_input("February 6t, 1998")

def test_user_input_corret():
    assert user_input("2005-01-10") == "Ten million, three hundred ninety-six thousand, eight hundred minutes"

