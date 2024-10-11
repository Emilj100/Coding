from um import count

def test_count():
    assert count("hi this is um yummy food!") == 1
    assert count("hi this is UM yummy food!") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um?") == 1
