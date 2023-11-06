import pytest
from working import convert 

def main():
    test_time()
    test_versatile_am_pm()
    test_valueerror()

# checks that times are converted correctly
def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_versatile_am_pm():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")                
    with pytest.raises(ValueError):
        convert("9 to 5")     
    with pytest.raises(ValueError):
        convert("what to who")              

if __name__ == "__main__":
    main()