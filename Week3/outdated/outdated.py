import re
import datetime

months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April": 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

while True:
    inp = input("Date: ")
    try:
        if inp[1]=='/' or inp[2]=='/':
            m, d, y = inp.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            if m >= 1 and m <= 12 and d >= 1 and d <= 31:
                x = datetime.datetime(y,m,d)
                day = x.strftime("%d")
                month = x.strftime("%m")
                year = x.strftime("%Y")
                print(f"{year}-{month}-{day}")
                break
        if ',' not in inp:
            raise ValueError  
        m, d, y = re.split(r'\s*,\s*|\s+', inp)
        if m in months:
            m = int(months[m])
            d = int(d)
            y = int(y)
            if m >= 1 and m <= 12 and d >= 1 and d <= 31:
                x = datetime.datetime(y,m,d)
                day = x.strftime("%d")
                month = x.strftime("%m")
                year = x.strftime("%Y")
                print(f"{year}-{month}-{day}")
                break
    except (ValueError, IndexError, EOFError):
        pass


