import pytest
from twttr import shorten

def test_shorten_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("banana") == "bnn"
    assert shorten("elephant") == "lphnt"

def test_shorten_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("BANANA") == "BNN"
    assert shorten("ELEPHANT") == "LPHNT"

def test_shorten_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("BaNaNa") == "BNN"

def test_shorten_with_numbers():
    assert shorten("t3st") == "t3st"
    assert shorten("1234") == "1234"

def test_shorten_with_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("Python's cool.") == "Pythn's cl."

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_no_vowels():
    assert shorten("rhythm") == "rhythm"
