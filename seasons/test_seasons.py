import pytest
from seasons import Minutes_alive

def main():
    test_minute()

def test_minute():
    assert Minutes_alive().convert_to_min("2022-09-03") == 'Five hundred twenty-five thousand, six hundred minutes'
    assert Minutes_alive().convert_to_min("2021-09-03") == 'One million, fifty-one thousand, two hundred minutes'

def test_value_error():
    with pytest.raises(SystemExit):
        Minutes_alive().convert_to_min("January, 1, 2019")


if __name__ == "__main__":
    main()