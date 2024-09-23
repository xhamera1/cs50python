import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches1 = re.search(r"^.*src=\"(.+?)\".*$", s)
    if matches1:
        link = matches1.group(1)
        link = link.replace("youtube", "youtu.be")
        link = link.replace(".com", "")
        link = link.replace("www.", "")
        matches2 = re.search(r"^(.*)youtu.be/(.*)/(.*)$", link)
        if matches2:
            first, third = matches2.group(1), matches2.group(3)
            result = f"{first}youtu.be/{third}"
            if "https" not in result:
                result = result.replace("http", "https")
            return result
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()
