import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    s = s.strip()
    count = 0
    if len(s) < 2:
        return 0
    if s == "um":
        return 1
    if len(s) == 2:
        return 0
    if len(s) == 3:
        if s[0] == "u" and s[1] == "m" and s[2].isalpha() == False:
            return 1
    for i in range(0, len(s)-3):
        if i == 0:
            if s[i] == "u" and s[i+1] == "m" and s[i+2].isalpha() == False:
                count += 1
            else:
                continue
        else:
            if s[i] == " " and s[i+1] == "u" and s[i+2] == "m" and s[i+3].isalpha() == False:
                count += 1
            else:
                continue
    return count





if __name__ == "__main__":
    main()
