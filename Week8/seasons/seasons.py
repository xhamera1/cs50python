from datetime import date
import inflect
import sys
import re

def main():
    inp=input('Date of Birth: ')
    print(calculate(inp))


def calculate(inpt):
    p = inflect.engine()
    if search := re.search(r'^(\d{4})-(\d{2})-(\d{2})$',inpt):
        inpt=list(search.groups())
    else:
        sys.exit('Invalid date')
    born = check(inpt)
    tod = date.today()
    bday = date(born[0], born[1], born[2])
    diff = bday - tod
    no_of_days = -int(diff.days)
    minutes = no_of_days * 24 * 60
    min_words = p.number_to_words(minutes)
    min_words = min_words.replace(' and','').capitalize()
    return f"{min_words} minutes"


def check(day):
    day = list(map(int, day))
    if day[1] <= -1 or day[1] >= 13:
        sys.exit('Invalid date')
    elif day[2] <= -1 or day[2] >= 32:
        sys.exit('Invalid date')
    return day



if __name__ == "__main__":
    main()
