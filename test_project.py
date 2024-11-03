from project import User
import pytest

def test_calorie_intake(capsys):
    user = User("Emil", "Male", "186", "19", "100.5", "1", "5")
    user.calorie_intake()
    capsys_output = capsys.readouterr()
    expected_output = "\nThis is your calorie intake: 2719.35 calories\n"
    assert capsys_output.out == expected_output
