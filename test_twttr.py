from twttr import shorten

def test_shorten():
    assert shorten("DAvid") == "Dvd"

def test_shorten_numbers():
    assert shorten("1da2k") == "1d2k"

def test_shorten_punctuation():
    assert shorten(".da,o") == ".d,"
