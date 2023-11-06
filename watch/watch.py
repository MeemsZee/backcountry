"""
This program takes embedded youtube urls and converts them back into shorter, shareable youtu.be urls
"""

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #split input
    html_split = s.split()

    for item in html_split:
        if matches := re.search(r"src=\"(https?://(?:www\.)?youtube\.com/embed/(.+))\"", item.strip()):
            return "https://youtu.be/" + matches.group(2)

if __name__ == "__main__":
    main()