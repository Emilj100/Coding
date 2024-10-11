import pytest
from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_multiple_um():
    assert count("um, um, um.") == 3
    assert count("Um... um... um") == 3
    assert count("UM um Um") == 3

def test_um_within_words():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("aluminum") == 0

def test_um_with_special_characters():
    assert count("um! How are you?") == 1
    assert count("Well, um... that's interesting.") == 1
    assert count("Hum, let me think about that.") == 0
