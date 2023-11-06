"""
Program counts number of "um"s in a given text
"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_counter = 0
    s = s.strip().lower().split()
    for item in s:
        if re.search(r"^ ?um([^\w]| |$)", item):
            um_counter += 1
        

    return um_counter


if __name__ == "__main__":
    main()