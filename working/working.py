"""
Converts 12-hr time to 24 hr time 
"""

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
#make sure the pattern we are looking for is correct 

    if matches := re.search(r"^(([1-9]|1[0-2])(:[0-5][0-9])? (am|pm)) to ((1[0-2]|[1-9])(:[0-5][0-9])? (am|pm))$", s.strip().lower()):
        start_hour = int(matches.group(2))
        start_minutes = matches.group(3)
        start_meridiem = matches.group(4)
        end_hour = int(matches.group(6))
        end_minutes = matches.group(7)
        end_meridiem = matches.group(8)
    else:
        raise ValueError
    
    
    if start_minutes == None:
        start_minutes = ":00"
    if end_minutes == None:
        end_minutes = ":00"

    if start_meridiem == "am" and start_hour < 10:
        start_hour = str(start_hour).zfill(2)
    elif start_hour == 12 and start_meridiem == "am":
        start_hour = "00"
    elif start_meridiem == "pm" and start_hour!= 12:
        start_hour = start_hour + 12
    else:
        pass

    if end_meridiem == "am" and end_hour < 10:
        end_hour = str(end_hour).zfill(2)
    elif end_hour == 12 and end_meridiem == "am":
        end_hour = "00"
    elif end_meridiem == "pm" and end_hour!= 12:
        end_hour = end_hour + 12
    else:
        pass
    
    return f"{start_hour}{start_minutes} to {end_hour}{end_minutes}"
    

if __name__ == "__main__":
    main()
