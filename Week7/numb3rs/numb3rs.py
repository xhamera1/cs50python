import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.fullmatch(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)
    if matches:
        parts = ip.split(".")
        for part in parts:
            if int(part) <= 255 and int(part) >= 0:
                continue
            else:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
