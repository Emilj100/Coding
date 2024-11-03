from project import User, main
import pytest

def test_calorie_intake():
    user = User("Emil", "Male", 186, 19, 100.5, "1", "5")
    user.calorie_intake()
    assert capsys.readouterr() == 2719.35
