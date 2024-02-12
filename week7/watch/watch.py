import re
import sys


def main():
    html = parse(input("HTML: "))
    print(html)


def parse(s):
    pattern = r'^<iframe.*src="https?://(www.)?youtube.com/embed/(.*?)"'
    if  matches := re.search(pattern, str(s)):
        return f"https://youtu.be/{matches.group(2)}"
    else:
        return "None"


if __name__ == "__main__":
    main()

