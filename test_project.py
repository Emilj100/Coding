from project import User, main
import pytest

def test_calorie_intake():
    user = User("Emil", "Male", "186", "19", "100.5", "1", "5")
    user.calorie_intake(weight=100.5, height=186, age=19)
