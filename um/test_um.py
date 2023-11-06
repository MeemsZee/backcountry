import pytest
from um import count

def main():
    test_case()
    test_additional_letters()
    test_spaces()
    test_punctuation()

def test_case():
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("um") == 1

def test_additional_letters():
    assert count("um, what album?") == 1
    assert count("that was crummy") == 0

def test_spaces():
    assert count("um what to do um here?") == 2

def test_punctuation():
    assert count("um... what, um?") == 2


if __name__ == "__main__":
    main()