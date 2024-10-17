from seasons import user_input
import pytest

def test_user_input_wrong():
    with pytest.raises(SystemExit):
        user_input("February 6t, 1998")
