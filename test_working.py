from working import convert

def test_convert():
    assert convert("9:30 PM to 9:30 AM") == "21:30 to 09:30"
    assert convert("10 AM to 5 PM") == "10:00 to 17:00"
