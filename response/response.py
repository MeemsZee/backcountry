"""
This program is a email address validator.  Reg ex is prohibited
"""

from validator_collection import validators, checkers, errors

def main():

    print(validate(input("What is your email address? ").strip()))

def validate(email):
    try:
        is_valid = validators.email(email)
        if is_valid == email:
            return "Valid"
    except ValueError:
        return "Invalid"

if __name__ == "__main__":
    main()

