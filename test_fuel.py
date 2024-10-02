from fuel import convert, gauge

def test_convert():
    assert convert("37/88") == "42%"

