"""
This program validates that a series of numbers can be an ip address
"""
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # search for a number in the range of 0-255 followed by "." 3 times and search again for a number in range 0-255
    if re.search(r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", ip.strip()):
        return True
    else:
        return False


if __name__ == "__main__":
    main()