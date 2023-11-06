from project import *
import pytest
import os.path
import pandas as pd 
import csv
from datetime import date

def main():
    test_user_validate()
    test_new_user()
    test_password_validate()
    test_add_to_tracker()
    test_add_to_tracker_mult()
    test_get_climbed_grades()
    test_get_climbed_grades_incorrect_input()
    test_read_tracker()
    test_get_climb_count()

def test_user_validate():
    assert user_validate("dog") == True
    assert user_validate("foo") == None
        
def test_new_user():
    #assert that username and password are in file 
    assert new_user("foo_bar", "times") == None
    assert user_validate("foo_bar") == True
    assert os.path.isfile('foo_bar_tracker.csv') == True
    df = pd.read_csv('climber_info.csv')
    df = df.drop(df.index[-1])
    df.to_csv('climber_info.csv', index=False)
    os.remove('foo_bar_tracker.csv')

def test_password_validate():
    assert password_validate("dog", "cat") == True
    assert password_validate("dog", "whoa") == False


def test_get_climbed_grades(monkeypatch) -> list[str]:
    monkeypatch.setattr('builtins.input', lambda _: "5.10c")
    result = get_climbed_grades()
    assert result == ["5.10c"]
    monkeypatch.setattr('builtins.input', lambda _: "5.10c, 5.9, 5.11a")
    result = get_climbed_grades()
    assert result == ["5.10c", "5.9", "5.11a"]
   
def test_get_climbed_grades_incorrect_input(monkeypatch) -> list[str]:
    inputs = iter(["5.11a, 5.10c, 5.10", "5.11a, 5.10c, 5.10b"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = get_climbed_grades()
    assert result == ["5.11a", "5.10c", "5.10b"]
    inputs_2 = iter(["Cats", "5.11a"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_2))
    result = get_climbed_grades()
    assert result == ["5.11a"]

def test_add_to_tracker():
    #check to see that the last thing entered to a csv is correct
    #using dog tracker as the prototype
    add_to_tracker(["5.9"], "dog")
    with open("dog_tracker.csv", "r") as file:
        last_row = file.readlines()[-1]
    file.close()
    assert os.path.isfile('dog_tracker.csv') == True
    assert last_row == str(date.today())+",5.9\n"
    df = pd.read_csv('dog_tracker.csv')
    df = df.drop(df.index[-1])
    df.to_csv('dog_tracker.csv', index=False)


def test_add_to_tracker_mult():
    # check to see that the latest grades entered to a csv is correct
    # using dog tracker as the prototype
    add_to_tracker(["5.9", "5.10c"], "dog")
    with open("dog_tracker.csv", "r") as file:
        last_entered = file.readlines()[-2:]
    file.close()
    assert os.path.isfile('dog_tracker.csv') == True
    assert last_entered == [str(date.today())+",5.9\n", str(date.today())+",5.10c\n"]
    df = pd.read_csv('dog_tracker.csv')
    df = df.drop(df.index[-2:])
    df.to_csv('dog_tracker.csv', index=False)
    
def test_read_tracker():
    # make sure that user has access to their tracking data
    # for our purposes, we will just look at the first 3 lines 
    tracker_list = read_tracker("dog")
    test_tracker = []
    counter = 0
    file = open("dog_tracker.csv", 'r')
    reader = csv.reader(file)
    while counter < 3:
        for line in reader:
            test_tracker.append(line)
            counter += 1
    assert tracker_list[:3] == test_tracker[:3]

def test_get_climb_count():
    data = get_climb_count("dog")
    assert data.iloc[0,1] == 10
    assert data.iloc[0,0] == "2023-09-30"

if __name__ == "__main__":
    main()