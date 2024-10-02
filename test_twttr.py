from twttr import shorten

def test_shorten():
    assert shorten("David") == "Dvd"

def test_shorten2():
    assert shorten("Twitter") == "Twitter"

