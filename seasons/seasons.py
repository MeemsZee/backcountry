"""
Program gives you how many minutes have you been alive spelled out with a birthday input. 
Assumption: everyone is born at midnight
"""
from datetime import date, datetime
import inflect
import sys

p = inflect.engine()

class Minutes_alive:
    def convert_to_min(self, birthday):
        self.birthday = birthday
        try:
            self.date_of_birth = datetime.strptime(self.birthday, "%Y-%m-%d").date()
        except ValueError:
            sys.exit("Invalid date")
        self.today = date.today()
        num_days = abs(self.date_of_birth - self.today)
        return (f"{p.number_to_words(num_days.days * 60 * 24).capitalize().replace('and ', '')} minutes")

def main():
    birth = Minutes_alive()
    print(birth.convert_to_min(input("Date of Birth: ").strip()))
    

if __name__ == "__main__":
    main()