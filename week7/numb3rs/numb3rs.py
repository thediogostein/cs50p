import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        ip_parts = ip.split(".")
        return all(0 <= int(n) <= 255 for n in ip_parts)
    else:
        return False


if __name__ == "__main__":
    main()
