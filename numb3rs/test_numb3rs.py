from numb3rs import validate
import pytest

def main():
    test_dots()
    test_num()

#check that ip address has 3 dots
def test_dots():
    assert validate("1.1.1") == False
    assert validate("1.1.1.1") == True
    assert validate("1.1.") == False
    assert validate("1") == False
    assert validate("1.1.1.1.1") == False

#check that each section outside of dots are between 0 and 255
def test_num():
    assert validate("1.1.1.1") == True
    assert validate("290.1.1.1") == False
    assert validate("1.290.1.1") == False
    assert validate("1.1.290.1") == False
    assert validate("1.1.1.290") == False

#check that characters return a false
def test_char():
    assert validate("cat") == False

if __name__ == "__main__":
    main()