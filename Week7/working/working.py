import re
import sys


def main():
    print(convert(input("Hours: ")))


def checkHour(st, time):
    if time.lower() == "am":
        if ':' in st:
            hour, minute = st.split(":")
            if int(hour) < 1 or int(hour) > 12 or int(minute) < 0 or int(minute) > 59:
                raise ValueError
            if int(hour) == 12:
                return f"00:{minute}"
            if int(hour) < 10:
                return f"0{hour}:{minute}"
            else:
                return f"{hour}:{minute}"
        else:
            if int(st) < 1 or int(st) > 12:
                raise ValueError
            if int(st) == 12:
                return f"00:00"
            if int(st) < 10:
                return f"0{st}:00"
            else:
                return f"{st}:00"
    elif time.lower() == "pm":
        # 1:00 -> 13:00
        if ':' in st:
            hour, minute = st.split(":")
            if int(hour) < 1 or int(hour) > 12 or int(minute) < 0 or int(minute) > 59:
                raise ValueError
            if int(hour) == 12:
                return f"12:{minute}"
            new_hour = int(hour) + 12
            hour = str(new_hour)
            return f"{hour}:{minute}"
        else:
            hour = st
            if int(hour) < 1 or int(hour) > 12:
                raise ValueError
            if int(hour) == 12:
                return f"12:00"
            new_hour = int(hour) + 12
            hour = str(new_hour)
            return f"{hour}:00"
    else:
        raise ValueError

def convert(s):
    try:
        p1, p2, p3, p4, p5 = s.split(" ")
        result_p1 = checkHour(p1, p2)
        if p3 != "to":
            raise ValueError
        result_p3 = checkHour(p4, p5)
        return f"{result_p1} {p3} {result_p3}"

    except ValueError:
        raise ValueError




if __name__ == "__main__":
    main()
