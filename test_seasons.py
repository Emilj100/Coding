from seasons import user_input
import pytest

def test_user_input():
    with pytest.raises(ValueError):
        user_input()
