import pytest
from seasons import age_in_minutes


def test_age_in_minutes():
    assert age_in_minutes("2000-01-01") == "Twelve million five hundred sixty-four thousand seven hundred sixty minutes"
    assert age_in_minutes("1990-05-17") == "Eighteen million one hundred twelve thousand eighty minutes"
    assert age_in_minutes("2023-01-01") == "One hundred twenty-six thousand seven hundred twenty minutes"


def test_invalid_dates():
    with pytest.raises(SystemExit):
        age_in_minutes("2000-13-01")
    with pytest.raises(SystemExit):
        age_in_minutes("2000-01-32")
    with pytest.raises(SystemExit):
