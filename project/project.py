"""
This program tracks climbing progress for users
"""
import csv
import sys
from datetime import date
from tabulate import tabulate
from pandas import DataFrame

# current YDS climbing grades 
accepted_grades = ["5.0", "5.1", "5.2", "5.3", "5.4", "5.5", "5.6", "5.7", "5.8", "5.9", "5.10a", "5.10b", "5.10c", "5.10d", "5.11a", "5.11b", 
                    "5.11c", "5.11d", "5.12a", "5.12b", "5.12c", "5.12d", "5.13a", "5.13b", "5.13c", "5.13d", "5.14a", "5.14b", "5.14c", "5.14d",
                    "5.15a", "5.15b", "5.15c", "5.15d"]

def main():
    # prompt for username or have option to create new user
    new_session = input("Enter Username or Enter N for New User: ").strip().lower()

    # create a new user
    if new_session == 'n':
        # validate that the username provided isn't already taken and that input has no spaces and is not empty
        while True:
            username = input("Create new username(not case sensitive): ").strip().lower().split()
            if len(username) != 1:
                print("Username cannot be empty or have spaces.  Please pick another one: ")
            
            if user_validate(username) == True:
                print(f"{username[0]} is taken. Try another one. ")
            else:
                break
       
        # ask user to create password and confirm the password
        while True:
            password = input("Create password(case sensitive): ").strip()
            if len(username) != 1:
                print("Username cannot be empty or have spaces.  Please pick another one: ")

            password_repeat = input("Confirm password: ").strip()
            if password != password_repeat:
                print("Passwords do not match. Please try again. ")

            else:
                break
        
        # create new username and password 
        new_user(username[0], password)

        # username[0] is used because username is a list and will print as so
        print(f"Username and password created.  Welcome, {username[0]}!")

    # user presumably entered a username.  validate the username and pwd 
    else:
        username = new_session
        if user_validate(username):
            while True:
                pwd = input("Password: ")
                if password_validate(username, pwd) == False:
                    print("Incorrect password.  Please try again: ")
                else:
                    print(f"Welcome, {username}!")
                    break

        else:
            # try to make this more dynamic and prompt user to either enter their username again or create a new one
            sys.exit("User not in system. Please restart program. ")

    while True:
        # user is to pick from 4 choices (a, b, c, d)
        selection = input("Please select from the following: (A) Add to tracker. (B) View Tracker (C) View Number of Climbs by Date (D) All set: "
                          ).lower().strip()
        if type(username) == list:
            username = username[0]
        # user selected d, which means they are done with the program
        if selection == 'd':
            print("Have a great day! See you soon crusher!")
            break

        # this selection add grades to tracker on the day entered
        if selection == 'a':
            grades = get_climbed_grades()
            add_to_tracker(grades, username)
            print(f"Grade(s) added {grades}")

        # this selection provides tracker table
        if selection == 'b':
            tracker = read_tracker(username)
            print(tabulate(tracker, headers="firstrow"))

        # this selection will return number of climbs completed in date order
        if selection == 'c':
            climb_count = get_climb_count(username)
            print(tabulate(climb_count, headers="keys", tablefmt="psql", showindex=False))

        if selection not in ["a", "b", "c", "d"]:
            print("Invalid selection.  Please select A, B, C or D")

# Open file of climbers read mode to find if the user exists 
def user_validate(username):
    file = open('climber_info.csv', 'r')
    for line in file:
        user, pwd = line.split(',')
        if user == username:
            return True
    file.close()
        
def new_user(name, password):
    # open file of all climbers to add new user and password
    file = open('climber_info.csv', "a")
    writer = csv.writer(file)
    writer.writerow([name, password])
    file.close()

    #create a new file with name of user and create header
    file_track = open(name+'_tracker.csv', 'w')
    writer = csv.writer(file_track)
    writer.writerow(["date", "grade"])
    file_track.close()

#make sure that the passwords provided are the same
def password_validate(username, password):
    file = open('climber_info.csv', 'r')
    for line in file:
        user, pwd = line.split(',')
        if user.strip() == username and pwd.strip() == password:
            return True
    return False
    file.close()

#add grades climber tracker csv file
def add_to_tracker(grades, username):
    file_track = open(username+'_tracker.csv', 'a')
    writer = csv.writer(file_track)
    for grade in grades:
        writer.writerow([date.today(), grade])
    file_track.close()

# this function makes sure that the grades provided by user are valid YDS climbing grades
def get_climbed_grades() -> list[str]:
    grades = input("Please enter grade(s) climbed today: Multiple grades allowed: ").lower().split(", ")
    invalid_grades = map(lambda grade: grade not in accepted_grades, grades)
    while any(invalid_grades):
        print(f'One of the grades entered was invalid. Please pick from: {", ".join(accepted_grades)}')            
        grades = input("Please enter grade(s) climbed today: Multiple grades allowed: ").lower().split(", ")
        invalid_grades = map(lambda grade: grade not in accepted_grades, grades)
    return grades

# this function access the user's tracker csv file and returns the contents of the file
def read_tracker(username):
    file_track = open(username+'_tracker.csv', 'r')
    reader = csv.reader(file_track)
    tracker_list = []
    for line in reader:
        tracker_list.append(line)
    file_track.close()
    return tracker_list


def get_climb_count(username):
    file_track = open(username+'_tracker.csv', 'r')
    reader = csv.reader(file_track)
    dates_list = []
    climbs_count = []

    #skip the first line
    next(reader)
    for line in reader:
        date_data = line[0]
        dates_list.append(date_data)

    #create a set of the dates to get distinct dates
    unique_date = set(dates_list)

    #get count of climbs per day
    for date in unique_date:
        num_climbs = dates_list.count(date)
        climbs_count.append({"date": date, "number_of_climbs": num_climbs})
    sorted_climbs_count = sorted(climbs_count, key=lambda x: x['date'])

    df = DataFrame(sorted_climbs_count)

    return df

if __name__ == "__main__":
    main()